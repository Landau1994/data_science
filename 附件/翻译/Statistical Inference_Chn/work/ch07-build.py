from pathlib import Path
import re,json,collections
r=Path(r'E:/project/math/data_science/附件/翻译/Statistical Inference_Chn')
main=(r/'Statistical Inference_Chn.tex').read_text(encoding='utf-8')
preamble=main.split(r'\begin{document}')[0]
(r/'work/ch07-preview.tex').write_text(preamble+'\n\\begin{document}\n\\setcounter{section}{6}\n\\input{chapters-tex/07.tex}\n\\end{document}\n',encoding='utf-8')
tex='\n'.join(p.read_text(encoding='utf-8') for p in sorted((r/'sections-tex').glob('07-*.tex')))
labels=re.findall(r'\\label\{([^}]+)\}',tex)
types={1:['def'],2:['ex','ex','ex','def','ex','ex','ex','ex','ex','thm','ex','ex','ex','ex','def','ex','ex','ex','ex','thm'],3:['def','def','ex','ex','ex','ex','def','ex','thm','cor','lem','ex','ex','ex','cor','ex','thm','ex','thm','thm','ex','ex','thm','ex','ex','ex','ex','ex','ex','ex'],5:['thm','thm']}
expected=[f'{t}:7.{s}.{i}' for s,ts in types.items() for i,t in enumerate(ts,1)]
actual=[x for x in labels if re.match(r'(def|ex|thm|lem|cor):7\.',x)]
eqs=[f'eq:7.{s}.{i}' for s,n in [(2,24),(3,19)] for i in range(1,n+1)]
parts={2:'ab',5:'ab',6:'abc',8:'abc',10:'abc',11:'ab',12:'abc',15:'ab',16:'abcde',17:'abcd',18:'ab',19:'abc',20:'ab',21:'ab',22:'abc',24:'ab',25:'ab',27:'abc',28:'ab',29:'abcd',30:'abc',31:'ab',32:'abc',34:'abc',35:'abc',36:'abcd',38:'ab',41:'ab',42:'ab',43:'ab',45:'abcde',46:'abcd',48:'ab',49:'abc',50:'abc',51:'abcd',52:'abc',54:'abc',55:'abc',57:'ab',58:'abc',62:'abc',65:'abcde',66:'abcd'}
exs=[]
for b in re.findall(r'\\begin\{exercise\}(.*?)\\end\{exercise\}',tex,re.S):
 ident=re.search(r'\\label\{exercise:(7\.\d+)\}',b).group(1);n=int(ident.split('.')[-1]);depth=0;counts=collections.Counter()
 for tok in re.finditer(r'\\begin\{enumerate\}|\\end\{enumerate\}|\\item\b',b):
  t=tok.group()
  if t==r'\begin{enumerate}':depth+=1
  elif t==r'\end{enumerate}':depth-=1
  else:counts[depth]+=1
 actualparts='abcdefghijklmnopqrstuvwxyz'[:counts[1]]
 exs.append({'id':ident,'source_letter_parts':parts.get(n,''),'tex_letter_parts':actualparts,'match':parts.get(n,'')==actualparts,'nested_roman_parts':counts[2]})
anchors=list(map(int,re.findall(r'\\sourcepageanchor\{(\d+)\}',tex)))
data={'source':json.loads((r/'work/source-baseline.json').read_text(encoding='utf-8')),'range':{'physical':[283,332],'printed':[252,301]},'source_pages_visually_checked':list(range(283,333)),'source_object_order':expected,'tex_object_order':actual,'object_order_match':expected==actual,'source_equation_order':eqs,'tex_equation_order':[x for x in labels if x.startswith('eq:7.')],'equations_match':eqs==[x for x in labels if x.startswith('eq:7.')],'exercises':exs,'exercise_order_match':[x['id'] for x in exs]==[f'7.{n}' for n in range(1,68)],'source_explicit_proofs':8,'counts':dict(collections.Counter(re.findall(r'\\begin\{(theorem|definition|corollary|lemma|example|proof|equation|figure|table|exercise)\}',tex))),'source_footnotes':1,'translator_footnotes':len(re.findall(r'\\footnote(?:text)?\{译注：',tex)),'anchors':anchors,'anchors_match':anchors==list(range(283,333)),'duplicate_labels':[k for k,v in collections.Counter(labels).items() if v>1],'figures':[{'id':'fig:7.3.1','source_physical':300,'clip':[62,387,446,533],'asset':'assets/chapter7/fig-7-3-1.pdf'},{'id':'fig:7.3.2','source_physical':315,'clip':[126,56,381,301],'asset':'assets/chapter7/fig-7-3-2.pdf'}],'numbered_tables':['tab:7.3.1','tab:7.4.2'],'unnumbered_tables':['exercise:7.1'],'scope_note':'源页逐页目视核对；有序对象和分问集合对账不替代逐段内容核对.局部预览的章外引用待全书解析.'}
(r/'work/ch07-manifest.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
print({k:data[k] for k in ['object_order_match','equations_match','exercise_order_match','counts','translator_footnotes','anchors_match','duplicate_labels']})
print('part mismatches',[x for x in exs if not x['match']])
