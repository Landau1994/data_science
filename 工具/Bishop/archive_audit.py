"""只读核对 DS003 已录入章节的来源题号与 Markdown 映射；需要 PyYAML。"""

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import sys

import yaml

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = Path(__file__).with_name("source-manifest.json")
TOPICS = {
    "P": ("01 - 概率论", "probability-theory", "概率论"),
    "ST": ("02 - 数理统计", "mathematical-statistics", "数理统计"),
    "LA": ("03 - 线性代数与优化", "linear-algebra-optimization", "线性代数与优化"),
    "ML": ("04 - 统计学习", "statistical-learning", "统计学习"),
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--chapter", type=int, help="仅核对一个已登记章节")
    args = parser.parse_args()
    manifest = json.loads(MANIFEST.read_text(encoding="utf8"))
    chapters = manifest["chapters"]
    if args.chapter is not None:
        key = str(args.chapter)
        if key not in chapters:
            parser.error("该章尚未登记原题集合，不能据零条查询结果认定为零题。")
        chapters = {key: chapters[key]}
    errors, notes = [], []
    source = ROOT / manifest["source_file"]
    if not source.exists():
        errors.append("原始 PDF 不存在，无法核对版本哈希")
    elif hashlib.sha256(source.read_bytes()).hexdigest() != manifest["source_sha256"]:
        errors.append("原始 PDF 的 SHA-256 与已核对版本不同")
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
    summaries = []
    for chapter, data in chapters.items():
        expected = data["expected_exercises"]
        mappings = data["exercises"]
        if [row["source_exercise"] for row in mappings] != expected:
            errors.append(f"第{chapter}章来源清单映射次序或题号不一致")
        if len(set(expected)) != len(expected):
            errors.append(f"第{chapter}章来源题号重复")
        if not expected and not data.get("audit_note"):
            errors.append(f"第{chapter}章缺少零题依据")
        actual = [n for n in notes if str(n[1].get("source_chapter")) == chapter]
        counts = Counter(str(n[1].get("source_exercise")) for n in actual)
        missing = [n for n in expected if not counts[n]]
        extra = sorted(set(counts) - set(expected))
        duplicates = [n for n, count in counts.items() if count > 1]
        errors.extend(f"第{chapter}章{kind}：{values}" for kind, values in
                      [("缺失", missing), ("多余或无法解析", extra), ("重复", duplicates)] if values)
        by_path = {row[0]: row for row in actual}
        for mapping in mappings:
            key = mapping["note"]
            if key not in by_path:
                errors.append(f"映射无法解析：{key}")
                continue
            _, meta, raw = by_path[key]
            local_id = mapping["local_id"]
            prefix = re.fullmatch(r"([A-Z]+)\d+", local_id)[1]
            folder, topic, label = TOPICS[prefix]
            checks = {
                "source_exercise": mapping["source_exercise"],
                "source_stars": mapping["stars"],
                "topic": topic, "topic_label": label,
                "source_status": "verified",
            }
            for field, expected_value in checks.items():
                if meta.get(field) != expected_value:
                    errors.append(f"字段不一致 {field}：{key}")
            if not key.startswith(folder + "/习题/习题 " + local_id + " - "):
                errors.append(f"编号或主题路径不一致：{key}")
            if not str(meta.get("title", "")).startswith("习题 " + local_id + "："):
                errors.append(f"标题不符合编号约定：{key}")
            for field in ("title", "source", "source_refs", "created"):
                if not meta.get(field):
                    errors.append(f"缺少字段 {field}：{key}")
            if meta.get("status") not in {"not-started", "in-progress", "completed"}:
                errors.append(f"学习状态非法：{key}")
            if meta.get("difficulty") not in {"beginner", "intermediate", "advanced"}:
                errors.append(f"难度非法：{key}")
            if "exercise" not in meta.get("tags", []):
                errors.append(f"缺少 exercise 标签：{key}")
            for heading in ("题目", "提示", "解答", "相关概念", "备注"):
                if f"## {heading}\n" not in raw:
                    errors.append(f"缺少结构 {heading}：{key}")
            for fragment in ("### 英文原题", "### 中文转述", "> [!question]", "> [!hint]-", "> [!success]- 解答"):
                if fragment not in raw:
                    errors.append(f"缺少双语或 callout 结构 {fragment}：{key}")
        summaries.append({"chapter": int(chapter), "expected": len(expected), "actual": len(actual),
                          "missing": missing, "duplicates": duplicates, "extra_or_unparsed": extra})
    unknown = [path for path, meta, _ in notes if str(meta.get("source_chapter")) not in manifest["chapters"]]
    errors.extend(f"未登记章节的 DS003 习题：{path}" for path in unknown)
    print(json.dumps({"source_id": manifest["source_id"], "chapters": summaries,
                      "total_source_exercises": len(notes), "errors": errors}, ensure_ascii=False, indent=2))
    return bool(errors)


if __name__ == "__main__":
    sys.exit(main())
