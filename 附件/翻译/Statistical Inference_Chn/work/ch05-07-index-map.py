from pathlib import Path
import json,re
r=Path(r'E:/project/math/data_science/附件/翻译/Statistical Inference_Chn')
entries=json.loads((r/'work/ch05-07-index-sorted.json').read_text(encoding='utf-8'))
maps={}
def labels(label,ids):
 for ident in ids.split():
  assert ident not in maps,ident
  maps[ident]={'id':ident,'label':label}
def phrase(file,after,ids):
 t=(r/'sections-tex'/file).read_text(encoding='utf-8')
 assert t.count(after)==1,(file,after,t.count(after))
 for ident in ids.split():
  assert ident not in maps,ident
  maps[ident]={'id':ident,'file':'sections-tex/'+file,'after':after}

# Each assignment below follows the indexed concept and its source-page discussion.
groups=r'''
def:5.1.1|545:200 554:200 917:200
eq:5.1.1|839:200 857:200 932:200
def:5.2.2|921:203
def:5.2.1|951:203 981:203
lem:5.2.5|1068:204 433:204
def:5.2.3|935:204 936:204
thm:5.2.6|923:205 938:205
thm:5.2.9|213:206
thm:5.2.7|694:206 925:206
ex:5.2.8|926:206
ex:5.2.10|922:207
thm:5.2.11|441:208 918:208
thm:5.3.1|926:209 940:209
lem:5.3.2|282:210
lem:5.3.3|362:211
def:5.3.4|381:213
def:5.3.6|301:214
thm:5.3.8|258:215 302:215 303:215 304:215 383:215
def:5.4.1|731:215
thm:5.4.3|732:216 736:216
thm:5.4.4|735:217
ex:5.4.5|389:218
thm:5.4.6|734:218
ex:5.4.7|931:219 945:219
def:5.5.1|206:220
thm:5.5.2|210:220 605:220 565:220
ex:5.5.3|196:221
def:5.5.6|201:221 211:221
def:5.5.10|204:222
thm:5.5.9|209:222 604:222
thm:5.5.12|205:223 207:223
thm:5.5.13|208:223
ex:5.5.11|388:223
thm:5.5.14|102:223
thm:5.5.15|102:225 105:225
ex:5.5.16|63:225
thm:5.5.17|979:226 204:226
sec:5.5.4|246:226
def:5.5.20|1029:227
thm:5.5.21|1030:227
eq:5.5.9|1069:228 764:228
ex:5.5.27|812:230
ex:5.6.3|290:232 1041:232 847:232
eq:5.6.5|255:233 281:233 307:233 361:233
ex:5.6.4|1038:233 99:233
ex:5.6.5|263:234 286:234
ex:5.6.6|752:234 96:234
ex:5.6.7|1:235 6:235 255:235
thm:5.6.8|1:237 6:237
ex:5.6.9|255:238
exercise:5.4|421:239
exercise:5.5|927:239
exercise:5.8|939:240
exercise:5.9|542:240
exercise:5.15|928:241 941:241
exercise:5.18|367:241 384:241
exercise:5.19|990:241 991:241
exercise:5.20|345:242 347:242
exercise:5.26|733:243
exercise:5.35|985:244
exercise:5.38|574:244
exercise:5.44|253:245
exercise:5.50|861:245
exercise:5.52|861:246
exercise:5.57|215:246
exercise:5.64|14:247
exercise:5.61|255:247 307:247
sec:5.8.1|102:248 600:248 643:248
sec:5.8.2|937:249
sec:5.8.3|565:249
sec:5.8.4|995:250 202:250
sec:5.8.5|17:250 666:250
def:6.2.1|1000:253
ex:6.2.3|1002:254
ex:6.2.4|1011:255
thm:6.2.6|1005:256 443:256
ex:6.2.7|1011:256
ex:6.2.8|1003:257
ex:6.2.9|1011:258
thm:6.2.10|1004:258
def:6.2.11|1006:259
thm:6.2.13|1007:259
ex:6.2.12|1011:259
ex:6.2.14|1009:260
ex:6.2.15|1010:260
def:6.2.16|18:261
ex:6.2.17|24:261
ex:6.2.18|20:262
ex:6.2.19|23:262
ex:6.2.20|25:263
def:6.2.21|110:263
ex:6.2.22|114:263
ex:6.2.23|120:264
thm:6.2.24|112:264 117:264 547:264 76:264
thm:6.2.25|116:265
ex:6.2.26|115:266 19:266
def:6.3.1|619:267
ex:6.3.2|622:267
thm:6.3.6|626:270 93:270
ex:6.3.7|126:271 625:271 628:271 999:271
sec:6.4|403:272
ex:6.4.1|400:273
def:6.4.2|466:273
def:6.4.4|588:274
ex:6.4.6|464:274 591:274 405:274
exercise:6.8|738:275
exercise:6.10|1010:275
exercise:6.18|118:276
exercise:6.11|20:276
exercise:6.12|22:276
exercise:6.26|1006:277
exercise:6.27|324:277
exercise:6.30|115:278
exercise:6.31|710:278
exercise:6.33|626:278 93:278
exercise:6.34|629:279
exercise:6.37|725:279
exercise:6.39|401:279
exercise:6.40|21:280
exercise:6.41|1054:280 402:280 590:280 784:280
exercise:6.42|465:280 785:280
exercise:6.43|467:280
sec:6.6.1|77:281
thm:6.6.2|111:281
sec:6.6.2|18:281
sec:6.6.3|623:281
def:6.6.3|719:281
thm:6.6.4|1008:282
def:7.1.1|763:283
sec:7.2.1|806:284
ex:7.2.1|809:284
ex:7.2.2|807:285
ex:7.2.3|808:285 952:285
def:7.2.4|667:286
ex:7.2.5|679:287
ex:7.2.7|669:288
ex:7.2.9|671:289
eq:7.2.5|620:290
thm:7.2.10|677:290
ex:7.2.11|679:291
ex:7.2.12|673:291
ex:7.2.13|671:292 676:292
ex:7.2.14|79:293
def:7.2.15|195:294
ex:7.2.16|80:294
sec:7.2.4|395:295 7:295 13:295
eq:7.2.13|12:295
eq:7.2.11|9:295
thm:7.2.20|10:297
def:7.3.2|1044:298 90:298
ex:7.3.3|1055:298
def:7.3.1|683:298
eq:7.3.1|801:298
ex:7.3.5|79:300 800:300
ex:7.3.6|464:301 789:301
def:7.3.7|1045:302
ex:7.3.8|1057:302
thm:7.3.9|228:302
ex:7.3.12|1049:305
ex:7.3.13|1059:306
ex:7.3.14|1060:306
cor:7.3.15|229:307
thm:7.3.17|1050:308 817:308 877:308
thm:7.3.19|1052:309
thm:7.3.20|1047:310
ex:7.3.21|1059:310 1061:310
thm:7.3.23|1048:311 113:311
ex:7.3.22|1051:311
ex:7.3.24|1046:312
sec:7.3.4|244:313
eq:7.3.16|914:313
ex:7.3.26|778:314
ex:7.3.27|658:315 662:315
ex:7.3.28|654:316 659:316 661:316 683:316 776:316
eq:7.3.19|660:316 820:316
ex:7.3.30|777:317
exercise:7.3|621:318
exercise:7.16|1037:320 452:320 786:320 811:320 821:320
exercise:7.15|324:320
exercise:7.18|672:321
exercise:7.19|911:321
exercise:7.22|80:321
exercise:7.23|81:321 826:321
exercise:7.24|827:321
exercise:7.25|782:322
exercise:7.35|755:324 790:324
exercise:7.41|1053:325 792:325
exercise:7.45|599:325
exercise:7.50|1056:326
exercise:7.54|859:327
exercise:7.66|791:328
sec:7.5.1|680:329 810:329
sec:7.5.2|1058:329 82:329
thm:7.5.1|617:330
sec:7.5.4|395:330 7:330
thm:7.5.2|10:331
'''
for line in groups.strip().splitlines():
 label,ids=line.split('|');labels(label,ids)

