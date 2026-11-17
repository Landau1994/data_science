# 第3–4章索引语义落点核验

核对范围：原PDF物理101–199（印刷70–168）中的234条原书索引定位，全部已按术语实际定义、公式、证明、例、习题或相关说明匹配。正文原页已在两章翻译中逐页查看；此次另复看物理121、122、126、129、139，核实跨页或多主题定位。

输出 `work/index-locations-ch03-04.json` 为根任务约定的数组，186条用现有真实对象label，48条用当前TeX文件中的唯一文本片段。没有插入正文标记，没有修改第3–4章正文。全部234个ID完整唯一，无额外ID；对象label实际存在，文本片段在所指定文件中恰好出现一次。

习题3.24的Weibull、Rayleigh、Maxwell、Gumbel/极值，习题3.26的各风险函数，以及习题3.49的Gamma/Beta恒等式均细化到实际字母分问，而非统一指向习题首部。

本范围未确认原书索引页码错误。两个需要区分的边界：

- `279:164`、`365:164`所指正态比值与Cauchy关系属于例4.3.6的续文；映到该例实际对象label，其例题开始在物理163。
- `435:121`指数族定义和式3.4.1实际在原物理121下部，已据原图确认。译稿中图3.3.6的物理122标记在此节之前，不能仅按最近sourcepageanchor机械定位；本映射直接使用式3.4.1的label。

下表给出每条实际落点（原页为PDF物理页）。

