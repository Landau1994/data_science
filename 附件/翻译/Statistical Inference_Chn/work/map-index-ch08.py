from pathlib import Path
import json
B=Path(__file__).resolve().parents[1];rows={}
table='''
2:340 ex:8.2.9
87:363 exercise:8.42
244:355 sec:8.3.5
382:361 exercise:8.35
474:333 def:8.1.1
475:333 def:8.1.2
477:333 def:8.1.2
482:333 def:8.1.3
483:359 exercise:8.16
487:367 sec:8.5.2
488:338 ex:8.2.7
489:365 exercise:8.53
490:365 exercise:8.47
492:355 sec:8.3.5
493:356 ex:8.3.31
494:340 eq:8.2.6
495:340 ex:8.2.9
495:352 ex:8.3.25
496:351 thm:8.3.23
497:340 ex:8.2.9
497:352 ex:8.3.25
498:343 def:8.3.6
500:366 exercise:8.58
501:341 def:8.3.1
502:341 ex:8.3.2
503:366 sec:8.5.1
504:342 ex:8.3.3
505:355 eq:8.3.12
510:343 ex:8.3.4
511:343 def:8.3.5
512:347 cor:8.3.13
513:341 tab:8.3.1
513:343 ex:8.3.4
514:341 tab:8.3.1
514:343 ex:8.3.4
515:345 def:8.3.11
516:347 ex:8.3.14
517:348 ex:8.3.15
517:349 ex:8.3.18
517:362 exercise:8.37
519:361 exercise:8.33
520:345 def:8.3.9
522:339 eq:8.2.4
524:351 thm:8.3.21
525:339 ex:8.2.8
525:344 ex:8.3.8
594:348 thm:8.3.17
630:334 def:8.2.1
633:359 exercise:8.17
634:335 ex:8.2.3
634:337 ex:8.2.5
634:344 ex:8.3.7
634:358 exercise:8.6
638:335 ex:8.2.2
638:337 ex:8.2.6
638:344 ex:8.3.7
638:362 exercise:8.37
639:337 ex:8.2.6
640:363 exercise:8.41
641:357 exercise:8.5
642:336 thm:8.2.4
652:361 exercise:8.34
655:355 eq:8.3.11
656:355 eq:8.3.11
663:355 eq:8.3.11
700:348 def:8.3.16
701:360 exercise:8.25
702:361 exercise:8.29
703:360 exercise:8.27
704:360 exercise:8.28
705:361 exercise:8.35
706:360 exercise:8.25
707:360 exercise:8.25
708:360 exercise:8.26
722:346 thm:8.3.12
723:360 exercise:8.24
637:360 exercise:8.24
742:353 def:8.3.26
743:354 eq:8.3.10
744:367 sec:8.5.3
947:343 ex:8.3.4
952:363 exercise:8.42
992:361 exercise:8.34
993:360 exercise:8.26
994:366 sec:8.5.1
1018:363 exercise:8.42
1019:338 ex:8.2.6
1020:362 exercise:8.40
1021:340 ex:8.2.8
1022:362 exercise:8.39
1024:363 exercise:8.41
1025:363 exercise:8.41
1027:362 exercise:8.37
1028:344 ex:8.3.8
'''
for l in table.splitlines():
 if l.strip():rid,label=l.split();rows[rid]={'id':rid,'label':label}
after=[
 ('243:344','08-03-1.tex','等点称为临界点（cutoff points）.'),
 ('2:333','08-01.tex','验收抽样（acceptance sampling）'),
 ('4:355','08-03-5.tex',r'行动空间是两点集合 $\mathscr A=\{a_0,a_1\}$.'),
 ('476:348','08-03-2.tex','复合假设（composite hypotheses）'),
 ('478:348','08-03-2.tex','单侧假设（one-sided hypotheses）'),
 ('479:344','08-03-1.tex','研究假设（research hypothesis）'),
 ('480:345','08-03-2.tex','即二者均为简单假设时'),
 ('480:348','08-03-2.tex','简单假设（simple hypotheses）'),
 ('481:348','08-03-2.tex','双侧假设（two-sided hypotheses）'),
 ('484:333','08-01.tex','接受域（acceptance region）'),
 ('506:333','08-01.tex','拒绝域（rejection region）'),
 ('635:335','08-02.tex',r'记为 $\hat\theta_0$.'),
 ('678:335','08-02.tex',r'记为 $\hat\theta_0$.'),
 ('727:337','08-02.tex','干扰参数（nuisance parameters）'),
 ('1032:346','08-03-2.tex','检验函数（test function）'),
 ('1033:334','08-01.tex','检验统计量（test statistic）')
]
for rid,f,t in after:rows[rid]={'id':rid,'file':'sections-tex/'+f,'after':t}
alltext='\n'.join(p.read_text(encoding='utf-8') for p in (B/'sections-tex').glob('08-*.tex'))
bad=[]
for r in rows.values():
 n=alltext.count(r'\label{'+r['label']+'}') if 'label'in r else (B/r['file']).read_text(encoding='utf-8').count(r['after'])
 if n!=1:bad.append((r,n))
expected={r['id'] for r in json.loads((B/'work/index-semantic-candidates.json').read_text(encoding='utf-8')) if 333<=r['source_physical']<=367}
print('Missing',expected-set(rows),'Extra',set(rows)-expected,'Bad',bad)
assert not bad and expected==set(rows)
(B/'work/index-locations-ch08.json').write_text(json.dumps(list(rows.values()),ensure_ascii=False,indent=2),encoding='utf-8')
print('chapter 8:',len(rows),'semantic locations')
