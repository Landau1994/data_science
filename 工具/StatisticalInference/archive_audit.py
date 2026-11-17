"""只读核对DS011的来源题号、选定归档范围与笔记映射；不修改学习状态。"""

from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import sys

import yaml


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = Path(__file__).with_name("source-manifest.json")


def main():
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    errors, notes, summaries = [], [], []
    source = ROOT / manifest["source_file"]
    if not source.exists() or hashlib.sha256(source.read_bytes()).hexdigest() != manifest["source_sha256"]:
        errors.append("原始PDF缺失或SHA-256与已核对版本不同")
    for asset in manifest.get("assets", []):
        path = ROOT / asset["file"]
        if not path.exists() or hashlib.sha256(path.read_bytes()).hexdigest() != asset["sha256"]:
            errors.append(f"图件缺失或版本哈希不一致：{asset['file']}")
    for path in ROOT.glob("*/习题/习题 *.md"):
        raw = path.read_text(encoding="utf-8-sig")
        match = re.match(r"\A---\n(.*?)\n---\n", raw, re.S)
        try:
            meta = yaml.safe_load(match[1]) if match else {}
        except yaml.YAMLError:
            errors.append(f"无法解析元数据：{path.relative_to(ROOT).as_posix()}")
            continue
        if meta and meta.get("source_id") == manifest["source_id"]:
            notes.append((path.relative_to(ROOT).as_posix(), meta, raw))

    for chapter, data in manifest["chapters"].items():
        expected = data["expected_exercises"]
        scope = data["archive_scope_exercises"]
        mappings = data["exercises"]
        lettered_subparts = sum(len(row["subparts"]) for row in mappings)
        if "lettered_subpart_total" in data and lettered_subparts != data["lettered_subpart_total"]:
            errors.append(f"第{chapter}章字母分题总数与来源清单不一致")
        if len(set(expected)) != len(expected) or expected != sorted(expected, key=lambda x: int(x.split(".")[1])):
            errors.append(f"第{chapter}章来源题号重复或失序")
        if len(set(scope)) != len(scope) or not set(scope) <= set(expected):
            errors.append(f"第{chapter}章归档范围重复或超出原题集合")
        if [m["source_exercise"] for m in mappings] != scope:
            errors.append(f"第{chapter}章清单映射与选定范围不一致")
        actual = [n for n in notes if str(n[1].get("source_chapter")) == chapter]
        counts = Counter(str(n[1].get("source_exercise")) for n in actual)
        missing = [n for n in scope if not counts[n]]
        extra = sorted(set(counts) - set(scope))
        duplicates = [n for n, count in counts.items() if count > 1]
        for kind, values in (("本批缺失", missing), ("多余或无法解析题号", extra), ("重复", duplicates)):
            if values:
                errors.append(f"第{chapter}章{kind}：{values}")
        by_path = {row[0]: row for row in actual}
        for mapping in mappings:
            key = mapping["note"]
            if key not in by_path:
                errors.append(f"映射无法解析：{key}")
                continue
            _, meta, raw = by_path[key]
            local_id = mapping["local_id"]
            statistics = local_id.startswith("ST")
            topic = "mathematical-statistics" if statistics else "probability-theory"
            label = "数理统计" if statistics else "概率论"
            folder = "02 - 数理统计" if statistics else "01 - 概率论"
            for field, value in {
                "source_exercise": mapping["source_exercise"], "source_stars": mapping.get("stars", 0),
                "topic": topic, "topic_label": label,
                "source_status": "verified", "solution_status": "independently-derived",
            }.items():
                if meta.get(field) != value:
                    errors.append(f"字段不一致 {field}：{key}")
            if not key.startswith(f"{folder}/习题/习题 {local_id} - "):
                errors.append(f"主题路径或编号不符：{key}")
            if not str(meta.get("title", "")).startswith(f"习题 {local_id}："):
                errors.append(f"标题编号不符：{key}")
            for field in ("title", "source", "source_refs", "created"):
                if not meta.get(field):
                    errors.append(f"缺少字段 {field}：{key}")
            if meta.get("status") not in {"not-started", "in-progress", "completed"}:
                errors.append(f"学习状态非法：{key}")
            if meta.get("difficulty") not in {"beginner", "intermediate", "advanced"}:
                errors.append(f"难度非法：{key}")
            if "exercise" not in meta.get("tags", []):
                errors.append(f"缺少exercise标签：{key}")
            for heading in ("题目", "提示", "解答", "相关概念", "备注"):
                if f"## {heading}\n" not in raw:
                    errors.append(f"缺少结构 {heading}：{key}")
            for fragment in ("### 英文原题", "### 中文转述", "> [!question]", "> [!hint]-", "> [!success]- 解答\n"):
                if fragment not in raw:
                    errors.append(f"缺少双语或callout结构 {fragment.strip()}：{key}")
            english = raw.partition("### 英文原题")[2].partition("### 中文转述")[0]
            chinese = raw.partition("### 中文转述")[2].partition("## 提示")[0]
            for language, block in (("英文原题", english), ("中文转述", chinese)):
                # 分题也可能在表格或一行中；只将来源清单声明的标号作为有序检查对象。
                # 罗马嵌套标号、正文交叉引用不当作额外顶层分题。
                cursor = 0
                for part in mapping["subparts"]:
                    found = re.search(r"\(" + re.escape(part) + r"\)", block[cursor:])
                    if not found:
                        errors.append(f"{language}分题标号集合或次序不符({part})：{key}")
                        break
                    cursor += found.end()
                for parent, nested in mapping.get("nested_subparts", {}).items():
                    for part in nested:
                        # 原排版的罗马编号可在Markdown中保留为i.，不误报为缺问。
                        if not re.search(r"\("+re.escape(part)+r"\)|(?m:^>\s*)"+re.escape(part)+r"\.", block):
                            errors.append(f"{language}缺少嵌套分题({parent})({part})：{key}")
            for part in mapping["subparts"]:
                for language, block in (("英文原题", english), ("中文转述", chinese)):
                    if f"({part})" not in block:
                        errors.append(f"{language}缺分题({part})：{key}")
            body = raw[match.end():]
            # cases中的换行\\\\后可直接跟圆括号，不能把第二个反斜线误当成数学开界。
            if re.search(r"(?<!\\)\\[\[(]", body):
                errors.append(f"使用了非Obsidian数学定界符：{key}")
            if body.count("$$") % 2 or re.sub(r"\$\$", "", body).count("$") % 2:
                errors.append(f"数学定界符未配对：{key}")
            in_display, callout_display = False, False
            for line in body.splitlines():
                if line.strip() in {"$$", "> $$"}:
                    if not in_display:
                        callout_display = line.lstrip().startswith(">")
                    in_display = not in_display
                elif in_display and callout_display and not line.startswith(">"):
                    errors.append(f"callout内公式行缺少 >：{key}")
        summaries.append({
            "chapter": int(chapter), "source_total": len(expected),
            "archive_scope": len(scope), "actual": len(actual),
            "missing_in_scope": missing, "duplicates": duplicates,
            "extra_or_unparsed": extra,
            "lettered_subparts": lettered_subparts,
            "pending_outside_scope": [n for n in expected if n not in scope],
            "chapter_complete": set(counts) == set(expected) and not duplicates,
        })
    unknown = [p for p, m, _ in notes if str(m.get("source_chapter")) not in manifest["chapters"]]
    errors.extend(f"存在未登记章节：{p}" for p in unknown)
    if errors:
        for summary in summaries:
            summary["chapter_complete"] = False
    print(json.dumps({"source_id": manifest["source_id"], "chapters": summaries, "errors": errors}, ensure_ascii=False, indent=2))
    return bool(errors)


if __name__ == "__main__":
    sys.exit(main())
