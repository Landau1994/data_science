"""UDL 归档对账与手动预览；不记录抽样历史，不改学习状态。"""

from __future__ import annotations

import argparse
from collections import Counter
from datetime import date
import hashlib
import json
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = Path(__file__).with_name("source-manifest.json")
BEGIN = "<!-- UDL-PREVIEW:BEGIN -->"
END = "<!-- UDL-PREVIEW:END -->"
STATES = {"not-started", "in-progress", "completed"}


def metadata(path: Path) -> tuple[dict, str]:
    """读取本库受控笔记使用的顶层标量；不执行模板或 YAML 标签。"""
    text = path.read_text(encoding="utf-8-sig")
    match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", text, re.S)
    if not match:
        raise ValueError(f"缺少元数据：{path.relative_to(ROOT)}")
    fields = {}
    for line in match.group(1).splitlines():
        item = re.match(r"^([a-z_]+):\s*(.*?)\s*$", line)
        if not item:
            continue
        key, value = item.groups()
        if key in fields:
            raise ValueError(f"重复字段 {key}：{path.relative_to(ROOT)}")
        if value.startswith(('"', "[")):
            value = json.loads(value)
        elif value.startswith("'") and value.endswith("'"):
            value = value[1:-1].replace("''", "'")
        fields[key] = value
    return fields, text


def inside(relative: str) -> Path:
    path = (ROOT / relative).resolve()
    if not path.is_relative_to(ROOT):
        raise ValueError("文件位置超出本知识库")
    return path


def audit(manifest: dict, chapter: int) -> dict:
    spec = manifest["chapters"][str(chapter)]
    expected = spec["expected_exercises"]
    expected_set = set(expected)
    errors = []
    if len(expected_set) != len(expected):
        errors.append("来源清单含重复题号")
    mapped = spec["exercises"]
    mapping_keys = [item["source_exercise"] for item in mapped]
    if mapping_keys != expected:
        errors.append("映射未按已核对的有序题号集合列出")
    if len({item["note"] for item in mapped}) != len(mapped):
        errors.append("不同题号指向同一篇笔记")
    source = inside(manifest["source_file"])
    if not source.is_file():
        errors.append("原始 PDF 文件不存在")
    elif hashlib.sha256(source.read_bytes()).hexdigest() != manifest["source_sha256"]:
        errors.append("原始 PDF 已变化，请重新核对版本与题号")

    found = []
    unparseable = []
    states = {}
    for path in sorted(ROOT.glob("[0-9][0-9] - */习题/*.md")):
        try:
            fields, text = metadata(path)
        except (ValueError, json.JSONDecodeError) as exc:
            # 不能跳过损坏的元数据并宣称对账通过。
            unparseable.append(str(path.relative_to(ROOT)))
            continue
        if fields.get("source_id") != manifest["source_id"]:
            continue
        source_chapter = fields.get("source_chapter", "")
        if not re.fullmatch(r"[1-9][0-9]*", str(source_chapter)):
            unparseable.append(str(path.relative_to(ROOT)))
            continue
        key = str(fields.get("source_exercise", ""))
        if not re.fullmatch(r"[0-9]+\.[0-9]+", key):
            unparseable.append(str(path.relative_to(ROOT)))
            continue
        if key.split(".", 1)[0] != str(source_chapter):
            errors.append(f"来源章号与题号不一致：{path.relative_to(ROOT)}")
        if str(source_chapter) != str(chapter):
            continue
        relative = path.relative_to(ROOT).as_posix()
        if not re.fullmatch(r"习题 (?:P|ST|LA|ML|PM|DL|CI|TS|DC|AE)[0-9]+ - .+\.md", path.name):
            errors.append(f"习题文件名不符合约定：{relative}")
        found.append((key, relative))
        states[relative] = fields.get("status")
        if fields.get("status") not in STATES:
            errors.append(f"学习状态非法：{relative}")
        for required in ("title", "topic", "topic_label", "difficulty", "source", "source_refs", "created"):
            if not fields.get(required):
                errors.append(f"缺少字段 {required}：{relative}")
        if not re.search(r"(?:^|\n)\s*- exercise(?:\s|$)", text):
            errors.append(f"缺少 exercise 标签：{relative}")
        if fields.get("difficulty") not in {"beginner", "intermediate", "advanced"}:
            errors.append(f"难度字段非法：{relative}")
        topic_folders = {
            "probability-theory": "01 - 概率论",
            "mathematical-statistics": "02 - 数理统计",
            "linear-algebra-optimization": "03 - 线性代数与优化",
            "statistical-learning": "04 - 统计学习",
            "probabilistic-models": "05 - 概率模型与推断",
            "deep-learning": "06 - 深度学习",
            "causal-inference": "07 - 因果推断与实验设计",
            "stochastic-processes": "08 - 随机过程与时间序列",
            "data-computing": "09 - 数据计算与可复现性",
            "ai-engineering": "10 - AI工程",
        }
        if topic_folders.get(fields.get("topic")) != path.relative_to(ROOT).parts[0]:
            errors.append(f"主题与实际路径不一致：{relative}")
        for heading in ("题目", "提示", "解答", "相关概念", "备注"):
            if f"## {heading}" not in text:
                errors.append(f"缺少结构 {heading}：{relative}")
        if "> [!success]- 解答\n" not in text:
            errors.append(f"解答折叠标题不符：{relative}")
        if manifest.get("source_language") == "en":
            for heading in ("### 英文原题", "### 中文转述"):
                if heading not in text:
                    errors.append(f"缺少英文教材双语题目结构 {heading}：{relative}")

    counts = Counter(key for key, _ in found)
    missing = [key for key in expected if counts[key] == 0]
    duplicate = [key for key, count in counts.items() if count > 1]
    extra = sorted(set(counts) - expected_set)
    actual_map = {key: path for key, path in found}
    for item in mapped:
        if item["source_exercise"] in actual_map and actual_map[item["source_exercise"]] != item["note"]:
            errors.append(f"笔记位置与清单不一致：{item['source_exercise']}")
    passed = not (missing or duplicate or extra or unparseable or errors)
    return {
        "source_id": manifest["source_id"], "chapter": chapter,
        "expected_exercises": expected, "expected_count": len(expected),
        "actual_count": len(found), "missing": missing, "duplicate": duplicate,
        "extra": extra, "unparseable": unparseable, "errors": errors,
        "passed": passed, "learning_states": states,
    }


