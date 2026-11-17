from pathlib import Path
import re,json,collections,sys,hashlib
root=Path('.')
files=sorted((root/'sections-tex').glob('04-*.tex'))
T='\n'.join(p.read_text(encoding='utf-8-sig') for p in files)
L=re.findall(r'\\label\{([^}]+)\}',T)
O=[x for x in L if re.match(r'(ex|thm|lem|def|cor):4\.',x)]
# Source heading positions were checked on all original page images.
page_groups={145:'4.1.1 4.1.2',146:'4.1.3',147:'4.1.4 4.1.5',148:'4.1.6 4.1.7',149:'4.1.8 4.1.9 4.1.10',150:'4.1.11',151:'4.1.12',152:'4.2.1',153:'4.2.2',154:'4.2.3 4.2.4',155:'4.2.5',156:'4.2.6 4.2.7',157:'4.2.8 4.2.9',158:'4.2.10 4.2.11 4.2.12',159:'4.2.13 4.2.14',160:'4.3.1 4.3.2',161:'4.3.3',162:'4.3.4',163:'4.3.5 4.3.6',164:'4.4.1',165:'4.4.2 4.4.3',166:'4.4.4 4.4.5',168:'4.4.6 4.4.7',169:'4.4.8 4.5.1',170:'4.5.2 4.5.3 4.5.4',171:'4.5.5 4.5.6',172:'4.5.7 4.5.8',174:'4.5.9 4.5.10',177:'4.6.1',179:'4.6.2 4.6.3 4.6.4',180:'4.6.5',181:'4.6.6 4.6.7 4.6.8 4.6.9',182:'4.6.10 4.6.11 4.6.12',183:'4.6.13 4.7.1',184:'4.7.2 4.7.3 4.7.4',185:'4.7.5',186:'4.7.6 4.7.7',187:'4.7.8',188:'4.7.9'}
SO=[{'id':next(o for o in O if o.split(':')[1]==n),'source_physical_page':p} for p,nums in page_groups.items() for n in nums.split()]
assert [a['id'] for a in SO]==O
exercises=[]
for m in re.finditer(r'\\begin\{exercise\}(.*?)\\end\{exercise\}',T,re.S):
 s=m.group(1);lab=re.search(r'\\label\{([^}]+)\}',s).group(1)
 parts=re.findall(r'\\item\[\(([a-z]+)\)\]',s)
 exercises.append({'id':lab,'lettered_parts':[x for x in parts if len(x)==1 and x not in ['i']],'roman_items':[x for x in parts if x in ['i','ii','iii']]})
assert [x['id'] for x in exercises]==[f'exercise:4.{i}' for i in range(1,66)]
proofs=[]
for m in re.finditer(r'\\begin\{proof\}',T):proofs.append(re.findall(r'\\label\{((?:ex|thm|lem|def|cor):[^}]+)\}',T[:m.start()])[-1])
notes=[]
for p in files:
 s=p.read_text(encoding='utf-8-sig')
 for m in re.finditer(r'\\footnote\{',s):
  d=1;i=m.end()
  while d:
   d+=(s[i]=='{')-(s[i]=='}');i+=1
  before=s[:m.start()];notes.append({'file':str(p).replace('\\','/'),'source_physical_page':int(re.findall(r'\\sourcepageanchor\{(\d+)\}',before)[-1]) if re.findall(r'\\sourcepageanchor\{(\d+)\}',before) else 197,'text':s[m.end():i-1]})
