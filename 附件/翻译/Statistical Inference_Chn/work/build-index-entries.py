from pathlib import Path
import json,re
B=Path(__file__).resolve().parents[1]
r=json.loads((B/'work/index-lines.json').read_text(encoding='utf-8'));out=[]
for x in r:
    o=round(x['x']-(54.2 if x['col']==0 else 256.4))
    t=x['raw'].replace('´e','é').replace('H¨older','Hölder').replace('˘i','ĭ')
    if out and (re.fullmatch(r'[\d, –-]+',t) or o==40):
        out[-1]['raw']+=' '+t;out[-1]['raw_ids'].append(x['id']);continue
    out.append({'id':len(out)+1,'raw_ids':[x['id']],'physical':x['physical'],'level':0 if o==0 else 1 if o==20 else 2,'raw':t})
for e in out:
    m=re.search(r',\s*(\d[\d, –-]*)$',e['raw'])
    e['term']=e['raw'][:m.start()].strip() if m else e['raw']
    e['refs']=m.group(1) if m else ''
(B/'work/index-entries.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
terms=list(dict.fromkeys(e['term'] for e in out))
(B/'work/index-terms.txt').write_text('\n'.join(terms)+'\n',encoding='utf-8')
print('logical entries',len(out),'distinct terms',len(terms),'source page references',sum(len(re.findall(r'\d+',e['refs'])) for e in out))
