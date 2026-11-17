from pathlib import Path
import json
B=Path(__file__).resolve().parents[1];rows={}
table='''
60:85 ex:2.3.13
104:100 thm:2.6.1
241:72 thm:2.1.3
257:98 exercise:2.40
261:70 ex:2.1.1
264:76 ex:2.2.3
265:83 ex:2.3.9
268:98 exercise:2.40
272:81 ex:2.3.5
277:94 exercise:2.12
278:77 ex:2.2.4
283:98 exercise:2.38
284:74 ex:2.1.9
292:76 ex:2.2.2
294:90 eq:2.4.7
296:72 ex:2.1.4
297:80 ex:2.3.3
308:82 ex:2.3.8
313:73 ex:2.1.6
326:73 ex:2.1.6
333:98 exercise:2.36
334:84 ex:2.3.10
354:98 exercise:2.38
366:74 ex:2.1.9
372:86 lem:2.3.14
390:72 ex:2.1.4
422:76 def:2.2.1
430:78 ex:2.2.6
431:95 exercise:2.15
432:77 thm:2.2.5
434:79 eq:2.2.5
459:91 ex:2.4.7
536:95 exercise:2.14
537:95 exercise:2.14
585:92 thm:2.4.8
586:93 thm:2.4.10
599:96 exercise:2.28
601:85 eq:2.3.8
618:87 thm:2.4.1
684:95 exercise:2.17
685:95 exercise:2.18
689:82 def:2.3.6
689:100 sec:2.6.3
690:85 thm:2.3.12
691:85 thm:2.3.11
693:86 thm:2.3.15
697:79 def:2.3.1
698:84 ex:2.3.10
698:98 exercise:2.35
699:99 sec:2.6.1
720:82 def:2.3.6
750:70 ex:2.1.1
832:96 exercise:2.25
835:72 thm:2.1.5
837:74 thm:2.1.8
840:96 exercise:2.26
842:96 exercise:2.27
847:74 thm:2.1.10
849:94 exercise:2.10
870:85 thm:2.3.11
978:96 exercise:2.28
980:79 def:2.3.2
988:94 exercise:2.10
1062:79 def:2.3.2
1066:80 thm:2.3.4
'''
for line in table.splitlines():
 if line.strip():
  rid,label=line.split();rows[rid]={'id':rid,'label':label}
after=[
('101:99','02-06.tex','Carleman 条件'),
('103:100','02-06.tex',r'\paragraph{特征函数.}'),
('364:90','02-04.tex','其他分布也有这种关系.'),
('454:99','02-06.tex',r'\paragraph{累积量母函数.}'),
('455:99','02-06.tex',r'\paragraph{阶乘矩母函数.}'),
('456:99','02-06.tex','阶乘矩母函数又称为概率母函数（probability generating function）'),
('595:83','02-03.tex','核（kernel）'),
('598:70','02-01.tex','容易验证它满足 Kolmogorov 公理.'),
('616:88','02-04.tex','Lebesgue 控制收敛定理（Dominated Convergence Theorem）'),
('664:69','02-01.tex','的映射，即'),
('665:69','02-01.tex','一个逆映射（inverse mapping）'),
('729:71','02-01.tex','所以它是一一的；'),
('730:71','02-01.tex','它也是满的.'),
('861:76','02-01.tex','的一个应用是从给定分布产生随机样本.'),
('1015:71','02-01.tex','支撑集（support set）'),
('1040:71','02-01.tex','单调函数（monotone function）'),
]
for rid,f,target in after:rows[rid]={'id':rid,'file':'sections-tex/'+f,'after':target}
alltext='\n'.join(p.read_text(encoding='utf-8') for p in (B/'sections-tex').glob('02-*.tex'))
errors=[]
for r in rows.values():
 if 'label'in r:
  if alltext.count(r'\label{'+r['label']+'}')!=1:errors.append(r)
 else:
  count=(B/r['file']).read_text(encoding='utf-8').count(r['after'])
  if count!=1:errors.append((r,count))
expected={r['id'] for r in json.loads((B/'work/index-semantic-candidates.json').read_text(encoding='utf-8')) if 69<=r['source_physical']<=100}
print('missing',sorted(expected-set(rows)),'extra',sorted(set(rows)-expected),'badloc',errors)
if errors or expected!=set(rows):raise SystemExit(1)
(B/'work/index-locations-ch02.json').write_text(json.dumps(list(rows.values()),ensure_ascii=False,indent=2),encoding='utf-8')
print('chapter 2:',len(rows),'semantic locations')
