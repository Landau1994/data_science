"""按MAIN真实输入图执行全书编译前语言/结构检查；不代替来源忠实性审阅.

保留技能check_fidelity.py的检查意图，适配本项目递归input、复合cite键、
完整书后习题/提示及嵌套数学索引。这里只写机器检查报告，不改正文。
"""
from pathlib import Path
import argparse
import importlib.util
import json
import re
import sys

BASE = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("audit_full", Path(__file__).with_name("audit-full.py"))
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--main", type=Path, default=BASE / (module.STEM + ".tex"))
    args = parser.parse_args()
    audit = module.Audit(args)
    audit.walk(args.main.resolve())
    text = "\n".join(part for _, part in audit.segments)
    audit.body = text
    audit.check_structure()
    failures = audit.errors
    patterns = [
        (r"\\newtheorem(?:\*)?\{[^}]*\}(?:\[[^]]*\])?\{(?:Proposition|Theorem|Remark|Lemma|Corollary|Definition|Example|Problem)\}", "English-theorem-name"),
        (r"\\(?:providecommand|renewcommand)\*?\{\\[A-Za-z]*autorefname\}\{(?:Proposition|Theorem|Remark|Lemma|Corollary|Definition|Figure|Table)\}", "English-autoref-name"),
        (r"\\renewcommand\{\\proofname\}\{Proof\}", "English-proofname"),
        (r"\\renewcommand\{\\(?:figure|table)name\}\{(?:Figure|Table)\}", "English-caption-name"),
        (r"\[概述\]|详见原论文|完整证明见", "abbreviated-proof-review-needed"),
    ]
    for pattern, code in patterns:
        for match in re.finditer(pattern, text):
            failures.append({"code": code, "detail": match.group()})
    for item in module.command_args(text, "begin"):
        if item["args"][0] != "proof":
            continue
        tail = text[item["end"]:]
        if tail.lstrip().startswith("["):
            title, _ = module.group(tail, 0, "[", "]")
            if re.search(r"\bProof\b", title, re.I):
                failures.append({"code": "English-proof-title", "detail": title})
    begins = len(re.findall(r"\\begin\s*\{proof\}", text))
    ends = len(re.findall(r"\\end\s*\{proof\}", text))
    if begins != ends or begins != 154:
        failures.append({"code": "full-proof-count", "detail": [begins, ends], "expected": 154})
    keys = set(re.findall(r"@\w+\s*\{\s*([^,\s]+)\s*,", (BASE / "bib/references.bib").read_text(encoding="utf-8")))
    cited = {key.strip() for item in module.command_args(text, "cite", optional=True) for key in item["args"][0].split(",") if "#" not in key}
    if cited - keys:
        failures.append({"code": "undefined-citation", "detail": sorted(cited - keys)})
    report = {"scope": "最终MAIN递归input图：前置、1–8章、69题、69提示及索引入口", "status": "failed" if failures else "passed-language-and-structure-checks", "input_files": [module.rel(p) for p in audit.files], "proof_begin": begins, "proof_end": ends, "citation_keys": len(cited), "bibliography_keys": len(keys), "failures": failures, "limitations": "自动语言/结构检查，不代表已逐页核对来源或最终PDF。技能原文件未改。"}
    (BASE / "work/fidelity-static-full.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in report.items() if key != "input_files"}, ensure_ascii=False))
    return bool(failures)


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
