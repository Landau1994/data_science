from pathlib import Path
import json,re
B=Path(__file__).resolve().parents[1]
rows={}
table='''
73:63 exercise:1.12
74:38 def:1.2.4
74:63 exercise:1.12
75:63 exercise:1.12
86:50 thm:1.3.5
91:43 def:1.2.17
97:36 def:1.2.1
122:48 def:1.3.2
123:50 eq:1.3.3
124:66 exercise:1.38
218:44 tab:1.2.1
219:42 sec:1.2.3
237:55 def:1.5.1
240:58 ex:1.5.6
242:56 thm:1.5.3
247:63 exercise:1.9
249:35 def:1.1.5
250:66 exercise:1.39
319:57 ex:1.5.4
321:59 ex:1.6.2
329:57 ex:1.5.5
331:61 ex:1.6.4
418:33 def:1.1.2
442:43 def:1.2.16
448:60 eq:1.6.2
449:42 thm:1.2.14
460:57 eq:1.5.4
531:64 exercise:1.27
540:66 exercise:1.42
549:66 exercise:1.39
550:51 def:1.3.7
551:53 def:1.3.12
552:51 thm:1.3.9
560:40 eq:1.2.9
560:42 eq:1.2.10
560:68 sec:1.8.1
563:40 thm:1.2.11
563:68 sec:1.8.1
571:65 exercise:1.28
596:37 def:1.2.4
598:54 eq:1.4.1
686:51 ex:1.3.8
711:66 exercise:1.37
745:35 def:1.1.5
753:35 def:1.1.6
753:50 thm:1.3.5
828:60 def:1.6.3
838:61 thm:1.6.5
841:67 exercise:1.52
843:37 def:1.2.4
844:37 thm:1.2.6
845:54 eq:1.4.1
846:39 thm:1.2.8
850:59 def:1.6.1
856:61 thm:1.6.5
864:54 def:1.4.1
867:58 def:1.5.7
868:58 def:1.5.7
869:59 def:1.5.8
948:32 def:1.1.1
960:34 thm:1.1.4
961:34 thm:1.1.4
963:34 thm:1.1.4
964:34 thm:1.1.4
965:62 exercise:1.2
972:36 def:1.2.1
973:36 ex:1.2.2
975:63 exercise:1.11
977:36 ex:1.2.3
985:64 exercise:1.28
988:67 exercise:1.49
1071:49 ex:1.3.4
1071:66 exercise:1.37
'''
for line in table.splitlines():
 if line.strip():
  rid,label=line.split();rows[rid]={'id':rid,'label':label}
after=[
('74:38','01-02.tex','公理3，通常称为可数可加性公理（Axiom of Countable Additivity）'),
('75:39','01-02.tex',r'\noindent\emph{有限可加性公理（Axiom of Finite Additivity）：}'),
('247:36','01-02.tex','此外，由德摩根律可知'),
('397:33','01-01.tex',r'\emph{空集}（empty set，即不含任何元素的集合）'),
('540:68','01-08.tex','那么，容斥恒等式表明'),
('559:41','01-02.tex','布尔不等式和邦费罗尼不等式之间有相似之处.'),
('597:49','01-03.tex',r'概率函数$P(\cdot\mid B)$满足Kolmogorov公理'),
('598:55','01-04.tex',r'若$\mathscr X$不可数，则用类似\eqref{eq:1.4.1}的方式定义诱导概率函数$P_X$.'),
('831:61','01-06.tex','反向蕴含同样容易证明.'),
('852:61','01-06.tex','反向蕴含同样容易证明.'),
('865:62','01-06.tex','则称其为绝对连续（absolutely continuous）.'),
('962:33','01-01.tex',r'\item[补（complementation）：]'),
('966:33','01-01.tex',r'\item[交（intersection）：]'),
('967:34','01-01.tex','并和交的运算也可以推广到无穷集合族.'),
('968:35','01-01.tex','也可以对不可数的集合族定义并和交.'),
('969:33','01-01.tex',r'\item[并（union）：]'),
('970:34','01-01.tex','并和交的运算也可以推广到无穷集合族.'),
('971:35','01-01.tex','也可以对不可数的集合族定义并和交.'),
('974:59','01-05.tex','证明这一点需要大量使用'),
('976:36','01-02.tex','通常称为平凡$\sigma$代数.'),
('1070:34','01-01.tex','维恩图（Venn diagram）'),
]
for rid,f,target in after:rows[rid]={'id':rid,'file':'sections-tex/'+f,'after':target}
alltext='\n'.join(p.read_text(encoding='utf-8') for p in (B/'sections-tex').glob('01-*.tex'))
errors=[]
for r in rows.values():
 if 'label'in r:
  if alltext.count(r'\label{'+r['label']+'}')!=1:errors.append(r)
 else:
  count=(B/r['file']).read_text(encoding='utf-8').count(r['after'])
  if count!=1:errors.append((r,count))
expected={r['id'] for r in json.loads((B/'work/index-semantic-candidates.json').read_text(encoding='utf-8')) if 32<=r['source_physical']<=68}
print('missing',sorted(expected-set(rows)),'extra',sorted(set(rows)-expected),'badloc',errors)
if errors or expected!=set(rows):raise SystemExit(1)
(B/'work/index-locations-ch01.json').write_text(json.dumps(list(rows.values()),ensure_ascii=False,indent=2),encoding='utf-8')
print('chapter 1:',len(rows),'semantic locations')
