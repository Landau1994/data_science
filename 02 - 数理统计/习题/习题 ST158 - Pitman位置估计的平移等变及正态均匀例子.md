---
title: "习题 ST158：Pitman位置估计的平移等变及正态均匀例子"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第7章习题7.35，印刷页293／PDF物理页324"
source_id: "DS011"
source_chapter: 7
source_exercise: "7.35"
source_stars: 0
source_refs: ["DS011 Exercise 7.35，印刷293／PDF物理324", "DS011 例7.3.6位置等变方程(7.3.2)与风险(7.3.3)，印刷270／PDF物理301"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST158：Pitman位置估计的平移等变及正态均匀例子

## 题目

### 英文原题

> [!question] 英文原题
> **7.35** The Pitman Estimator of Location (see Lehmann and Casella (1998, Section 3.1) or the original paper by Pitman (1939)) is given by
> $$
> d_P(\mathbf X)=\frac{\int_{-\infty}^{\infty}t\prod_{i=1}^nf(x_i-t)dt}{\int_{-\infty}^{\infty}\prod_{i=1}^nf(x_i-t)dt},
> $$
> where we observe a random sample $X_1,\ldots,X_n$ from $f(x-\theta)$. Pitman showed that this estimator is the location-equivariant estimator with smallest mean squared error (that is, it minimizes (7.3.3)). The goals of this exercise are more modest.
>
> (a) Show that $d_P(\mathbf X)$ is invariant with respect to the location group of Example 7.3.6.
>
> (b) Show that if $f(x-\theta)$ is $n(\theta,1)$, then $d_P(\mathbf X)=\bar X$.
>
> (c) Show that if $f(x-\theta)$ is uniform$(\theta-\frac12,\theta+\frac12)$, then $d_P(\mathbf X)=\frac12(X_{(1)}+X_{(n)})$.

### 中文转述

> [!question] 中文转述
> **原题7.35。** Pitman位置估计量（Pitman estimator of location；见Lehmann和Casella 1998，第3.1节，或Pitman 1939的原始论文）为
>
> $$
> d_P(\boldsymbol X)=\frac{\int_{-\infty}^\infty t\prod_{i=1}^nf(x_i-t)\,dt}{\int_{-\infty}^\infty\prod_{i=1}^nf(x_i-t)\,dt},
> $$
>
> 其中观测到来自$f(x-\theta)$的随机样本$X_1,\ldots,X_n$.Pitman说明，该估计量是在位置等变估计量中均方误差最小者（即使式7.3.3最小）.本题的目标较为有限.
>
> (a)  说明$d_P(\boldsymbol X)$关于例7.3.6的位置群不变.
>
> (b)  说明若$f(x-\theta)$为$n(\theta,1)$，则$d_P(\boldsymbol X)=\bar X$.
>
> (c)  说明若$f(x-\theta)$为$\operatorname{uniform}(\theta-\frac12,\theta+\frac12)$，则$d_P(\boldsymbol X)=\frac12(X_{(1)}+X_{(n)})$.

## 提示

> [!hint]- 提示
> 把积分变量与观测同步平移；均匀情形的可行位置区间取中点。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 假定分母有限且正、分子绝对可积，这样比值才有意义；本题只证明列出的性质，未另行复证Pitman最优性定理。
>
> **(a)** 对任意平移$c$，在分子分母都令$u=t-c$。分母变为原分母，分子变为$\int(u+c)\prod_i f(x_i-u)du$，所以
> $$
> d_P(\mathbf x+c\mathbf1)=d_P(\mathbf x)+c.
> $$
> 这叫**平移等变（location equivariance）**。原题invariant若解释为数值不变则错误；例如正态样本均值加$c$也会加$c$，并非相等。它与例7.3.6的等变方程一致。
>
> **(b)** 正态核用$\sum_i(x_i-t)^2=\sum_i(x_i-\bar x)^2+n(t-\bar x)^2$配方，分母中的$t$核为均值$\bar x$、方差$1/n$的正态。分子的奇函数部分积分为零，故比值是$\bar x$。
>
> **(c)** 均匀核为$\prod_i\mathbf1\{|x_i-t|<1/2\}=\mathbf1\{M-1/2<t<m+1/2\}$，$m=x_{(1)},M=x_{(n)}$。有效样本下$M-m<1$几乎必然，分母为区间长度$1-M+m>0$，比值是该区间中点$[(M-1/2)+(m+1/2)]/2=(m+M)/2$。边界零长度样本需另取极限版本，不能在零分母上直接求比值。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=324|印刷第293页／PDF物理第324页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 原(a)invariant照录，解答给正确的equivariant关系及数值不变断言的反例。
- 英文原文、中文转述与本库独立解答分别保留；实际核对正文位置列于`source_refs`。题内文献引用不表示已查阅其原文。`source_status: verified`只指本题及所列位置的核对范围，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
