"""Plan local subpart links; apply only to released chapters after reviewing the plan."""
from pathlib import Path
import re,json,sys,importlib.util
B=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('scan',B/'work/scan-plain-references.py');scan=importlib.util.module_from_spec(spec);spec.loader.exec_module(scan)
chapters=[a for a in sys.argv[1:]if a!='--apply']or['01','03','05','09'];apply='--apply'in sys.argv
plan=[];errors=[]
for p in (B/'sections-tex').glob('*.tex'):
 if p.name[:2]not in chapters:continue
 s=p.read_text(encoding='utf-8');edits=[]
 for ex in re.finditer(r'\\begin\{exercise\}.*?\\end\{exercise\}',s,re.S):
  body=ex[0];n=re.search(r'\\label\{exercise:([\d.]+)\}',body)
  if not n:continue
  items={};depth=0;counter=0;style='alpha'
  for t in re.finditer(r'\\(begin|end)\{enumerate\}(?:\[([^]]+)\])?|\\item(?:\[([^]]+)\])?',body):
   if t[1]=='begin':
    depth+=1
    if depth==1:
     start=re.search(r'\bstart\s*=\s*(\d+)',t[2]or'')
     counter=int(start[1])-1 if start else 0;style='roman'if t[2]and r'\roman' in t[2]else'alpha'
   elif t[1]=='end':depth-=1
   elif depth==1:
    counter+=1;part=t[3].strip('()（） .:：')if t[3]else(['','i','ii','iii','iv','v','vi','vii','viii','ix','x'][counter]if style=='roman'else chr(96+counter))
    if part in items:items[part]=None
    else:items[part]=(t.end(),re.search(r'^\s*(?:\\phantomsection)?\\label\{([^}]+)\}',body[t.end():]))
  mask=scan.mask(body);needed=set()
  for r in re.finditer(r'[（(]([a-z]|[ivx]+)[)）]',mask):
   part=r[1]
   if part not in items:continue
   if items[part]is None:errors.append((p.name,n[1],part,'duplicate top-level item'));continue
   # Do not guess local targets when an explicit cross-object reference precedes the part.
   prefix=body[max(0,r.start()-70):r.start()]
   explicit=re.search(r'\\(?:autoref|ref)\{([^}]+)\}(?:的|中|部分|\s)*$',prefix)
   if explicit:continue
   pos,label=items[part];key=label[1]if label else 'itm:exercise:'+n[1]+':'+part
   edits.append((ex.start()+r.start(),ex.start()+r.end(),r'\hyperref['+key+']{'+r[0]+'}'))
   needed.add(part)
   plan.append({'file':p.name,'exercise':n[1],'part':part,'target':key,'context':body[max(0,r.start()-25):r.end()+65].replace('\n',' ')})
  for part in needed:
   pos,label=items[part]
   if not label:edits.append((ex.start()+pos,ex.start()+pos,r'\phantomsection\label{itm:exercise:'+n[1]+':'+part+'}'))
 if apply and not errors:
  for a,z,t in sorted(edits,reverse=True):s=s[:a]+t+s[z:]
  p.write_text(s,encoding='utf-8')
(B/'work/exercise-part-link-plan.json').write_text(json.dumps({'applied':apply,'links':plan,'errors':errors},ensure_ascii=False,indent=2),encoding='utf-8')
if apply:
 log=B/'work/exercise-part-link-edits.json';old=json.loads(log.read_text(encoding='utf-8'))if log.exists()else[]
 log.write_text(json.dumps(old+plan,ensure_ascii=False,indent=2),encoding='utf-8')
for r in plan:print(r['file'],r['target'],r['context'])
print('Links',len(plan),'Errors',errors,'Applied',apply)
if errors:raise SystemExit(1)