phrase('05-01.tex',r'中的随机抽样模型有时称为从无限总体中抽样.','920:201')
phrase('05-01.tex',r'从有限总体中抽样时，','919:201')
phrase('05-01.tex',r'这种抽样称为有放回抽样（sampling with replacement），','942:202')
phrase('05-01.tex',r'从有限总体抽取随机样本的第二种方法称为无放回抽样（sampling without replacement）.','943:202')
phrase('05-01.tex',r'从有限总体无放回抽样有时称为简单随机抽样（simple random sampling）.','934:202')
phrase('05-08.tex',r'遍历定理（Ergodic Theorem）是大数定律的推广，','203:250 406:250')
phrase('06-01.tex',r'以某个特定统计量进行的数据约简，可以看作样本空间$\mathcal X$的一个划分.','753:252')
phrase('06-01.tex',r'充分性原则（Sufficiency Principle）提出一种在概括数据的同时不丢弃关于$\theta$的信息的方法.','997:252')
phrase('06-04.tex',r'第一类可称为测量等变性（measurement equivariance）.','401:272')
phrase('06-04.tex',r'第二类等变性实际上是不变性，可称为形式不变性（formal invariance）.','589:272')
phrase('06-04.tex',r'\textbf{等变性原则：}','404:272')
phrase('07-05.tex',r'\item \textbf{经验贝叶斯分析（empirical Bayes analysis）.}','396:331 766:331')
phrase('07-05.tex',r'\item \textbf{稳健贝叶斯分析（robust Bayes analysis）.}','768:331')
phrase('07-05.tex',r'\item \textbf{层次贝叶斯分析（hierarchical Bayes analysis）.}','470:332 767:332')

