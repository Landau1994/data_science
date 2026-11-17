"""Link only author/year forms that are verified against the source bibliography.
Run after chapters are released by their translators; all edits and unresolved years logged.
"""
from pathlib import Path
import re,json,sys
B=Path(__file__).resolve().parents[1]
keys=json.loads((B/'work/bibliography-author-keys.json').read_text(encoding='utf-8'))
chapters=sys.argv[1:] or ['01','02','05','09']
paths=[p for p in (B/'sections-tex').glob('*.tex') if p.name[:2] in chapters]+[B/'backmatter/02-distributions.tex']
namespecial={'deFinetti':r'(?:de\s*Finetti)','Luceño':r'(?:Luceño|Luce\\~n[o]|Luceno)', 'Scheffé':r'(?:Scheffé|Scheffe|Scheff\\\'e)', 'Rouseeuw':r'(?:Rouseeuw|Rousseeuw)', 'Shervisch':r'(?:Shervisch|Schervish)'}
def np(n):return namespecial.get(n,re.escape(n).replace(r'\ ',r'\s*'))
connector=r'\s*(?:,\s*and|and|与|和|及|、|,|–|—|--)\s*'
patterns=[]
for k in keys:
 names=k['names'];author=connector.join(np(n) for n in names)
 if len(names)>2:author='(?:'+author+'|'+np(names[0])+r'\s*(?:et\s+al\.|等))'
 elif len(names)==2:author='(?:'+author+')'
 for year in k['years']:
  # Closing punctuation is consumed only when present; commas with a following year need manual splitting.
  p=re.compile(r'(?<![A-Za-z])'+author+r'\s*(?:[（(，,]\s*)?'+year+r'(?![0-9a-z])(?:\s*[）)])?',re.I)
  patterns.append((p,k['number'],len(names)))
def braced_end(s,start):
 depth=0
 for i in range(start,len(s)):
  if s[i]=='{' and (i==0 or s[i-1]!='\\'):depth+=1
  elif s[i]=='}' and (i==0 or s[i-1]!='\\'):
   depth-=1
   if depth==0:return i+1
 raise ValueError('unclosed brace')
def protected(s):
 spans=[]
 for m in re.finditer(r'\\hyperref\[[^]]+\]\{',s):spans.append((m.start(),braced_end(s,m.end()-1)))
 for m in re.finditer(r'\\(?:index|footnote)\{',s):
  if m[0].startswith(r'\index'):spans.append((m.start(),braced_end(s,m.end()-1)))
 return spans
def hits(s):
 out=[]
 for pat,n,authors in patterns:
  for m in pat.finditer(s):
   if authors==1 and re.search(r'(?:和|与)$',s[max(0,m.start()-8):m.start()]):continue
   out.append((m.start(),m.end(),n,m[0],authors))
 return sorted(out,key=lambda x:(x[0],-(x[1]-x[0])))
changes=[];ambiguous=[]
for p in paths:
 s=p.read_text(encoding='utf-8')
 # Existing first-batch source-PDF citation wrappers become precise bibliography links.
 def source_repl(m):
  matches=hits(m[2]);ids={h[2] for h in matches}
  if len(ids)==1:
   n=next(iter(ids));changes.append({'file':str(p.relative_to(B)),'text':m[2],'number':n,'kind':'source-wrapper'})
   return r'\hyperref[bib:source'+str(n)+']{'+m[2]+'}'
  return m[0]
 s=re.sub(r'\\sourcepageref\{(\d+)\}\{([^{}]+)\}',source_repl,s)
 spans=protected(s);selected=[]
 for a,z,n,t,count in hits(s):
  if any(a<y and z>x for x,y in spans):continue
  if any(a<y and z>x for x,y,_,_,_ in selected):continue
  if re.match(r'\s*[，,]\s*(?:18|19|20)\d{2}',s[z:]):
   ambiguous.append({'file':str(p.relative_to(B)),'text':s[a:z+12],'reason':'multiple years'});continue
  selected.append((a,z,n,t,count))
 for a,z,n,t,count in reversed(selected):
  s=s[:a]+r'\hyperref[bib:source'+str(n)+']{'+t+'}'+s[z:]
  changes.append({'file':str(p.relative_to(B)),'text':t,'number':n,'kind':'author-year'})
 p.write_text(s,encoding='utf-8')
log=B/'work/citation-link-edits.json'
prior=json.loads(log.read_text(encoding='utf-8')) if log.exists() else []
log.write_text(json.dumps(prior+changes,ensure_ascii=False,indent=2),encoding='utf-8')
(B/'work/citation-link-pending.json').write_text(json.dumps(ambiguous,ensure_ascii=False,indent=2),encoding='utf-8')
print('linked',len(changes),'manual multiple-year cases',len(ambiguous))
print(json.dumps(ambiguous,ensure_ascii=False,indent=2))
