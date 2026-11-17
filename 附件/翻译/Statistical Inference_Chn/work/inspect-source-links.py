from pathlib import Path
import sys,json
B=Path(__file__).resolve().parents[1];sys.path.insert(0,str(B/'work/python-deps'))
import pymupdf as fitz
d=fitz.open(json.loads((B/'work/source-baseline.json').read_text(encoding='utf-8'))['path'])
rows=[]
for i,p in enumerate(d):
 for l in p.get_links():
  if (540<=i+1<=555)or l['kind']==fitz.LINK_URI:
   r=fitz.Rect(l['from']);r.x0-=2;r.x1+=2;r.y0-=2;r.y1+=2
   rows.append({'physical':i+1,'text':p.get_textbox(r).replace('\n',' '),'kind':l['kind'],'target':l.get('uri')or l.get('nameddest')or l.get('name'),'page':l.get('page',-1)+1})
(B/'work/source-bib-external-links.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
for r in rows:print(r)
