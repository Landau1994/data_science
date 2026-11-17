import pathlib,re,json,hashlib
b=pathlib.Path(r'E:/project/math/data_science/附件/翻译/Statistical Inference_Chn')
files=[b/'chapters-tex/12.tex']+sorted((b/'sections-tex').glob('12-*.tex'));txt='\n'.join(f.read_text(encoding='utf-8') for f in files)
counts=[0,0,2,5,0,0,2,2,2,4,3,3,2,0,7,2,2,4,2,3,0,0,2,0,2,2,2,0,0,5,3]
exs=re.findall(r'\\begin\{exercise\}(.*?)\\end\{exercise\}',txt,re.S);assert len(exs)==31
assert [len(re.findall(r'\\label\{item:12\.[0-9]+\.[a-z]\}',e)) for e in exs]==counts
anchors=[int(p) for p in re.findall(r'\\sourcepageanchor\{(\d+)\}',txt)];assert anchors==list(range(498,527)),anchors
labels=re.findall(r'\\label\{([^}]+)\}',txt);assert len(labels)==len(set(labels))
assert re.findall(r'\\label\{exercise:([^}]+)\}',txt)==[f'12.{i}' for i in range(1,32)]
expected_eq=[f'12.2.{i}' for i in range(1,25)]+[f'12.3.{i}' for i in range(1,11)]+[f'12.4.{i}' for i in range(1,7)]
assert re.findall(r'\\label\{eq:([^}]+)\}',txt)==expected_eq
obj={e:len(re.findall(r'\\begin\{'+e+r'\}',txt)) for e in ['definition','lemma','theorem','corollary','example','proof','exercise','equation','figure','table','tabular']}
d={'chapter':12,'source_printed_pages':[467,495],'source_physical_pages':anchors,'source_pages_visually_checked':anchors,'source_numbered_objects':{e:re.findall(r'\\label\{'+p+r':([^}]+)\}',txt) for e,p in [('definitions','def'),('lemmas','lem'),('theorems','thm'),('examples','ex'),('equations','eq'),('figures','fig'),('tables','tab'),('exercises','exercise')]},'object_counts':obj,'exercise_letter_parts':[{'number':f'12.{i+1}','parts':list('abcdefghijklmnopqrstuvwxyz'[:c])} for i,c in enumerate(counts)],'exercise_letter_part_count':sum(counts),'exercise_stars':[],'exercise_nested_parts':{'12.3.b':['i','ii','iii','iv'],'12.26.a':['i','ii']},'source_footnotes':0,'translator_footnotes':len(re.findall(r'\\footnote\{译注：',txt)),'figures':[str(f.relative_to(b)).replace('\\','/') for f in (b/'assets/chapter12').glob('*.pdf')],'local_build':'pending final visual','files':{str(f.relative_to(b)):hashlib.sha256(f.read_bytes()).hexdigest() for f in files}}
(b/'work/ch12-manifest.json').write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps({'counts':obj,'parts':sum(counts),'notes':d['translator_footnotes'],'anchors':len(anchors)},ensure_ascii=False))
