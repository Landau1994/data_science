"""Audit actual PDF annotations, object numbers and named destinations by source unit."""
from pathlib import Path
from collections import Counter
import sys,json,re,hashlib
B=Path(__file__).resolve().parents[1];sys.path.insert(0,str(B/'work/python-deps'))
import pymupdf as fitz
target=Path(sys.argv[1])if len(sys.argv)>1 else B/'work/Statistical Inference_Chn.pdf'
if not target.is_absolute():target=B/target
baseline=json.loads((B/'work/source-baseline.json').read_text(encoding='utf-8'))
source=fitz.open(baseline['path']);doc=fitz.open(target)
def groups(s):
 out=[];depth=0;start=None
 for i,c in enumerate(s):
  if i and s[i-1]=='\\':continue
  if c=='{':
   if depth==0:start=i+1
   depth+=1
  elif c=='}':
   depth-=1
   if depth==0:out.append(s[start:i])
 return out
aux=target.with_suffix('.aux').read_text(encoding='utf-8');labels={}
for line in aux.splitlines():
 if line.startswith(r'\newlabel{'):
  a=groups(line)
  if len(a)>=2:
   vals=groups(a[1])
   if len(vals)>=4:labels[a[0]]={'number':vals[0],'page_text':vals[1],'title':vals[2],'destination':vals[3]}
names=doc.resolve_names()
for val in labels.values():val['resolved_destination']=names.get(val['destination'])
def countlinks(d,start,end):
 c=Counter();bad=[];details=[]
 for i in range(start-1,end):
  for l in d[i].get_links():
   kind=l['kind'];cat='internal'if kind==fitz.LINK_GOTO or(kind==fitz.LINK_NAMED and l.get('page',-1)>=0)else'remote'if kind==fitz.LINK_GOTOR else'uri'if kind==fitz.LINK_URI else'named'if kind==fitz.LINK_NAMED else'other'
   c[cat]+=1
   rec={'page':i+1,'kind':cat,'rect':list(l['from']),'target_page':l.get('page',-1)+1,'name':l.get('nameddest')or l.get('name'),'uri':l.get('uri')}
   if cat=='internal'and not 0<=l.get('page',-1)<len(d):bad.append(rec)
   if cat=='named'and l.get('page',-1)<0:bad.append(rec)
   details.append(rec)
 return dict(c),bad,details
source_counts,source_bad,source_links=countlinks(source,1,len(source));target_counts,target_bad,target_links=countlinks(doc,1,len(doc))
boundaries=[('front',1,31,None)]
starts=[32,69,101,145,200,252,283,333,368,408,452,498,528]
for ch in range(1,13):boundaries.append((f'chapter{ch}',starts[ch-1],starts[ch]-1,f'sec:{ch}'))
boundaries += [('computer-algebra',528,533,'app:computer-algebra'),('distributions',534,539,'app:distributions'),('references',540,555,'app:references'),('index',556,566,'app:index')]
present=[]
for name,a,z,label in boundaries:
 dest=labels.get(label,{}).get('resolved_destination')if label else{'page':0}
 if dest and dest.get('page',-1)>=0:present.append({'name':name,'source_start':a,'source_end':z,'target_start':dest['page']+1,'label':label})
for i,u in enumerate(present):
 u['target_end']=present[i+1]['target_start']-1 if i+1<len(present)else len(doc)
 u['source_links']=countlinks(source,u['source_start'],u['source_end'])[0]
 u['target_links']=countlinks(doc,u['target_start'],u['target_end'])[0]
 u['raw_internal_difference']=u['target_links'].get('internal',0)-u['source_links'].get('internal',0)
number_errors=[];number_checks=0
for key,val in labels.items():
 m=re.fullmatch(r'(?:def|thm|lem|cor|ex|exercise|eq|fig|tab):([\d.]+)',key)
 if m:
  number_checks+=1
  if m[1]!=val['number']:number_errors.append({'label':key,'actual':val['number']})
indexmap=json.loads((B/'work/index-semantic-resolved.json').read_text(encoding='utf-8'))
missing_index_targets=[]
rows=indexmap.values()if isinstance(indexmap,dict)else indexmap
for r in rows:
 key=r['target']
 if not labels.get(key,{}).get('resolved_destination'):missing_index_targets.append(r)
result={'target':str(target.relative_to(B)),'pages':len(doc),'sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'source_counts':source_counts,'target_counts':target_counts,'units':present,'bad_links':target_bad,'number_checks':number_checks,'number_errors':number_errors,'index_resolved_count':len(indexmap),'missing_index_targets':missing_index_targets,'named_destinations':len(names),'bookmarks':doc.get_toc()}
(B/'work/full-pdf-link-audit.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
(B/'work/full-pdf-label-destinations.json').write_text(json.dumps(labels,ensure_ascii=False,indent=2),encoding='utf-8')
(B/'work/full-pdf-link-rectangles.json').write_text(json.dumps({'source':source_links,'target':target_links},ensure_ascii=False),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items()if k not in ['bookmarks','bad_links','missing_index_targets']},ensure_ascii=False,indent=2))
print('Bad link annotations:',len(target_bad),'Unresolved semantic index targets:',len(missing_index_targets))
print('Bad link names:',sorted(set(l['name']or''for l in target_bad)))
print('Labels without a PDF destination:',[(k,v['destination'])for k,v in labels.items()if not v.get('resolved_destination')])
