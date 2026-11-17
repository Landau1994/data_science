from pathlib import Path
import json,re
root=Path('.')
C={x['id']:x for x in json.loads((root/'work/index-semantic-candidates.json').read_text(encoding='utf-8')) if 101<=x['source_physical']<=199}
M={};issues=[]
def L(ids,label):
 for id in ids.split():
  assert id in C and id not in M,id
  M[id]={'id':id,'label':label}
def P(ids,fn,needle):
 s=(root/'sections-tex'/fn).read_text(encoding='utf-8-sig')
 lines=[l for l in s.splitlines() if needle in l]; assert len(lines)==1,(fn,needle,len(lines))
 after=lines[0]
 for id in ids.split():
  assert id in C and id not in M,id
  M[id]={'id':id,'file':'sections-tex/'+fn,'after':after}
# Chapter 3: actual definitions, identities, examples, exercises, and precise prose.
L('287:101','eq:3.2.1');L('323:102','eq:3.2.2');L('3:103','ex:3.2.1')
P('531:103','03-02.tex','为计算这个表达式，使用已经')
L('252:104','eq:3.2.3');P('261:104','03-02.tex',r'\paragraph{二项分布.}')
P('88:104','03-02.tex','二项分布是一种十分有用的离散分布')
L('686:105','ex:3.2.3');L('92:105','thm:3.2.2');L('371:106','eq:3.2.5')
L('267:108','eq:3.2.7');L('375:108','eq:3.2.6');L('60:108','eq:3.2.8');L('351:109','eq:3.2.10')
P('1067:110 352:110','03-02.tex','用均值对负二项分布重新参数化')
P('356:110 378:110','03-02.tex','负二项分布族以Poisson分布为其极限情形')
L('592:110','ex:3.2.6');P('318:111','03-02.tex',r'\paragraph{几何分布.}');L('320:111','eq:3.2.11')
L('306:112','eq:3.3.6');L('387:112','eq:3.3.1');L('450:112','eq:3.3.2');L('315:113 377:113','ex:3.3.1')
L('245:114 280:114','eq:3.3.10');L('289:114','eq:3.3.11');P('293:114','03-03.tex','指数分布可以用来对寿命建模')
P('317:114 358:114','03-03.tex',r'\paragraph{正态分布.}')
L('391:114','eq:3.3.12');P('469:114','03-03.tex','Weibull分布非常适合对风险函数')
P('368:115','03-03.tex','也称为标准正态分布（standard normal distribution）')
L('198:117 59:117','ex:3.3.2');L('254:118','eq:3.3.16');L('89:118','eq:3.3.17');L('276:119','eq:3.3.19');L('332:120','eq:3.3.21');L('288:121','eq:3.3.23');L('435:121','eq:3.4.1')
L('262:123','ex:3.4.1');L('439:123 538:123','thm:3.4.2');L('266:124','ex:3.4.3');L('360:124','ex:3.4.4');L('556:124','def:3.4.5');L('436:125','def:3.4.7')
P('440:125','03-04.tex','称为该族的自然参数空间（natural parameter space）')
L('373:126','ex:3.4.9');L('647:126','sec:3.5');P('651:126','03-05.tex','称为该族的标准pdf（standard pdf）')
L('648:127','def:3.5.2');L('1034:128','ex:3.5.3');L('650:128','def:3.5.4');L('648:129 651:129','def:3.5.5')
L('565:131','thm:3.6.1');L('576:132','ex:3.6.3');L('310:133','thm:3.6.4');L('375:133','eq:3.6.2');L('541:133 984:133','lem:3.6.5');L('532:134','thm:3.6.7');L('473:135','thm:3.6.8');L('543:135','eq:3.6.6');L('544:135','eq:3.6.5')
L('109:136','exercise:3.9');L('270:137 353:137','exercise:3.12');L('61:137 62:137','exercise:3.11');L('305:138','exercise:3.20');L('309:138','exercise:3.17');L('314:138 355:138','exercise:3.18');L('315:138 377:138','exercise:3.19');L('327:138','exercise:3.14');L('378:138','exercise:3.15');L('385:138','exercise:3.13')
L('291:139 330:139 392:139','exercise:3.26');L('300:139 322:139 335:139 380:139 391:139','exercise:3.24');L('370:139','exercise:3.23');L('469:139','exercise:3.25')
L('435:140','exercise:3.28');L('437:140','exercise:3.34');L('276:141','exercise:3.39');L('987:141','exercise:3.43');L('989:141','exercise:3.41');L('374:142 818:142','thm:3.8.1');L('530:142 539:142','exercise:3.49');L('574:142','exercise:3.45');L('576:142','exercise:3.47');L('565:143','thm:3.8.2');L('567:143','thm:3.8.4');L('572:143','lem:3.8.3');L('579:143','thm:3.8.5');L('438:144','sec:3.8.3')
# Chapter 4.
L('871:145','def:4.1.1');L('854:146','def:4.1.3');P('873:146','04-01.tex','这个随机向量称为离散的（discrete）')
P('423:147','04-01.tex','随机向量的函数的期望也与单变量情形相同')
L('855:148','thm:4.1.6');L('833:149 872:149','def:4.1.10')
P('423:149','04-01.tex','联合 pdf 与单变量 pdf 的用法相同')
L('834:150','eq:4.1.2');P('239:152','04-01.tex','联合累积分布函数（joint cumulative distribution function')
L('448:152','eq:4.1.3');L('851:152','def:4.2.1');L('830:154','def:4.2.3');P('425:154','04-02.tex','条件期望（conditional expected value）')
P('1064:155','04-02.tex','条件方差（conditional variance）');L('554:155','def:4.2.5');P('236:157','04-02.tex','笛卡尔积（cross-product）')
L('427:158 553:158','thm:4.2.10');L('555:158 692:158','thm:4.2.12');L('369:159','ex:4.2.13')
P('248:160 593:160 729:160 730:160','04-03.tex','变换的 Jacobian（雅可比行列式）')
L('379:160','thm:4.3.2');L('256:161','ex:4.3.3');L('829:161','eq:4.3.2');L('369:162','ex:4.3.4');L('363:163 279:164 365:164','ex:4.3.6');L('554:163','thm:4.3.5');L('340:164','ex:4.4.1');L('428:165','thm:4.4.3');L('336:166','def:4.4.4');L('341:166','ex:4.4.5')
P('339:167','04-04.tex','$Y$ 的这个 pmf 就是负二项 pmf')
P('346:167','04-04.tex','一个有用的推广是 Poisson--Gamma 混合')
L('342:167 357:167','eq:4.4.3');L('1064:168','thm:4.4.7');L('337:168','ex:4.4.6');L('223:169','def:4.5.1');L('337:169','ex:4.4.8');L('216:170 217:170','def:4.5.2');L('1068:171','thm:4.5.6');L('221:171 548:171','thm:4.5.5');L('217:172 564:172','thm:4.5.7');L('273:174','def:4.5.10')
L('429:176','eq:4.6.3');L('833:176','eq:4.6.2');L('853:176','eq:4.6.1');P('834:176 855:176','04-06.tex','中任意一部分坐标的边缘 pdf 或 pmf')
L('830:177 851:177','eq:4.6.6');L('348:179','def:4.6.2');L('713:179','thm:4.6.4');P('712:179','04-06.tex','多项系数（multinomial coefficient）')
P('269:179 350:179','04-06.tex','现在考虑多项模型的一些边缘与条件分布')
P('349:180','04-06.tex','所有两两协方差都为负')
L('554:180','def:4.6.5');L('316:181','ex:4.6.8');L('427:181 553:181','thm:4.6.6');L('695:181','thm:4.6.7');L('362:182','cor:4.6.10');L('836:182','eq:4.6.7');P('248:182','04-06.tex','记根据第 $i$ 个逆变换计算的 Jacobian')
P('737:183','04-06.tex','次序统计量之间的间距（spacings）')
L('564:184','thm:4.7.3');L('568:184','thm:4.7.2');L('570:185','eq:4.7.6');L('575:185','thm:4.7.5');L('578:185','eq:4.7.8');L('121:186 212:186','def:4.7.6');L('569:186','thm:4.7.7');L('457:187 468:187 573:187 64:187','ex:4.7.8');L('424:188','exercise:4.2');L('566:188','thm:4.7.9');L('238:189','exercise:4.9');L('271:190 376:190','exercise:4.15');L('426:190 884:190','exercise:4.13')
L('259:191 311:191','exercise:4.24');L('279:191 365:191','exercise:4.28');L('346:191 351:191','exercise:4.32');L('866:191','exercise:4.26');L('260:192 338:192','exercise:4.34');L('344:192 876:192','exercise:4.33');L('295:193 312:193 343:193','exercise:4.38');L('349:193','exercise:4.39');L('446:193','exercise:4.37');L('1068:194','exercise:4.44');L('273:194','exercise:4.45');L('359:195','exercise:4.47')
P('398:196','04-08.tex','称为熵（entropy）')
L('533:196','exercise:4.59');L('749:196','exercise:4.55');L('420:197 748:197','sec:4.9.1');L('578:197','exercise:4.64');L('558:198 577:198 821:198','sec:4.9.2');L('747:198 98:198','sec:4.9.3')

