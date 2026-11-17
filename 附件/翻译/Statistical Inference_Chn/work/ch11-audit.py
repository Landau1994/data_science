import pathlib,re,json,hashlib
b=pathlib.Path(r'E:/project/math/data_science/附件/翻译/Statistical Inference_Chn')
files=[b/'chapters-tex/11.tex']+sorted((b/'sections-tex').glob('11-*.tex'));txt='\n'.join(f.read_text(encoding='utf-8') for f in files)
counts=[2,3,2,2,0,3,0,0,2,3,0,2,0,0,3,2,3,2,2,2,3,0,2,3,3,0,0,0,3,3,0,3,3,4,3,2,5,3,0,4,4]
exs=re.findall(r'\\begin\{exercise\}(.*?)\\end\{exercise\}',txt,re.S);assert len(exs)==41
assert [len(re.findall(r'\\item(?:\s|\\)',e)) for e in exs]==counts
anchors=[int(p) for p in re.findall(r'\\sourcepageanchor\{(\d+)\}',txt)];assert anchors==list(range(452,498))
labels=re.findall(r'\\label\{([^}]+)\}',txt);assert len(labels)==len(set(labels))
assert re.findall(r'\\label\{exercise:([^}]+)\}',txt)==[f'11.{i}' for i in range(1,42)]
expected_eq=[f'11.2.{i}' for i in range(1,19)]+[f'11.3.{i}' for i in range(1,45)]
assert re.findall(r'\\label\{eq:([^}]+)\}',txt)==expected_eq
obj={e:len(re.findall(r'\\begin\{'+e+r'\}',txt)) for e in ['definition','lemma','theorem','corollary','example','proof','exercise','equation','figure','table','tabular']}
d={'chapter':11,'source_printed_pages':[421,466],'source_physical_pages':anchors,'source_pages_visually_checked':anchors,'source_numbered_objects':{e:re.findall(r'\\label\{'+p+r':([^}]+)\}',txt) for e,p in [('definitions','def'),('lemmas','lem'),('theorems','thm'),('examples','ex'),('equations','eq'),('figures','fig'),('tables','tab'),('exercises','exercise')]},'object_counts':obj,'exercise_letter_parts':[{'number':f'11.{i+1}','parts':list('abcdefghijklmnopqrstuvwxyz'[:c])} for i,c in enumerate(counts)],'exercise_letter_part_count':sum(counts),'exercise_stars':[],'exercise_nested_parts':{},'source_footnotes':0,'translator_footnotes':len(re.findall(r'\\footnote\{译注：',txt)),'figures':[str(f.relative_to(b)).replace('\\','/') for f in (b/'assets/chapter11').glob('*.pdf')],'local_build':'pending final visual','files':{str(f.relative_to(b)):hashlib.sha256(f.read_bytes()).hexdigest() for f in files}}
(b/'work/ch11-manifest.json').write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps({'counts':obj,'parts':sum(counts),'notes':d['translator_footnotes'],'anchors':len(anchors)},ensure_ascii=False))
