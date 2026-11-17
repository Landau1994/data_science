from pathlib import Path
import json
B=Path(__file__).resolve().parents[1]
for name in ['index-locations-ch03-04.json','index-locations-ch08.json']:
 p=B/'work'/name;rows=json.loads(p.read_text(encoding='utf-8'))
 for r in rows:
  if r['id']=='398:196':r['after']=r'量 $\sum_i a_i\log(1/a_i)$ 称为熵（entropy）'
  elif 'after'in r and r['id'] in {'243:344','476:348','478:348','479:344','480:348','481:348','484:333'}:
   r['after']=r['after'].removesuffix('.').replace('）',r'\mbox{）.}')
 p.write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
print('Refreshed semantic fragments after citation and punctuation binding edits.')
