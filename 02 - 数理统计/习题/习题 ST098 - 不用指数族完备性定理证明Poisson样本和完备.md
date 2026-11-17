---
title: "习题 ST098：不用指数族完备性定理证明Poisson样本和完备"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第6章习题6.18，印刷页245／PDF物理页276"
source_id: "DS011"
source_chapter: 6
source_exercise: "6.18"
source_stars: 0
source_refs: ["DS011 Exercise 6.18，印刷245／PDF物理276"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST098：不用指数族完备性定理证明Poisson样本和完备

## 题目

### 英文原题

> [!question] 英文原题
> **6.18** Let $X_1,\ldots,X_n$ be iid Poisson$(\lambda)$. Show that the family of distributions of $\sum X_i$ is complete. Prove completeness without using Theorem 6.2.25.

### 中文转述

> [!question] 中文转述
> **原题6.18。**
> 设$X_1,\ldots,X_n$为iid $\operatorname{Poisson}(\lambda)$.说明$\sum X_i$的分布族完备.不用定理6.2.25证明其完备性.

## 提示

> [!hint]- 提示 1
> 把零期望等式乘以$e^{n\lambda}$，识别关于$n\lambda$的幂级数。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 教材输入与补充假设另行标明。
>
> 令$T=\sum_iX_i$。由独立Poisson变量卷积或概率生成函数相乘，$T\sim\operatorname{Poisson}(n\lambda)$。设$E_\lambda|g(T)|<\infty$、$E_\lambda g(T)=0$对所有$\lambda>0$成立，则
> $$
> 0=e^{n\lambda}E_\lambda g(T)
> =\sum_{t=0}^\infty g(t)\frac{(n\lambda)^t}{t!}.
> $$
> 任给$R>0$，取$\lambda>R/n$，绝对可积性说明右端幂级数在$|z|\le R$绝对收敛；因此它作为$z=n\lambda$的函数是整函数，并在正实轴恒为0。其Taylor系数只能全为0，即$g(t)/t!=0$。所以$g(t)=0$对每个非负整数成立，证明完备。若参数集另包含$\lambda=0$，此时$T=0$，也由$g(0)=0$覆盖。
>
> 也可避免整函数术语：幂级数在0邻域内为零，其各阶导数在0为0，逐项求导得到同样结论。这里明确使用幂级数唯一性，而非题目禁止调用的定理6.2.25。

## 相关概念

- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[01 - 概率论/概念/概率模型|概率模型]]

## 备注

- 统一来源见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011教材台账]]；原题位于[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=276|印刷245／PDF物理276]]。已对照原始页面核对完整英文、分题与定位，原题无星号。
- 解答为独立推导；引用的教材结论按source_refs核对，不使用答案册代替证明。
- 来源核对、归档与个人学习分别记录；verified只指所列来源核对范围，学习状态保持not-started。未实测Obsidian渲染。
