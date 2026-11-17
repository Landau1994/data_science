import pathlib,re,json,hashlib,sys
b=pathlib.Path(r'E:/project/math/data_science/附件/翻译/Statistical Inference_Chn')
p=b/'sections-tex/09-02.tex';t=p.read_text(encoding='utf-8').replace(r'\autoref{exercise:3.41}--\ref{exercise:3.43}',r'\autoref{exercise:3.41}至\autoref{exercise:3.43}');p.write_text(t,encoding='utf-8')
s=(b/'Statistical Inference_Chn.tex').read_text(encoding='utf-8').split(r'\begin{document}')[0]
s+=r'\providecommand{\sourcepageanchor}[1]{\phantomsection\label{src:#1}}'+'\n'+r'\begin{document}\setcounter{section}{8}\input{chapters-tex/09.tex}\end{document}'
(b/'work/ch09-preview.tex').write_text(s,encoding='utf-8')
files=[b/'chapters-tex/09.tex']+sorted((b/'sections-tex').glob('09-*.tex'));txt='\n'.join(f.read_text(encoding='utf-8') for f in files)
subcounts=[0,0,2,3,2,2,2,0,0,2,0,0,3,3,3,3,2,3,0,4,0,0,2,0,0,0,3,3,2,3,2,4,2,2,2,0,0,3,0,2,2,2,2,2,4,0,0,3,2,2,0,5,4,3,0,0,3,3]
exs=re.findall(r'\\begin\{exercise\}(.*?)\\end\{exercise\}',txt,re.S)
actual=[len(re.findall(r'\\item(?:\s|\\)',e)) for e in exs]
assert len(exs)==58,(len(exs),actual)
assert actual==subcounts,[(i+1,a,c) for i,(a,c) in enumerate(zip(actual,subcounts)) if a!=c]
anchors=[int(p) for p in re.findall(r'\\sourcepageanchor\{(\d+)\}',txt)]
assert anchors==list(range(368,408)),anchors
labels=re.findall(r'\\label\{([^}]+)\}',txt);assert len(labels)==len(set(labels))
obj={e:len(re.findall(r'\\begin\{'+e+r'\}',txt)) for e in ['definition','theorem','corollary','example','proof','exercise','equation','figure','table','tabular']}
notes=re.findall(r'\\footnote\{译注：',txt)
manifest={'chapter':9,'source_printed_pages':[337,376],'source_physical_pages':anchors,'source_pages_visually_checked':list(range(368,408)),'source_numbered_objects':{e:re.findall(r'\\label\{'+p+r':([^}]+)\}',txt) for e,p in [('definitions','def'),('theorems','thm'),('corollaries','cor'),('examples','ex'),('equations','eq'),('figures','fig'),('tables','tab'),('exercises','exercise')]},'object_counts':obj,'exercise_letter_parts':[{'number':f'9.{i+1}','parts':list('abcdefghijklmnopqrstuvwxyz'[:c])} for i,c in enumerate(subcounts)],'exercise_letter_part_count':sum(subcounts),'source_footnotes':0,'translator_footnotes':len(notes),'figures':[str(f.relative_to(b)).replace('\\','/') for f in (b/'assets/chapter9').glob('*.pdf')],'local_build':'pending final build/visual','files':{str(f.relative_to(b)):hashlib.sha256(f.read_bytes()).hexdigest() for f in files}}
(b/'work/ch09-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'counts':obj,'parts':sum(subcounts),'notes':len(notes),'anchors':len(anchors)},ensure_ascii=False))