| ID | 词条 | 原页 | 目标 |
|---|---|---:|---|
| 287:101 | Distribution / discrete uniform | 101 | `eq:3.2.1` |
| 323:102 | Distribution / hypergeometric | 102 | `eq:3.2.2` |
| 3:103 | Acceptance sampling / hypergeometric | 103 | `ex:3.2.1` |
| 531:103 | Identity / binomial coefficients | 103 | `sections-tex/03-02.tex：为计算这个表达式，使用已经在\autoref{sec:2.3}中遇到的恒等式` |
| 252:104 | Distribution / Bernoulli | 104 | `eq:3.2.3` |
| 261:104 | Distribution / binomial | 104 | `sections-tex/03-02.tex：\paragraph{二项分布.}` |
| 88:104 | Bernoulli trials | 104 | `sections-tex/03-02.tex：二项分布是一种十分有用的离散分布，其基础是 Bernoulli 试验（Bernoulli trial）的思想. Bernoulli 试验以概率论奠基人之一 James Bernoulli 命名，是恰有` |
| 686:105 | Meré dice problem | 105 | `ex:3.2.3` |
| 92:105 | Binomial Theorem | 105 | `thm:3.2.2` |
| 371:106 | Distribution / Poisson | 106 | `eq:3.2.5` |
| 267:108 | Distribution / binomial / recursion relation | 108 | `eq:3.2.7` |
| 375:108 | Distribution / Poisson / recursion relation | 108 | `eq:3.2.6` |
| 60:108 | Approximation / binomial by Poisson | 108 | `eq:3.2.8` |
| 351:109 | Distribution / negative binomial | 109 | `eq:3.2.10` |
| 1067:110 | Variance / quadratic function of mean | 110 | `sections-tex/03-02.tex：用均值对负二项分布重新参数化，是一种有趣且有时很有用的做法. 若定义参数$\mu=r(1-p)/p$，则$EY=\mu$，且稍作代数运算便可得到` |
| 352:110 | Distribution / negative binomial / quadratic variance | 110 | `sections-tex/03-02.tex：用均值对负二项分布重新参数化，是一种有趣且有时很有用的做法. 若定义参数$\mu=r(1-p)/p$，则$EY=\mu$，且稍作代数运算便可得到` |
| 356:110 | Distribution / negative binomial / relation to Poisson | 110 | `sections-tex/03-02.tex：负二项分布族以Poisson分布为其极限情形. 若$r\to\infty$且$p\to1$，使得$r(1-p)\to\lambda$，其中$0<\lambda<\infty$，则` |
| 378:110 | Distribution / Poisson / relation to negative binomial | 110 | `sections-tex/03-02.tex：负二项分布族以Poisson分布为其极限情形. 若$r\to\infty$且$p\to1$，使得$r(1-p)\to\lambda$，其中$0<\lambda<\infty$，则` |
| 592:110 | Inverse binomial sampling | 110 | `ex:3.2.6` |
| 318:111 | Distribution / geometric | 111 | `sections-tex/03-02.tex：\paragraph{几何分布.}` |
| 320:111 | Distribution / geometric / memoryless | 111 | `eq:3.2.11` |
| 306:112 | Distribution / gamma | 112 | `eq:3.3.6` |
| 387:112 | Distribution / uniform | 112 | `eq:3.3.1` |
| 450:112 | Gamma function | 112 | `eq:3.3.2` |
| 315:113 | Distribution / gamma / relation to Poisson | 113 | `ex:3.3.1` |
| 377:113 | Distribution / Poisson / relation to gamma | 113 | `ex:3.3.1` |
| 245:114 | Degrees of freedom | 114 | `eq:3.3.10` |
| 280:114 | Distribution / chi squared | 114 | `eq:3.3.10` |
| 289:114 | Distribution / exponential | 114 | `eq:3.3.11` |
| 293:114 | Distribution / exponential / memoryless | 114 | `sections-tex/03-03.tex：指数分布可以用来对寿命建模，类似于离散情形中几何分布的用途. 实际上，指数分布也具有几何分布的“无记忆”性质. 若$X\sim\operatorname{exponential}(\beta)$，即p` |
| 317:114 | Distribution / Gaussian | 114 | `sections-tex/03-03.tex：\paragraph{正态分布.}` |
| 358:114 | Distribution / normal | 114 | `sections-tex/03-03.tex：\paragraph{正态分布.}` |
| 391:114 | Distribution / Weibull | 114 | `eq:3.3.12` |
| 469:114 | Hazard function | 114 | `sections-tex/03-03.tex：显然，我们也可以从Weibull分布出发，再把指数分布作为特例（$\gamma=1$）推导出来. 这只是取舍偏好的问题. Weibull分布在失效时间数据分析中起着极为重要的作用［这一主题的全面论述见` |
| 368:115 | Distribution / normal / standard | 115 | `sections-tex/03-03.tex：若$X\sim\operatorname n(\mu,\sigma^2)$，则随机变量$Z=(X-\mu)/\sigma$具有$\operatorname n(0,1)$分布，也称为标准正态分布（st` |
| 198:117 | Continuity correction | 117 | `ex:3.3.2` |
| 59:117 | Approximation / binomial by normal | 117 | `ex:3.3.2` |
| 254:118 | Distribution / beta | 118 | `eq:3.3.16` |
| 89:118 | Beta function | 118 | `eq:3.3.17` |
| 276:119 | Distribution / Cauchy | 119 | `eq:3.3.19` |
| 332:120 | Distribution / lognormal | 120 | `eq:3.3.21` |
| 288:121 | Distribution / double exponential | 121 | `eq:3.3.23` |
| 435:121 | Exponential family | 121 | `eq:3.4.1` |
| 262:123 | Distribution / binomial / exponential family | 123 | `ex:3.4.1` |
| 439:123 | Exponential family / moments | 123 | `thm:3.4.2` |
| 538:123 | Identity / exponential family | 123 | `thm:3.4.2` |
| 266:124 | Distribution / binomial / moments | 124 | `ex:3.4.3` |
| 360:124 | Distribution / normal / exponential family | 124 | `ex:3.4.4` |
| 556:124 | Indicator function | 124 | `def:3.4.5` |
| 436:125 | Exponential family / curved | 125 | `def:3.4.7` |
| 440:125 | Exponential family / natural parameter | 125 | `sections-tex/03-04.tex：称为该族的自然参数空间（natural parameter space）. 如果$X$为离散型，就把积分换成对使$h(x)>0$的$x$值求和. 对$\eta\in\mathcal H$，必须有` |
| 373:126 | Distribution / Poisson / normal approximation | 126 | `ex:3.4.9` |
| 647:126 | Location–scale family | 126 | `sec:3.5` |
| 651:126 | Location–scale family / standard pdf | 126 | `sections-tex/03-05.tex：这三类族称为位置族、尺度族和位置—尺度族. 每一类族的构造，都是先指定一个pdf，例如$f(x)$，称为该族的标准pdf（standard pdf）. 然后按指定方式变换这个标准pdf，生成族中的所有` |
| 648:127 | Location–scale family / location parameter | 127 | `def:3.5.2` |
| 1034:128 | Threshold parameter | 128 | `ex:3.5.3` |
| 650:128 | Location–scale family / scale parameter | 128 | `def:3.5.4` |
| 648:129 | Location–scale family / location parameter | 129 | `def:3.5.5` |
| 651:129 | Location–scale family / standard pdf | 129 | `def:3.5.5` |
| 565:131 | Inequality / Chebychev’s | 131 | `thm:3.6.1` |
| 576:132 | Inequality / normal | 132 | `ex:3.6.3` |
| 310:133 | Distribution / gamma / recursion relation | 133 | `thm:3.6.4` |
| 375:133 | Distribution / Poisson / recursion relation | 133 | `eq:3.6.2` |
| 541:133 | Identity / integration–by–parts | 133 | `lem:3.6.5` |
| 984:133 | Stein’s Lemma | 133 | `lem:3.6.5` |
| 532:134 | Identity / chi squared | 134 | `thm:3.6.7` |
| 473:135 | Hwang’s Lemma | 135 | `thm:3.6.8` |
| 543:135 | Identity / negative binomial | 135 | `eq:3.6.6` |
| 544:135 | Identity / Poisson | 135 | `eq:3.6.5` |
| 109:136 | Coincidences | 136 | `exercise:3.9` |
| 270:137 | Distribution / binomial / relation to negative binomial | 137 | `exercise:3.12` |
| 353:137 | Distribution / negative binomial / relation to binomial | 137 | `exercise:3.12` |
| 61:137 | Approximation / hypergeometric by binomial | 137 | `sections-tex/03-07.tex：\item[(a)] 证明，当$N\to\infty$、$M\to\infty$且$M/N\to p$时，` |
| 62:137 | Approximation / hypergeometric by Poisson | 137 | `itm:exercise:3.11:b` |
| 305:138 | Distribution / folded normal | 138 | `exercise:3.20` |
| 309:138 | Distribution / gamma / moments | 138 | `exercise:3.17` |
| 314:138 | Distribution / gamma / relation to negative binomial | 138 | `exercise:3.18` |
| 315:138 | Distribution / gamma / relation to Poisson | 138 | `exercise:3.19` |
| 327:138 | Distribution / logarithmic series | 138 | `exercise:3.14` |
| 355:138 | Distribution / negative binomial / relation to gamma | 138 | `exercise:3.18` |
| 377:138 | Distribution / Poisson / relation to gamma | 138 | `exercise:3.19` |
| 378:138 | Distribution / Poisson / relation to negative binomial | 138 | `exercise:3.15` |
| 385:138 | Distribution / truncated | 138 | `exercise:3.13` |
| 291:139 | Distribution / exponential / hazard function | 139 | `sections-tex/03-07.tex：\item[(a)] 若$T\sim\operatorname{exponential}(\beta)$，则$h_T(t)=1/\beta$.` |
| 300:139 | Distribution / extreme value | 139 | `sections-tex/03-07.tex：\item[(e)] 若$X\sim\operatorname{exponential}(1)$，则$Y=\alpha-\gamma\log X$具有Gumbel$(\alpha,\gamma)$分布` |
| 322:139 | Distribution / Gumbel | 139 | `sections-tex/03-07.tex：\item[(e)] 若$X\sim\operatorname{exponential}(1)$，则$Y=\alpha-\gamma\log X$具有Gumbel$(\alpha,\gamma)$分布` |
| 330:139 | Distribution / logistic / hazard function | 139 | `sections-tex/03-07.tex：\item[(c)] 若$T\sim\operatorname{logistic}(\mu,\beta)$，即` |
| 335:139 | Distribution / Maxwell | 139 | `sections-tex/03-07.tex：\item[(d)] 若$X\sim\operatorname{gamma}(3/2,\beta)$，则$Y=(X/\beta)^{1/2}$具有Maxwell分布.` |
| 370:139 | Distribution / Pareto | 139 | `exercise:3.23` |
| 380:139 | Distribution / Rayleigh | 139 | `sections-tex/03-07.tex：\item[(b)] 若$X\sim\operatorname{exponential}(\beta)$，则$Y=(2X/\beta)^{1/2}$具有Rayleigh分布.` |
| 391:139 | Distribution / Weibull | 139 | `sections-tex/03-07.tex：\item[(a)] 若$X\sim\operatorname{exponential}(\beta)$，则$Y=X^{1/\gamma}$具有Weibull$(\gamma,\beta)$分布，其中` |
| 392:139 | Distribution / Weibull / hazard function | 139 | `sections-tex/03-07.tex：\item[(b)] 若$T\sim\operatorname{Weibull}(\gamma,\beta)$，则$h_T(t)=(\gamma/\beta)t^{\gamma-1}$.` |
| 469:139 | Hazard function | 139 | `exercise:3.25` |
| 435:140 | Exponential family | 140 | `exercise:3.28` |
| 437:140 | Exponential family / curved / normal approximations | 140 | `exercise:3.34` |
| 276:141 | Distribution / Cauchy | 141 | `exercise:3.39` |
| 987:141 | Stochastic order / decreasing | 141 | `exercise:3.43` |
| 989:141 | Stochastic order / increasing | 141 | `exercise:3.41` |
| 374:142 | Distribution / Poisson / postulates | 142 | `thm:3.8.1` |
| 530:142 | Identity / beta | 142 | `sections-tex/03-07.tex：\item[(b)] 若$X\sim\operatorname{beta}(\alpha,\beta)$，则` |
| 539:142 | Identity / gamma | 142 | `sections-tex/03-07.tex：\item[(a)] 若$X\sim\operatorname{gamma}(\alpha,\beta)$，则` |
| 574:142 | Inequality / mgf | 142 | `exercise:3.45` |
| 576:142 | Inequality / normal | 142 | `exercise:3.47` |
| 818:142 | Poisson postulates | 142 | `thm:3.8.1` |
| 565:143 | Inequality / Chebychev’s | 143 | `thm:3.8.2` |
| 567:143 | Inequality / Gauss | 143 | `thm:3.8.4` |
| 572:143 | Inequality / Markov’s | 143 | `lem:3.8.3` |
| 579:143 | Inequality / Vysochanskiĭ-Petunin | 143 | `thm:3.8.5` |
| 438:144 | Exponential family / lognormal | 144 | `sec:3.8.3` |
| 871:145 | Random vector | 145 | `def:4.1.1` |
| 854:146 | Probability mass function (pmf) / joint / bivariate | 146 | `def:4.1.3` |
| 873:146 | Random vector / discrete | 146 | `sections-tex/04-01.tex：这个随机向量称为离散的（discrete），因为其可能取值的个数是可数的（此处为有限个）. 一旦知道函数 $f(x,y)=P(X=x,Y=y)$，就能计算所有这类事件的概率.` |
| 423:147 | Expected value / bivariate | 147 | `sections-tex/04-01.tex：随机向量的函数的期望也与单变量情形相同. 若 $g(x,y)$ 是在随机向量所有可能取值处定义的实值函数，则 $g(X,Y)$ 是一个随机变量，其期望为` |
| 855:148 | Probability mass function (pmf) / marginal | 148 | `thm:4.1.6` |
| 423:149 | Expected value / bivariate | 149 | `sections-tex/04-01.tex：联合 pdf 与单变量 pdf 的用法相同，只是需要在平面集合上做二重积分. 记号 $\iint_A$ 表示选择积分限，使积分遍及整个集合 $A$. 计算函数的期望时，将求和换为积分、pmf 换为 p` |
| 833:149 | Probability density function (pdf) / joint | 149 | `def:4.1.10` |
| 872:149 | Random vector / continuous | 149 | `def:4.1.10` |
| 834:150 | Probability density function (pdf) / marginal | 150 | `eq:4.1.2` |
| 239:152 | Cumulative distribution function (cdf) / joint | 152 | `sections-tex/04-01.tex：$(X,Y)$ 的联合概率分布也可以用联合累积分布函数（joint cumulative distribution function，联合 cdf）来完全描述，而不使用联合 pmf 或联合 pdf. ` |
| 448:152 | Fundamental Theorem of Calculus | 152 | `eq:4.1.3` |
| 851:152 | Probability mass function (pmf) / conditional | 152 | `def:4.2.1` |
| 425:154 | Expected value / conditional | 154 | `sections-tex/04-02.tex：条件 pdf 或 pmf 除了可用来计算概率，也可用来计算期望. 只要记住 $f(y\mid x)$ 作为 $y$ 的函数是 pdf 或 pmf，就可以像之前使用无条件 pdf 或 pmf 那样使用它` |
| 830:154 | Probability density function (pdf) / conditional | 154 | `def:4.2.3` |
| 1064:155 | Variance / conditional | 155 | `sections-tex/04-02.tex：由 $f(y\mid x)$ 描述的概率分布的方差，称为给定 $X=x$ 时 $Y$ 的条件方差（conditional variance）. 将其记为 $\operatorname{Var}(Y\m` |
| 554:155 | Independence / random variables | 155 | `def:4.2.5` |
| 236:157 | Cross product set | 157 | `sections-tex/04-02.tex：若 $X$ 与 $Y$ 独立，则由\eqref{eq:4.2.1} 可见，$f(x,y)>0$ 的集合为 $\{(x,y):x\in A\text{ 且 }y\in B\}$，其中 $A=\{x:f_` |
| 427:158 | Expected value / independence | 158 | `thm:4.2.10` |
| 553:158 | Independence / expected value | 158 | `thm:4.2.10` |
| 555:158 | Independence / random variables / sums | 158 | `thm:4.2.12` |
| 692:158 | Moment generating function (mgf) / independent random variables | 158 | `thm:4.2.12` |
| 369:159 | Distribution / normal / sum | 159 | `ex:4.2.13` |
| 248:160 | Determinant | 160 | `sections-tex/04-03.tex：若 $(X,Y)$ 是联合 pdf 为 $f_{X,Y}(x,y)$ 的连续随机向量，则可用类似\eqref{eq:2.1.8} 的方式，通过 $f_{X,Y}(x,y)$ 表示 $(U,V)$ 的联` |
| 379:160 | Distribution / Poisson / sum | 160 | `thm:4.3.2` |
| 593:160 | Jacobian | 160 | `sections-tex/04-03.tex：若 $(X,Y)$ 是联合 pdf 为 $f_{X,Y}(x,y)$ 的连续随机向量，则可用类似\eqref{eq:2.1.8} 的方式，通过 $f_{X,Y}(x,y)$ 表示 $(U,V)$ 的联` |
| 729:160 | One-to-one transformation | 160 | `sections-tex/04-03.tex：若 $(X,Y)$ 是联合 pdf 为 $f_{X,Y}(x,y)$ 的连续随机向量，则可用类似\eqref{eq:2.1.8} 的方式，通过 $f_{X,Y}(x,y)$ 表示 $(U,V)$ 的联` |
| 730:160 | Onto transformation | 160 | `sections-tex/04-03.tex：若 $(X,Y)$ 是联合 pdf 为 $f_{X,Y}(x,y)$ 的连续随机向量，则可用类似\eqref{eq:2.1.8} 的方式，通过 $f_{X,Y}(x,y)$ 表示 $(U,V)$ 的联` |
| 256:161 | Distribution / beta / product | 161 | `ex:4.3.3` |
| 829:161 | Probability density function (pdf) / bivariate transformation | 161 | `eq:4.3.2` |
| 369:162 | Distribution / normal / sum | 162 | `ex:4.3.4` |
| 363:163 | Distribution / normal / ratio | 163 | `ex:4.3.6` |
| 554:163 | Independence / random variables | 163 | `thm:4.3.5` |
| 279:164 | Distribution / Cauchy / relation to normal | 164 | `ex:4.3.6` |
| 340:164 | Distribution / mixture / binomial–Poisson | 164 | `ex:4.4.1` |
| 365:164 | Distribution / normal / relation to Cauchy | 164 | `ex:4.3.6` |
| 428:165 | Expected value / iterated | 165 | `thm:4.4.3` |
| 336:166 | Distribution / mixture | 166 | `def:4.4.4` |
| 341:166 | Distribution / mixture / binomial–Poisson–exponential | 166 | `ex:4.4.5` |
| 339:167 | Distribution / mixture / binomial–negative binomial | 167 | `sections-tex/04-04.tex：$Y$ 的这个 pmf 就是负二项 pmf 的\hyperref[eq:3.2.10]{式 (3.1.10)} 形式.\footnote{译注：原文引用 (3.1.10)，对应公式实际编号为\eqre` |
| 342:167 | Distribution / mixture / chi squared–Poisson | 167 | `eq:4.4.3` |
| 346:167 | Distribution / mixture / Poisson–gamma | 167 | `sections-tex/04-04.tex：一个有用的推广是 Poisson--Gamma 混合，它推广了上述模型的一部分. 若有层次结构` |
| 357:167 | Distribution / noncentral chi squared | 167 | `eq:4.4.3` |
| 1064:168 | Variance / conditional | 168 | `thm:4.4.7` |
| 337:168 | Distribution / mixture / Bernoulli–beta | 168 | `ex:4.4.6` |
| 223:169 | Covariance | 169 | `def:4.5.1` |
| 337:169 | Distribution / mixture / Bernoulli–beta | 169 | `ex:4.4.8` |
| 216:170 | Correlation / coefficient | 170 | `def:4.5.2` |
| 217:170 | Correlation | 170 | `def:4.5.2` |
| 1068:171 | Variance / sum | 171 | `thm:4.5.6` |
| 221:171 | Covariance / independence | 171 | `thm:4.5.5` |
| 548:171 | Independence / covariance | 171 | `thm:4.5.5` |
| 217:172 | Correlation | 172 | `thm:4.5.7` |
| 564:172 | Inequality / Cauchy–Schwarz | 172 | `thm:4.5.7` |
| 273:174 | Distribution / bivariate normal | 174 | `def:4.5.10` |
| 429:176 | Expected value / joint | 176 | `eq:4.6.3` |
| 833:176 | Probability density function (pdf) / joint | 176 | `eq:4.6.2` |
| 834:176 | Probability density function (pdf) / marginal | 176 | `sections-tex/04-06.tex：$(X_1,\ldots,X_n)$ 中任意一部分坐标的边缘 pdf 或 pmf，都可以通过对其他坐标的所有可能值积分或求和得到.` |
| 853:176 | Probability mass function (pmf) / joint | 176 | `eq:4.6.1` |
| 855:176 | Probability mass function (pmf) / marginal | 176 | `sections-tex/04-06.tex：$(X_1,\ldots,X_n)$ 中任意一部分坐标的边缘 pdf 或 pmf，都可以通过对其他坐标的所有可能值积分或求和得到.` |
| 830:177 | Probability density function (pdf) / conditional | 177 | `eq:4.6.6` |
| 851:177 | Probability mass function (pmf) / conditional | 177 | `eq:4.6.6` |
| 269:179 | Distribution / binomial / relation to multinomial | 179 | `sections-tex/04-06.tex：现在考虑多项模型的一些边缘与条件分布. 对单个坐标 $X_i$，若把第 $i$ 个结果称为“成功”，其他结果称为“失败”，则 $X_i$ 统计 $m$ 次独立试验中的成功次数，每次成功概率为 $p_i` |
| 348:179 | Distribution / multinomial | 179 | `def:4.6.2` |
| 350:179 | Distribution / multinomial / relation to binomial | 179 | `sections-tex/04-06.tex：现在考虑多项模型的一些边缘与条件分布. 对单个坐标 $X_i$，若把第 $i$ 个结果称为“成功”，其他结果称为“失败”，则 $X_i$ 统计 $m$ 次独立试验中的成功次数，每次成功概率为 $p_i` |
| 712:179 | Multinomial coefficient | 179 | `sections-tex/04-06.tex：因子 $m!/(x_1!\cdots x_n!)$ 称为多项系数（multinomial coefficient）. 它表示将 $m$ 个物体分成 $n$ 组、第一组有 $x_1$ 个、第二组有 $x` |
| 713:179 | Multinomial Theorem | 179 | `thm:4.6.4` |
| 349:180 | Distribution / multinomial / covariance | 180 | `sections-tex/04-06.tex：从条件分布可以看出，向量 $(X_1,\ldots,X_n)$ 的各坐标有关系. 尤其是 $m$ 固定时，必然有某种负相关. 事实上，所有两两协方差都为负，由下式给出（\autoref{exercis` |
| 554:180 | Independence / random variables | 180 | `def:4.6.5` |
| 316:181 | Distribution / gamma / sum | 181 | `ex:4.6.8` |
| 427:181 | Expected value / independence | 181 | `thm:4.6.6` |
| 553:181 | Independence / expected value | 181 | `thm:4.6.6` |
| 695:181 | Moment generating function (mgf) / sum | 181 | `thm:4.6.7` |
| 248:182 | Determinant | 182 | `sections-tex/04-06.tex：设 $(X_1,\ldots,X_n)$ 的 pdf 为 $f_{\mathbf X}(x_1,\ldots,x_n)$，令 $\mathscr A=\{\mathbf x:f_{\mathbf X}` |
| 362:182 | Distribution / normal / linear combination | 182 | `cor:4.6.10` |
| 836:182 | Probability density function (pdf) / multivariate transformation | 182 | `eq:4.6.7` |
| 737:183 | Order statistics / spacings | 183 | `sections-tex/04-06.tex：\autoref{ex:4.6.13} 的模型可以如下产生. 假设 $Y_1,Y_2,Y_3,Y_4$ 相互独立，每个都服从 $\operatorname{exponential}(1)$ 分布. 定` |
| 564:184 | Inequality / Cauchy–Schwarz | 184 | `thm:4.7.3` |
| 568:184 | Inequality / Hölder’s | 184 | `thm:4.7.2` |
| 570:185 | Inequality / Liapounov’s | 185 | `eq:4.7.6` |
| 575:185 | Inequality / Minkowski’s | 185 | `thm:4.7.5` |
| 578:185 | Inequality / triangle | 185 | `eq:4.7.8` |
| 121:186 | Concave function | 186 | `def:4.7.6` |
| 212:186 | Convex function | 186 | `def:4.7.6` |
| 569:186 | Inequality / Jensen’s | 186 | `thm:4.7.7` |
| 457:187 | Geometric mean | 187 | `ex:4.7.8` |
| 468:187 | Harmonic mean | 187 | `ex:4.7.8` |
| 573:187 | Inequality / means | 187 | `ex:4.7.8` |
| 64:187 | Arithmetic mean | 187 | `ex:4.7.8` |
| 424:188 | Expected value / bivariate / properties | 188 | `exercise:4.2` |
| 566:188 | Inequality / covariance | 188 | `thm:4.7.9` |
| 238:189 | Cumulative distribution function (cdf) / independence | 189 | `exercise:4.9` |
| 271:190 | Distribution / binomial / relation to Poisson | 190 | `exercise:4.15` |
| 376:190 | Distribution / Poisson / relation to binomial | 190 | `exercise:4.15` |
| 426:190 | Expected value / conditional / minimizing | 190 | `exercise:4.13` |
| 884:190 | Regression / conditional expectation | 190 | `exercise:4.13` |
| 259:191 | Distribution / beta / relation to gamma | 191 | `exercise:4.24` |
| 279:191 | Distribution / Cauchy / relation to normal | 191 | `exercise:4.28` |
| 311:191 | Distribution / gamma / relation to beta | 191 | `exercise:4.24` |
| 346:191 | Distribution / mixture / Poisson–gamma | 191 | `exercise:4.32` |
| 351:191 | Distribution / negative binomial | 191 | `exercise:4.32` |
| 365:191 | Distribution / normal / relation to Cauchy | 191 | `exercise:4.28` |
| 866:191 | Random variable / censored | 191 | `exercise:4.26` |
| 260:192 | Distribution / beta–binomial | 192 | `exercise:4.34` |
| 338:192 | Distribution / mixture / binomial–beta | 192 | `exercise:4.34` |
| 344:192 | Distribution / mixture / logarithmic series–Poisson | 192 | `exercise:4.33` |
| 876:192 | Randomly stopped sum | 192 | `exercise:4.33` |
| 295:193 | Distribution / exponential / relation to gamma | 193 | `exercise:4.38` |
| 312:193 | Distribution / gamma / relation to exponential | 193 | `exercise:4.38` |
| 343:193 | Distribution / mixture / exponential-gamma | 193 | `exercise:4.38` |
| 349:193 | Distribution / multinomial / covariance | 193 | `exercise:4.39` |
| 446:193 | Forced binary choice | 193 | `exercise:4.37` |
| 1068:194 | Variance / sum | 194 | `exercise:4.44` |
| 273:194 | Distribution / bivariate normal | 194 | `exercise:4.45` |
| 359:195 | Distribution / normal / bivariate | 195 | `exercise:4.47` |
| 398:196 | Entropy | 196 | `sections-tex/04-08.tex：量 $\sum_i a_i\log(1/a_i)$ 称为熵（entropy），有时视为不确定性的绝对度量，见 Bernardo and Smith (1994, Section 2.7). (iii)` |
| 533:196 | Identity / conditional covariance | 196 | `exercise:4.59` |
| 749:196 | Parallel system | 196 | `exercise:4.55` |
| 420:197 | Exchange paradox | 197 | `sec:4.9.1` |
| 578:197 | Inequality / triangle | 197 | `exercise:4.64` |
| 748:197 | Paradox / exchange | 197 | `sec:4.9.1` |
| 558:198 | Inequality / arithmetic-geometric-harmonic mean | 198 | `sec:4.9.2` |
| 577:198 | Inequality / power mean | 198 | `sec:4.9.2` |
| 747:198 | Paradox / Borel | 198 | `sec:4.9.3` |
| 821:198 | Power means | 198 | `sec:4.9.2` |
| 98:198 | Borel Paradox | 198 | `sec:4.9.3` |
