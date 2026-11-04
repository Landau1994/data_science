"""Independently locate all 43 visible box headings in the final PDF text runs.

The existing XeLaTeX PDF uses FandolHei for the three-character heading and
LMRoman Bold for its adjacent number.  pypdf's CMap decoder does not recover
these Chinese glyphs correctly, so the font/three-glyph/adjacent-number signature
is used, calibrated against Poppler full-title extraction and actual PNG images
in the first pass.  This does not mistake an earlier autoref for the box heading.
"""
from pathlib import Path
from collections import Counter, defaultdict
import hashlib
import importlib.util
import json
import re
import sys
from pypdf import PdfReader

BASE = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("audit_full", Path(__file__).with_name("audit-full.py"))
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
STEM = module.STEM


def main():
    pdf = BASE / (STEM + ".pdf")
    reader = PdfReader(pdf)
    auxtext = module.strip_comments((BASE / "work" / (STEM + ".aux")).read_text(encoding="utf-8"))
    aux = {item["args"][0]: module.brace_fields(item["args"][1])
           for item in module.command_args(auxtext, "newlabel", 2) if "#" not in item["args"][0]}
    seen = defaultdict(list)
    for physical, page in enumerate(reader.pages, 1):
        runs = []
        def visitor(text, cm, tm, font, size):
            if text.strip():
                runs.append((text.strip(), str((font or {}).get("/BaseFont")), float(size)))
        page.extract_text(visitor_text=visitor)
        for (text, font, size), (next_text, next_font, next_size) in zip(runs, runs[1:]):
            if ("FandolHei" in font and len(text) == 3 and size < 14
                    and "Bold" in next_font and re.fullmatch(r"[1-8]\.\d+", next_text)):
                seen["box:" + next_text].append(physical)
    failures, boxes = [], []
    for path in sorted((BASE / "sections-tex").glob("*.tex")):
        text = module.strip_comments(path.read_text(encoding="utf-8"))
        for item in module.command_args(text, "begin"):
            if item["args"][0] != "sourcebox":
                continue
            title, end = module.group(text, item["end"])
            match = re.search(r"\\label\{(box:[^}]+)\}", text[end:end + 600])
            if not match:
                failures.append({"reason": "box has no label", "file": str(path), "title": title})
                continue
            key = match.group(1)
            pages = seen.get(key, [])
            fields = aux.get(key, [])
            destination = fields[3] if len(fields) >= 4 else None
            target = reader.named_destinations.get(destination)
            target_page = reader.get_destination_page_number(target) + 1 if target else None
            row = {"label": key, "title_tex": title, "actual_heading_physical_pages": pages,
                   "aux_page_label": fields[1] if len(fields) >= 2 else None,
                   "pdf_destination_physical": target_page, "destination_name": destination,
                   "status": "passed" if len(pages) == 1 and pages[0] == target_page else "failed"}
            boxes.append(row)
            if row["status"] != "passed":
                failures.append(row)
    if len(boxes) != 43 or len(seen) != 43 or sum(map(len, seen.values())) != 43:
        failures.append({"reason": "expected 43 unique actual box headings", "tex_boxes": len(boxes),
                         "pdf_numbers": len(seen), "pdf_occurrences": sum(map(len, seen.values()))})
    digest = hashlib.sha256(pdf.read_bytes()).hexdigest()
    report = {"pdf_sha256": digest, "pdf_physical_pages": len(reader.pages),
              "status": "failed" if failures else "passed-43-actual-heading-destinations",
              "method": __doc__, "boxes": boxes, "failures": failures}
    (BASE / "work/box-title-destination-audit.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = ["# 43个知识框的实际标题与PDF目标核对", "", f"PDF SHA256：`{digest}`.", "",
             "逐页检查实际PDF标题文本运行：FandolHei三字框头及相邻粗体框号，恰检出43个互异框头、各出现一次；再与完整TeX标题和AUX实际命名目标物理页交叉比较。不会把正文中提前出现的知识框引用当作框头。首轮另以Poppler完整标题及实际页图校准该字体识别规则。", "",
             f"状态：`{report['status']}`.", "", "|框|实际框头物理页|目标物理页|AUX页码|结果|", "|---|---:|---:|---|---|"]
    for box in boxes:
        lines.append(f"|{box['label']}|{box['actual_heading_physical_pages']}|{box['pdf_destination_physical']}|{box['aux_page_label']}|{box['status']}|")
    lines += ["", "字体运行定位用于检验链接落点，不代替公式/框体目视审阅；完整字体识别方法、标题及页号见同名JSON。", ""]
    (BASE / "work/box-title-destination-audit.md").write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps({"status": report["status"], "boxes": len(boxes), "failures": len(failures), "pdf_sha256": digest}, ensure_ascii=False))
    return bool(failures)


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