# Refine multi-topic exercise entries to their actual lettered statement.
for id in ['291:139','330:139','392:139','300:139','322:139','335:139','380:139','391:139','530:142','539:142','61:137','62:137']:
 del M[id]
P('291:139','03-07.tex',r'\item[(a)] 若$T\sim\operatorname{exponential}(\beta)$')
P('330:139','03-07.tex',r'\item[(c)] 若$T\sim\operatorname{logistic}(\mu,\beta)$')
P('392:139','03-07.tex',r'\item[(b)] 若$T\sim\operatorname{Weibull}(\gamma,\beta)$')
P('300:139 322:139','03-07.tex',r'\item[(e)] 若$X\sim\operatorname{exponential}(1)$')
P('335:139','03-07.tex',r'\item[(d)] 若$X\sim\operatorname{gamma}(3/2,\beta)$')
P('380:139','03-07.tex',r'\item[(b)] 若$X\sim\operatorname{exponential}(\beta)$')
P('391:139','03-07.tex',r'\item[(a)] 若$X\sim\operatorname{exponential}(\beta)$')
P('539:142','03-07.tex',r'\item[(a)] 若$X\sim\operatorname{gamma}(\alpha,\beta)$，则')
P('530:142','03-07.tex',r'\item[(b)] 若$X\sim\operatorname{beta}(\alpha,\beta)$，则')
P('61:137','03-07.tex',r'\item[(a)] 证明，当$N\to\infty$、$M\to\infty$且$M/N\to p$时')
L('62:137','itm:exercise:3.11:b')

missing=sorted(set(C)-set(M));assert not missing,missing
labels=set()
for f in list((root/'sections-tex').glob('03-*.tex'))+list((root/'sections-tex').glob('04-*.tex')):
 labels.update(re.findall(r'\\label\{([^}]+)\}',f.read_text(encoding='utf-8-sig')))
for m in M.values():
 if 'label'in m:assert m['label'] in labels,m
 else:assert (root/m['file']).read_text(encoding='utf-8-sig').count(m['after'])==1,m
out=[M[k] for k in C]
(root/'work/index-locations-ch03-04.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
print('mapped',len(out),'labels',sum('label'in x for x in out),'prose',sum('after'in x for x in out))
