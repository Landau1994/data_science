---
title: "习题 ST220：Cauchy尺度的绝对值充分约简与MLR"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第8章习题8.30，印刷页330／PDF物理页361"
source_id: "DS011"
source_chapter: 8
source_exercise: "8.30"
source_stars: 0
source_refs: ["DS011 Exercise 8.30，印刷页330／PDF物理页361"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST220：Cauchy尺度的绝对值充分约简与MLR

## 题目

### 英文原题

> [!question] 英文原题
> **8.30** Let $f(x\mid\theta)$ be the Cauchy scale pdf
> $$f(x\mid\theta)=\frac\theta\pi\frac1{\theta^2+x^2},\qquad-\infty<x<\infty,\quad\theta>0.$$
> (a) Show that this family does not have an MLR.
> (b) If $X$ is one observation from $f(x\mid\theta)$, show that $|X|$ is sufficient for $\theta$, and that the distribution of $|X|$ does have an MLR.

### 中文转述

> [!question] 中文转述
> **原题8.30。**
> 设 $f(x\mid\theta)$ 是 Cauchy 尺度密度
>
> $$
> f(x\mid\theta)=\frac\theta\pi\frac1{\theta^2+x^2},\qquad-\infty<x<\infty,\quad\theta>0.
> $$
>
> (a)  证明此族没有单调似然比.
>
> (b)  若 $X$ 是来自 $f(x\mid\theta)$ 的一次观测，证明 $|X|$ 对 $\theta$ 充分，且 $|X|$ 的分布确实具有单调似然比.

## 提示

> [!hint]- 提示
> 原坐标的似然比关于0对称，绝对值坐标只保留递增半轴。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** (a) 对$\theta_2>\theta_1>0$，比值$r(x)=(\theta_2/\theta_1)(\theta_1^2+x^2)/(\theta_2^2+x^2)$，在$x<0$递减、$x>0$递增且非常量，所以原$x$轴没有MLR。
> (b) 密度只通过$|x|$依赖参数，因子分解即给充分性；也可看给定$|X|=t>0$后符号独立公平，不含参数。$T=|X|$密度为$g_\theta(t)=2\theta/[\pi(\theta^2+t^2)]$，$t>0$。两比值与(a)相同但限制$t>0$，导数为正常数乘$t(\theta_2^2-\theta_1^2)/(\theta_2^2+t^2)^2>0$，故$T$族具有非减MLR。这不矛盾，因为MLR取决于所选统计量的次序。

## 相关概念

- [[02 - 数理统计/概念/假设检验|假设检验（hypothesis testing）]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[01 - 概率论/概念/条件概率|条件概率]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 完整原题已逐页对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=361|印刷330／PDF物理361]]；原题无星号。教材信息及归档进度见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 充分性先修：[[02 - 数理统计/概念/充分统计量|充分统计量]]。
- 来源已核对与独立解答写成不等于个人已完成练习；学习状态保留`not-started`。未实测Obsidian界面渲染。
