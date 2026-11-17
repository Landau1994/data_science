from pathlib import Path
import re,json,sys,collections
r=Path(r'E:/project/math/data_science/附件/翻译/Statistical Inference_Chn');sys.path.insert(0,str(r/'work/python-deps'));import pymupdf as fitz
files=sorted((r/'sections-tex').glob('05-*.tex'));tex='\n'.join(p.read_text(encoding='utf-8') for p in files)
labels=re.findall(r'\\label\{([^}]+)\}',tex)
expected_types={1:['def','ex','ex'],2:['def','def','def','thm','lem','thm','thm','ex','thm','ex','thm','ex'],3:['thm','lem','lem','def','ex','def','ex','thm'],4:['def','def','thm','thm','ex','thm','ex'],5:['def','thm','ex','thm','ex','def','ex','ex','thm','def','ex','thm','thm','thm','thm','ex','thm','ex','ex','def','thm','ex','ex','thm','ex','thm','ex','thm'],6:['ex','ex','ex','ex','ex','ex','ex','thm','ex']}
expected_objects=[f'{typ}:5.{s}.{i}' for s,ts in expected_types.items() for i,typ in enumerate(ts,1)]
actual_objects=[x for x in labels if re.match(r'(def|ex|thm|lem):5\.',x)]
expected_equations=[f'eq:5.{s}.{i}' for s,n in [(1,4),(2,6),(3,9),(4,7),(5,13),(6,12)] for i in range(1,n+1)]
parts={2:'ab',4:'ab',6:'abc',7:'ab',8:'abc',10:'abc',14:'ab',15:'ab',16:'abc',17:'abcd',18:'abcde',19:'abc',20:'abc',26:'abc',27:'ab',28:'ab',32:'ab',35:'ab',36:'ab',37:'abc',38:'abcd',39:'ab',40:'abc',41:'ab',42:'ab',43:'ab',44:'abc',45:'abc',49:'abc',51:'abc',52:'abc',53:'ab',54:'ab',56:'ab',57:'abc',58:'abcd',60:'ab',61:'abcd',62:'abc',64:'abc',66:'abc',67:'abc',68:'abcd'}
exercise_data=[]
for body in re.findall(r'\\begin\{exercise\}(.*?)\\end\{exercise\}',tex,re.S):
 id=re.search(r'\\label\{exercise:(5\.\d+)\}',body).group(1);n=int(id.split('.')[-1]); count=len(re.findall(r'\\item\b',body));actual='abcdefghijklmnopqrstuvwxyz'[:count];exercise_data.append({'id':id,'source_letter_parts':parts.get(n,''),'tex_letter_parts':actual,'match':parts.get(n,'')==actual})
counts=collections.Counter(re.findall(r'\\begin\{(theorem|definition|lemma|example|proof|equation|figure|table|exercise)\}',tex))
anchors=list(map(int,re.findall(r'\\sourcepageanchor\{(\d+)\}',tex)))
notes=re.findall(r'\\footnote\{译注：',tex)
data={'source':json.loads((r/'work/source-baseline.json').read_text(encoding='utf-8')),'range':{'physical':[200,251],'printed':[169,220]},'source_pages_visually_checked':list(range(200,252)),'source_object_order':expected_objects,'tex_object_order':actual_objects,'object_order_match':expected_objects==actual_objects,'source_equation_order':expected_equations,'tex_equation_order':[x for x in labels if x.startswith('eq:5.')],'equations_match':expected_equations==[x for x in labels if x.startswith('eq:5.')],'exercises':exercise_data,'exercise_order_match':[d['id'] for d in exercise_data]==[f'5.{n}' for n in range(1,70)],'source_explicit_proofs':14,'counts':dict(counts),'source_footnotes':0,'translator_footnotes':len(notes),'anchors':anchors,'anchors_match':anchors==list(range(200,252)),'duplicate_labels':[k for k,v in collections.Counter(labels).items() if v>1],'figures':[f'assets/chapter5/fig-{n}.pdf' for n in ['5-4-1','5-6-1','5-6-2','5-6-3']],'scope_note':'编号与分问题目集合依据实际逐页核对登记；对账不能替代逐段内容校对.局部预览的章外引用待全书整合解析.'}
(r/'work/ch05-manifest.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
print({k:data[k] for k in ['object_order_match','equations_match','exercise_order_match','counts','translator_footnotes','anchors_match','duplicate_labels']});print('parts mismatches',[d for d in exercise_data if not d['match']])
d=fitz.open(r/'work/ch05-preview.pdf');out=r/'work/ch05-render';out.mkdir(exist_ok=True)
for i,p in enumerate(d):p.get_pixmap(matrix=fitz.Matrix(1.1,1.1)).save(out/f'p{i+1:03d}.png')
print('rendered',len(d))
