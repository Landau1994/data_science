from pathlib import Path
import json
B=Path(__file__).resolve().parents[1]
p=B/'work/wholebook-visual-delta.json';d=json.loads(p.read_text(encoding='utf-8'))
rows=[]
for name in 'abc':
 r=json.loads((B/f'work/wholebook-delta-{name}.json').read_text(encoding='utf-8'))
 assert r['pdf_sha256']==d['after_pdf_sha256'],name
 assert not r['findings'],(name,r['findings'])
 rows.append(r)
seen=set(n for r in rows for n in r['pages_viewed'])
assert set(d['changed_pages'])<=seen,(sorted(set(d['changed_pages'])-seen))
d['reviewed_pages']=sorted(seen);d['review_reports']=[f'work/wholebook-delta-{x}.json'for x in 'abc'];d['status']='passed';d['review_scope']='全页视觉，不仅是改动位置；未修改页经像素一致性确认承接原核验。'
p.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf-8')
print('All',len(d['changed_pages']),'changed pages visually reviewed; remaining',len(d['unchanged_pages']),'pages pixel-identical.')
