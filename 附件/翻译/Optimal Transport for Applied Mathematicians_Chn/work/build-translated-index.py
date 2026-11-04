"""Generate only the translated, source-complete index from verified locations."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parent.parent
path = ROOT / "work/index-map.json"
data = json.loads(path.read_text(encoding="utf-8"))
entries = data["entries"]
english_math = {
    1: r"$H^{-1}$ norm",
    2: r"$L^\infty$ density constraints",
    3: r"$L^\infty$ transport cost",
    4: r"$\Gamma$-convergence",
    6: r"$\lambda$-convexity",
    7: r"$c$-cyclical monotonicity",
    18: r"$d_\alpha$ distance",
    66: r"in $\mathbb W_p$",
    67: r"in $\operatorname{SDiff}(\Omega)$",
}
original_ranges = {
    58: "15, 17–19, 63, 99, 109, 110",
    82: "9, 31–35",
    137: "18–20, 97, 200",
}
for entry in entries:
    eid = entry["id"]
    entry["source_index_physical_page"] = 374 if eid <= 54 else 375 if eid <= 124 else 376
    entry["source_page_expression"] = original_ranges.get(
        eid, ", ".join(r["source_printed_page"] for r in entry["references"])
    )
    entry["english_tex"] = english_math.get(eid, entry["english"])
    entry["see"] = None
    group_prefix = "0" if entry["group"] == "Symbols" else entry["group"]
    own_key = (f"{eid:03d}" if entry["level"] else f"{group_prefix}{eid:03d}")
    own_key += "@" + entry["chinese_tex"] + "（" + entry["english_tex"] + "）"
    entry["index_key"] = (
        entries[entry["parent"] - 1]["index_key"] + "!" + own_key
        if entry["level"] else own_key
    )

pending = [(e["id"], r["source_printed_page"]) for e in entries
           for r in e["references"] if not r.get("target")]
if pending:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    raise SystemExit(f"Refusing incomplete index: {len(pending)} source locations remain")

all_files = list((ROOT / "sections-tex").glob("*.tex"))
all_files += list((ROOT / "frontmatter").glob("*.tex"))
all_files += [ROOT / "Optimal Transport for Applied Mathematicians_Chn.tex"]
label_files = {}
for file in all_files:
    for label in re.findall(r"\\label\{([^}]+)\}", file.read_text(encoding="utf-8")):
        label_files.setdefault(label, []).append(str(file.relative_to(ROOT)))
for entry in entries:
    for ref in entry["references"]:
        target = ref["target"]
        assert len(label_files.get(target, [])) == 1, (target, label_files.get(target))
        ref["target_file"] = label_files[target][0]
        assert ref.get("basis"), (entry["id"], ref)
        ref["status"] = "verified-location"

registry_path = ROOT / "work/index-generated-anchors.json"
sources = {file: file.read_text(encoding="utf-8") for file in all_files}
previous = json.loads(registry_path.read_text(encoding="utf-8")) if registry_path.exists() else []
for old in previous:
    marker = r"\label{" + old["target"] + "}"
    sequence = marker + old["commands"]
    found = [file for file, text in sources.items() if sequence in text]
    assert len(found) <= 1, ("duplicate old managed anchor", old["target"])
    if found:
        sources[found[0]] = sources[found[0]].replace(sequence, marker, 1)

anchors = {}
for entry in entries:
    key = entry["index_key"]
    assert key.count("$") % 2 == 0, key
    assert key.count("{") == key.count("}"), key
    for ref in entry["references"]:
        target = ref["target"]
        anchors.setdefault(target, {}).setdefault(key, []).append({
            "entry_id": entry["id"],
            "source_printed_page": ref["source_printed_page"],
            "source_physical_page": ref["source_physical_page"],
        })
registry = []
for target, keys in anchors.items():
    marker = r"\label{" + target + "}"
    found = [file for file, text in sources.items() if marker in text]
    assert len(found) == 1, ("missing or duplicate exact target", target)
    file = found[0]
    commands = "".join(r"\index{" + key + "|hyperpage}" for key in keys)
    sources[file] = sources[file].replace(marker, marker + commands, 1)
    registry.append({
        "target": target,
        "file": str(file.relative_to(ROOT)),
        "commands": commands,
        "keys": keys,
    })
for file, text in sources.items():
    if file.read_text(encoding="utf-8") != text:
        file.write_text(text, encoding="utf-8")
registry_path.write_text(json.dumps(registry, ensure_ascii=False, indent=2), encoding="utf-8")
lines = [
    "% 原书印刷351--353／PDF物理374--376的完整中文／英文索引.",
    "% 全部356个源定位保留在work/index-map.json；精确index锚点由该表重建并按target/key去重.",
    "% 页码由makeindex读取真实译文shipout页号，hyperpage提供点击；同词同页自动合并.",
    "% 原163词条的英文顺序及主子层级由ASCII稳定排序键保留；四个无页码父项由子项自然生成.",
    "% 标题、sec:index、目录入口及multicol双栏环境由主稿的theindex环境统一提供.",
    r"\printindex",
    "",
]
out = ROOT / "backmatter/10-index.tex"
out.parent.mkdir(exist_ok=True)
out.write_text("\n".join(lines), encoding="utf-8")
data["coverage"] = {
    "main_entries": sum(e["level"] == 0 for e in entries),
    "subentries": sum(e["level"] == 1 for e in entries),
    "all_entries": len(entries),
    "source_link_annotations": 351,
    "source_locations_after_expanding_ranges": sum(len(e["references"]) for e in entries),
    "unique_source_pages": len({r["source_printed_page"] for e in entries for r in e["references"]}),
    "see_guides": 0,
    "unresolved_locations": 0,
    "unique_label_targets": len(anchors),
    "unique_index_anchors": sum(len(keys) for keys in anchors.values()),
}
path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
print(out)
print(data["coverage"])
