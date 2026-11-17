---
title: "习题 ST215：正态Poisson与二项族的单调似然比"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "beginner"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第8章习题8.25，印刷页329／PDF物理页360"
source_id: "DS011"
source_chapter: 8
source_exercise: "8.25"
source_stars: 0
source_refs: ["DS011 Exercise 8.25，印刷页329／PDF物理页360"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST215：正态Poisson与二项族的单调似然比

## 题目

### 英文原题

> [!question] 英文原题
> **8.25** Show that each of the following families has an MLR.
> (a) n$(\theta,\sigma^2)$ family with $\sigma^2$ known
> (b) Poisson$(\theta)$ family
> (c) binomial$(n,\theta)$ family with $n$ known

### 中文转述

> [!question] 中文转述
> **原题8.25。**
> 证明下列各族均具有单调似然比：
>
> (a)  $\sigma^2$ 已知的 $\mathrm n(\theta,\sigma^2)$ 族；
>
> (b)  $\operatorname{Poisson}(\theta)$ 族；
>
> (c)  $n$ 已知的 $\operatorname{binomial}(n,\theta)$ 族.

## 提示

> [!hint]- 提示
> 固定$\theta_2>\theta_1$，把比值写为常数乘随观察值递增的指数。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** (a) $\sigma^2>0$已知时，$f_{\theta_2}(x)/f_{\theta_1}(x)=\exp\{(\theta_2-\theta_1)x/\sigma^2-(\theta_2^2-\theta_1^2)/(2\sigma^2)\}$，关于$x$严格递增。
> (b) 对$0<\theta_1<\theta_2$，比值$e^{-(\theta_2-\theta_1)}(\theta_2/\theta_1)^x$在整数$x\ge0$递增。参数0的边界通过其点质量及无穷比值约定处理。
> (c) 对$0<\theta_1<\theta_2<1$，比值$[(1-\theta_2)/(1-\theta_1)]^n[\theta_2(1-\theta_1)/(\theta_1(1-\theta_2))]^x$，方括号底数大于1，因此递增；边界0、1作退化分布极限。三者都给出方向一致的非减MLR。

## 相关概念

- [[02 - 数理统计/概念/假设检验|假设检验（hypothesis testing）]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[01 - 概率论/概念/条件概率|条件概率]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 完整原题已逐页对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=360|印刷329／PDF物理360]]；原题无星号。教材信息及归档进度见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 来源已核对与独立解答写成不等于个人已完成练习；学习状态保留`not-started`。未实测Obsidian界面渲染。