phrase('05-02.tex',r'是统计量与总体参数之间的关系，也是无偏统计量（unbiased statistics）的例子.','1044:206')
phrase('05-02.tex',r'开集条件排除了$n(\theta,\theta^2)$这样的密度；','299:208')
phrase('05-02.tex',r'先讨论\autoref{sec:3.5}中的位置–尺度情形.','924:208')
phrase('05-03.tex',r'W. S. Gosset（以Student为笔名发表论文）在20世纪初首次研究这个问题.','461:212')
labels('eq:5.4.1','930:215')
phrase('05-04.tex',r'样本极差（sample range）','933:215')
phrase('05-04.tex',r'对0与1之间任意数$p$，第$100p$样本百分位数（sample percentile）','754:216')
phrase('05-04.tex',r'除了中位数，还常用两个样本百分位数：','860:216')
phrase('05-05.tex',r'把$M_Y(t/\sqrt n)$在0附近展开为Taylor级数','1031:224 696:224')
labels('sec:5.6','863:231')
phrase('05-06.tex',r'\noindent\textbf{Metropolis算法.}','15:238 688:238')
phrase('06-02.tex',r'用本章开头所述的划分集合来说，','753:259')
labels('thm:6.2.24','111:264 119:264')
phrase('06-02.tex',r'要求参数空间包含开集，是为避免如下情形.','436:265')
phrase('06-02.tex',r'这里不证明该定理，但指出其证明依赖Laplace变换的唯一性，','601:265')
phrase('06-03.tex',r'一种称为信仰推断（fiducial inference）的推断形式，','444:268')
phrase('06-03.tex',r'\textbf{似然原则：}','624:268')
phrase('06-03.tex',r'\textbf{条件性原则（Conditionality Principle）：}','125:269')
phrase('06-03.tex',r'以$\operatorname{Ev}(E,\boldsymbol x)$表示这个结论，','419:269')
phrase('06-03.tex',r'\textbf{形式化的充分性原则：}','998:269')
labels('sec:6.3.2','627:269')
phrase('06-03.tex',r'\textbf{形式化的似然原则：}','627:270')
phrase('07-01.tex',r'有一点必须区分清楚，即估计值（estimate）与估计量（estimator）的差别.','762:283')
phrase('07-02.tex',r'（称为对数似然，log likelihood），','621:288')
phrase('07-02.tex',r'这个分布称为先验分布（prior distribution）.','824:293')
phrase('07-02.tex',r'更新后的先验称为后验分布（posterior distribution）.','819:293')
phrase('07-02.tex',r'称为完全数据.数据缺失很常见，','8:295')
phrase('07-02.tex',r'基于\eqref{eq:7.2.13}的似然是不完全数据似然（incomplete-data likelihood）.','11:295')
phrase('07-03.tex',r'形式不变性：','788:301')
phrase('07-03.tex',r'称为样本的信息数（information number），或Fisher信息（Fisher information）.','582:305')
phrase('07-03.tex',r'点估计问题中的损失函数反映了这样的事实：','653:313')
phrase('07-03.tex',r'允许决策的集合称为行动空间（action space），记为$\mathcal A$.','751:313')
phrase('07-03.tex',r'它称为Bayes风险（Bayes risk）.','83:316')
phrase('07-03.tex',r'称为关于先验$\pi$的Bayes规则（Bayes rule with respect to a prior $\pi$），','85:316')

# Save only mappings already reviewed; report every remaining locator explicitly.
validids={d['id'] for d in entries}
assert not (set(maps)-validids),set(maps)-validids
alltex='\n'.join(p.read_text(encoding='utf-8') for f in ['sections-tex','chapters-tex'] for p in (r/f).glob('*.tex'))
alllabels=set(re.findall(r'\\label\{([^}]+)\}',alltex))
assert all(m.get('label') in alllabels for m in maps.values() if 'label' in m),[m for m in maps.values() if 'label' in m and m['label'] not in alllabels]
(r/'work/index-locations-ch05-08.json').write_text(json.dumps(list(maps.values()),ensure_ascii=False,indent=2),encoding='utf-8')
missing=[d for d in entries if d['id'] not in maps]
print('mapped',len(maps),'remaining',len(missing))
for d in missing:print(d['id'],' > '.join(d['path']))
