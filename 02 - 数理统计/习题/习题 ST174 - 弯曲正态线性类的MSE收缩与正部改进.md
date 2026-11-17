---
title: "习题 ST174：弯曲正态线性类的MSE收缩与正部改进"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "advanced"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第7章习题7.51，印刷页295／PDF物理页326"
source_id: "DS011"
source_chapter: 7
source_exercise: "7.51"
source_stars: 0
source_refs: ["DS011 Exercise 7.51，印刷295／PDF物理326"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST174：弯曲正态线性类的MSE收缩与正部改进

## 题目

### 英文原题

> [!question] 英文原题
> **7.51** Gleser and Healy (1976) give a detailed treatment of the estimation problem in the $n(\theta,a\theta^2)$ family, where $a$ is a known constant (of which Exercise 7.50 is a special case). We explore a small part of their results here. Again, let $X_1,\ldots,X_n$ be iid $n(\theta,\theta^2)$, $\theta>0$, and let $\bar X$ and $cS$ be as in Exercise 7.46. Define the class of estimators
> $$
> \mathcal T=\{T:T=a_1\bar X+a_2(cS)\},
> $$
> where we do not assume that $a_1+a_2=1$.
>
> (a) Find the estimator $T\in\mathcal T$ that minimizes $E_\theta(\theta-T)^2$, call it $T^*$.
>
> (b) Show that the MSE of $T^*$ is smaller than the MSE of the estimator derived in Exercise 7.50b.
>
> (c) Show that the MSE of $T^{*+}=\max\{0,T^*\}$ is smaller than the MSE of $T^*$.
>
> (d) Would $\theta$ be classified as a location parameter or a scale parameter? Explain.

### 中文转述

> [!question] 中文转述
> **原题7.51。** Gleser和Healy（1976）详细讨论了$n(\theta,a\theta^2)$族中的估计问题，其中$a$是已知常数（习题7.50是其特殊情形）.这里考察他们结果的一小部分.仍设$X_1,\ldots,X_n$独立同分布于$n(\theta,\theta^2)$，$\theta>0$，令$\bar X$与$cS$如习题7.46.定义估计量类
>
> $$
> \mathcal T=\{T:T=a_1\bar X+a_2(cS)\},
> $$
>
> 其中不假设$a_1+a_2=1$.
>
> (a)  求使$E_\theta(\theta-T)^2$最小的估计量$T\in\mathcal T$，记为$T^*$.
>
> (b)  说明$T^*$的MSE小于习题7.50(b)所得估计量的MSE.
>
> (c)  说明$T^{*+}=\max\{0,T^*\}$的MSE小于$T^*$的MSE.
>
> (d)  $\theta$应归为位置参数还是尺度参数？解释理由.

## 提示

> [!hint]- 提示
> 解除无偏约束后最优规则是无偏最佳线性组合的进一步收缩。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 原题引用7.46应为7.50。对$n\ge2$，取$c=\sqrt{n-1}\Gamma((n-1)/2)/[\sqrt2\Gamma(n/2)]$、$d=c^2-1>0$。由正态样本性质，$\bar X$与$cS$独立、均值均为$\theta$，方差分别$\theta^2/n$、$d\theta^2$。
>
> **(a)** 精确风险为
> $$
> \frac{E_\theta(T-\theta)^2}{\theta^2}=(a_1+a_2-1)^2+a_1^2/n+d a_2^2.
> $$
> 它为严格凸二次式。令两偏导为0，得$a_1+a_2-1=-a_1/n=-d a_2$，所以
> $$
> a_1^*=\frac{nd}{1+(n+1)d},\qquad a_2^*=\frac1{1+(n+1)d},\qquad
> \operatorname{MSE}T^*=\frac{d}{1+(n+1)d}\theta^2.
> $$
> 系数仅依赖$n$，因此同一规则在全部$\theta$同时为该线性类的最优者。
>
> **(b)** 7.50(b)最佳无偏线性组合为$T_0=[nd\bar X+cS]/(1+nd)$，MSE为$v\theta^2$，$v=d/(1+nd)>0$。本题$T^*=T_0/(1+v)$，其MSE为$v\theta^2/(1+v)<v\theta^2$。改进来自允许偏差后的收缩，未声称它对所有可能估计量全局最优。
>
> **(c)** 对真实$\theta>0$，若$T^*<0$，则$(0-\theta)^2<(T^*-\theta)^2$；若$T^*\ge0$两损失相同。由于$a_1^*>0$、$\bar X$为全实轴正态，且独立的$S$在正数区间有正密度，事件$T^*<0$有正概率，因此积分后MSE严格减小。二阶矩有限，比较合法。
>
> **(d)** $X_i=\theta Z_i$，$Z_i\sim n(1,1)$不依赖$\theta$，且$\theta>0$，所以它是尺度参数（scale parameter）。虽然均值也随$\theta$变化，平移$X_i$不会保持方差与均值平方的同一关系，故不是纯位置族。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=326|印刷第295页／PDF物理第326页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 原题误引Exercise 7.46照录；解答明确采用7.50的c与模型。
- 英文原文、中文转述与本库独立解答分别保留；实际核对正文位置列于`source_refs`。题内文献引用不表示已查阅其原文。`source_status: verified`只指本题及所列位置的核对范围，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
