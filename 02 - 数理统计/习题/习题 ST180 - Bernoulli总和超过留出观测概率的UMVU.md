---
title: "习题 ST180：Bernoulli总和超过留出观测概率的UMVU"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第7章习题7.57，印刷页296／PDF物理页327"
source_id: "DS011"
source_chapter: 7
source_exercise: "7.57"
source_stars: 0
source_refs: ["DS011 Exercise 7.57，印刷296／PDF物理327"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST180：Bernoulli总和超过留出观测概率的UMVU

## 题目

### 英文原题

> [!question] 英文原题
> **7.57** Let $X_1,\ldots,X_{n+1}$ be iid Bernoulli$(p)$, and define the function $h(p)$ by
> $$
> h(p)=P\left(\sum_{i=1}^nX_i>X_{n+1}\mid p\right),
> $$
> the probability that the first $n$ observations exceed the $(n+1)$st.
>
> (a) Show that
> $$
> T(X_1,\ldots,X_{n+1})=\begin{cases}1&\text{if }\sum_{i=1}^nX_i>X_{n+1}\\0&\text{otherwise}\end{cases}
> $$
> is an unbiased estimator of $h(p)$.
>
> (b) Find the best unbiased estimator of $h(p)$.

### 中文转述

> [!question] 中文转述
> **原题7.57。** 设$X_1,\ldots,X_{n+1}$独立同分布于$\operatorname{Bernoulli}(p)$，定义函数$h(p)$为
>
> $$
> h(p)=P\left(\sum_{i=1}^nX_i>X_{n+1}\mid p\right),
> $$
>
> 即前$n$个观测值之和超过第$n+1$个观测值的概率.
>
> (a)  说明
>
> $$
> T(X_1,\ldots,X_{n+1})=\begin{cases}1&\text{若 }\sum_{i=1}^nX_i>X_{n+1},\\0&\text{其他情形}\end{cases}
> $$
>
> 是$h(p)$的无偏估计量.
>
> (b)  求$h(p)$的最佳无偏估计量.

## 提示

> [!hint]- 提示
> 给定全部n+1项的成功总数后，只需考虑最后一位是否为1。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** **(a)** $T$正是目标事件的指示变量，所以$E_pT=P_p(\sum_{i=1}^nX_i>X_{n+1})=h(p)$。例如按最后一位分解，$h(p)=1-(1-p)^n-np^2(1-p)^{n-1}$（$n\ge1$）。
>
> **(b)** 令$S=\sum_{i=1}^{n+1}X_i$，它为完备充分二项总数；完备性由把零期望除以$(1-p)^{n+1}$后得到零多项式而逐系数证明。事件可改写成$S>2X_{n+1}$。条件于$S=s$，$P(X_{n+1}=1\mid S=s)=s/(n+1)$，所以
> $$
> E(T\mid S=s)=\begin{cases}
> 0,&s=0,\\
> 1-s/(n+1),&s=1,2,\\
> 1,&3\le s\le n+1.
> \end{cases}
> $$
> 不存在的分段区间忽略；例如$n=1$时只有$s=0,1,2$，分别为0、1/2、0。该函数是Rao–Blackwell化的无偏估计，由完备性为唯一UMVU；在$p=0,1$端点按相应退化总数取值也成立。原题文字“前n个观测超过”须按显示式的**前n项之和**解释，而非每个都超过。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=327|印刷第296页／PDF物理第327页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 英文原文、中文转述与本库独立解答分别保留；实际核对正文位置列于`source_refs`。题内文献引用不表示已查阅其原文。`source_status: verified`只指本题及所列位置的核对范围，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
