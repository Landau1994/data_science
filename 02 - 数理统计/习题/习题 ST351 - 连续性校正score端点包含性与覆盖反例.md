---
title: 习题 ST351：连续性校正score端点包含性与覆盖反例
topic: mathematical-statistics
topic_label: 数理统计
difficulty: advanced
status: not-started
tags:
- exercise
- mathematical-statistics
source: George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第10章习题10.45，印刷页416／PDF物理页447
source_id: DS011
source_chapter: 10
source_exercise: '10.45'
source_stars: 0
source_refs:
- DS011 Exercise 10.45，印刷416／PDF物理447
- DS011题内依赖核对：印刷405／PDF物理436
source_status: verified
solution_status: independently-derived
created: '2026-11-13'
---

# 习题 ST351：连续性校正score端点包含性与覆盖反例

## 题目

### 英文原题

> [!question] 英文原题
> **10.45** Solve for the endpoints of the approximate binomial confidence interval, with continuity correction, given in Example 10.4.6. Show that this interval is wider than the corresponding interval without continuity correction, and that the continuity corrected interval has a uniformly higher coverage probability. (In fact, the coverage probability of the uncorrected interval does not maintain $1-\alpha$; it dips below this level for some parameter values. The corrected interval does maintain a coverage probability greater than $1-\alpha$ for all parameter values.)

### 中文转述

> [!question] 中文转述
> **原题10.45。** 解出例10.4.6所给带连续性校正的近似二项置信区间端点. 证明该区间比不带连续性校正的对应区间更宽，且经过校正的区间具有一致更高的覆盖概率. （事实上，未校正区间的覆盖概率不能保持$1-\alpha$，会在一些参数值处低于此水平. 经过校正的区间则对所有参数值都保持大于$1-\alpha$的覆盖概率.）

## 提示

> [!hint]- 提示
> 加入半个计数是扩张score接受域，保证相对覆盖不减；它并不自动保证所有n与α都达到名义值。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 设$\hat p=y/n,z=z_{\alpha/2}$，定义二次根函数
> $$
> R_\pm(q)=\frac{2nq+z^2\pm z\sqrt{z^2+4nq(1-q)}}{2(n+z^2)},\quad0\le q\le1.
> $$
> 未校正Wilson为$[R_-(\hat p),R_+(\hat p)]$。连续性校正端点为
> $$
> L_c(y)=\begin{cases}0,&y=0,\\R_-(\hat p-1/(2n)),&y>0,\end{cases}\qquad
> U_c(y)=\begin{cases}R_+(\hat p+1/(2n)),&y<n,\\1,&y=n.\end{cases}
> $$
> 它们分别解$[\hat p\mp1/(2n)-p]^2=z^2p(1-p)/n$的外侧根，正好对应原例两条二次式。
>
> **包含性证明。** 原score集满足$|y-np|\le z\sqrt{np(1-p)}$。校正集为$|y-np|\le z\sqrt{np(1-p)}+.5$，包含原集；分开左右支求根并作端点截断即上式。因此每个样本区间弱加宽，对所有$p$，$P_p(p\in C_c(Y))\ge P_p(p\in C_W(Y))$。这里“uniformly higher”准确为逐点不低于，未必处处严格：$p=0,1$时两者覆盖都是1。
>
> **原括号中的普适名义下界不成立。** 独立枚举找到明确反例：$n=1$、名义95%、$z=1.9599639845$，$Y=1$时校正下端$R_-(.5)=.05462075553$。取$p=.0546$，只有$Y=0$的区间覆盖真值，而$Y=1$的不覆盖，所以精确覆盖为$P(Y=0)=1-p=.9454<.95$。因此无法证明题称对所有参数都大于$1-\alpha$；反例同时给定合法$n,\alpha,p$，不是网格舍入误差。该校正通常改善离散近似，包含性和相对改进仍成立，但并非精确保守区间的一般定理。

## 相关概念

- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/期望|期望]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[02 - 数理统计/概念/参数估计|参数估计]]

## 备注

- 来源：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=447|印刷第416页／PDF物理第447页]]；版本与归档见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 原例连续性校正二次式实读印刷405／PDF436。实际还检查n=1,…,150及α=.1,.05,.01的所有端点左右，反例记录见[[work/DS011/ch10/results.json|结果10.45]]；有限搜索不作为无反例范围的证明。
- 已实读本题所用正文：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=436|印刷405／PDF物理436]]；其余题内外部文献仅保留原引用，未声称查阅。
- 英文原题逐题对照PDF原始页面，保留原分题、提示、引用及可见疑误；原题无星号。题内引用补充与独立解答不混入原文；未查阅答案册或题内外部文献。
- 来源核对不表示个人学习完成，学习状态保持not-started。公式、链接与元数据检查不等于Obsidian实际渲染检查。
