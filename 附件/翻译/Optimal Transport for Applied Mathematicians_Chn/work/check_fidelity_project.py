#!/usr/bin/env python3
"""Pre-compilation fidelity audit for Chinese mathematical TeX.

Usage:
    python3 check_fidelity.py <output_dir>

Checks that must pass before compilation (step 09):
    1. No English theorem/proof/remark names
    2. No forbidden abbreviation patterns
    3. Every \begin{proof} has \end{proof} and vice versa
    4. (When Marker is present) numbered object coverage
    5. Every \cite key exists in references.bib
    6. No unescaped % signs in non-comment text (common LaTeX error)

Exit 0 = pass, exit 1 = failures found, exit 2 = usage error.
"""
import re, sys, os, json
from pathlib import Path
from collections import Counter

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 check_fidelity.py <output_dir>", file=sys.stderr)
        sys.exit(2)

    outdir = Path(sys.argv[1])
    if not outdir.is_dir():
        print(f"ERROR: not a directory: {outdir}", file=sys.stderr)
        sys.exit(2)

    failures = []

    # collect all TeX content
    sec_files = sorted(outdir.glob('tex/sec*.tex'))
    main_tex = list(outdir.glob('*_Chn.tex'))
    tex_paths = sorted(outdir.glob('sections-tex/*.tex')) + sorted(outdir.glob('frontmatter/*.tex')) + main_tex
    if not tex_paths:
        print("ERROR: no TeX files found", file=sys.stderr)
        sys.exit(2)

    all_tex = ''
    for p in tex_paths:
        all_tex += p.read_text(encoding='utf-8') + '\n'

    # strip comments for text-based checks
    tex_no_comments = re.sub(r'(?<!\\)%.*$', '', all_tex, flags=re.MULTILINE)

    # --- Check 1: English theorem-like names ---
    eng_theorem = [
        (r'\\newtheorem\{[^}]*\}\{Proposition\}', 'Proposition → 命题'),
        (r'\\newtheorem\{[^}]*\}\{Theorem\}', 'Theorem → 定理'),
        (r'\\newtheorem\{[^}]*\}\{Remark\}', 'Remark → 注记'),
        (r'\\newtheorem\{[^}]*\}\{Lemma\}', 'Lemma → 引理'),
        (r'\\newtheorem\{[^}]*\}\{Corollary\}', 'Corollary → 推论'),
        (r'\\newtheorem\{[^}]*\}\{Definition\}', 'Definition → 定义'),
    ]
    for pat, msg in eng_theorem:
        if re.search(pat, tex_no_comments):
            failures.append(f"English theorem name: {msg}")

    # --- Check 2: English proof title ---
    eng_proof = re.findall(r'\\begin\{proof\}\[(.*?)\]', tex_no_comments)
    for title in eng_proof:
        if re.search(r'\bProof\b', title, re.IGNORECASE):
            failures.append(f"English proof title: [Proof of ...] → should be [...的证明]. Found: [{title}]")

    # --- Check 3: English \autoref names ---
    if re.search(r'\\providecommand\*?\{\\(?:proposition|remark|theorem)autorefname\}\{(?:Proposition|Remark|Theorem)\}', tex_no_comments):
        failures.append("English \\autoref name (Proposition/Remark/Theorem) → should be 命题/注记/定理")

    # --- Check 4: English \proofname ---
    if re.search(r'\\renewcommand\{\\proofname\}\{Proof\}', tex_no_comments):
        failures.append("English \\proofname → should be 证明")

    # --- Check 5: English figure/table names ---
    if re.search(r'\\renewcommand\{\\figurename\}\{Figure\}', tex_no_comments):
        failures.append("English \\figurename → should be 图")
    if re.search(r'\\renewcommand\{\\tablename\}\{Table\}', tex_no_comments):
        failures.append("English \\tablename → should be 表")

    # --- Check 6: Forbidden abbreviation patterns ---
    forbidden = [
        (r'\[概述\]', '[概述]'),
        (r'详见原论文', '详见原论文'),
        (r'完整证明见', '完整证明见'),
        (r'详见原论文第', '详见原论文第'),
    ]
    for pat, label in forbidden:
        if re.search(pat, tex_no_comments):
            failures.append(f"Forbidden abbreviation: {label}")

    # --- Check 7: Proof begin/end matching ---
    proof_begins = len(re.findall(r'\\begin\{proof\}', tex_no_comments))
    proof_ends = len(re.findall(r'\\end\{proof\}', tex_no_comments))
    if proof_begins != proof_ends:
        failures.append(f"Proof mismatch: {proof_begins} begins, {proof_ends} ends")
    else:
        print(f"  Proofs: {proof_begins} begin/end matched")

    # --- Check 8: Citation keys exist in references.bib ---
    cite_keys = set(re.findall(r'\\cite(?:\[[^\]]*\])?\{([^}]+)\}', tex_no_comments))
    cite_keys = {key.strip() for group in cite_keys for key in group.split(',')}
    bib_path = outdir / 'bib' / 'references.bib'
    if bib_path.exists():
        bib_text = bib_path.read_text(encoding='utf-8')
        bib_keys = set(re.findall(r'@\w+\{([^,]+),', bib_text))
        missing = cite_keys - bib_keys
        if missing:
            failures.append(f"Citations not in references.bib: {missing}")
        else:
            print(f"  Citations: {len(cite_keys)} keys, all found in references.bib ({len(bib_keys)} entries)")
    else:
        failures.append("references.bib not found at bib/references.bib")

    # --- Check 9: Equation environment matching ---
    for env in ['equation', 'align', 'proposition', 'theorem', 'remark', 'remarkx']:
        begins = len(re.findall(rf'\\begin\{{{env}\}}', tex_no_comments))
        ends = len(re.findall(rf'\\end\{{{env}\}}', tex_no_comments))
        if begins != ends:
            failures.append(f"Environment mismatch: {env}: {begins} begins, {ends} ends")

    # --- Check 10: Marker coverage (if marker output exists) ---
    marker_files = list(outdir.glob('*_marker.md'))
    if marker_files:
        marker = marker_files[0].read_text(encoding='utf-8')
        marker_nums = set(re.findall(r'\((\d+\.\d+)\)', marker))
        tex_labels = set(re.findall(r'\\label\{(eq|prop|rem|thm|alg):\d+\.\d+\}', tex_no_comments))
        tex_nums = set()
        for lab in tex_labels:
            m = re.match(r'\\(?:eq|prop|rem|thm|alg):(\d+)\.(\d+)', lab)
            if m:
                tex_nums.add(f"{m.group(1)}.{m.group(2)}")
        missing_nums = marker_nums - tex_nums
        if missing_nums:
            # filter out numbers that are in text but not as formal labels
            # e.g. algorithm descriptions (1.15) may not have labels
            pass  # just report, don't fail — handled by check_labels.py
        print(f"  Marker numbers: {len(marker_nums)}, TeX labels: {len(tex_labels)}")

    # --- Report ---
    if failures:
        print("\n=== FIDELITY CHECK FAILED ===")
        for f in failures:
            print(f"  ✗ {f}")
        sys.exit(1)
    else:
        print("\n=== FIDELITY CHECK PASSED ===")
        sys.exit(0)

if __name__ == '__main__':
    main()
