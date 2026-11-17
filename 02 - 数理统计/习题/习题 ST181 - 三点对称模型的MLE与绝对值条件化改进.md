---
title: "习题 ST181：三点对称模型的MLE与绝对值条件化改进"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第7章习题7.58，印刷页296／PDF物理页327"
source_id: "DS011"
source_chapter: 7
source_exercise: "7.58"
source_stars: 0
source_refs: ["DS011 Exercise 7.58，印刷296／PDF物理327"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST181：三点对称模型的MLE与绝对值条件化改进

## 题目

### 英文原题

> [!question] 英文原题
> **7.58** Let $X$ be an observation from the pdf
> $$
> f(x\mid\theta)=\left(\frac\theta2\right)^{|x|}(1-\theta)^{1-|x|},\qquad x=-1,0,1;\quad0\le\theta\le1.
> $$
> (a) Find the MLE of $\theta$.
>
> (b) Define the estimator $T(X)$ by
> $$
> T(X)=\begin{cases}2&\text{if }x=1\\0&\text{otherwise}.\end{cases}
> $$
> Show that $T(X)$ is an unbiased estimator of $\theta$.
>
> (c) Find a better estimator than $T(X)$ and prove that it is better.

### 中文转述

> [!question] 中文转述
> **原题7.58。** 设$X$是来自下列pdf的一个观测：
>
> $$
> f(x\mid\theta)=\left(\frac\theta2\right)^{|x|}(1-\theta)^{1-|x|},\qquad x=-1,0,1;\quad0\le\theta\le1.
> $$
>
> (a)  求$\theta$的MLE.
>
> (b)  定义估计量$T(X)$为
>
> $$
> T(X)=\begin{cases}2&\text{若 }x=1,\\0&\text{其他情形}.\end{cases}
> $$
>
> 说明$T(X)$是$\theta$的无偏估计量.
>
> (c)  求一个优于$T(X)$的估计量，并证明它更好.

## 提示

> [!hint]- 提示
> 观测符号在给定绝对值后等概率；它只增加无偏估计的噪声。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 分布实际是pmf：$P(X=0)=1-\theta$、$P(X=\pm1)=\theta/2$。
>
> **(a)** 当$x=0$时似然$1-\theta$在0最大；当$x=\pm1$时似然$\theta/2$在1最大。因此$\widehat\theta=|X|$。
>
> **(b)** $ET=2P(X=1)=\theta$，$ET^2=4P(X=1)=2\theta$，故$\operatorname{Var}T=2\theta-\theta^2$。
>
> **(c)** $U=|X|\sim\operatorname{Bernoulli}(\theta)$，因此$EU=\theta$、$\operatorname{Var}U=\theta(1-\theta)$，严格少$\theta$；对$\theta>0$严格改善，$\theta=0$时相同。也可见$E(T\mid|X|=1)=1$、$E(T\mid|X|=0)=0$，这正是条件化去掉对称符号噪声。$|X|$充分，Bernoulli族完备：$(1-\theta)h(0)+\theta h(1)=0$对所有$\theta$迫使两值均0，所以这个改进估计还为最佳无偏。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=327|印刷第296页／PDF物理第327页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 原题将离散pmf称作pdf照录；严格改进的退化端点另行说明。
- 英文原文、中文转述与本库独立解答分别保留；实际核对正文位置列于`source_refs`。题内文献引用不表示已查阅其原文。`source_status: verified`只指本题及所列位置的核对范围，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
