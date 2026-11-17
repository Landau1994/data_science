"""Plan precise index locations, keeping source-page fallback explicit for review.
Uses the skill's pattern utility on real source terms; does not mutate chapter files.
"""
from pathlib import Path
import re,json,importlib.util
B=Path(__file__).resolve().parents[1]
skill=Path('C:/Users/Administrator/.codex/skills/pdf-to-chinese-tex/scripts/generate_index_anchors.py')
spec=importlib.util.spec_from_file_location('index_toolkit',skill);toolkit=importlib.util.module_from_spec(spec);spec.loader.exec_module(toolkit)
entries=json.loads((B/'work/index-translated.json').read_text(encoding='utf-8'))
translations={}
for line in (B/'work/index-translations.tsv').read_text(encoding='utf-8').splitlines():
 if line.strip():
  en,zh=line.split('|',1);translations[en.casefold()]=zh
def base(t):return re.split(r'\s*\(see',t,flags=re.I)[0]
anc=[]
for e in entries:
 anc=anc[:e['level']];anc.append(base(e['term']));e['path']=list(anc)
texts={p.name:p.read_text(encoding='utf-8') for p in sorted((B/'sections-tex').glob('*.tex'))}
segments={}
for f,s in texts.items():
 matches=list(re.finditer(r'\\sourcepageanchor\{(\d+)\}',s))
 for i,m in enumerate(matches):
  start=m.end();end=matches[i+1].start() if i+1<len(matches) else len(s)
  segments.setdefault(int(m[1]),[]).append({'file':f,'start':start,'end':end,'text':s[start:end]})
 # Continuation at the start of the next section belongs to the previous source page.
 if not matches:continue
 preceding=s[:matches[0].start()]
 prev=int(matches[0][1])-1
 if preceding.strip() and prev in segments:segments[prev].append({'file':f,'start':0,'end':matches[0].start(),'text':preceding})
source=(B/'work/source-layout.txt').read_text(encoding='utf-8').split('\f')
records=[]
for e in entries:
 for printed in re.findall(r'\d+',e['refs']):
  physical=int(printed)+31;rid=f"{e['id']}:{physical}"
  names=e['path'][::-1]
  patterns=[]
  for rank,name in enumerate(names):
   z=translations.get(name.casefold(),'')
   if z and len(z)>1:patterns.append((z,3/(rank+1),False))
   # The toolkit handles apostrophes/word-boundaries for ordinary English terms.
   pat,_=toolkit.generate_patterns(name)
   if pat:patterns.append((pat,2/(rank+1),True))
  hits=[]
  for seg in segments.get(physical,[]):
   for pat,weight,isregex in patterns:
    matches=list(pat.finditer(seg['text'])) if isregex else list(re.finditer(re.escape(pat),seg['text']))
    for m in matches:
     a=seg['start']+m.start();s=texts[seg['file']]
     ls=s.rfind('\n',0,a)+1;le=s.find('\n',a)
     if le<0:le=len(s)
     line=s[ls:le]
     if line.lstrip().startswith('%') or re.search(r'\\(?:label|ref|eqref|autoref|sourcepageanchor)\{[^}]*$',s[max(0,a-70):a]):continue
     hits.append({'file':seg['file'],'offset':a,'line':s.count('\n',0,a)+1,'matched':m[0],'weight':weight,'context':line})
  hits.sort(key=lambda h:(-h['weight'],h['offset']))
  unique=[];seen=set()
  for h in hits:
   key=(h['file'],h['line'])
   if key not in seen:unique.append(h);seen.add(key)
  sourcematches=[]
  for name in names:
   pat,_=toolkit.generate_patterns(name)
   if pat:
    for m in pat.finditer(source[physical-1]):
     sourcematches.append(re.sub(r'\s+',' ',source[physical-1][max(0,m.start()-100):m.end()+160]))
  records.append({'id':rid,'entry':e['id'],'path':e['path'],'zh':e['zh'],'source_physical':physical,'source_printed':int(printed),'source_contexts':sourcematches[:6],'tex_candidates':unique[:10],'translated_source_page_available':physical in segments})
(B/'work/index-semantic-candidates.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')
for ch,low,high in [(1,32,68),(2,69,100),(5,200,251),(9,368,407)]:
 rs=[r for r in records if low<=r['source_physical']<=high]
 out=[]
 for r in rs:
  hs=r['tex_candidates'];out.append(r['id']+' | '+' > '.join(r['path'])+' | '+r['zh']+' | '+str(r['source_printed']))
  for h in hs[:3]:out.append(f"  {h['file']}:{h['line']} {h['matched']} | {h['context'][:240]}")
  if not hs:out.extend('  EN '+t for t in r['source_contexts'][:2])
 (B/f'work/index-candidates-ch{ch:02}.txt').write_text('\n'.join(out)+'\n',encoding='utf-8')
 print(ch,'refs',len(rs),'with candidate',sum(bool(r['tex_candidates']) for r in rs))
print('source references:',len(records))
