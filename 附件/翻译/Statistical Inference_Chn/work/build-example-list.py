from pathlib import Path
import re, json

base = Path(__file__).resolve().parent.parent
source = (base / 'work/front-lists.txt').read_text(encoding='utf-8')
source = source.replace('10.1.2                             X)\n             Example (Consistency of X̄', '10.1.2    Example (Consistency of Xbar)')
entries = re.findall(r'^\s*(\d+\.\d+\.\d+)\s+Example\s+(.+?)\s+(\d+)\s*$', source, re.M)
translated = dict(line.split('\t',1) for line in (base / 'work/example-titles-zh.tsv').read_text(encoding='utf-8').splitlines() if line)
ids = [i for i,_,_ in entries]
assert len(ids) == len(set(ids)), 'duplicate source entries'
assert set(ids) == set(translated), {'missing': sorted(set(ids)-set(translated)), 'extra': sorted(set(translated)-set(ids))}
lines = [r'% 原书例目录：印刷xxiii–xxix／PDF物理24–30；原编号与原页保留。',
         r'\clearpage\phantomsection',
         r'\section*{例目录（原书页码）}\label{front:examples}',
         r'\addcontentsline{toc}{section}{例目录（原书页码）}',
         r'\begin{longtable}{@{}p{.82\textwidth}r@{}}']
chapter = None
for i, title, page in entries:
    newchap = i.split('.')[0]
    if chapter is not None and newchap != chapter:
        lines.append(r'\addlinespace[.5em]')
    chapter = newchap
    lines.append('例 ' + i + '（' + translated[i] + '） & \\sourcepageref{' + str(int(page)+31) + '}{' + page + r'} \\')
lines += [r'\end{longtable}', '']
(base / 'frontmatter').mkdir(exist_ok=True)
(base / 'frontmatter/00-example-list.tex').write_text('\n'.join(lines), encoding='utf-8')
report = {'count': len(ids), 'first':ids[0], 'last':ids[-1], 'source_order_matches':True,
          'source_number_and_page_pairs': [[i,int(p)] for i,_,p in entries],
          'note':'10.1.2 source extraction split was repaired after image inspection; printed title is bar X, page 378.'}
(base / 'work/example-list-audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k!='source_number_and_page_pairs'},ensure_ascii=False))
