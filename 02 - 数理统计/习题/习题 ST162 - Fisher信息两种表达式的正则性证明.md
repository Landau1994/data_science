---
title: "习题 ST162：Fisher信息两种表达式的正则性证明"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第7章习题7.39，印刷页294／PDF物理页325"
source_id: "DS011"
source_chapter: 7
source_exercise: "7.39"
source_stars: 0
source_refs: ["DS011 Exercise 7.39，印刷294／PDF物理325", "DS011 引理7.3.11完整陈述及求导条件，印刷274／PDF物理305"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST162：Fisher信息两种表达式的正则性证明

## 题目

### 英文原题

> [!question] 英文原题
> **7.39** Prove Lemma 7.3.11.

### 中文转述

> [!question] 中文转述
> **原题7.39。** 证明引理7.3.11.

## 提示

> [!hint]- 提示
> 对得分期望零再求一次导数，记住概率密度本身也随参数变。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 引理的目标是$E_\theta[(\partial_\theta\log f(X\mid\theta))^2]=-E_\theta[\partial_\theta^2\log f(X\mid\theta)]$。明确假设支持不依赖参数、参数在内点，$f$在正密度支持两次可微，并可在归一化积分及得分期望中交换求导；例如邻域内一、二阶密度导数受可积函数控制。所用期望须存在。
>
> 令得分$S_\theta(x)=\partial_\theta\log f(x\mid\theta)$。先由归一化得到
> $$
> E_\theta S_\theta=\int\partial_\theta f(x\mid\theta)dx
> =\partial_\theta\int f(x\mid\theta)dx=0.
> $$
> 再使用引理所列的求导交换条件，
> $$
> 0=\partial_\theta E_\theta S_\theta
> =\int\partial_\theta[S_\theta(x)f(x\mid\theta)]dx
> =E_\theta[\partial_\theta S_\theta]+E_\theta[S_\theta^2],
> $$
> 其中$\partial_\theta f=fS_\theta$。移项即得结论。离散分布把积分换成求和，需同样可交换条件。
>
> 支持依赖参数时不能忽略边界：例如Uniform$(0,\theta)$在内部$S=-1/\theta$，$ES=-1/\theta\ne0$，且$ES^2=1/\theta^2$、$-E\partial_\theta S=-1/\theta^2$不相等。因而“指数族成立”指正则、共同支持、参数内点的适用情形，不能只看代数上像指数形式。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=325|印刷第294页／PDF物理第325页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 英文原文、中文转述与本库独立解答分别保留；实际核对正文位置列于`source_refs`。题内文献引用不表示已查阅其原文。`source_status: verified`只指本题及所列位置的核对范围，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
