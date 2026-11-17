"""Retain original visible page/number text and resolve book links to real objects."""
from pathlib import Path
import re,json
B=Path(__file__).resolve().parents[1]
special={12:'front:preface-second',14:'front:preface-first',18:'front:authors',20:'front:tables',22:'front:figures',24:'front:examples',528:'app:computer-algebra',534:'app:distributions',540:'app:references',556:'app:index'}
def endbrace(s,i):
 d=0
 for j in range(i,len(s)):
  if s[j]=='{' and (j==0 or s[j-1]!='\\'):d+=1
  elif s[j]=='}' and (j==0 or s[j-1]!='\\'):
   d-=1
   if d==0:return j+1
 raise ValueError('unclosed brace')
def spans(s):
 out=[]
 for m in re.finditer(r'\\sourcepageref\{(\d+)\}\{',s):
  z=endbrace(s,m.end()-1);out.append((m.start(),z,int(m[1]),s[m.end():z-1]))
 return out
log=[]
for p in list((B/'frontmatter').glob('*.tex'))+list((B/'sections-tex').glob('01-*.tex')):
 lines=p.read_text(encoding='utf-8').splitlines(True);new=[]
 for line in lines:
  found=spans(line);rowtarget=None
  if found and p.name=='00-contents.tex':
   title=found[0][3];m=re.match(r'(\d+(?:\.\d+)*)\s',title)
   rowtarget='sec:'+m[1] if m else special.get(found[0][2])
  elif found and p.name in ('00-figures.tex','00-tables.tex'):
   m=re.match(r'(\d+(?:\.\d+)+)\s',found[0][3]);assert m,line
   rowtarget=('fig:' if 'figures' in p.name else 'tab:')+m[1]
  elif found and p.name=='00-example-list.tex':
   m=re.match(r'(?:例|习题)\s*(\d+\.\d+\.\d+)',line);assert m,line
   rowtarget='ex:'+m[1]
  for a,z,page,visible in reversed(found):
   target=rowtarget
   if target is None:
    m=re.fullmatch(r'第(\d+(?:\.\d+)*)(?:章|节)',visible)
    if m:target='sec:'+m[1]
    else:
     m=re.fullmatch(r'(定义|定理|引理|例|习题|推论|图|表)\s*(\d+(?:\.\d+)+)',visible)
     if m:target={'定义':'def','定理':'thm','引理':'lem','例':'ex','习题':'exercise','推论':'cor','图':'fig','表':'tab'}[m[1]]+':'+m[2]
     elif page==528 and '附录'in visible:target='app:computer-algebra'
   assert target,(p.name,page,visible)
   log.append({'file':str(p.relative_to(B)),'source_physical':page,'text':visible,'target':target})
   line=line[:a]+r'\hyperref['+target+']{'+visible+'}'+line[z:]
  new.append(line)
 p.write_text(''.join(new),encoding='utf-8')
out=B/'work/internalized-source-links.json';old=json.loads(out.read_text(encoding='utf-8')) if out.exists() else []
out.write_text(json.dumps(old+log,ensure_ascii=False,indent=2),encoding='utf-8')
print('Resolved',len(log),'original book links; all visible numbers retained.')
