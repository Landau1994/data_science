"""只读检查概念、来源与习题链接；需 PyYAML，不运行 Obsidian 或改学习状态。"""

from collections import Counter
import json
from pathlib import Path
import re
import sys

import yaml

ROOT = Path(__file__).resolve().parents[1]
SECTIONS = ("定义", "直觉与解释", "主要性质", "例子与边界", "相关概念", "相关习题", "来源与证明状态")
TOPICS = {
    "01 - 概率论": "probability-theory", "02 - 数理统计": "mathematical-statistics",
    "03 - 线性代数与优化": "linear-algebra-optimization", "04 - 统计学习": "statistical-learning",
    "05 - 概率模型与推断": "probabilistic-models", "06 - 深度学习": "deep-learning",
    "07 - 因果推断与实验设计": "causal-inference", "08 - 随机过程与时间序列": "stochastic-processes",
    "09 - 数据计算与可复现性": "data-computing", "10 - AI工程": "ai-engineering",
}


def main():
    errors = []
    notes = {}
    targets = {}
    for p in ROOT.rglob("*"):
        rel = p.relative_to(ROOT)
        if not p.is_file() or any(v.startswith(".") for v in rel.parts):
            continue
        key = rel.as_posix()
        targets[key] = key
        targets.setdefault(p.name, key)
        if p.suffix == ".md":
            targets[key[:-3]] = key
            targets.setdefault(p.stem, key)
            if rel.parts[0] == "模板":
                continue
            raw = p.read_text(encoding="utf-8-sig")
            match = re.match(r"\A---\n(.*?)\n---(?:\n|$)", raw, re.S)
            try:
                meta = yaml.safe_load(match[1]) if match else {}
            except yaml.YAMLError as exc:
                errors.append(f"元数据无法解析：{key}：{exc}")
                meta = {}
            notes[key] = {"meta": meta or {}, "body": raw[match.end():] if match else raw, "raw": raw}

    def links(body):
        return [m[1].replace(r"\|", "|").split("|", 1)[0] for m in re.finditer(r"\[\[([^\]]+)\]\]", body)]

    def resolve(link):
        name = link.split("#", 1)[0].strip()
        return targets.get(name) if name else None

    for key, note in notes.items():
        for link in links(note["raw"]):
            name = link.split("#", 1)[0].strip()
            if name and not resolve(link):
                errors.append(f"失效链接：{key} -> {link}")
            if "#" in link and resolve(link) in notes:
                anchor = link.split("#", 1)[1]
                if anchor and not anchor.startswith("^"):
                    headings = re.findall(r"(?m)^#{1,6} (.+?)\s*$", notes[resolve(link)]["body"])
                    if anchor not in headings:
                        errors.append(f"失效标题定位：{key} -> {link}")

    concepts = {k: n for k, n in notes.items() if "concept" in n["meta"].get("tags", [])}
    exercises = {k: n for k, n in notes.items() if "exercise" in n["meta"].get("tags", [])}
    sources = {k: n for k, n in notes.items() if "source" in n["meta"].get("tags", [])}
    for key, note in concepts.items():
        meta, body = note["meta"], note["body"]
        for field in ("title", "aliases", "topic", "topic_label", "status", "source", "source_status", "created"):
            if not meta.get(field):
                errors.append(f"概念缺字段 {field}：{key}")
        if not isinstance(meta.get("source"), str) or "[[" in meta.get("source", "") or re.search(r"\[[^\]]+\]\(", meta.get("source", "")):
            errors.append(f"概念source应为教材名和定位的普通文字：{key}")
        if isinstance(meta.get("source"), str) and re.match(r"^DS\d{3}(?:\b|\s|；|，)", meta["source"]):
            errors.append(f"概念source需写完整题名，不能仅用来源编号：{key}")
        if meta.get("topic") != TOPICS.get(key.split("/", 1)[0]):
            errors.append(f"概念主题与路径不符：{key}")
        if meta.get("source_status") not in {"unverified", "partially-verified", "verified"}:
            errors.append(f"来源状态非法：{key}")
        for heading in SECTIONS:
            if f"## {heading}\n" not in body:
                errors.append(f"概念缺结构 {heading}：{key}")
        if not re.search(r"FROM\s+#exercise\s+WHERE\s+contains\(file\.outlinks,\s*this\.file\.link\)", body):
            errors.append(f"缺动态习题回查：{key}")
        if not any(resolve(link) in sources for link in links(note["raw"])):
            errors.append(f"概念未链接真实来源记录：{key}")
        if "\\(" in body or "\\[" in body:
            errors.append(f"公式定界符不符：{key}")
        math_body = re.sub(r"```.*?```", "", body, flags=re.S)
        if len(re.findall(r"(?<!\\)\$", math_body)) % 2:
            errors.append(f"美元公式定界符不配对：{key}")
        in_display = False
        callout_display = False
        for line in body.splitlines():
            if line.strip() in {"$$", "> $$"}:
                if not in_display:
                    callout_display = line.lstrip().startswith(">")
                in_display = not in_display
            elif in_display and callout_display and not line.startswith(">"):
                errors.append(f"callout内公式行缺 >：{key}")
        if in_display:
            errors.append(f"展示公式未闭合：{key}")

    relation_rows = []
    for key, note in exercises.items():
        for concept in sorted({resolve(v) for v in links(note["body"])} & concepts.keys()):
            physical_return = key in {resolve(v) for v in links(concepts[concept]["body"])}
            dynamic_return = bool(re.search(r"FROM\s+#exercise\s+WHERE\s+contains\(file\.outlinks,\s*this\.file\.link\)", concepts[concept]["body"]))
            relation_rows.append({"exercise": key, "concept": concept, "dynamic_return": dynamic_return, "explicit_return": physical_return})
            if not dynamic_return:
                errors.append(f"习题概念缺动态回查：{key} <-> {concept}")
    for concept, note in concepts.items():
        for exercise in {resolve(v) for v in links(note["body"])} & exercises.keys():
            if concept not in {resolve(v) for v in links(exercises[exercise]["body"])}:
                errors.append(f"概念所引习题缺回链：{concept} <-> {exercise}")
    source_concept_edges = 0
    for key, note in sources.items():
        for concept in {resolve(v) for v in links(note["body"])} & concepts.keys():
            source_concept_edges += 1
            if key not in {resolve(v) for v in links(concepts[concept]["raw"])}:
                errors.append(f"概念缺来源回链：{key} <-> {concept}")
    academic_terms = 0
    material_terms = 0
    for key, note in sources.items():
        sid = note["meta"].get("source_id", "")
        if not re.fullmatch(r"DS0(?:0[1-9]|1[0-7])", sid):
            continue
        match = re.search(r"## 关键术语\n(.*?)(?=\n## |\Z)", note["body"], re.S)
        if not match:
            continue
        for line in match[1].splitlines():
            if line.startswith("### "):
                break
            if line.startswith("- "):
                if "资料使用用语" in line:
                    material_terms += 1
                elif "[[" in line:
                    academic_terms += 1
                else:
                    errors.append(f"教材学科术语未连概念：{key}：{line}")
    for p in (ROOT / "知识图谱").glob("*.canvas"):
        data = json.loads(p.read_text(encoding="utf-8-sig"))
        for node in data["nodes"]:
            if node.get("type") == "file" and node.get("file") not in targets:
                errors.append(f"Canvas文件不存在：{p.name} -> {node.get('file')}")
    report = {
        "notes": len(notes), "concepts": len(concepts), "exercises": len(exercises), "sources": len(sources),
        "concept_states": dict(Counter(n["meta"].get("status") for n in concepts.values())),
        "source_states": dict(Counter(n["meta"].get("source_status") for n in concepts.values())),
        "textbook_academic_term_occurrences": academic_terms, "material_term_occurrences": material_terms,
        "source_concept_edges": source_concept_edges, "exercise_concept_pairs": len(relation_rows),
        "relations": relation_rows, "errors": errors,
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
