---
title: "习题 ST135：受限Bernoulli参数中截断最大似然的风险改进"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第7章习题7.12，印刷页288／PDF物理页319"
source_id: "DS011"
source_chapter: 7
source_exercise: "7.12"
source_stars: 0
source_refs: ["DS011 Exercise 7.12，印刷288／PDF物理319"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST135：受限Bernoulli参数中截断最大似然的风险改进

## 题目

### 英文原题

> [!question] 英文原题
> **7.12** Let $X_1,\ldots,X_n$ be a random sample from a population with pmf
> $$
> P_\theta(X=x)=\theta^x(1-\theta)^{1-x},\qquad x=0\text{ or }1,\quad0\le\theta\le\frac12.
> $$
> (a) Find the method of moments estimator and MLE of $\theta$.
>
> (b) Find the mean squared errors of each of the estimators.
>
> (c) Which estimator is preferred? Justify your choice.

### 中文转述

> [!question] 中文转述
> **原题7.12。** 设$X_1,\ldots,X_n$为来自具有下列pmf的总体的随机样本：
>
> $$
> P_\theta(X=x)=\theta^x(1-\theta)^{1-x},\qquad x=0\text{ 或 }1,\quad0\le\theta\le\frac12.
> $$
>
> (a)  求$\theta$的矩估计量和MLE.
>
> (b)  求两个估计量各自的均方误差.
>
> (c)  更倾向于哪个估计量？说明选择的理由.

## 提示

> [!hint]- 提示
> 将无约束估计投影到已知参数区间，逐样本比较平方误差。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 记$S=\sum_iX_i\sim\operatorname{binomial}(n,\theta)$。
>
> **(a)** 普通矩方程$EX=\theta$给$\widetilde\theta=S/n$。似然$\theta^S(1-\theta)^{n-S}$在无约束最大点$S/n$前增后降，约束MLE为$\widehat\theta=\min\{S/n,1/2\}$。普通矩估计可能落在参数空间外；若另把矩估计定义为约束投影，则它与此MLE相同，这一术语约定须说清。
>
> **(b)** $\widetilde\theta$无偏，故$\operatorname{MSE}_\theta(\widetilde\theta)=\theta(1-\theta)/n$。MLE的精确有限和为
> $$
> \operatorname{MSE}_\theta(\widehat\theta)=
> \sum_{s=0}^{\lfloor n/2\rfloor}(s/n-\theta)^2\binom ns\theta^s(1-\theta)^{n-s}
> +(1/2-\theta)^2\sum_{s=\lfloor n/2\rfloor+1}^{n}\binom ns\theta^s(1-\theta)^{n-s}.
> $$
> 等价地，它等于矩估计的风险减去
> $$
> \sum_{s>n/2}(s/n-1/2)(s/n+1/2-2\theta)\binom ns\theta^s(1-\theta)^{n-s}.
> $$
> **(c)** 对$\theta\in[0,1/2]$，截断前后的逐样本距离满足$|\min\{u,1/2\}-\theta|\le|u-\theta|$；$u>1/2$时严格。因此MLE在所有参数处MSE不大于普通矩估计；对$0<\theta\le1/2$，事件$S=n$有正概率，风险严格更小；$\theta=0$时均为零。平方损失下偏好MLE，理由是投影的逐点损失改进。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=319|印刷第288页／PDF物理第319页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 英文原文、中文转述与本库独立解答分别保留；实际核对正文位置列于`source_refs`。题内文献引用不表示已查阅其原文。`source_status: verified`只指本题及所列位置的核对范围，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
