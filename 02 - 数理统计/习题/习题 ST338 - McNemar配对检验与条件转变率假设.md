---
title: 习题 ST338：McNemar配对检验与条件转变率假设
topic: mathematical-statistics
topic_label: 数理统计
difficulty: intermediate
status: not-started
tags:
- exercise
- mathematical-statistics
source: George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第10章习题10.32，印刷页414/415／PDF物理页445/446
source_id: DS011
source_chapter: 10
source_exercise: '10.32'
source_stars: 0
source_refs:
- DS011 Exercise 10.32，印刷414/415／PDF物理445/446
source_status: verified
solution_status: independently-derived
created: '2026-11-13'
---

# 习题 ST338：McNemar配对检验与条件转变率假设

## 题目

### 英文原题

> [!question] 英文原题
> **10.32** (a) Let $(X_1,\ldots,X_n)\sim\operatorname{multinomial}(m,p_1,\ldots,p_n)$. Consider testing $H_0:p_1=p_2$ versus $H_1:p_1\ne p_2$. A test that is often used, called McNemar's Test, rejects $H_0$ if
> $$
> \frac{(X_1-X_2)^2}{X_1+X_2}>\chi^2_{1,\alpha}.
> $$
> Show that this test statistic has the form (as in Exercise 10.31)
> $$
> \sum_1^n\frac{(\text{observed}-\text{expected})^2}{\text{expected}},
> $$
> where the $X_i$s are the observed cell frequencies and the expected cell frequencies are the MLEs of $mp_i$, under the assumption that $p_1=p_2$.
>
> (b) McNemar's Test is often used in the following type of problem. Subjects are asked if they agree or disagree with a statement. Then they read some information about the statement and are asked again if they agree or disagree. The numbers of responses in each category are summarized in a $2\times2$ table like this.
>
> |After\Before|Agree|Disagree|
> |---|---|---|
> |Agree|$X_3$|$X_2$|
> |Disagree|$X_1$|$X_4$|
>
> The hypothesis $H_0:p_1=p_2$ states that the proportion of people who change from agree to disagree is the same as the proportion of people who change from disagree to agree. Another hypothesis that might be tested is that the proportion of those who initially agree, then change is the same as the proportion of those who initially disagree, then change. Express this hypothesis in terms of conditional probabilities and show that it is different from the above $H_0$. (This hypothesis can be tested with a $\chi^2$ test like those in Exercise 10.31.)

### 中文转述

> [!question] 中文转述
> **原题10.32。** (a)  设$(X_1,\ldots,X_n)\sim\operatorname{multinomial}(m,p_1,\ldots,p_n)$. 考虑检验$H_0:p_1=p_2$对$H_1:p_1\ne p_2$. 一个常用的检验称为McNemar检验（McNemar's Test），在
>
> $$
> \frac{(X_1-X_2)^2}{X_1+X_2}>\chi_{1,\alpha}^2
> $$
>
> 时拒绝$H_0$. 证明这个检验统计量具有如下形式（如习题10.31）：
>
> $$
> \sum_1^n\frac{(\text{观测值}-\text{期望值})^2}{\text{期望值}},
> $$
>
> 其中$X_i$是观测单元频数，期望单元频数是在$p_1=p_2$假设下$mp_i$的MLE.
>
> (b)  McNemar检验常用于以下类型的问题. 先问受试者赞成还是反对某个陈述，再让他们阅读与该陈述有关的信息，随后再次询问赞成还是反对. 各类别回答人数汇总于如下$2\times2$表：
> |之后\之前|赞成|反对|
> |---|---|---|
> |赞成|$X_3$|$X_2$|
> |反对|$X_1$|$X_4$|
> 假设$H_0:p_1=p_2$意味着，从赞成改为反对者的比例，与从反对改为赞成者的比例相同. 另一种可检验的假设是：最初赞成的人中改变意见的比例，与最初反对的人中改变意见的比例相同. 用条件概率表达这个假设，证明它不同于上述$H_0$. （此假设可用类似习题10.31的$\chi^2$检验检验.）

## 提示

> [!hint]- 提示
> 在约束p_1=p_2下，两格合并总数不变，各占一半。新假设的分母是原始赞成与反对的人数比例。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** **(a)** 约束$p_1=p_2=a$，联合似然在其余格给$\hat p_i=X_i/m$（$i\ge3$），前两格共享余下质量，故$\hat p_1=\hat p_2=(X_1+X_2)/(2m)$。期望频数$E_1=E_2=(X_1+X_2)/2$，其余$E_i=X_i$。于是Pearson和只有前两项非零：
> $$
> \frac{[X_1-(X_1+X_2)/2]^2}{(X_1+X_2)/2}+\frac{[X_2-(X_1+X_2)/2]^2}{(X_1+X_2)/2}=\frac{(X_1-X_2)^2}{X_1+X_2}.
> $$
> 若$X_1+X_2=0$，两种不一致对都没有，定义统计量0并不拒绝；常规卡方校准需不一致对期望数增长。条件于$D=X_1+X_2$，$H_0$下$X_1\sim\operatorname{Bin}(D,1/2)$，也给该渐近检验及小样本精确版本。
>
> **(b)** “原先赞成者中改变”概率为$p_1/(p_1+p_3)$，“原先反对者中改变”为$p_2/(p_2+p_4)$，分母正时新假设为
> $$
> \frac{p_1}{p_1+p_3}=\frac{p_2}{p_2+p_4}\quad\Longleftrightarrow\quad p_1p_4=p_2p_3.
> $$
> 它与$p_1=p_2$不同。例如$(p_1,p_2,p_3,p_4)=(.1,.1,.3,.5)$满足McNemar零假设，但条件转变率$.25$与$1/6$不同；$(.1,.15,.3,.45)$满足条件率同为$.25$，却$p_1\ne p_2$。两种检验回答不同问题，不能用未配对两组比例检验替代配对边际同质性检验。

## 相关概念

- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/期望|期望]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/假设检验|假设检验]]

## 备注

- 来源：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=445|印刷第414/415页／PDF物理第445/446页]]；版本与归档见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 英文原题逐题对照PDF原始页面，保留原分题、提示、引用及可见疑误；原题无星号。题内引用补充与独立解答不混入原文；未查阅答案册或题内外部文献。
- 来源核对不表示个人学习完成，学习状态保持not-started。公式、链接与元数据检查不等于Obsidian实际渲染检查。
