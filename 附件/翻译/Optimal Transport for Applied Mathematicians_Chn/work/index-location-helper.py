from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parent.parent


def apply(rows):
    path = ROOT / "work/index-map.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    files = list((ROOT / "sections-tex").glob("*.tex"))
    files += list((ROOT / "frontmatter").glob("*.tex"))
    files += [ROOT / "Optimal Transport for Applied Mathematicians_Chn.tex"]
    done = 0
    for line in rows.strip().splitlines():
        parts = line.split("|")
        eid, page, target = parts[:3]
        entry = data["entries"][int(eid) - 1]
        ref = next(r for r in entry["references"] if r["source_printed_page"] == page)
        if target.startswith("@"):
            filename, needle = target[1:], parts[3]
            file = ROOT / filename
            source = file.read_text(encoding="utf-8")
            matches = [m.start() for m in re.finditer(re.escape(needle), source)]
            if len(matches) != 1:
                print("NEED FIX", eid, page, filename, repr(needle), "hits", len(matches))
                continue
            target = f"idx:i{eid}-p{page}"
            if rf"\label{{{target}}}" not in source:
                start = matches[0]
                source = source[:start] + rf"\phantomsection\label{{{target}}}" + "\n" + source[start:]
                file.write_text(source, encoding="utf-8")
            basis = f"原页关于{entry['english']}的段落；译文段落匹配“{needle}”"
        else:
            hits = [f for f in files if rf"\label{{{target}}}" in f.read_text(encoding="utf-8")]
            if len(hits) != 1:
                print("LABEL ERROR", eid, page, target, len(hits))
                continue
            filename = str(hits[0].relative_to(ROOT))
            basis = f"原页{entry['english']}所对应的编号陈述／知识框／专题小节，与译文{target}核对"
        ref.update(target=target, target_file=filename, basis=basis, status="verified-location")
        done += 1
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print("mapped", done, "remaining", sum(not r["target"] for e in data["entries"] for r in e["references"]))
