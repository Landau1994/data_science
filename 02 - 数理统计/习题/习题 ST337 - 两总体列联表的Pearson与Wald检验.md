---
title: 习题 ST337：两总体列联表的Pearson与Wald检验
topic: mathematical-statistics
topic_label: 数理统计
difficulty: advanced
status: not-started
tags:
- exercise
- mathematical-statistics
source: George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第10章习题10.31，印刷页413/414／PDF物理页444/445
source_id: DS011
source_chapter: 10
source_exercise: '10.31'
source_stars: 0
source_refs:
- DS011 Exercise 10.31，印刷413/414／PDF物理444/445
source_status: verified
solution_status: independently-derived
created: '2026-11-13'
---

# 习题 ST337：两总体列联表的Pearson与Wald检验

## 题目

### 英文原题

> [!question] 英文原题
> **10.31** Binomial data gathered from more than one population are often presented in a contingency table. For the case of two populations, the table might look like
>
> | |Population 1|Population 2|Total|
> |---|---|---|---|
> |Successes|$S_1$|$S_2$|$S=S_1+S_2$|
> |Failures|$F_1$|$F_2$|$F=F_1+F_2$|
> |Total|$n_1$|$n_2$|$n=n_1+n_2$|
>
> where Population 1 is binomial$(n_1,p_1)$, with $S_1$ successes and $F_1$ failures, and Population 2 is binomial$(n_2,p_2)$, with $S_2$ successes and $F_2$ failures. A hypothesis that is usually of interest is
> $$
> H_0:p_1=p_2\quad\text{versus}\quad H_1:p_1\ne p_2.
> $$
> (a) Show that a test can be based on the statistic
> $$
> T=\frac{(\hat p_1-\hat p_2)^2}{(1/n_1+1/n_2)(\hat p(1-\hat p))},
> $$
> where $\hat p_1=S_1/n_1$, $\hat p_2=S_2/n_2$, and $\hat p=(S_1+S_2)/(n_1+n_2)$. Also, show that as $n_1,n_2\to\infty$, the distribution of $T$ approaches $\chi_1^2$. (This is a special case of a test known as a chi squared test of independence.)
>
> (b) Another way of measuring departure from $H_0$ is by calculating an expected frequency table. This table is constructed by conditioning on the marginal totals, and filling in the table according to $H_0:p_1=p_2$, that is,
>
> | |Expected Frequencies 1|Expected Frequencies 2|Total|
> |---|---|---|---|
> |Successes|$n_1S/(n_1+n_2)$|$n_2S/(n_1+n_2)$|$S=S_1+S_2$|
> |Failures|$n_1F/(n_1+n_2)$|$n_2F/(n_1+n_2)$|$F=F_1+F_2$|
> |Total|$n_1$|$n_2$|$n=n_1+n_2$|
>
> Using the expected frequency table, a statistic $T^*$ is computed by going through the cells of the tables and computing
> $$
> T^*=\sum\frac{(\text{observed}-\text{expected})^2}{\text{expected}}=\frac{(S_1-n_1S/(n_1+n_2))^2}{n_1S/(n_1+n_2)}+\cdots+\frac{(F_2-n_2F/(n_1+n_2))^2}{n_2F/(n_1+n_2)}.
> $$
> Show, algebraically, that $T^*=T$ and hence that $T^*$ is asymptotically chi squared.
>
> (c) Another statistic that could be used to test for equality of $p_1$ and $p_2$ is
> $$
> T^{**}=\frac{\hat p_1-\hat p_2}{\sqrt{\hat p_1(1-\hat p_1)/n_1+\hat p_2(1-\hat p_2)/n_2}}.
> $$
> Show that, under $H_0$, $T^{**}$ is asymptotically $\operatorname n(0,1)$, and hence its square is asymptotically $\chi_1^2$. Furthermore, show that $(T^{**})^2\ne T^*$.
>
> (d) Under what circumstances is one statistic preferable to the other?
>
> (e) A famous medical experiment was conducted by Joseph Lister in the late 1800s. Mortality associated with surgery was quite high and Lister conjectured that the use of a disinfectant, carbolic acid, would help. Over a period of several years Lister performed 75 amputations with and without using carbolic acid. The data are
>
> |Patient lived?|Carbolic acid used? Yes|No|
> |---|---:|---:|
> |Yes|34|19|
> |No|6|16|
>
> Use these data to test whether the use of carbolic acid is associated with patient mortality.

