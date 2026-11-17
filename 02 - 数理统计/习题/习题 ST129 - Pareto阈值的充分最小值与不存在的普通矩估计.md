---
title: "习题 ST129：Pareto阈值的充分最小值与不存在的普通矩估计"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第7章习题7.6，印刷页287／PDF物理页318"
source_id: "DS011"
source_chapter: 7
source_exercise: "7.6"
source_stars: 0
source_refs: ["DS011 Exercise 7.6，印刷287／PDF物理318"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST129：Pareto阈值的充分最小值与不存在的普通矩估计

## 题目

### 英文原题

> [!question] 英文原题
> **7.6** Let $X_1,\ldots,X_n$ be a random sample from the pdf
> $$
> f(x\mid\theta)=\theta x^{-2},\qquad0<\theta\le x<\infty.
> $$
> (a) What is a sufficient statistic for $\theta$?
>
> (b) Find the MLE of $\theta$.
>
> (c) Find the method of moments estimator of $\theta$.

### 中文转述

> [!question] 中文转述
> **原题7.6。** 设$X_1,\ldots,X_n$为来自下列pdf的随机样本：
>
> $$
> f(x\mid\theta)=\theta x^{-2},\qquad0<\theta\le x<\infty.
> $$
>
> (a)  $\theta$的充分统计量是什么？
>
> (b)  求$\theta$的MLE.
>
> (c)  求$\theta$的矩估计量.

## 提示

> [!hint]- 提示
> 先检查期望是否有限，再考虑矩估计方程。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** **(a)** 对正观测，联合密度分解为$\theta^n\mathbf1\{0<\theta\le X_{(1)}\}\prod_i x_i^{-2}$，由因子分解定理，$X_{(1)}=\min_iX_i$充分。
>
> **(b)** 在支持允许的$0<\theta\le x_{(1)}$内，$\theta^n$严格递增，故$\widehat\theta=X_{(1)}$。端点原题包含等号，最大值被取得。
>
> **(c)** $E_\theta X=\theta\int_\theta^\infty x^{-1}dx=\infty$，更高正整数矩亦发散；因此不能令$\bar X=E_\theta X$得到通常基于原始正整数矩的矩估计量（method of moments estimator）。这不是漏解，而是方法所需矩不存在。
>
> 若允许**广义矩方法**，则$E(1/X)=\theta\int_\theta^\infty x^{-3}dx=1/(2\theta)$，得到$\widetilde\theta=[2n^{-1}\sum_iX_i^{-1}]^{-1}$；也可用$E\log X=\log\theta+1$得到$\exp(n^{-1}\sum_i\log X_i-1)$。这些是明确更换矩函数后的替代方法，不能称为原始一阶矩估计。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=318|印刷第287页／PDF物理第318页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 普通原始矩不存在；给出的倒数矩与对数矩属于明确标记的广义矩方法。
- 英文原文、中文转述与本库独立解答分别保留；实际核对正文位置列于`source_refs`。题内文献引用不表示已查阅其原文。`source_status: verified`只指本题及所列位置的核对范围，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