anchors=[int(a) for a in re.findall(r'\\sourcepageanchor\{(\d+)\}',T)]
aux=Path('work/ch04-preview.aux').read_text(encoding='utf-8')
actual=dict(re.findall(r'\\newlabel\{([^}]+)\}\{\{([^}]+)\}',aux))
checked=[x for x in L if re.match(r'(ex|thm|lem|def|cor|eq|fig|tab|exercise):',x)]
numbering_bad=[(x,actual.get(x)) for x in checked if actual.get(x)!=x.split(':')[1]]
refs={a or b for a,b in re.findall(r'\\(?:auto|eq|page)?ref\{([^}]+)\}|\\hyperref\[([^]]+)\]',T)}
internal_bad=sorted(x for x in refs if re.match(r'\w+:4(?:\.|$)',x) and x not in L)
external=sorted(x for x in refs if x not in L)
sys.path.insert(0,str(root/'work/python-deps'));import pymupdf as fitz
D=fitz.open('work/ch04-preview.pdf');changes=[];badpunct=[]
for i,p in enumerate(D):
 path=Path(f'work/ch04-render/p{i+1:03}.png');old=hashlib.sha256(path.read_bytes()).hexdigest();p.get_pixmap(matrix=fitz.Matrix(1.25,1.25)).save(path)
 if old!=hashlib.sha256(path.read_bytes()).hexdigest():changes.append(i+1)
 for b in p.get_text('dict')['blocks']:
  for l in b.get('lines',[]):
   s=''.join(z['text'] for z in l['spans']).strip()
   if l['bbox'][0]<90 and re.match(r'^[.,;:!]',s):badpunct.append([i+1,s])
data={'chapter':4,'source_sha256':'52e6acfaceca3c7492d6436de2fe25c2b468a3fe74b47c7ecd0a5f130ace0707','source_physical_pages':list(range(145,200)),'printed_pages':[114,168],'source_pages_visually_inspected':list(range(145,200)),'translated_anchors':anchors,'anchor_order_matches':anchors==list(range(145,200)),'numbered_objects':O,'source_numbered_objects':SO,'source_object_order_matches':True,'object_counts':dict(collections.Counter(x.split(':')[0] for x in O)),'equation_labels':[x for x in L if x.startswith('eq:')],'figure_labels':[x for x in L if x.startswith('fig:')],'table_labels':[x for x in L if x.startswith('tab:')],'exercise_objects':exercises,'exercise_count':len(exercises),'lettered_part_count':sum(len(x['lettered_parts']) for x in exercises),'roman_item_count':sum(len(x['roman_items']) for x in exercises),'exercise_source_visual_check':'物理188–197全部原页；包括跨页4.40、4.46及4.56/4.57罗马数字列表；无星号题。','proof_count':len(proofs),'proof_objects':proofs,'additional_unboxed_derivations':'例内推导及二元正态相关系数推导均完整保留，不另计proof环境。','original_footnotes':0,'translator_note_count':len(notes),'translator_notes':notes,'duplicate_labels':[x for x,c in collections.Counter(L).items() if c>1],'actual_numbering_mismatches':numbering_bad,'unresolved_internal_references':internal_bad,'local_preview_external_references':external,'preview_pages':len(D),'preview_pages_visually_inspected':list(range(1,len(D)+1)),'final_punctuation_candidates':badpunct,'source_figure_crops':[{'file':'assets/chapter4/fig4-1-1.pdf','source_physical':151,'clip':[155,57,348,239]},{'file':'assets/chapter4/fig4-5-1.pdf','source_physical':173,'clip':[54,57,447,225]},{'file':'assets/chapter4/fig4-5-2.pdf','source_physical':174,'clip':[132,56,367,225]},{'file':'assets/chapter4/fig4-7-1.pdf','source_physical':186,'clip':[99,54,411,263]},{'file':'assets/chapter4/fig4-7-2.pdf','source_physical':187,'clip':[103,54,400,224]}],'unresolved':'文献作者年份待总编映射；最终全书互审、跨章编号及合并版面由总编完成。'}
Path('work/ch04-object-inventory.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
print('counts',data['object_counts'],'exercises',len(exercises),'lettered',data['lettered_part_count'],'roman',data['roman_item_count'],'notes',len(notes));print('numbering_bad',numbering_bad,'internal_bad',internal_bad,'render_changes',changes,'punctuation',badpunct);print('proofs',proofs)
for i,n in enumerate(notes,1):print(i,n['source_physical_page'],n['text'][:110])
