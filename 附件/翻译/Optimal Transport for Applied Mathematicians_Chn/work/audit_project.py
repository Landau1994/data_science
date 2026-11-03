"""检查当前分批译稿的结构、实际编号、书目及 PDF 链接；不代替来源和视觉审阅。"""
from collections import Counter
from pathlib import Path
import hashlib
import json
import re
from pypdf import PdfReader

BASE = Path(__file__).resolve().parent.parent
STEM = "Optimal Transport for Applied Mathematicians_Chn"
SOURCE = BASE.parent.parent / "books" / "Santambrogio 2015 Optiomal Transport For Applied Mathematicians.pdf"
files = sorted((BASE / "sections-tex").glob("*.tex")) + sorted((BASE / "frontmatter").glob("*.tex"))
texts = {str(p.relative_to(BASE)).replace("\\", "/"): p.read_text(encoding="utf-8") for p in files}
main = (BASE / (STEM + ".tex")).read_text(encoding="utf-8")
all_text = "\n".join(texts.values()) + "\n" + main
labels = re.findall(r"\\label\{([^}]+)\}", all_text)
duplicates = [k for k, n in Counter(labels).items() if n > 1]
assert not duplicates, duplicates
refs = re.findall(r"\\(?:autoref|eqref|ref)\{([^}]+)\}", all_text)
assert not set(refs) - set(labels), set(refs) - set(labels)
cites = {k.strip() for group in re.findall(r"\\cite\{([^}]+)\}", all_text) for k in group.split(",")}
bibtext = (BASE / "bib/references.bib").read_text(encoding="utf-8")
bibkeys = set(re.findall(r"@\w+\{([^,]+),", bibtext))
assert not cites - bibkeys, cites - bibkeys
assert len(bibkeys) == 300
for name, text in texts.items():
    text = re.sub(r"(?<!\\)%.*", "", text)
    stack = []
    for token in re.finditer(r"\\(begin|end)\{([^}]+)\}", text):
        kind, env = token.groups()
        if kind == "begin":
            stack.append(env)
        else:
            assert stack and stack.pop() == env, (name, token.group())
    assert not stack, (name, stack)
    assert len(re.findall(r"(?<!\\)\\\[", text)) == len(re.findall(r"(?<!\\)\\\]", text)), name
    assert len(re.findall(r"(?<!\\)\$", text)) % 2 == 0, name

aux = (BASE / "work" / (STEM + ".aux")).read_text(encoding="utf-8")
actual = {k: v.strip("{}") for k, v in re.findall(r"\\newlabel\{([^}]+)\}\{\{([^}]+)\}", aux)}
for prefix, count in [("obj:", 54), ("box:", 14), ("eq:", 8)]:
    for number in range(1, count + 1):
        assert actual.get(prefix + f"1.{number}") == f"1.{number}", (prefix, number)
assert actual["eq:DP-var"] == "DP-var"
assert actual["eq:intro1"] == "1" and actual["eq:intro2"] == "2"
bibnumbers = dict(re.findall(r"\\bibcite\{(b\d+)\}\{(\d+)\}", aux))
assert len(bibnumbers) == 300
assert all(key == "b" + value for key, value in bibnumbers.items())
pdf = PdfReader(BASE / (STEM + ".pdf"))
source = PdfReader(SOURCE)
destinations = pdf.named_destinations
linktypes = Counter()
bad_links = []
for page_number, page in enumerate(pdf.pages, 1):
    for ref in page.get("/Annots", []):
        annot = ref.get_object()
        if annot.get("/Subtype") != "/Link":
            continue
        action = annot.get("/A", {})
        kind = action.get("/S", "/Dest" if "/Dest" in annot else "unknown")
        linktypes[str(kind)] += 1
        dest = annot.get("/Dest", action.get("/D"))
        if kind == "/GoTo" and isinstance(dest, str) and dest not in destinations:
            bad_links.append((page_number, dest))
        if kind == "/GoToR":
            assert isinstance(dest, list) and 0 <= dest[0] < len(source.pages), (page_number, dest)
            target = action.get("/F")
            if isinstance(target, dict):
                target = target.get("/F")
            assert target and (BASE / str(target)).resolve().is_file(), (page_number, target)
assert not bad_links, bad_links

def count_links(pages):
    total = Counter()
    for page in pages:
        for ref in page.get("/Annots", []):
            annot = ref.get_object()
            if annot.get("/Subtype") == "/Link":
                total[str(annot.get("/A", {}).get("/S", "/Dest"))] += 1
    return dict(total)

start = pdf.get_destination_page_number(destinations["section.1"])
log = (BASE / "work" / (STEM + ".log")).read_text(encoding="utf-8", errors="replace")
for problem in ["undefined", "multiply defined", "Missing character", "Overfull", "LaTeX Error", "Token not allowed"]:
    assert not re.search(re.escape(problem), log, re.I), problem
expected_hash = (BASE / "work/source-sha256.txt").read_text(encoding="utf-8").split()[0]
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest() == expected_hash
stats = {
    "source_id": "DS026", "source_physical_pages": len(source.pages), "output_pdf_pages": len(pdf.pages),
    "source_sha256": expected_hash, "labels": len(labels), "reference_commands": len(refs),
    "citation_commands": len(re.findall(r"\\cite\{", all_text)), "citation_keys": len(cites),
    "original_pdf_reference_commands": len(re.findall(r"\\orig\{", all_text)),
    "numbered_statements": 54, "boxes": 14, "chapter_numbered_equations": 8,
    "named_equations": ["DP-var"], "intro_equations": ["1", "2"],
    "proof_environments": sum(s.count(r"\begin{proof}") for s in texts.values()),
    "unnumbered_figures": 1, "bibliography_entries": 300, "original_contents_entries": 109,
    "link_types": dict(linktypes), "named_destinations": len(destinations),
    "source_selected_links": count_links([source.pages[i] for i in list(range(85)) + list(range(361, 373))]),
    "source_chapter1_links": count_links(source.pages[28:85]),
    "output_chapter1_links": count_links(pdf.pages[start:start + 50]),
    "bad_links": bad_links,
    "translated_scope": {"front_physical": [1, 28], "chapter1_printed": [1, 57], "chapter1_physical": [29, 85], "bibliography_physical": [362, 373]},
    "files": {name: {"characters": len(text), "environments": dict(Counter(re.findall(r"\\begin\{([^}]+)\}", text)))} for name, text in texts.items()},
}
(BASE / "manifest.json").write_text(json.dumps(stats, ensure_ascii=False, indent=2), encoding="utf-8")
(BASE / "work/final-audit.json").write_text(json.dumps(stats, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps({k: v for k, v in stats.items() if k != "files"}, ensure_ascii=True, indent=2))
