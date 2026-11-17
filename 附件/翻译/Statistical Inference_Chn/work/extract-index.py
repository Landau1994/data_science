from pathlib import Path
import json,sys,unicodedata,re
B=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(B/'work/python-deps'))
import pymupdf as fitz
s=json.loads((B/'work/source-baseline.json').read_text(encoding='utf-8'));d=fitz.open(s['path'])
rows=[]
for num in range(556,567):
    p=d[num-1]
    top=150 if num==556 else 49
    for col,(x0,x1) in enumerate([(45,251),(252,458)]):
        lines=[]
        for b in p.get_text('dict',clip=fitz.Rect(x0,top,x1,683))['blocks']:
            for l in b.get('lines',[]):
                t=unicodedata.normalize('NFC',''.join(s['text'] for s in l['spans'])).strip()
                if not t:continue
                lines.append((round(l['bbox'][1],1),l['bbox'][0],t))
        for y,x,t in sorted(lines):
            if t=='INDEX' or (re.fullmatch(r'\d{3}',t) and y<70):continue
            rows.append({'id':len(rows)+1,'physical':num,'col':col,'x':round(x,1),'y':y,'raw':t})
(B/'work/index-lines.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
(B/'work/index-lines.txt').write_text('\n'.join(f"{r['id']:04}|{r['physical']}|{r['col']}|{r['x']}|{r['raw']}" for r in rows)+'\n',encoding='utf-8')
print('Index raw lines:',len(rows))
