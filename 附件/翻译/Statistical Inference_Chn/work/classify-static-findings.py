from pathlib import Path
import re,json,importlib.util,collections
B=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('checker',Path('C:/Users/Administrator/.codex/skills/pdf-to-chinese-tex/scripts/check_tex_static.py'))
c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c)
s=c.strip_comments((B/'work/book-static-input/Combined_Chn.tex').read_text(encoding='utf-8'))
math=[]
mode=None;start=None
for m in re.finditer(r'(?<!\\)\${1,2}',s):
 if mode is None:mode=m.group();start=m.start()
 elif mode==m.group():math.append((start,m.end()));mode=None
for pat in [r'\\\[.*?\\\]',r'\\\(.*?\\\)']:
 math.extend((m.start(),m.end())for m in re.finditer(pat,s,re.S))
for env in ['equation','equation*','align','align*','gather','gather*','multline','multline*']:
 math.extend((m.start(),m.end())for m in re.finditer(r'\\begin\{'+re.escape(env)+r'\}.*?\\end\{'+re.escape(env)+r'\}',s,re.S))
commands=[]
for m in re.finditer(r'\\(?:footnote(?:text)?|hyperref|bibitem)(?:\[[^]]*\])?\{',s):
 d=1;i=m.end()
 while i<len(s)and d:
  if s[i]=='{'and s[i-1]!='\\':d+=1
  elif s[i]=='}'and s[i-1]!='\\':d-=1
  i+=1
 commands.append((m.start(),i,m.group().split('{')[0]))
items=[]
for m in c.RAW_EQUATION_REF.finditer(s):
 before=s[max(0,m.start()-20):m.start()]
 if '\\tag'in before or '\\label'in before or 'item'in before:continue
 cat=None
 if re.fullmatch(r'\((?:18|19|20)\d{2}\)',m.group()):cat='publication-year'
 elif any(a<=m.start()<b for a,b in math):cat='mathematical-expression'
 else:
  containers=[cmd for a,b,cmd in commands if a<=m.start()<b]
  if containers:cat='already-linked-or-translator-note: '+','.join(containers)
  elif s.rfind('\\begin{thebibliography}',0,m.start())>s.rfind('\\end{thebibliography}',0,m.start()):cat='bibliography-text'
  else:cat='manual-review'
 line,col=c.line_col(s,m.start())
 items.append({'kind':'raw-number','line':line,'col':col,'value':m.group(),'category':cat,'context':c.context(s,m.start(),m.end(),120)})
for pat in c.BARE_REF_PATTERNS:
 for m in re.finditer(pat,s):
  line,col=c.line_col(s,m.start());items.append({'kind':'bare-reference','line':line,'col':col,'value':m.group(),'category':'manual-review','context':c.context(s,m.start(),m.end(),150)})
for i in items:
 if i['category']!='manual-review':continue
 if i['kind']=='raw-number'and i['value']in ['(1)','(2)']and '说明：(1) 似然可等价地因子分解'in i['context']:
  i['category']='inline-enumeration';i['review']='已读上下文；这是本句两项陈述的编号，不是回引。'
 elif i['kind']=='bare-reference':
  if i['value']in ['Exercise 2.4.7','Section 11.3','Exercise 10.2.1','Chapter 7']:
   i['category']='quoted-source-error';i['review']='已读上下文；译注引述原书错误名称或编号；正文另有真实目标链接。'
  elif i['value']in ['Section 5.21','Section 2.7','Section 34']:
   i['category']='external-book-section';i['review']='已读上下文；外部专著小节，作者年份已链接本书参考文献，不应伪造本书节目标。'
  elif i['value']=='Section 57'and 'Business and Economic Statistics Section 57'in i['context']:
   i['category']='bibliography-title-and-pages';i['review']='已读上下文；书目题名末词Section后接页码57–66，不是节57。'
(B/'work/final-checks/static-findings-classified.json').write_text(json.dumps(items,ensure_ascii=False,indent=2),encoding='utf-8')
print(collections.Counter(i['category']for i in items))
for i in items:
 if i['category']=='manual-review':print(json.dumps(i,ensure_ascii=False))
actual=c.check_file(B/'work/book-static-input/Combined_Chn.tex')
hard=[x for x in actual if 'possible bare reference'not in x and 'possible raw equation/number reference'not in x]
summary={'findings':len(actual),'classified':len(items),'categories':dict(collections.Counter(i['category']for i in items)),'hard_findings':hard,'unreviewed':[i for i in items if i['category']=='manual-review'],'method':'脚本保守扫描保留原始退出码1；数学/年份/命令作用域分类，剩余11项人工逐项读上下文。'}
(B/'work/final-checks/static-findings-summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
assert len(actual)==len(items)and not hard and not summary['unreviewed'],summary
