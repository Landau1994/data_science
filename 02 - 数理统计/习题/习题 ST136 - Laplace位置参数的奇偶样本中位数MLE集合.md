---
title: "习题 ST136：Laplace位置参数的奇偶样本中位数MLE集合"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第7章习题7.13，印刷页288／PDF物理页319"
source_id: "DS011"
source_chapter: 7
source_exercise: "7.13"
source_stars: 0
source_refs: ["DS011 Exercise 7.13，印刷288／PDF物理319"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST136：Laplace位置参数的奇偶样本中位数MLE集合

## 题目

### 英文原题

> [!question] 英文原题
> **7.13** Let $X_1,\ldots,X_n$ be a sample from a population with double exponential pdf
> $$
> f(x\mid\theta)=\frac12e^{-|x-\theta|},\qquad-\infty<x<\infty,\quad-\infty<\theta<\infty.
> $$
> Find the MLE of $\theta$. [Hint: Consider the case of even $n$ separate from that of odd $n$, and find the MLE in terms of the order statistics. A complete treatment of this problem is given in Norton (1984).]

### 中文转述

> [!question] 中文转述
> **原题7.13。** 设$X_1,\ldots,X_n$为来自双指数pdf总体的样本：
>
> $$
> f(x\mid\theta)=\frac12e^{-|x-\theta|},\qquad-\infty<x<\infty,\quad-\infty<\theta<\infty.
> $$
>
> 求$\theta$的MLE.［提示：分别考虑$n$为偶数和奇数的情形，用次序统计量表示MLE.Norton（1984）给出了此问题的完整处理.］

## 提示

> [!hint]- 提示
> 原题提示：把奇数样本和偶数样本分开，利用次序统计量。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 最大化$2^{-n}\exp[-\sum_i|x_i-\theta|]$等价于最小化$A(\theta)=\sum_i|x_i-\theta|$。在没有观测点的区间，导数为“左侧点数减右侧点数”；在观测点可用左右导数。凸函数最小的充要条件是左导数不大于0、右导数不小于0，即至少一半观测不大于$\theta$且至少一半不小于$\theta$。
>
> 若$n=2m+1$，唯一最小点是$x_{(m+1)}$。若$n=2m$，整个闭区间$[x_{(m)},x_{(m+1)}]$内左右各有$m$点，目标恒定，区间外目标增加，故MLE集合正是此区间。中间两数相等时区间退化为一点。通常样本中位数采用两者平均，是其中一个MLE，但不能漏掉其他并列解。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=319|印刷第288页／PDF物理第319页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 英文原文、中文转述与本库独立解答分别保留；实际核对正文位置列于`source_refs`。题内文献引用不表示已查阅其原文。`source_status: verified`只指本题及所列位置的核对范围，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
