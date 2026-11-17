---
title: "习题 ST159：Pitman尺度估计的齐次性与三个积分闭式"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第7章习题7.36，印刷页293／PDF物理页324"
source_id: "DS011"
source_chapter: 7
source_exercise: "7.36"
source_stars: 0
source_refs: ["DS011 Exercise 7.36，印刷293／PDF物理324"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST159：Pitman尺度估计的齐次性与三个积分闭式

## 题目

### 英文原题

> [!question] 英文原题
> **7.36** The Pitman Estimator of Scale is given by
> $$
> d_P^r(\mathbf X)=\frac{\int_0^\infty t^{n+r-1}\prod_{i=1}^nf(tx_i)dt}{\int_0^\infty t^{n+2r-1}\prod_{i=1}^nf(tx_i)dt},
> $$
> where we observe a random sample $X_1,\ldots,X_n$ from $\frac1\sigma f(x/\sigma)$. Pitman showed that this estimator is the scale-equivariant estimator of $\sigma^r$ with smallest scaled mean squared error (that is, it minimizes $E(d-\sigma^r)^2/\sigma^{2r}$).
>
> (a) Show that $d_P^r(\mathbf X)$ is equivariant with respect to the scale group, that is, it satisfies
> $$
> d_P^r(cx_1,\ldots,cx_n)=c^r d_P^r(x_1,\ldots,x_n),
> $$
> for any constant $c>0$.
>
> (b) Find the Pitman scale-equivariant estimator for $\sigma^2$ if $X_1,\ldots,X_n$ are iid $n(0,\sigma^2)$.
>
> (c) Find the Pitman scale-equivariant estimator for $\beta$ if $X_1,\ldots,X_n$ are iid exponential$(\beta)$.
>
> (d) Find the Pitman scale-equivariant estimator for $\theta$ if $X_1,\ldots,X_n$ are iid uniform$(0,\theta)$.

### 中文转述

> [!question] 中文转述
> **原题7.36。** Pitman尺度估计量（Pitman estimator of scale）为
>
> $$
> d_P^r(\boldsymbol X)=\frac{\int_0^\infty t^{n+r-1}\prod_{i=1}^nf(tx_i)\,dt}{\int_0^\infty t^{n+2r-1}\prod_{i=1}^nf(tx_i)\,dt},
> $$
>
> 其中观测到来自$\frac1\sigma f(x/\sigma)$的随机样本$X_1,\ldots,X_n$.Pitman说明，它是估计$\sigma^r$的尺度等变估计量中，尺度化均方误差最小者（即使$E(d-\sigma^r)^2/\sigma^{2r}$最小）.
>
> (a)  说明$d_P^r(\boldsymbol X)$关于尺度群等变，即对任意常数$c>0$满足
>
> $$
> d_P^r(cx_1,\ldots,cx_n)=c^rd_P^r(x_1,\ldots,x_n).
> $$
>
> (b)  若$X_1,\ldots,X_n$独立同分布于$n(0,\sigma^2)$，求$\sigma^2$的Pitman尺度等变估计量.
>
> (c)  若$X_1,\ldots,X_n$独立同分布于$\operatorname{exponential}(\beta)$，求$\beta$的Pitman尺度等变估计量.
>
> (d)  若$X_1,\ldots,X_n$独立同分布于$\operatorname{uniform}(0,\theta)$，求$\theta$的Pitman尺度等变估计量.

## 提示

> [!hint]- 提示
> 缩放时积分变量作反向缩放；各实例都化为Gamma积分或幂积分。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 假定两个积分有限、分母正；以下指定例子中除零概率退化样本外均满足。
>
> **(a)** 在缩放数据的两个积分中令$u=ct$。分子乘$c^{-(n+r)}$，分母乘$c^{-(n+2r)}$，比值因此乘$c^r$。
>
> **(b)** $r=2$，标准正态核的乘积与$e^{-Qt^2/2}$成正比，$Q=\sum_i x_i^2>0$。利用
> $$
> \int_0^\infty t^{a-1}e^{-Qt^2/2}dt=\frac12(2/Q)^{a/2}\Gamma(a/2),
> $$
> 分子取$a=n+2$、分母取$a=n+4$，比值为$(Q/2)\Gamma((n+2)/2)/\Gamma((n+4)/2)=Q/(n+2)$。
>
> **(c)** $r=1$、正数据总和$S=\sum_i x_i$，标准指数核乘积为$e^{-St}$。分子积分为$\Gamma(n+1)/S^{n+1}$，分母为$\Gamma(n+2)/S^{n+2}$，故$\widehat\beta_P=S/(n+1)$。
>
> **(d)** $r=1$，标准均匀核乘积为$\mathbf1\{0<t<1/M\}$，$M=\max_i x_i>0$。分子$\int_0^{1/M}t^n dt=(1/M)^{n+1}/(n+1)$，分母$\int_0^{1/M}t^{n+1}dt=(1/M)^{n+2}/(n+2)$，比值为$(n+2)M/(n+1)$。这些规则针对原题的缩放平方风险，通常有偏，不等同于最佳无偏估计。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=324|印刷第293页／PDF物理第324页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 英文原文、中文转述与本库独立解答分别保留；实际核对正文位置列于`source_refs`。题内文献引用不表示已查阅其原文。`source_status: verified`只指本题及所列位置的核对范围，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
