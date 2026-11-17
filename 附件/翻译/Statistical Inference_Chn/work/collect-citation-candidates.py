from pathlib import Path
import re,json
B=Path(__file__).resolve().parents[1]
paths=list((B/'frontmatter').glob('*.tex'))+list((B/'sections-tex').glob('*.tex'))+[B/'backmatter/01-computer-algebra.tex',B/'backmatter/01-computer-algebra-b.tex',B/'backmatter/02-distributions.tex']
records=[]
for p in paths:
 for line_no,line in enumerate(p.read_text(encoding='utf-8').splitlines(),1):
  if line.lstrip().startswith('%') or r'\includegraphics' in line:continue
  for m in re.finditer(r'(?<!\d)(?:18|19|20)\d{2}[a-z]?(?!\d)',line):
   window=line[max(0,m.start()-125):min(len(line),m.end()+70)]
   # Dates only become citation candidates when a Latin author name is nearby.
   if not re.search(r'[A-Za-z]{3}',window):continue
   records.append({'file':str(p.relative_to(B)).replace('\\','/'),'line':line_no,'year':m[0],'context':window})
(B/'work/citation-candidates.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')
for ch in ['01','02','05','09']:
 rs=[r for r in records if '/'+ch+'-' in r['file']]
 (B/f'work/citations-ch{ch}.txt').write_text('\n'.join(f"{r['file']}:{r['line']} {r['context']}" for r in rs)+'\n',encoding='utf-8')
 print(ch,len(rs))
