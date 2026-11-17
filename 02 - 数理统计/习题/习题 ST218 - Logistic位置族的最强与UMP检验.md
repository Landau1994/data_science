---
title: "习题 ST218：Logistic位置族的最强与UMP检验"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第8章习题8.28，印刷页329／PDF物理页360"
source_id: "DS011"
source_chapter: 8
source_exercise: "8.28"
source_stars: 0
source_refs: ["DS011 Exercise 8.28，印刷页329／PDF物理页360"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST218：Logistic位置族的最强与UMP检验

## 题目

### 英文原题

> [!question] 英文原题
> **8.28** Let $f(x\mid\theta)$ be the logistic location pdf
> $$f(x\mid\theta)=\frac{e^{(x-\theta)}}{(1+e^{(x-\theta)})^2},\qquad-\infty<x<\infty,\quad-\infty<\theta<\infty.$$
> (a) Show that this family has MLR.
> (b) Based on one observation, $X$, find the most powerful size $\alpha$ test of $H_0:\theta=0$ versus $H_1:\theta=1$. For $\alpha=.2$, find the size of the Type II Error.
> (c) Show that the test in part (b) is UMP size $\alpha$ for testing $H_0:\theta\le0$ versus $H_1:\theta>0$. What can be said about UMP tests in general for the logistic location family?

### 中文转述

> [!question] 中文转述
> **原题8.28。**
> 设 $f(x\mid\theta)$ 是 logistic 位置密度
>
> $$
> f(x\mid\theta)=\frac{e^{x-\theta}}{(1+e^{x-\theta})^2},\qquad-\infty<x<\infty,\quad-\infty<\theta<\infty.
> $$
>
> (a)  证明此族具有单调似然比.
>
> (b)  基于一次观测 $X$，求 $H_0:\theta=0$ 对 $H_1:\theta=1$ 的大小 $\alpha$ 最强检验. 当 $\alpha=.2$ 时，求第二类错误的大小.
>
> (c)  证明(b) 中的检验是 $H_0:\theta\le0$ 对 $H_1:\theta>0$ 的大小 $\alpha$ 一致最强检验. 对 logistic 位置族的一致最强检验，一般可以说些什么？

## 提示

> [!hint]- 提示
> 求CDF及两似然比对$x$的导数。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 令$L(u)=1/(1+e^{-u})$，则CDF为$L(x-\theta)$。
> (a) 对$\theta_2>\theta_1$，比值对数的$x$导数为$2[L(x-\theta_1)-L(x-\theta_2)]>0$，故MLR非减。
> (b) Neyman–Pearson检验拒绝$X>c$，由$1-L(c)=\alpha$得$c=\log[(1-\alpha)/\alpha]$。在$\theta=1$处第二类错误为$L(c-1)$；$\alpha=.2$时为$4/(e+4)\approx.59539$。
> (c) 对任意正备择参数，相对边界0的似然比均递增，且原假设上拒绝概率$1-L(c-\theta)$在0达到上确界$\alpha$，故同一规则UMP。一般单观测位置假设$\theta\le\theta_0$对$\theta>\theta_0$拒绝$X>\theta_0+\log[(1-\alpha)/\alpha]$；反向单侧用对应左尾也UMP。对$\theta=\theta_0$的双侧备择，$0<\alpha<1$时不存在无约束UMP：任一正备择的唯一最强上尾域与任一负备择的唯一最强下尾域不相同，无法由同一检验同时实现。这里一般结论限于本题单观测族，不自动声称多观测联合似然仅靠样本均值有同样MLR。

## 相关概念

- [[02 - 数理统计/概念/假设检验|假设检验（hypothesis testing）]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[01 - 概率论/概念/条件概率|条件概率]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 完整原题已逐页对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=360|印刷329／PDF物理360]]；原题无星号。教材信息及归档进度见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 来源已核对与独立解答写成不等于个人已完成练习；学习状态保留`not-started`。未实测Obsidian界面渲染。
