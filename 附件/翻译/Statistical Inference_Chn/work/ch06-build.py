from pathlib import Path
import re,json,collections,sys
r=Path(r'E:/project/math/data_science/附件/翻译/Statistical Inference_Chn')
main=(r/'Statistical Inference_Chn.tex').read_text(encoding='utf-8')
preamble=main.split(r'\begin{document}')[0]
(r/'work/ch06-preview.tex').write_text(preamble+'\n\\begin{document}\n\\setcounter{section}{5}\n\\input{chapters-tex/06.tex}\n\\end{document}\n',encoding='utf-8')
tex='\n'.join(p.read_text(encoding='utf-8') for p in sorted((r/'sections-tex').glob('06-*.tex')))
labels=re.findall(r'\\label\{([^}]+)\}',tex)
types={2:['def','thm','ex','ex','ex','thm','ex','ex','ex','thm','def','ex','thm','ex','ex','def','ex','ex','ex','ex','def','ex','ex','thm','thm','ex','ex','thm'],3:['def','ex','ex','ex','ex','thm','ex'],4:['ex','def','ex','def','ex','ex'],6:['def','thm','def','thm','thm']}
expected=[f'{t}:6.{s}.{i}' for s,ts in types.items() for i,t in enumerate(ts,1)]
actual=[x for x in labels if re.match(r'(def|ex|thm|lem):6\.',x)]
eqs=[f'eq:6.{s}.{i}' for s,n in [(2,7),(3,5),(4,1)] for i in range(1,n+1)]
parts={9:'abcde',11:'ab',12:'ab',15:'ab',16:'abc',20:'abcde',21:'abc',22:'ab',25:'abcd',26:'abcde',27:'ab',30:'ab',31:'abc',33:'abc',36:'ab',37:'ab',39:'ab',40:'ab',41:'abc',42:'ab',43:'ab'}
exs=[]
for b in re.findall(r'\\begin\{exercise\}(.*?)\\end\{exercise\}',tex,re.S):
 ident=re.search(r'\\label\{exercise:(6\.\d+)\}',b).group(1);n=int(ident.split('.')[-1]);depth=0;counts=collections.Counter()
 for tok in re.finditer(r'\\begin\{enumerate\}|\\end\{enumerate\}|\\item\b',b):
  t=tok.group()
  if t==r'\begin{enumerate}':depth+=1
  elif t==r'\end{enumerate}':depth-=1
  else:counts[depth]+=1
 count=counts[1] if n!=26 else len(re.findall(r'^\([a-e]\)&',b,re.M))
 actualparts='abcdefghijklmnopqrstuvwxyz'[:count]
 exs.append({'id':ident,'source_letter_parts':parts.get(n,''),'tex_letter_parts':actualparts,'match':parts.get(n,'')==actualparts,'nested_roman_parts':counts[2]})
anchors=list(map(int,re.findall(r'\\sourcepageanchor\{(\d+)\}',tex)))
data={'source':json.loads((r/'work/source-baseline.json').read_text(encoding='utf-8')),'range':{'physical':[252,282],'printed':[221,251]},'source_pages_visually_checked':list(range(252,283)),'source_object_order':expected,'tex_object_order':actual,'object_order_match':expected==actual,'source_equation_order':eqs,'tex_equation_order':[x for x in labels if x.startswith('eq:6.')],'equations_match':eqs==[x for x in labels if x.startswith('eq:6.')],'exercises':exs,'exercise_order_match':[x['id'] for x in exs]==[f'6.{n}' for n in range(1,44)],'source_explicit_proofs':4,'counts':dict(collections.Counter(re.findall(r'\\begin\{(theorem|definition|lemma|example|proof|equation|figure|table|exercise)\}',tex))),'source_footnotes':2,'translator_footnotes':len(re.findall(r'\\footnote\{译注：',tex)),'anchors':anchors,'anchors_match':anchors==list(range(252,283)),'duplicate_labels':[k for k,v in collections.Counter(labels).items() if v>1],'figures':[],'unnumbered_tables':['exercise:6.19','exercise:6.26'],'scope_note':'源页逐页目视核对；有序对象和分问集合对账不替代逐段内容核对.局部预览的章外引用待全书解析.'}
(r/'work/ch06-manifest.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
print({k:data[k] for k in ['object_order_match','equations_match','exercise_order_match','counts','translator_footnotes','anchors_match','duplicate_labels']})
print('part mismatches',[x for x in exs if not x['match']])
