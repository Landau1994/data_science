"""Audit the FINAL main input graph and compiled book; never compile or repair files.

Run only after the final MAIN/PDF/AUX/BBL/LOG are ready.  This is an automated
structure/link audit, not a substitute for source-fidelity or page-image review.
The old 94-page/chapter-1 manifest is read only for the immutable source hash.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlparse

from pypdf import PdfReader
from pypdf.generic import IndirectObject


BASE = Path(__file__).resolve().parent.parent
STEM = "Optimal Transport for Applied Mathematicians_Chn"
SOURCE_NAME = "Santambrogio 2015 Optiomal Transport For Applied Mathematicians.pdf"
SOURCE_SHA256 = "7820e876d4312d7355f0a1549b2af2186594eebef8d411d651c6235b8c119b68"
# Independent, source-reviewed inventories, not inferred from whatever is input.
# Order: shared numbered statements, numbered equations, boxes, numbered figures.
EXPECTED = {
    1: (54, 8, 14, 0), 2: (26, 8, 4, 5), 3: (28, 8, 3, 5),
    4: (46, 35, 6, 7), 5: (36, 7, 2, 4), 6: (5, 4, 8, 5),
    7: (32, 4, 3, 1), 8: (11, 28, 3, 0),
}
EXPECTED_PROOFS = {1: 41, 2: 12, 3: 20, 4: 19, 5: 28, 6: 3, 7: 23, 8: 8}
EXPECTED_FOOTNOTES = {1: 15, 2: 0, 3: 4, 4: 22, 5: 7, 6: 10, 7: 5, 8: 4}
SOURCE_UNITS = [
    ("front", 1, 28), ("chapter1", 29, 85), ("chapter2", 86, 112),
    ("chapter3", 113, 145), ("chapter4", 146, 200),
    ("chapter5", 201, 242), ("chapter6", 243, 272),
    ("chapter7", 273, 308), ("chapter8", 309, 347),
    ("exercises", 348, 357), ("hints", 358, 361),
    ("bibliography", 362, 373), ("index", 374, 376),
]
FRONT_FILES = {
    "frontmatter/00-title.tex", "frontmatter/00-publication.tex",
    "frontmatter/00-preface.tex", "frontmatter/00-introduction.tex",
    "frontmatter/00-acknowledgments.tex", "frontmatter/00-source-contents.tex",
    "frontmatter/00-notation.tex",
}
NUMBERED_ENVS = {
    "theorem", "definition", "lemma", "corollary", "remark", "example",
    "proposition", "problem",
}
COMMAND = re.compile(r"\\([A-Za-z@]+)(\*)?")


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def strip_comments(text):
    """A percent is escaped iff preceded by an odd number of backslashes."""
    out = []
    for line in text.splitlines(keepends=True):
        cut = len(line)
        for pos, char in enumerate(line):
            if char != "%":
                continue
            back = pos - 1
            while back >= 0 and line[back] == "\\":
                back -= 1
            if (pos - back - 1) % 2 == 0:
                cut = pos
                break
        out.append(line[:cut] + ("\n" if cut < len(line) else ""))
    return "".join(out)


def escaped(text, pos):
    back = pos - 1
    while back >= 0 and text[back] == "\\":
        back -= 1
    return (pos - back - 1) % 2 == 1


def skip_space(text, pos):
    while pos < len(text) and text[pos].isspace():
        pos += 1
    return pos


def group(text, pos, opening="{", closing="}"):
    """Read one balanced argument without flattening nested TeX groups."""
    pos = skip_space(text, pos)
    if pos >= len(text) or text[pos] != opening:
        raise ValueError(f"expected {opening!r} at character {pos}")
    start, depth = pos + 1, 1
    pos += 1
    while pos < len(text):
        if not escaped(text, pos):
            if text[pos] == opening:
                depth += 1
            elif text[pos] == closing:
                depth -= 1
                if depth == 0:
                    return text[start:pos], pos + 1
        pos += 1
    raise ValueError(f"unclosed {opening!r} argument from character {start - 1}")


def brace_fields(text):
    fields, pos = [], 0
    while skip_space(text, pos) < len(text):
        value, pos = group(text, pos)
        fields.append(value)
    return fields


def command_args(text, name, required=1, optional=False):
    """Yield literal command arguments, preserving nested braces and positions."""
    for match in COMMAND.finditer(text):
        if match.group(1) != name or escaped(text, match.start()):
            continue
        pos, opt = match.end(), None
        try:
            if optional and text[skip_space(text, pos):].startswith("["):
                opt, pos = group(text, pos, "[", "]")
            args = []
            for _ in range(required):
                value, pos = group(text, pos)
                args.append(value)
        except ValueError:
            # A command definition such as \let\ref... is not an invocation.
            continue
        yield {"start": match.start(), "end": pos, "star": bool(match.group(2)),
               "optional": opt, "args": args}


def rel(path):
    try:
        return Path(path).resolve().relative_to(BASE).as_posix()
    except ValueError:
        return str(Path(path).resolve())


class Audit:
    def __init__(self, args):
        self.args = args
        self.errors = []
        self.warnings = []
        self.stats = {}
        self.files = {}
        self.edges = []
        self.segments = []
        self.dependencies = set()

    def error(self, code, detail, **context):
        self.errors.append({"code": code, "detail": detail, **context})

    def warn(self, code, detail, **context):
        self.warnings.append({"code": code, "detail": detail, **context})

    def resolve_input(self, value, parent):
        value = value.strip()
        if not value or any(char in value for char in "#{}") or "\\" in value:
            self.error("dynamic-input", "不能把动态文件名当作已核实输入", value=value)
            return None
        path = Path(value)
        if not path.suffix:
            path = path.with_suffix(".tex")
        choices = [path] if path.is_absolute() else [BASE / path, parent.parent / path]
        found = list(dict.fromkeys(p.resolve() for p in choices if p.is_file()))
        if not found:
            self.error("missing-input", "主文件输入图缺少文件", value=value, parent=rel(parent))
            return None
        if len(found) > 1:
            self.error("ambiguous-input", "文件名在根目录和当前目录解析成不同文件", value=value)
        return found[0]

    def walk(self, path, active=()):
        path = path.resolve()
        if path in active:
            self.error("input-cycle", "输入图存在循环", path=rel(path))
            return
        if path in self.files:
            self.error("duplicate-input", "同一文件被主稿重复输入", path=rel(path))
            return
        if not path.is_file():
            self.error("missing-main", "主文件不存在", path=str(path))
            return
        raw = path.read_text(encoding="utf-8")
        text = strip_comments(raw)
        text = re.split(r"\\endinput(?![A-Za-z@])", text, maxsplit=1)[0]
        self.files[path] = text
        self.dependencies.add(path)
        if re.search(r"\\includeonly(?![A-Za-z@])", text):
            self.error("includeonly", "最终全书主稿不应采用部分includeonly", path=rel(path))
        cursor = 0
        matches = sorted(list(command_args(text, "input")) + list(command_args(text, "include")),
                         key=lambda m: m["start"])
        for item in matches:
            self.segments.append((path, text[cursor:item["start"]]))
            child = self.resolve_input(item["args"][0], path)
            if child:
                self.edges.append({"from": rel(path), "to": rel(child)})
                self.walk(child, active + (path,))
            cursor = item["end"]
        self.segments.append((path, text[cursor:]))

    def static(self):
        self.walk(self.args.main)
        joined = "\n".join(text for _, text in self.segments)
        self.joined = joined
        start = re.search(r"\\begin\s*\{document\}", joined)
        end = re.search(r"\\end\s*\{document\}", joined)
        if len(re.findall(r"\\begin\s*\{document\}", joined)) != 1 or len(re.findall(r"\\end\s*\{document\}", joined)) != 1:
            self.error("document-boundary", "begin/end document必须各出现一次")
        self.body = joined[start.end():end.start()] if start and end and start.end() < end.start() else joined
        paths = {rel(path) for path in self.files}
        for path in sorted(FRONT_FILES - paths):
            self.error("front-coverage", "前置文件没有进入MAIN输入图", path=path)
        for path in ["backmatter/09-exercises.tex", "backmatter/09-hints.tex", "backmatter/10-index.tex"]:
            if path not in paths:
                self.error("back-coverage", "全书书后部分没有进入MAIN输入图", path=path)
        self.check_structure()
        self.check_number_inventory()
        self.check_source_counts()
        self.check_references()
        self.check_bibliography()
        self.check_assets()
        self.check_index()
        contents = next((s for p, s in self.files.items() if rel(p) == "frontmatter/00-source-contents.tex"), "")
        rows = [line for line in contents.splitlines() if line.count("&") == 2 and not line.lstrip().startswith(r"\textbf{编号}")]
        if len(rows) != 109:
            self.error("original-contents", "原书目录应保留109行全部层级", actual=len(rows), expected=109)
        self.stats["original_contents_entries"] = len(rows)
        orig = list(command_args(self.body, "orig", required=2))
        self.stats["original_pdf_reference_commands"] = len(orig)
        if orig:
            self.error("remaining-orig", "完整译稿仍有orig回源引用，须核实是否漏做内部目标", pages=[x["args"][0] for x in orig])
        self.stats["input_files"] = [rel(p) for p in self.files]
        self.stats["input_edges"] = self.edges
        self.stats["environment_counts"] = dict(Counter(re.findall(r"\\begin\s*\{([^}]+)\}", self.body)))
        self.stats["static_input_graph_status"] = "failed" if self.errors else "passed"
        self.stats["static_input_graph_failures"] = list(self.errors)

    def check_structure(self):
        for path, text in self.files.items():
            # A proof or tcolorbox may be defined in the preamble in two braces;
            # the begin/end order nevertheless remains balanced in this project.
            stack = []
            for match in re.finditer(r"\\(begin|end)\s*\{([^}]+)\}", text):
                kind, env = match.groups()
                if kind == "begin":
                    stack.append(env)
                elif not stack or stack.pop() != env:
                    self.error("environment", "环境不匹配", path=rel(path), environment=env)
            if stack:
                self.error("environment", "环境未闭合", path=rel(path), remaining=stack)
            dollars = sum(c == "$" and not escaped(text, i) for i, c in enumerate(text))
            if dollars % 2:
                self.error("math-delimiter", "美元定界符为奇数", path=rel(path))
            for left, right in [(r"\[", r"\]"), (r"\(", r"\)")]:
                counts = [sum(not escaped(text, m.start()) for m in re.finditer(re.escape(token), text)) for token in [left, right]]
                if counts[0] != counts[1]:
                    self.error("math-delimiter", "数学定界符不配对", path=rel(path), pair=[left, right])
            depth = 0
            for i, char in enumerate(text):
                if escaped(text, i):
                    continue
                depth += (char == "{") - (char == "}")
                if depth < 0:
                    break
            if depth:
                self.error("brace-balance", "花括号未配对", path=rel(path), depth=depth)
        for env in NUMBERED_ENVS:
            for item in command_args(self.body, "begin", optional=False):
                if item["args"][0] != env:
                    continue
                tail = self.body[item["end"]:]
                if tail.lstrip().startswith("["):
                    title, _ = group(tail, 0, "[", "]")
                    if re.fullmatch(r"\s*(?:[1-8]\.)?\d+\s*", title):
                        self.error("number-in-title", "原编号不得放入定理可选标题", environment=env, title=title)

    def check_number_inventory(self):
        definitions = defaultdict(list)
        for path, text in self.files.items():
            for item in command_args(text, "label"):
                key = item["args"][0]
                if "#" not in key:
                    definitions[key].append(rel(path))
        hints = [int(x) for x in re.findall(r"\\begin\s*\{sourcehint\}\s*\{(\d+)\}", self.body)]
        for number in hints:
            definitions[f"hint:{number}"].append("sourcehint environment")
        self.labels = definitions
        for label, places in definitions.items():
            if len(places) != 1:
                self.error("duplicate-label", "标签必须唯一", label=label, places=places)
        for chapter in range(1, 9):
            if f"sec:{chapter}" not in definitions:
                self.error("chapter-coverage", "未输入该章", chapter=chapter)
        for chapter, counts in EXPECTED.items():
            for prefix, total in zip(["obj", "eq", "box", "fig"], counts):
                expected = {f"{prefix}:{chapter}.{n}" for n in range(1, total + 1)}
                actual = {k for k in definitions if re.fullmatch(fr"{prefix}:{chapter}\.\d+", k)}
                if actual != expected:
                    self.error("numbered-coverage", "原编号标签集合不符", chapter=chapter, prefix=prefix,
                               missing=sorted(expected - actual), extra=sorted(actual - expected))
        exercises = [int(n) for n in re.findall(r"\\label\s*\{ex:(\d+)\}", self.body)]
        for name, sequence in [("exercises", exercises), ("hints", hints)]:
            if sequence != list(range(1, 70)):
                self.error("exercise-hint-order", "应恰为有序1–69且无重复", kind=name, actual=sequence)
        if len(re.findall(r"\\begin\s*\{exercise\}", self.body)) != 69:
            self.error("exercise-count", "习题环境应为69个")
        self.stats["expected_chapter_numbering"] = {str(k): dict(zip(["statements", "equations", "boxes", "figures"], v)) for k, v in EXPECTED.items()}
        self.stats["labels"] = len(definitions)
        self.stats["exercises"] = len(exercises)
        self.stats["hints"] = len(hints)

    def check_source_counts(self):
        chapters = defaultdict(lambda: Counter(proofs=0, footnotes=0, graphics=0))
        front = Counter(proofs=0, footnotes=0, graphics=0)
        exercises = Counter(proofs=0, footnotes=0, graphics=0)
        for path, text in self.files.items():
            name = rel(path)
            match = re.match(r"sections-tex/0([1-8])-", name)
            counter = chapters[int(match.group(1))] if match else front if name.startswith("frontmatter/") else exercises if name.startswith("backmatter/09-exercises") else None
            if counter is None:
                continue
            counter["proofs"] += len(re.findall(r"\\begin\s*\{proof\}", text))
            counter["footnotes"] += len(list(command_args(text, "footnote", optional=True)))
            counter["graphics"] += len(list(command_args(text, "includegraphics", optional=True)))
        for chapter in range(1, 9):
            for kind, expected in [("proofs", EXPECTED_PROOFS[chapter]), ("footnotes", EXPECTED_FOOTNOTES[chapter]), ("graphics", EXPECTED[chapter][3] + (1 if chapter in [1, 2, 4] else 0))]:
                if chapters[chapter][kind] != expected:
                    self.error("source-inventory", "按原页独立盘点的章内数量不符", chapter=chapter, kind=kind, expected=expected, actual=chapters[chapter][kind])
        if front["footnotes"] != 5 or exercises["footnotes"] != 1 or exercises["graphics"] != 2:
            self.error("front-exercise-inventory", "前置应5脚注，习题应1脚注和2图", front=dict(front), exercises=dict(exercises))
        self.stats["chapter_source_counts"] = {str(n): dict(c) for n, c in chapters.items()}
        self.stats["front_source_counts"] = dict(front)
        self.stats["exercise_source_counts"] = dict(exercises)
        self.stats["proof_environments"] = sum(c["proofs"] for c in chapters.values())
        self.stats["chapter_footnotes"] = sum(c["footnotes"] for c in chapters.values())

    def check_references(self):
        refs, expected = [], Counter()
        for name in ["autoref", "eqref", "ref", "pageref", "nameref", "cref", "Cref"]:
            for item in command_args(self.body, name):
                for key in item["args"][0].split(","):
                    key = key.strip()
                    if "#" in key:
                        continue
                    refs.append(key)
                    if not item["star"]:
                        expected[key] += 1
        for item in command_args(self.body, "hyperref", optional=True):
            if item["optional"] and "#" not in item["optional"]:
                refs.append(item["optional"])
                expected[item["optional"]] += 1
        for label in sorted(set(refs) - self.labels.keys()):
            self.error("undefined-reference", "引用目标不在实际输入图", label=label)
        # Every sourcehint renders one link to its matching exercise at run time.
        for number in range(1, 70):
            expected[f"ex:{number}"] += 1
        self.expected_label_links = expected
        self.stats["reference_commands"] = len(refs)

    def check_bibliography(self):
        resources = []
        for item in command_args(self.body, "bibliography"):
            resources += [v.strip() for v in item["args"][0].split(",")]
        for item in command_args(self.joined, "addbibresource", optional=True):
            resources.append(item["args"][0])
        if not resources:
            self.error("bibliography-missing", "MAIN没有输入书目数据库")
        keys = []
        for value in resources:
            path = BASE / value
            if path.suffix != ".bib":
                path = path.with_suffix(".bib")
            if not path.is_file():
                self.error("bibliography-file", "书目文件缺失", path=str(path))
                continue
            self.dependencies.add(path.resolve())
            keys += re.findall(r"@\w+\s*\{\s*([^,\s]+)\s*,", path.read_text(encoding="utf-8"))
        expected = {f"b{n}" for n in range(1, 301)}
        if Counter(keys) != Counter(expected):
            self.error("bibliography-keys", "书目必须恰为b1–b300且无重复", count=len(keys),
                       missing=sorted(expected - set(keys)), extra=sorted(set(keys) - expected))
        cites = Counter()
        citation_commands = 0
        for name in ["cite", "citep", "citet", "parencite", "textcite"]:
            for item in command_args(self.body, name, optional=True):
                citation_commands += 1
                cites.update(v.strip() for v in item["args"][0].split(",") if "#" not in v)
        for key in sorted(set(cites) - set(keys)):
            self.error("undefined-citation", "文献引用键不存在", key=key)
        if not any(item["args"][0].strip() == "*" for item in command_args(self.body, "nocite")):
            self.error("bibliography-completeness", "必须保留全部300条原书目，MAIN应nocite{*}")
        self.cites = cites
        self.stats["bibliography_entries"] = len(keys)
        self.stats["citation_commands"] = citation_commands
        self.stats["citation_keys"] = len(cites)

    def check_assets(self):
        assets = []
        for path, text in self.files.items():
            for item in command_args(text, "includegraphics", optional=True):
                value = item["args"][0]
                candidate = BASE / value
                choices = [candidate] if candidate.suffix else [candidate.with_suffix(s) for s in [".pdf", ".png", ".jpg", ".jpeg", ".eps"]]
                found = next((c.resolve() for c in choices if c.is_file()), None)
                if found is None:
                    self.error("missing-graphic", "图件不存在", parent=rel(path), graphic=value)
                    continue
                self.dependencies.add(found)
                if found.stat().st_size == 0:
                    self.error("empty-graphic", "图件为空", graphic=rel(found))
                assets.append(rel(found))
        self.stats["graphic_occurrences"] = assets

    def check_index(self):
        path = BASE / "work/index-map.json"
        self.index = None
        if not path.is_file():
            self.error("index-map", "完整索引映射缺失")
            return
        data = json.loads(path.read_text(encoding="utf-8"))
        entries = data.get("entries", [])
        self.index = data
        if [e.get("id") for e in entries] != list(range(1, 164)):
            self.error("index-entries", "索引必须恰为原163词条并保持顺序")
        levels = Counter(e.get("level") for e in entries)
        if levels != Counter({0: 143, 1: 20}):
            self.error("index-levels", "原索引应为143主项、20子项", actual=dict(levels))
        by_id = {e.get("id"): e for e in entries}
        for entry in entries:
            parent = entry.get("parent")
            if entry.get("level") == 0 and parent is not None:
                self.error("index-parent", "主项不应有父项", id=entry.get("id"))
            if entry.get("level") == 1 and (parent not in by_id or by_id[parent].get("level") != 0 or parent >= entry["id"]):
                self.error("index-parent", "子项父项无效", id=entry.get("id"), parent=parent)
            group_prefix = "0" if entry.get("group") == "Symbols" else entry.get("group", "")
            own_key = (f"{entry['id']:03d}" if entry.get("level") else f"{group_prefix}{entry['id']:03d}")
            own_key += "@" + entry["chinese_tex"] + "（" + entry.get("english_tex", entry["english"]) + "）"
            expected_key = by_id[parent].get("index_key", "") + "!" + own_key if entry.get("level") == 1 else own_key
            if entry.get("index_key") != expected_key:
                self.error("index-key", "索引排序键、显示文字或主子项组合不符", id=entry["id"])
            expression = entry.get("source_page_expression", "")
            expanded, _ = expand_expression(expression)
            actual = [str(r.get("source_printed_page")) for r in entry.get("references", [])]
            if actual != expanded:
                self.error("index-page-expression", "原页号序列与范围展开不符", id=entry.get("id"), expression=expression, actual=actual)
            for reference in entry.get("references", []):
                target = reference.get("target")
                if not target or target not in self.labels:
                    self.error("index-target", "索引目标不在MAIN真实输入图", id=entry.get("id"), target=target)
                if not reference.get("basis"):
                    self.error("index-basis", "索引没有逐条定位依据", id=entry.get("id"))
                if reference.get("target_file") and self.labels.get(target) != [reference["target_file"].replace("\\", "/")]:
                    self.error("index-target-file", "索引记录的目标文件不符", id=entry.get("id"), target=target)
        empty = [e.get("english") for e in entries if not e.get("references")]
        if empty != ["geodesics", "networks", "rectifiability", "regularity"]:
            self.error("index-empty-parents", "无页码父项应完整保留", actual=empty)
        if by_id.get(161, {}).get("parent") != 159:
            self.error("index-wasserstein", "Wasserstein spaces必须保持为Wasserstein distance子项")
        if any(e.get("see") for e in entries):
            self.error("index-see", "本底本索引无see引导，不应新增")
        index_file = next((s for p, s in self.files.items() if rel(p) == "backmatter/10-index.tex"), "")
        if len(list(command_args(index_file, "printindex", required=0))) != 1:
            self.error("index-printindex", "最终索引应通过一次printindex读取动态makeindex结果")
        expected_anchors = defaultdict(lambda: defaultdict(list))
        for entry in entries:
            for reference in entry.get("references", []):
                expected_anchors[reference.get("target")][entry.get("index_key")].append({
                    "entry_id": entry["id"], "source_printed_page": reference["source_printed_page"],
                    "source_physical_page": reference["source_physical_page"],
                })
        self.index_anchors = expected_anchors
        registry_path = BASE / "work/index-generated-anchors.json"
        if not registry_path.is_file():
            self.error("index-registry", "缺少逐目标索引锚点登记")
        else:
            registry = json.loads(registry_path.read_text(encoding="utf-8"))
            if Counter(item.get("target") for item in registry) != Counter(expected_anchors.keys()):
                self.error("index-registry-targets", "索引登记的目标集合与完整映射不符")
            file_contents = {rel(path): text for path, text in self.files.items()}
            for item in registry:
                target = item.get("target")
                keys = expected_anchors.get(target, {})
                if item.get("keys") != dict(keys):
                    self.error("index-registry-sources", "索引登记漏掉来源引用或多加引用", target=target)
                commands = "".join(r"\index{" + key + "|hyperpage}" for key in keys)
                if item.get("commands") != commands:
                    self.error("index-registry-commands", "登记的index命令与对应词条不符", target=target)
                name = item.get("file", "").replace("\\", "/")
                text = file_contents.get(name, "")
                if text.count(r"\label{" + str(target) + "}" + commands) != 1:
                    self.error("index-anchor-location", "每个索引命令必须紧随已核实目标标签且恰出现一次", target=target, path=name)
        actual_commands = Counter(item["args"][0] for item in command_args(self.body, "index"))
        expected_commands = Counter(key + "|hyperpage" for keys in expected_anchors.values() for key in keys)
        if actual_commands != expected_commands:
            self.error("index-command-set", "实际输入图中的index命令集合与逐目标去重后的完整356来源定位不符", actual=sum(actual_commands.values()), expected=sum(expected_commands.values()))
        self.stats["index"] = {"entries": len(entries), "main_entries": levels[0], "subentries": levels[1],
                               "expanded_locations": sum(len(e.get('references', [])) for e in entries),
                               "unique_label_targets": len(expected_anchors), "unique_index_commands": sum(expected_commands.values()), "empty_parents": empty}

    def source(self):
        path = self.args.source
        if not path.is_file():
            self.error("source-missing", "原PDF不存在", path=str(path))
            return None
        digest = sha(path)
        if digest != SOURCE_SHA256:
            self.error("source-sha256", "原PDF的SHA256与既定底本不符", actual=digest, expected=SOURCE_SHA256)
        ledger = BASE / "work/source-sha256.txt"
        if not ledger.is_file() or ledger.read_text(encoding="utf-8").split()[0].lower() != SOURCE_SHA256:
            self.error("source-hash-ledger", "既有源哈希记录缺失或不一致")
        manifest = BASE / "manifest.json"
        if manifest.is_file():
            prior = json.loads(manifest.read_text(encoding="utf-8"))
            old_hash = prior.get("source_sha256")
            if old_hash and old_hash != SOURCE_SHA256:
                self.error("source-hash-manifest", "原manifest所记录的底本不同", previous=old_hash)
        reader = PdfReader(path)
        if len(reader.pages) != 376:
            self.error("source-pages", "底本应为376物理页", actual=len(reader.pages))
        self.stats["source_sha256"] = digest
        self.stats["source_physical_pages"] = len(reader.pages)
        return reader

    def compiled(self):
        build = self.args.build_dir
        files = {suffix: build / (self.args.main.stem + suffix) for suffix in [".aux", ".bbl", ".log"]}
        if any(not p.is_file() for p in files.values()) or not self.args.pdf.is_file():
            self.error("compiled-artifacts", "最终PDF/AUX/BBL/LOG尚未全部就绪", missing=[str(p) for p in [self.args.pdf, *files.values()] if not p.is_file()])
            return None
        aux = strip_comments(files[".aux"].read_text(encoding="utf-8"))
        records = defaultdict(list)
        for item in command_args(aux, "newlabel", required=2):
            if "#" in item["args"][0]:
                continue
            try:
                records[item["args"][0]].append(brace_fields(item["args"][1]))
            except ValueError as error:
                self.error("aux-label", str(error), label=item["args"][0])
        self.aux = {key: values[0] for key, values in records.items() if values}
        for key, values in records.items():
            if len(values) != 1:
                self.error("aux-duplicate", "AUX标签重复", label=key)
        for key in self.labels:
            if key not in self.aux:
                self.error("aux-missing", "源码标签未进入实际编译AUX", label=key)
        for chapter, counts in EXPECTED.items():
            self.expect_number(f"sec:{chapter}", str(chapter))
            for prefix, total in zip(["obj", "eq", "box", "fig"], counts):
                for number in range(1, total + 1):
                    self.expect_number(f"{prefix}:{chapter}.{number}", f"{chapter}.{number}")
        for key, expected in [("eq:DP-var", "DP-var"), ("eq:intro1", "1"), ("eq:intro2", "2")]:
            self.expect_number(key, expected)
        for number in range(1, 70):
            self.expect_number(f"ex:{number}", str(number))
            if f"hint:{number}" not in self.aux:
                self.error("aux-hint", "编译缺少提示目标", number=number)
        for key in self.labels:
            match = re.fullmatch(r"sec:([1-8](?:\.\d+)+)", key)
            if match:
                self.expect_number(key, match.group(1))
        bibnumbers = {item["args"][0]: item["args"][1] for item in command_args(aux, "bibcite", required=2)}
        if bibnumbers != {f"b{n}": str(n) for n in range(1, 301)}:
            self.error("bibcite-numbering", "实际编译书目必须保持b1=1至b300=300")
        bbl = files[".bbl"].read_text(encoding="utf-8")
        bblkeys = [x["args"][0] for x in command_args(bbl, "bibitem", optional=True)]
        if bblkeys != [f"b{n}" for n in range(1, 301)]:
            self.error("bbl-order", "实际BBL书目数量、顺序或原编号不符", actual=len(bblkeys))
        log = files[".log"].read_text(encoding="utf-8", errors="replace")
        patterns = {
            "undefined-reference": r"(?:Reference|Citation) .+? undefined|There were undefined references",
            "multiply-defined": r"multiply defined|destination with the same identifier|duplicate destination",
            "missing-character": r"Missing character:",
            "overfull": r"Overfull \\[hv]box",
            "latex-error": r"(?:LaTeX|Package \S+) Error:|Undefined control sequence|^! ",
            "pdf-string": r"Token not allowed in a PDF string",
            "rerun": r"Rerun to get cross-references right|Label\(s\) may have changed|rerunfilecheck Warning: File .* has changed",
        }
        for code, pattern in patterns.items():
            hits = re.findall(pattern, log, re.I | re.M)
            if hits:
                self.error("log-" + code, "最终编译日志含未解决问题", occurrences=len(hits))
        if not re.search(r"Output written on .+?\([\d\s]+ pages?", log, re.S):
            self.error("log-no-output", "日志没有成功生成PDF的记录")
        pdf_time = self.args.pdf.stat().st_mtime
        newer = [rel(p) for p in self.dependencies if p.stat().st_mtime > pdf_time + 2]
        if newer:
            self.error("stale-pdf", "PDF早于实际输入或图件/书目，应重新编译", newer_inputs=newer)
        build_pdf = build / (self.args.main.stem + ".pdf")
        if build_pdf.is_file() and build_pdf.resolve() != self.args.pdf.resolve() and sha(build_pdf) != sha(self.args.pdf):
            self.error("pdf-copy-mismatch", "交付PDF与最终构建目录PDF字节不一致")
        fls = build / (self.args.main.stem + ".fls")
        if fls.is_file():
            content = fls.read_text(encoding="utf-8", errors="replace").replace("\\", "/")
            for path in self.files:
                if rel(path) not in content and str(path).replace("\\", "/") not in content:
                    self.error("fls-input", "recorder记录没有该真实输入文件", path=rel(path))
        else:
            self.warn("no-fls", "没有recorder文件；用输入图、完整AUX及时间戳检查编译覆盖")
        reader = PdfReader(self.args.pdf)
        self.stats["output_pdf_pages"] = len(reader.pages)
        self.stats["output_pdf_sha256"] = sha(self.args.pdf)
        self.stats["compiled_artifacts"] = {key: {"path": rel(p), "sha256": sha(p)} for key, p in files.items()}
        self.stats["aux_labels"] = len(self.aux)
        toc_path = build / (self.args.main.stem + ".toc")
        self.toc_entries = []
        if not toc_path.is_file():
            self.error("toc-file", "最终目录产物缺失")
        else:
            toc = strip_comments(toc_path.read_text(encoding="utf-8"))
            self.toc_entries = [{"level": item["args"][0], "title_tex": item["args"][1], "page_label": item["args"][2], "destination": item["args"][3]}
                                for item in command_args(toc, "contentsline", required=4)]
            self.stats["actual_toc_entries"] = len(self.toc_entries)
        self.compiled_index(build)
        return reader

    def compiled_index(self, build):
        if self.index is None or not hasattr(self, "index_anchors"):
            return
        paths = {suffix: build / (self.args.main.stem + suffix) for suffix in [".idx", ".ind", ".ilg"]}
        if any(not path.is_file() for path in paths.values()):
            self.error("compiled-index-files", "最终makeindex产物不完整", missing=[rel(path) for path in paths.values() if not path.is_file()])
            return
        expected = Counter()
        self.index_expected_pages = defaultdict(set)
        for target, keys in self.index_anchors.items():
            fields = self.aux.get(target, [])
            if len(fields) < 2:
                continue
            for key in keys:
                expected[(canonical_index(key + "|hyperpage"), fields[1])] += 1
                self.index_expected_pages[key].add(fields[1])
        idx = paths[".idx"].read_text(encoding="utf-8")
        actual = Counter((canonical_index(item["args"][0]), item["args"][1]) for item in command_args(idx, "indexentry", required=2))
        if actual != expected:
            self.error("idx-shipout-pages", "实际idx写出的词条/页号与对应标签的aux页号不符", missing=list((expected - actual).items())[:12], extra=list((actual - expected).items())[:12])
        ind = paths[".ind"].read_text(encoding="utf-8")
        items = []
        matches = list(re.finditer(r"\\(subitem|item)(?![A-Za-z@])\s*", ind))
        for i, match in enumerate(matches):
            text = ind[match.end():matches[i + 1].start() if i + 1 < len(matches) else len(ind)].strip()
            if text.startswith(r"\textbf{"):
                continue
            items.append((1 if match.group(1) == "subitem" else 0, text))
        entries = self.index["entries"]
        index_link_endpoints = Counter()
        if len(items) != len(entries):
            self.error("ind-entry-count", "makeindex的实际ind词条数必须保持163", actual=len(items), expected=len(entries))
        else:
            for entry, (level, text) in zip(entries, items):
                display = entry["chinese_tex"] + "（" + entry.get("english_tex", entry["english"]) + "）"
                if level != entry["level"] or not canonical_index(text).startswith(canonical_index(display)):
                    self.error("ind-entry-order", "实际ind显示词条、顺序或层级不符", id=entry["id"], level=level, beginning=text[:180])
                displayed = set()
                page_arguments = [item["args"][0] for item in command_args(text, "hyperpage")]
                page_arguments += [item["args"][1] for item in command_args(text, "hyperindexformat", required=2) if canonical_index(item["args"][0]) == r"\hyperpage"]
                for argument in page_arguments:
                    displayed.update(expand_display_pages(argument))
                    index_link_endpoints.update(display_endpoints(argument))
                wanted = self.index_expected_pages.get(entry["index_key"], set())
                if displayed != wanted:
                    self.error("ind-dynamic-pages", "实际ind的hyperpage页号/页码范围与真实锚点页号不符", id=entry["id"], expected=sorted(wanted), actual=sorted(displayed))
        ilg = paths[".ilg"].read_text(encoding="utf-8", errors="replace")
        if re.search(r"[1-9]\d* entries rejected|[1-9]\d* warnings|!! Input index error|Error", ilg, re.I):
            self.error("makeindex-log", "最终makeindex日志包含拒收条目、错误或警告")
        self.stats["index"]["idx_occurrences"] = sum(actual.values())
        self.stats["index"]["ind_items"] = len(items)
        self.stats["index"]["distinct_entry_page_pairs"] = sum(len(pages) for pages in self.index_expected_pages.values())
        self.index_link_endpoints = index_link_endpoints
        self.stats["index"]["rendered_page_link_endpoints"] = sum(index_link_endpoints.values())
        self.stats["compiled_index_artifacts"] = {suffix: {"path": rel(path), "sha256": sha(path)} for suffix, path in paths.items()}

    def expect_number(self, key, expected):
        fields = self.aux.get(key, [])
        actual = fields[0] if fields else None
        if actual is not None:
            while actual.startswith("{"):
                try:
                    inner, end = group(actual, 0)
                    if end != len(actual):
                        break
                    actual = inner
                except ValueError:
                    break
        if actual != expected:
            self.error("aux-numbering", "实际编号必须等于原编号，不可用修正源误替换", label=key, expected=expected, actual=actual)

    def links(self, source, output):
        source_info = inspect_pdf(source, self.args.source)
        target_info = inspect_pdf(output, self.args.pdf)
        self.stats["pdf_links"] = {"source": source_info["summary"], "output": target_info["summary"]}
        for issue in target_info["issues"]:
            self.error("pdf-link-target", "PDF实际链接或目标无效", **issue)
        names = target_info["names"]
        for entry in getattr(self, "toc_entries", []):
            physical = names.get(entry["destination"])
            if physical is None:
                self.error("toc-pdf-target", "实际目录项的PDF目标不存在", **entry)
            elif str(output.page_labels[physical - 1]) != entry["page_label"]:
                self.error("toc-pdf-page", "实际目录项的显示页码与目标页不符", **entry, target_physical=physical, target_page_label=output.page_labels[physical - 1])
        anchor_expect = Counter()
        for label, count in self.expected_label_links.items():
            fields = self.aux.get(label, [])
            if len(fields) < 4 or not fields[3]:
                self.error("aux-no-anchor", "引用标签没有PDF目标字段", label=label)
                continue
            anchor_expect[fields[3]] += count
        for label, fields in self.aux.items():
            if label not in self.labels:
                continue
            if len(fields) < 4 or fields[3] not in names:
                self.error("label-pdf-target", "AUX标签没有实际PDF命名目标", label=label, fields=fields)
                continue
            physical = names[fields[3]]
            if len(fields) > 1 and str(output.page_labels[physical - 1]) != fields[1]:
                self.error("label-pdf-page", "AUX显示页码与实际目标页的PDF PageLabel不符", label=label, aux_page=fields[1], pdf_physical=physical, pdf_label=output.page_labels[physical - 1])
        for key, count in self.cites.items():
            candidates = [name for name in names if re.fullmatch(r"(?:cite|citation)\." + re.escape(key), name)]
            if len(candidates) != 1:
                self.error("citation-pdf-target", "文献没有唯一实际PDF目标", key=key, candidates=candidates)
            else:
                anchor_expect[candidates[0]] += count
        for anchor, minimum in anchor_expect.items():
            actual = target_info["named_link_counts"].get(anchor, 0)
            if actual < minimum:
                self.error("reference-link-coverage", "实际指向该目标的命名链接少于真实引用命令数；须逐项排查", anchor=anchor, expected_minimum=minimum, actual=actual)
        boundaries = [("front", 1)]
        for chapter in range(1, 9):
            page = self.label_page(f"sec:{chapter}", names)
            if page:
                boundaries.append((f"chapter{chapter}", page))
        for unit, label in [("exercises", "sec:exercises"), ("hints", "sec:hints")]:
            page = self.label_page(label, names)
            if page:
                boundaries.append((unit, page))
        bib = next((self.label_page(k, names, required=False) for k in ["sec:references", "sec:bibliography"] if k in self.aux), None)
        if bib is None:
            bib = next((names[name] for name in ["cite.b1", "citation.b1"] if name in names), None)
        if bib is None:
            self.error("bibliography-boundary", "无法定位最终书目起页")
        else:
            boundaries.append(("bibliography", bib))
        page = self.label_page("sec:index", names)
        if page:
            boundaries.append(("index", page))
        ordered_units = [name for name, _, _ in SOURCE_UNITS]
        if [name for name, _ in boundaries] != ordered_units or any(b <= a for (_, a), (_, b) in zip(boundaries, boundaries[1:])):
            self.error("pdf-unit-boundaries", "最终各部分起页缺失、无序或未单独起页", boundaries=boundaries)
        comparisons = []
        index_minimum = sum(getattr(self, "index_link_endpoints", {}).values())
        if [name for name, _ in boundaries] == ordered_units:
            for i, (name, first) in enumerate(boundaries):
                last = boundaries[i + 1][1] - 1 if i + 1 < len(boundaries) else len(output.pages)
                _, source_first, source_last = SOURCE_UNITS[i]
                source_count = sum(x["internal"] for x in source_info["per_page"][source_first - 1:source_last])
                target_count = sum(x["internal"] for x in target_info["per_page"][first - 1:last])
                baseline = index_minimum if name == "index" else source_count
                basis = "makeindex合并同词同译页、压缩连续页后的真实hyperpage端点；356个原定位另逐一对账" if name == "index" else "底本同单元原始内部链接数"
                if name == "chapter2" and self.verify_chapter2_source_mislink(source_info, target_info, first, last):
                    baseline -= 1
                    basis = "底本80注释中1个把文献[65]第5章误链本书第5章；其余79个真实引用按目标类型和编号多重集合一一相等，详见ch2-link-reconciliation.json"
                row = {"unit": name, "source_physical": [source_first, source_last], "output_physical": [first, last], "source_internal_links": source_count, "relevant_link_baseline": baseline, "baseline_basis": basis, "output_internal_links": target_count, "status": "passed-count-baseline" if target_count >= baseline else "failed-count-baseline"}
                comparisons.append(row)
                if target_count < baseline:
                    self.error("unit-link-deficit", "该部分实际内部链接少于底本；须按页核对真实引用，不能用别处新增链接抵消", **row)
                if name == "index":
                    page_links = Counter(a.get("destination_name") for a in target_info["links"] if first <= a["page"] <= last and a["kind"] == "internal")
                    for label, minimum in getattr(self, "index_link_endpoints", {}).items():
                        if page_links.get("page." + label, 0) < minimum:
                            self.error("index-pdf-page-links", "索引实际PDF指向该译页的链接少于ind真实端点", page_label=label, expected_minimum=minimum, actual=page_links.get("page." + label, 0))
        relevant_baseline = sum(row["relevant_link_baseline"] for row in comparisons)
        self.stats["pdf_relevant_internal_baseline"] = relevant_baseline
        if comparisons and target_info["summary"]["internal"] < relevant_baseline:
            self.error("total-link-deficit", "全书内部链接总数少于按单元核定的相关链接基线")
        self.stats["pdf_link_units"] = comparisons
        self.stats["pdf_link_pages"] = {"source": source_info["per_page"], "output": target_info["per_page"]}
        self.stats["source_link_issues"] = source_info["issues"]
        self.check_source_index_links(source, source_info)

    def verify_chapter2_source_mislink(self, source_info, target_info, first, last):
        evidence_path = BASE / "work/ch2-link-reconciliation.json"
        ledger_path = BASE / "work/ch2-link-rectangles.json"
        if not evidence_path.is_file() or not ledger_path.is_file():
            return False
        evidence = json.loads(evidence_path.read_text(encoding="utf-8"))
        ledger = json.loads(ledger_path.read_text(encoding="utf-8"))
        if evidence.get("source_sha256") != self.stats.get("source_sha256") or not evidence.get("all_other_79_targets_match"):
            return False
        bad = [a for a in source_info["links"] if a["page"] == 109 and a.get("destination_name") == "chapter.120.5" and a.get("target_page") == 201]
        if len(bad) != 1 or any(abs(x - y) > .001 for x, y in zip(bad[0]["rect"], [200.394, 487.818, 207.363, 496.632])):
            return False
        original = [a for a in source_info["links"] if 86 <= a["page"] <= 112 and a["kind"] == "internal"]
        if Counter((a["page"], a.get("destination_name"), tuple(a["rect"])) for a in original) != Counter((a["page"], a["destination"], tuple(a["rect"])) for a in ledger["source"]):
            return False
        expected = Counter()
        for annotation in ledger["source"]:
            numbers = re.findall(r"\d+(?:\.\d+)*", annotation["visible"])
            name = annotation["destination"]
            prefix = "b" if name.startswith("cite.") else "obj:" if name.startswith("theorem.") else "eq:" if name.startswith("equation.") else "box:" if name.startswith("memobox.") else "sec:" if name.startswith(("section.", "subsection.", "chapter.")) else "fig:" if name.startswith("figure.") else "ex:" if name.startswith("exo.") else None
            if not prefix or not numbers:
                return False
            expected[prefix + numbers[0]] += 1
        actual = Counter()
        for annotation in target_info["links"]:
            if not first <= annotation["page"] <= last or annotation["kind"] != "internal":
                continue
            name = annotation.get("destination_name", "")
            if "." not in name:
                return False
            kind, number = name.split(".", 1)
            prefix = "" if kind == "cite" else "obj:" if kind in NUMBERED_ENVS else "eq:" if kind == "equation" else "box:" if kind == "boxcounter" else "sec:" if kind in ["section", "subsection", "subsubsection"] else "fig:" if kind == "figure" else "ex:" if kind == "exercise" else None
            if prefix is None:
                return False
            actual[prefix + number] += 1
        if expected - Counter({"sec:5": 1}) != actual:
            return False
        self.stats["chapter2_link_reconciliation"] = {"status": "verified-against-current-PDF", "source_internal": sum(expected.values()), "output_internal": sum(actual.values()), "excluded_source_error": bad[0], "evidence": rel(evidence_path), "visible_text": "文献[65]第5章，非本书第5章", "output_pdf_sha256": self.stats.get("output_pdf_sha256")}
        return True

    def label_page(self, label, names, required=True):
        fields = self.aux.get(label, [])
        if len(fields) >= 4 and fields[3] in names:
            return names[fields[3]]
        if required:
            self.error("pdf-boundary-target", "部分标题没有可达的实际PDF目标", label=label)
        return None

    def check_source_index_links(self, reader, info):
        if self.index is None:
            return
        source = []
        for physical in [374, 375, 376]:
            annotations = [a for a in info["links"] if a["page"] == physical and a["kind"] == "internal"]
            width = float(reader.pages[physical - 1].mediabox.width)
            ordered = []
            for column in [0, 1]:
                remaining = sorted([a for a in annotations if (0 if a["rect"][0] < width / 2 else 1) == column], key=lambda a: -a["rect"][1])
                while remaining:
                    baseline = remaining[0]["rect"][1]
                    row = [a for a in remaining if abs(a["rect"][1] - baseline) <= 2]
                    remaining = [a for a in remaining if abs(a["rect"][1] - baseline) > 2]
                    ordered.extend(sorted(row, key=lambda a: a["rect"][0]))
            source.extend((physical, str(reader.page_labels[a["target_page"] - 1])) for a in ordered if a.get("target_page"))
        expected = []
        for entry in self.index["entries"]:
            _, endpoints = expand_expression(entry.get("source_page_expression", ""))
            expected.extend((entry.get("source_index_physical_page"), value) for value in endpoints)
            for reference in entry.get("references", []):
                physical = reference.get("source_physical_page")
                if not isinstance(physical, int) or not 1 <= physical <= len(reader.pages) or str(reader.page_labels[physical - 1]) != str(reference.get("source_printed_page")):
                    self.error("index-source-physical", "索引物理页与原PDF PageLabels不符", id=entry["id"], reference=reference)
        if source != expected:
            mismatch = next((i for i, (a, b) in enumerate(zip(source, expected)) if a != b), min(len(source), len(expected)))
            self.error("source-index-link-sequence", "原索引实际链接的有序端点序列与完整映射不符", source_count=len(source), mapped_endpoint_count=len(expected), first_mismatch=mismatch, source_near=source[max(0, mismatch - 2):mismatch + 3], mapped_near=expected[max(0, mismatch - 2):mismatch + 3])
        self.stats["source_index_link_annotations"] = len(source)

    def finish(self):
        self.stats["files"] = {rel(path): {"sha256": sha(path), "bytes": path.stat().st_size} for path in sorted(self.dependencies)}
        if self.args.write_manifest and self.errors:
            self.warn("manifest-not-written", "自动审计失败，未覆盖manifest.json")
        report = {"audit": "full-book-final-input-and-PDF-audit", "generated_utc": datetime.now(timezone.utc).isoformat(),
                  "status": "failed" if self.errors else "passed-automated-checks", "source_id": "DS026",
                  "main": rel(self.args.main), "pdf": rel(self.args.pdf), **self.stats,
                  "failures": self.errors, "warnings": self.warnings,
                  "limitations": ["自动结构、编号及实际PDF链接审计，不能代替逐页原文忠实性核对或最终PDF目视检查.",
                                  "链接数量不足按失败报告；须逐页查真实引用，不能添加无关链接凑数.",
                                  "数学源错误必须保留原编号和可见写法；本脚本不作数学纠错或正文改写."]}
        prefix = self.args.report_prefix
        prefix.parent.mkdir(parents=True, exist_ok=True)
        prefix.with_suffix(".json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        prefix.with_suffix(".md").write_text(markdown_report(report), encoding="utf-8")
        (BASE / "work/pdf-link-audit-report.md").write_text(link_markdown_report(report), encoding="utf-8")
        (BASE / "work/static-check-report.md").write_text(static_markdown_report(report), encoding="utf-8")
        (BASE / "work/numbering-audit-report.md").write_text(numbering_markdown_report(report), encoding="utf-8")
        if self.args.write_manifest:
            if not self.errors:
                (BASE / "manifest.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(json.dumps({"status": report["status"], "failures": len(self.errors), "warnings": len(self.warnings), "report": rel(prefix.with_suffix('.json'))}, ensure_ascii=False))
        return 1 if self.errors else 0


def expand_expression(expression):
    expanded, endpoints = [], []
    for part in re.split(r"\s*,\s*", expression.strip()):
        if not part:
            continue
        match = re.fullmatch(r"(\d+)\s*[–−-]\s*(\d+)", part)
        if match:
            first, last = map(int, match.groups())
            expanded.extend(str(n) for n in range(first, last + 1))
            endpoints.extend([str(first), str(last)])
        else:
            expanded.append(part)
            endpoints.append(part)
    return expanded, endpoints


def canonical_index(text):
    text = re.sub(r"\s+", " ", text).strip()
    text = text.replace(r"|hyperindexformat{\hyperpage}", "|hyperpage")
    # protected@write may insert a harmless space after a control word.
    return re.sub(r"(\\[A-Za-z@]+)\s+(?=[{}])", r"\1", text)


def roman_value(text):
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total, previous = 0, 0
    for char in reversed(text.upper()):
        value = values[char]
        total += -value if value < previous else value
        previous = max(previous, value)
    return total


def as_roman(number, upper=False):
    result = ""
    for value, letters in [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]:
        while number >= value:
            result += letters
            number -= value
    return result if upper else result.lower()


def display_endpoints(text):
    endpoints = []
    for part in text.split(","):
        pieces = re.split(r"\s*(?:--|–|−)\s*", part.strip())
        endpoints.extend(piece for piece in pieces if piece)
    return endpoints


def expand_display_pages(text):
    pages = []
    for part in text.split(","):
        pieces = re.split(r"\s*(?:--|–|−)\s*", part.strip())
        if len(pieces) != 2:
            pages.extend(piece for piece in pieces if piece)
        elif all(piece.isdigit() for piece in pieces):
            pages.extend(str(n) for n in range(int(pieces[0]), int(pieces[1]) + 1))
        elif all(re.fullmatch(r"[ivxlcdm]+", piece, re.I) for piece in pieces):
            pages.extend(as_roman(n, pieces[0].isupper()) for n in range(roman_value(pieces[0]), roman_value(pieces[1]) + 1))
        else:
            pages.extend(pieces)
    return pages


def inspect_pdf(reader, path):
    """Resolve named AND direct-array destinations; validate every output link."""
    page_refs = {}
    for n, page in enumerate(reader.pages, 1):
        if page.indirect_reference:
            page_refs[(page.indirect_reference.idnum, page.indirect_reference.generation)] = n
    names, issues = {}, []
    for name, destination in reader.named_destinations.items():
        try:
            index = reader.get_destination_page_number(destination)
            if index is None or not 0 <= index < len(reader.pages):
                raise ValueError("named destination points outside PDF")
            names[str(name)] = index + 1
        except Exception as error:
            issues.append({"destination": str(name), "reason": str(error)})

    def resolve(destination):
        if isinstance(destination, str):
            key = str(destination)
            return names.get(key), key
        if isinstance(destination, (list, tuple)) and destination:
            page = destination[0]
            if isinstance(page, IndirectObject):
                return page_refs.get((page.idnum, page.generation)), None
            ref = getattr(page, "indirect_reference", None)
            if ref:
                return page_refs.get((ref.idnum, ref.generation)), None
        return None, None

    summary = Counter(total=0, internal=0, external=0, remote=0, unknown=0)
    named_counts, kinds, links, per_page = Counter(), Counter(), [], []
    remote_cache = {}
    for number, page in enumerate(reader.pages, 1):
        local = Counter(total=0, internal=0, external=0, remote=0, unknown=0)
        box = [float(v) for v in page.mediabox]
        if len(box) != 4 or not all(math.isfinite(v) for v in box) or box[2] <= box[0] or box[3] <= box[1]:
            issues.append({"page": number, "reason": "invalid MediaBox"})
        for reference in page.get("/Annots", []):
            annotation = reference.get_object()
            if annotation.get("/Subtype") != "/Link":
                continue
            action = annotation.get("/A", {})
            action = action.get_object() if hasattr(action, "get_object") else action
            action = action or {}
            typ = str(action.get("/S", "/Dest" if "/Dest" in annotation else "unknown"))
            destination = annotation.get("/Dest", action.get("/D"))
            destination = destination.get_object() if hasattr(destination, "get_object") else destination
            kind = "internal" if typ in ["/GoTo", "/Dest"] else "external" if typ == "/URI" else "remote" if typ == "/GoToR" else "unknown"
            summary["total"] += 1
            summary[kind] += 1
            local["total"] += 1
            local[kind] += 1
            kinds[typ] += 1
            try:
                rect = [float(v) for v in annotation.get("/Rect", [])]
            except (TypeError, ValueError):
                rect = []
            row = {"page": number, "kind": kind, "action": typ, "rect": rect}
            if len(rect) != 4 or not all(math.isfinite(v) for v in rect) or rect[2] <= rect[0] or rect[3] <= rect[1]:
                issues.append({"page": number, "reason": "invalid link rectangle", "rect": rect})
            elif rect[2] < box[0] or rect[0] > box[2] or rect[3] < box[1] or rect[1] > box[3]:
                issues.append({"page": number, "reason": "link rectangle entirely outside page", "rect": rect})
            if kind == "internal":
                target, name = resolve(destination)
                row.update(target_page=target, destination_name=name)
                if not target:
                    issues.append({"page": number, "reason": "unresolved internal destination", "destination": str(destination)[:250]})
                if name:
                    named_counts[name] += 1
            elif kind == "external":
                uri = str(action.get("/URI", ""))
                row["uri"] = uri
                if not uri or not urlparse(uri).scheme:
                    issues.append({"page": number, "reason": "empty or schemeless URI", "uri": uri})
            elif kind == "remote":
                filename = action.get("/F")
                filename = filename.get_object() if hasattr(filename, "get_object") else filename
                if isinstance(filename, dict):
                    filename = filename.get("/UF", filename.get("/F"))
                filename = str(filename or "")
                remote_path = (path.parent / unquote(filename).replace("\\", "/")).resolve()
                row["remote_file"] = str(remote_path)
                if not filename or not remote_path.is_file():
                    issues.append({"page": number, "reason": "remote PDF file does not exist", "file": filename})
                else:
                    try:
                        if remote_path not in remote_cache:
                            remote_cache[remote_path] = PdfReader(remote_path)
                        remote = remote_cache[remote_path]
                        if isinstance(destination, (list, tuple)) and destination and isinstance(destination[0], (int, float)):
                            valid = 0 <= int(destination[0]) < len(remote.pages)
                        elif isinstance(destination, str):
                            valid = destination in remote.named_destinations
                        else:
                            valid = False
                        if not valid:
                            issues.append({"page": number, "reason": "invalid remote PDF destination", "file": filename, "destination": str(destination)[:250]})
                    except Exception as error:
                        issues.append({"page": number, "reason": "cannot read remote PDF: " + str(error), "file": filename})
            else:
                issues.append({"page": number, "reason": "unsupported link action", "action": typ})
            links.append(row)
        per_page.append({"physical_page": number, **dict(local)})
    return {"summary": {**dict(summary), "action_types": dict(kinds), "named_destinations": len(names)}, "names": names,
            "named_link_counts": named_counts, "links": links, "per_page": per_page, "issues": issues}


def markdown_report(report):
    status = "失败" if report["failures"] else "自动检查通过（不代替忠实性及目视审阅）"
    lines = ["# 全书最终自动审计", "", f"状态：{status}.", "", f"MAIN：`{report['main']}`", f"PDF：`{report['pdf']}`", "",
             f"输入文件：{len(report.get('input_files', []))}；PDF物理页数：{report.get('output_pdf_pages', '未读取')}.",
             f"底本SHA256：`{report.get('source_sha256', '未读取')}`.", "", "## 实际链接分段比较", "",
             "|部分|原PDF物理页|译稿物理页|原内部链接|相关基线|译稿内部链接|状态|", "|---|---|---|---:|---:|---:|---|"]
    for row in report.get("pdf_link_units", []):
        lines.append(f"|{row['unit']}|{row['source_physical']}|{row['output_physical']}|{row['source_internal_links']}|{row['relevant_link_baseline']}|{row['output_internal_links']}|{row['status']}|")
    lines += ["", "## 失败项", ""]
    lines += ["- `" + e["code"] + "`：" + e["detail"] + "；" + json.dumps({k: v for k, v in e.items() if k not in ['code', 'detail']}, ensure_ascii=False) for e in report["failures"]] or ["无."]
    lines += ["", "## 提醒与边界", ""]
    lines += ["- " + w["detail"] for w in report["warnings"]]
    lines += ["- " + text for text in report["limitations"]]
    lines += ["", "完整输入图、编号期望、逐页链接计数、文件SHA256及具体失败上下文见同名JSON.", ""]
    return "\n".join(lines)


def link_markdown_report(report):
    links = report.get("pdf_links", {})
    lines = ["# 全书实际PDF链接审计", "", "范围为完整底本376物理页，及最终MAIN实际生成的全书PDF；不沿用首批94页或仅第1章结论。", "",
             "底本SHA256：`" + report.get("source_sha256", "未读取") + "`.",
             "输出SHA256：`" + report.get("output_pdf_sha256", "未读取") + "`.", "",
             "|PDF|全部链接|内部|URI外部|远程PDF|命名目标|", "|---|---:|---:|---:|---:|---:|"]
    for key in ["source", "output"]:
        row = links.get(key, {})
        lines.append(f"|{key}|{row.get('total', '未读取')}|{row.get('internal', '未读取')}|{row.get('external', '未读取')}|{row.get('remote', '未读取')}|{row.get('named_destinations', '未读取')}|")
    lines += ["", "实际内部链接分别解析GoTo与直接Dest，包括命名目标和直接页面数组；检查所有目标页有效、链接矩形有效、真实引用与文献目标存在，逐标签比较AUX页码和目标PDF PageLabel。外链检查非空URI及scheme，不假称已访问全部外部网站。", "",
              "索引原3页351个可见超链接端点，压缩范围展开后356个出处；逐条核对原PDF矩形排序后的目标序列、319个精确标签、356个index命令及idx真实shipout页码。makeindex合法合并同词同译页并压缩连续页，因此最终ind的163词条仍完整；实际PDF索引页链接按ind真实hyperpage端点检查，不能把合并后的页数硬比356。", ""]
    reconciliation = report.get("chapter2_link_reconciliation")
    if reconciliation:
        lines += ["第2章精确排除1个原PDF错链：原物理109／印刷82的“See also Chapter 5 in [65]”中的5错误指向本书第5章（物理201），矩形`[200.394,487.818,207.363,496.632]`。该句语义为文献[65]的第5章；中文完整保留句意及文献链接，不复制无关跳转。全章80个源注释排除此1条后，其余79个引用按目标类型和可见编号的多重集合与当前译稿79个链接逐个相等。不是跨行矩形，也不是用别处链接富余抵消；完整数字证据为`ch2-link-reconciliation.json`及`ch2-link-rectangles.json`，本次运行又核对当前PDF。", ""]
    lines += ["逐单元和逐页计数、所有失败项见`full-audit.md/json`。总量富余不能抵消某章真实引用缺失。", "",
              "本次整体自动审计状态：`" + report["status"] + "`。若仍有失败，不能声称最终链接审计通过。最终PDF视觉检查另行按PNG实际看图记录。", ""]
    return "\n".join(lines)


def static_markdown_report(report):
    lines = ["# 全书静态与编译结构核验", "", "此报告按最终MAIN递归输入图生成，替代原来只含前置与第1章的阶段报告。", "",
             "入口：`" + report["main"] + "`；实际显式输入文件" + str(len(report.get("input_files", []))) + "个。运行生成的BBL、IDX、IND、ILG及PDF另在full-audit中按其真实文件核对。", "",
             "静态输入图状态：`" + report.get("static_input_graph_status", "未完成") + "`。检查环境与数学定界符、花括号（支持index内复杂数学嵌套）、唯一标签和实际引用、图件存在、300条书目、69题与69条提示、有序完整索引与精确锚点。", "",
             "原页独立编号基线：238编号陈述、102章内数字式、43知识框、27编号图；另3幅无编号正文图和2习题图、154原文proof、67章内脚注＋前置5＋习题1。DP-var及导论(1)/(2)独立核对，不混入章内数字式。所有原数学疑误与编号保持可见，不作静默修正。", "",
             "全量`check_fidelity_project.py`按同一递归输入图执行，报告为`fidelity-static-full.json`；适配了技能原脚本的目录发现和逗号引用键，并检查全部154个proof，不改技能原文件。此语言/结构扫描不代替root维护的`fidelity-report.md`来源自审与独立cross记录。", "",
             "实际AUX编号、300条BBL顺序、日志、PDF新鲜度和所有实际链接另见`full-audit.json`。整体自动审计状态：`" + report["status"] + "`。存在链接/编译失败时不得把本报告的静态检查称为全稿通过。", "",
             "未执行Obsidian界面检查；最终PDF目视记录由全书分段PNG审阅单独提供。", ""]
    return "\n".join(lines)


def numbering_markdown_report(report):
    failures = [row for row in report["failures"] if row["code"] in ["numbered-coverage", "aux-numbering", "aux-missing", "exercise-hint-order", "aux-hint", "bbl-order", "bibcite-numbering"]]
    lines = ["# 全书实际编号核对", "", "最终PDF SHA256：`" + report.get("output_pdf_sha256", "未读取") + "`.", "",
             "按MAIN真实输入图的精确标签集合与实际编译AUX逐项核对；不是只检查上界，也不从当前稿件的数量反推原文基线。", "",
             "|章|编号陈述|数字公式|知识框|编号图|原文proof|章内脚注|", "|---|---:|---:|---:|---:|---:|---:|"]
    for chapter, counts in EXPECTED.items():
        lines.append(f"|{chapter}|{counts[0]}|{counts[1]}|{counts[2]}|{counts[3]}|{EXPECTED_PROOFS[chapter]}|{EXPECTED_FOOTNOTES[chapter]}|")
    totals = [sum(row[i] for row in EXPECTED.values()) for i in range(4)]
    lines += [f"|合计|{totals[0]}|{totals[1]}|{totals[2]}|{totals[3]}|{sum(EXPECTED_PROOFS.values())}|{sum(EXPECTED_FOOTNOTES.values())}|", "",
              "每章obj/eq/box/fig编号必须恰为1至表列上界且实际AUX值与标签原编号一致；额外对象同样报错。陈述共享章内theorem计数器，框/式/图独立。", "",
              "另核对：前置导论(1)、(2)；命名公式DP-var；有序习题1–69和全部对应hint:1–69；书目BBL顺序b1至b300及AUX的bN=N。前置脚注5、习题脚注1和正文无编号图3另计，正文30幅原图加2习题图齐全。", "",
              "本次编号失败项：" + str(len(failures)) + "。整体自动审计状态：`" + report["status"] + "`。源数学疑误与原编号忠实保留，不通过更改编号掩盖原错误。", ""]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--main", type=Path, default=BASE / (STEM + ".tex"))
    parser.add_argument("--pdf", type=Path, default=BASE / (STEM + ".pdf"))
    parser.add_argument("--source", type=Path, default=BASE.parent.parent / "books" / SOURCE_NAME)
    parser.add_argument("--build-dir", type=Path, default=BASE / "work")
    parser.add_argument("--report-prefix", type=Path, default=BASE / "work/full-audit")
    parser.add_argument("--write-manifest", action="store_true", help="仅在自动审计全部通过后更新manifest；不声称视觉审阅完成")
    args = parser.parse_args()
    for key in ["main", "pdf", "source", "build_dir", "report_prefix"]:
        setattr(args, key, getattr(args, key).resolve())
    audit = Audit(args)
    for stage in [audit.static]:
        try:
            stage()
        except Exception as error:
            audit.error("audit-exception", "审计阶段异常，不能视为通过", exception=repr(error))
    source, output = None, None
    try:
        source = audit.source()
        output = audit.compiled()
        if source is not None and output is not None:
            audit.links(source, output)
    except Exception as error:
        audit.error("audit-exception", "PDF/编译产物审计异常，不能视为通过", exception=repr(error))
    return audit.finish()


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
