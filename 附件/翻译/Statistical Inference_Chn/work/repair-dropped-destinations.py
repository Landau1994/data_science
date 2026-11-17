from pathlib import Path
import json,re
B=Path(__file__).resolve().parents[1]
labels=json.loads((B/'work/full-pdf-label-destinations.json').read_text(encoding='utf-8'))
missing={key for key,value in labels.items()if not value.get('resolved_destination')and re.match(r'(?:exercise|thm):',key)}
changed=[]
for p in (B/'sections-tex').glob('*.tex'):
 s=p.read_text(encoding='utf-8');before=s
 for key in missing:
  target=r'\label{'+key+'}'
  if target in s:
   if target+r'\leavevmode'in s:continue
   s=s.replace(target,target+r'\leavevmode');changed.append(key)
 if s!=before:p.write_text(s,encoding='utf-8')
(B/'work/repaired-destinations.json').write_text(json.dumps(changed),encoding='utf-8')
print('Restored heading emission at',len(changed),'missing numbered-object destinations.')
