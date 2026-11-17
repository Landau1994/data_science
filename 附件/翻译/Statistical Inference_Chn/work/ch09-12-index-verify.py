from pathlib import Path
import json,re,collections,hashlib
b=Path(__file__).resolve().parents[1]
rows=json.loads((b/'work/index-locations-ch09-12.json').read_text(encoding='utf-8'))
src={x['id']:x for x in json.loads((b/'work/index-semantic-candidates.json').read_text(encoding='utf-8')) if 368<=x['source_physical']<=526}
assert len(rows)==len(src)==318
assert {x['id'] for x in rows}==set(src)
labels={};locs={};page=None
for ch in range(9,13):
 for f in [b/f'chapters-tex/{ch:02}.tex']+sorted((b/'sections-tex').glob(f'{ch:02}-*.tex')):
  t=f.read_text(encoding='utf-8');init=page;marks=[];rel=f.relative_to(b).as_posix()
  for m in re.finditer(r'\\sourcepageanchor\{(\d+)\}|\\label\{([^}]+)\}',t):
   if m[1]:page=int(m[1]);marks.append((m.start(),page))
   else:
    assert m[2] not in labels,m[2]
    labels[m[2]]=(rel,m.start(),page)
  locs[rel]=(t,init,marks)
verify=[]
for row in rows:
 if 'label' in row:
  assert not row['label'].startswith('src:')
  f,pos,pg=labels[row['label']]
 else:
  f=row['file'];t,pg,marks=locs[f]
  assert t.count(row['after'])==1
  pos=t.index(row['after'])+len(row['after']);pg=next((v for k,v in reversed(marks) if k<pos),pg)
 t=locs[f][0];last=t.rfind('\n',0,pos);end=t.find('\n',pos)
 rec={'id':row['id'],'path':src[row['id']]['path'],'source_physical':src[row['id']]['source_physical'],'target_source_physical':pg,'file':f,'line':t.count('\n',0,pos)+1,'context':t[max(last+1,0):end if end>=0 else len(t)]}
 if 'after' in row:
  pre=t[:pos];depth=0
  for m in re.finditer(r'(?<!\\)[{}]',pre):depth+=1 if m[0]=='{' else -1
  assert depth==0,(row['id'],'brace depth',depth)
  assert len(re.findall(r'(?<!\\)\$',pre))%2==0,(row['id'],'math delimiter')
 assert abs(pg-rec['source_physical'])<=1,rec
 verify.append(rec)
report={'count':len(rows),'labels':sum('label'in x for x in rows),'paragraphs':sum('after'in x for x in rows),'chapter_counts':dict(collections.Counter(x['file'].split('/')[1][:2] for x in verify)),'source_page_anchor_targets':0,'unresolved':0,'duplicate_ids':0,'nonunique_text':0,'unsafe_text_insertions':0,'scope_physical':[368,526],'scope_printed':[337,495],'mapping_sha256':hashlib.sha256((b/'work/index-locations-ch09-12.json').read_bytes()).hexdigest(),'items':verify}
(b/'work/ch09-12-index-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k!='items'},ensure_ascii=False,indent=2))