### 中文转述

> [!question] 中文转述
> **原题10.31。** 从多个总体采集的二项数据常以列联表（contingency table）呈现. 对两个总体，表格可能如下：
> | |总体1|总体2|合计|
> |---|---|---|---|
> |成功|$S_1$|$S_2$|$S=S_1+S_2$|
> |失败|$F_1$|$F_2$|$F=F_1+F_2$|
> |合计|$n_1$|$n_2$|$n=n_1+n_2$|
> 其中总体1为binomial$(n_1,p_1)$，有$S_1$次成功与$F_1$次失败；总体2为binomial$(n_2,p_2)$，有$S_2$次成功与$F_2$次失败. 通常感兴趣的假设为
>
> $$
> H_0:p_1=p_2\qquad\text{对}\qquad H_1:p_1\ne p_2.
> $$
>
> (a)  证明可以基于统计量
>
> $$
> T=\frac{(\hat p_1-\hat p_2)^2}{\left(\frac1{n_1}+\frac1{n_2}\right)\bigl(\hat p(1-\hat p)\bigr)}
> $$
>
> 建立检验，其中$\hat p_1=S_1/n_1$、$\hat p_2=S_2/n_2$、$\hat p=(S_1+S_2)/(n_1+n_2)$. 再证明当$n_1,n_2\to\infty$时，$T$的分布趋于$\chi_1^2$. （这是称为独立性卡方检验，chi squared test of independence，的一类检验的特例.）
>
> (b)  另一种衡量偏离$H_0$程度的方法是计算期望频数表（expected frequency table）. 以边际合计为条件，按照$H_0:p_1=p_2$填表，即
> | |期望频数1|期望频数2|合计|
> |---|---|---|---|
> |成功|$n_1S/(n_1+n_2)$|$n_2S/(n_1+n_2)$|$S=S_1+S_2$|
> |失败|$n_1F/(n_1+n_2)$|$n_2F/(n_1+n_2)$|$F=F_1+F_2$|
> |合计|$n_1$|$n_2$|$n=n_1+n_2$|
> 利用期望频数表，逐个单元计算并求和，得到统计量$T^*$：
>
> $$
> \begin{aligned}
> T^*&=\sum\frac{(\text{观测值}-\text{期望值})^2}{\text{期望值}}\\
> &=\frac{\left(S_1-\frac{n_1S}{n_1+n_2}\right)^2}{\frac{n_1S}{n_1+n_2}}+\cdots+\frac{\left(F_2-\frac{n_2F}{n_1+n_2}\right)^2}{\frac{n_2F}{n_1+n_2}}.
> \end{aligned}
> $$
>
> 用代数方法证明$T^*=T$，从而$T^*$渐近服从卡方分布.
>
> (c)  另一个可用来检验$p_1$和$p_2$相等的统计量为
>
> $$
> T^{**}=\frac{\hat p_1-\hat p_2}{\sqrt{\frac{\hat p_1(1-\hat p_1)}{n_1}+\frac{\hat p_2(1-\hat p_2)}{n_2}}}.
> $$
>
> 证明在$H_0$下，$T^{**}$渐近服从$\mathrm n(0,1)$，因此其平方渐近服从$\chi_1^2$. 再证明$(T^{**})^2\ne T^*$.
>
> (d)  在什么情况下，一个统计量优于另一个？
>
> (e)  19世纪后期，Joseph Lister进行了一项著名的医学实验. 当时手术相关死亡率很高，Lister猜想使用消毒剂石炭酸会有所帮助. 数年间，Lister完成75例使用或不使用石炭酸的截肢手术，数据如下：
> |患者存活？|使用石炭酸|未使用石炭酸|
> |---|---:|---:|
> |是|34|19|
> |否|6|16|
> 用这些数据检验使用石炭酸是否与患者死亡有关.