def preview(manifest: dict, chapter: int, count: int, day: str, report: dict) -> Path:
    date.fromisoformat(day)
    if not report["passed"]:
        raise ValueError("来源映射对账未通过，不能生成预览")
    spec = manifest["chapters"][str(chapter)]
    eligible = [item for item in spec["exercises"] if report["learning_states"][item["note"]] != "completed"]
    if count < 1 or count > len(eligible):
        raise ValueError(f"题量应在 1–{len(eligible)} 之间")
    selected = eligible[:count]
    lines = [BEGIN, "## 本次预览", "",
             f"来源：[[00 - 首页/教材归档/DS001 - Understanding Deep Learning|UDL 学习台账]]，第 {chapter} 章 {spec['title_zh']}（{spec['title_en']}）。", "",
             "选题方式：按来源题号顺序选取尚未完成的笔记。本次为手动预览，不写入抽样历史，不修改学习状态。", "",
             f"核对结果：预期 {report['expected_count']} 题，已映射 {report['actual_count']} 题；缺失、重复、多余、无法解析均为 0。", "",
             "先在英文纸书中按章号、题号定位；具体纸书页码尚未逐项对齐。尝试作答后，再展开笔记内提示和解答。", ""]
    for index, item in enumerate(selected, 1):
        target = item["note"][:-3]
        star = "（原书星号题）" if item.get("starred") else ""
        lines.append(f"{index}. [[{target}|{item['local_id']}：{item['title_zh']}]] — 原题 {item['source_exercise']}{star}。")
    lines.extend(["", "### 阅读与作答", "", "- 建议先读本章第 2.1–2.3 节，再独立尝试题目。", "- 本页的生成不代表已经开始或完成学习；需要调整学习状态时，以习题笔记为准。", "", END])
    block = "\n".join(lines)
    output = inside(f"12 - 每日题单/UDL 试运行 - {day}.md")
    if output.exists():
        original = output.read_text(encoding="utf-8")
        if original.count(BEGIN) != 1 or original.count(END) != 1 or original.index(BEGIN) > original.index(END):
            raise ValueError("已有文件的受管理区块缺失或不唯一，已保留原文")
        start, finish = original.index(BEGIN), original.index(END) + len(END)
        updated = original[:start] + block + original[finish:]
    else:
        updated = (f'---\ntitle: "UDL 试运行题单（{day}）"\ntags:\n  - exercise-sheet\nsource_id: DS001\nmode: preview\ncreated: {day}\n---\n\n'
                   f'# UDL 试运行题单（{day}）\n\n{block}\n\n## 我的作答与备注\n\n')
    output.parent.mkdir(parents=True, exist_ok=True)
    if not output.exists() or output.read_text(encoding="utf-8") != updated:
        output.write_text(updated, encoding="utf-8")
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["audit", "preview"])
    parser.add_argument("--chapter", type=int, default=2)
    parser.add_argument("--count", type=int, default=3)
    parser.add_argument("--date", help="预览题单日期，例如 2026-10-24")
    args = parser.parse_args()
    try:
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        report = audit(manifest, args.chapter)
        if args.command == "preview":
            if not args.date:
                raise ValueError("生成预览时必须给出 --date")
            report["output"] = str(preview(manifest, args.chapter, args.count, args.date, report).relative_to(ROOT))
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 0 if report["passed"] else 1
    except (OSError, ValueError, KeyError) as exc:
        print(f"UDL 工具停止：{exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
