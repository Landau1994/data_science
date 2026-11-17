import pathlib,re,json,hashlib,sys
b=pathlib.Path(r'E:/project/math/data_science/附件/翻译/Statistical Inference_Chn')
files=[b/'chapters-tex/10.tex']+sorted((b/'sections-tex').glob('10-*.tex'));txt='\n'.join(f.read_text(encoding='utf-8') for f in files)
subcounts=[0,0,2,3,3,2,0,2,4,3,4,0,5,3,2,3,5,0,3,3,2,3,4,0,0,2,3,0,2,3,5,2,0,2,2,3,2,0,3,0,3,0,2,0,0,2,2,0]
exs=re.findall(r'\\begin\{exercise\}(.*?)\\end\{exercise\}',txt,re.S)
assert len(exs)==48
actual=[]
for e in exs:
 depth=0;c=0
 for m in re.finditer(r'\\begin\{enumerate\}|\\end\{enumerate\}|\\item(?:\s|\\)',e):
  if m.group().startswith(r'\begin'):depth+=1
  elif m.group().startswith(r'\end'):depth-=1
  elif depth==1:c+=1
 actual.append(c)
assert actual==subcounts,[(i+1,a,c) for i,(a,c) in enumerate(zip(actual,subcounts)) if a!=c]
anchors=[int(p) for p in re.findall(r'\\sourcepageanchor\{(\d+)\}',txt)]
assert anchors==list(range(408,452)),anchors
labels=re.findall(r'\\label\{([^}]+)\}',txt);assert len(labels)==len(set(labels))
obj={e:len(re.findall(r'\\begin\{'+e+r'\}',txt)) for e in ['definition','theorem','corollary','example','proof','exercise','equation','figure','table','tabular']}
notes=re.findall(r'\\footnote\{译注：',txt)
manifest={'chapter':10,'source_printed_pages':[377,420],'source_physical_pages':anchors,'source_pages_visually_checked':list(range(408,452)),'source_numbered_objects':{e:re.findall(r'\\label\{'+p+r':([^}]+)\}',txt) for e,p in [('definitions','def'),('theorems','thm'),('corollaries','cor'),('examples','ex'),('equations','eq'),('figures','fig'),('tables','tab'),('exercises','exercise')]},'object_counts':obj,'exercise_letter_parts':[{'number':f'10.{i+1}','parts':list('abcdefghijklmnopqrstuvwxyz'[:c])} for i,c in enumerate(subcounts)],'exercise_letter_part_count':sum(subcounts),'exercise_nested_roman_parts':{'10.29.b':['i','ii','iii','iv'],'10.30.b':['i','ii','iii']},'source_footnotes':1,'translator_footnotes':len(notes),'figures':[str(f.relative_to(b)).replace('\\','/') for f in (b/'assets/chapter10').glob('*.pdf')],'local_build':'pending final build/visual','files':{str(f.relative_to(b)):hashlib.sha256(f.read_bytes()).hexdigest() for f in files}}
(b/'work/ch10-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'counts':obj,'parts':sum(subcounts),'notes':len(notes),'anchors':len(anchors)},ensure_ascii=False))