## 提示

> [!hint]- 提示
> 零假设下估计公共比例；Pearson四个残差都等于同一差值的正负号。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 设两总体样本相互独立，零假设公共$p\in(0,1)$，两样本量均趋于无穷。
>
> **(a)** $D=\hat p_1-\hat p_2$在$H_0$下均值0、方差$p(1-p)(1/n_1+1/n_2)$。独立伯努利和的CLT给标准化$D\Rightarrow N(0,1)$，公共比例MLE$\hat p\to_pp$，Slutsky及平方映射给$T\Rightarrow\chi^2_1$。因此以$T>\chi^2_{1,\alpha}$拒绝。$\hat p=0,1$的有限样本零分母应视为无差异/信息不足边界单独定义，不在常规正态近似范围内。
>
> **(b)** 记$n=n_1+n_2$、$\Delta=S_1-n_1\hat p=(n_1n_2/n)D$。四个观测减期望依次为$\Delta,-\Delta,-\Delta,\Delta$，所以
> $$
> T^*=\Delta^2\left(\frac1{n_1\hat p}+\frac1{n_2\hat p}+\frac1{n_1(1-\hat p)}+\frac1{n_2(1-\hat p)}\right)=\frac{D^2}{(1/n_1+1/n_2)\hat p(1-\hat p)}=T.
> $$
> **(c)** 非合并方差估计除以真实零假设方差趋于1，故$T^{**}\Rightarrow N(0,1)$。平方一般不与$T$代数相同，因为两个分母使用不同估计。例如$n_1=n_2=10,S_1=8,S_2=2$，$T=7.2$，$(T^{**})^2=11.25$。原“$\ne$”应指并非同一统计量，不能声称每组数据都严格不同；$\hat p_1=\hat p_2$时二者都0。
>
> **(d)** 零假设检验通常用公共参数约束下的合并方差，Pearson/score有自然列联表解释；非合并Wald更直接反映各组观测变异，适合某些区间/替代参数分析，但小样本或边界可能标准误为0。两者同一一阶零假设极限，没有一般统一功效优势；稀疏单元应考虑精确条件检验或其他有限样本校准，不能仅看较小$p$值选择统计量。
>
> **(e)** 两组样本量40、35，存活比例$.85$、$19/35=.5428571$，公共估计$53/75$。期望四格为28.2667、24.7333、11.7333、10.2667。实际$T=8.4951605$，$\chi^2_1$上尾$p=.00356092$，在5%或1%水平拒绝无关联；非合并Wald$T^{**}=3.0296236$，双侧$p=.00244859$。附加Fisher双侧精确值$.00501805$也支持关联。该计算证明的是给定样本模型下的统计关联，历史表格本身未说明随机分配，不能据此单独识别因果效应。

## 相关概念

- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/期望|期望]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/假设检验|假设检验]]

## 备注

- 来源：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=444|印刷第413/414页／PDF物理第444/445页]]；版本与归档见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 原表、两个期望频数公式及Lister四格全部保留。数值由[[work/DS011/ch10/computations.py|独立计算]]实际求得；没有查阅外部历史资料。
- 英文原题逐题对照PDF原始页面，保留原分题、提示、引用及可见疑误；原题无星号。题内引用补充与独立解答不混入原文；未查阅答案册或题内外部文献。
- 来源核对不表示个人学习完成，学习状态保持not-started。公式、链接与元数据检查不等于Obsidian实际渲染检查。
