---
title: "习题 ST196：两独立指数样本尺度相等的Beta似然比检验"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第8章习题8.6，印刷页327／PDF物理页358"
source_id: "DS011"
source_chapter: 8
source_exercise: "8.6"
source_stars: 0
source_refs: ["DS011 Exercise 8.6，印刷页327／PDF物理页358", "DS011 所引正文，印刷83／PDF物理114"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST196：两独立指数样本尺度相等的Beta似然比检验

## 题目

### 英文原题

> [!question] 英文原题
> **8.6** Suppose that we have two independent random samples: $X_1,\ldots,X_n$ are exponential$(\theta)$, and $Y_1,\ldots,Y_m$ are exponential$(\mu)$.
> (a) Find the LRT of $H_0:\theta=\mu$ versus $H_1:\theta\ne\mu$.
> (b) Show that the test in part (a) can be based on the statistic
> $$T=\frac{\Sigma X_i}{\Sigma X_i+\Sigma Y_i}.$$
> (c) Find the distribution of $T$ when $H_0$ is true.

### 中文转述

> [!question] 中文转述
> **原题8.6。**
> 设有两个独立随机样本：$X_1,\ldots,X_n$ 来自 $\operatorname{exponential}(\theta)$，$Y_1,\ldots,Y_m$ 来自 $\operatorname{exponential}(\mu)$.
>
> (a)  求 $H_0:\theta=\mu$ 对 $H_1:\theta\ne\mu$ 的似然比检验.
>
> (b)  证明，(a) 中的检验可以基于统计量
>
> $$
> T=\frac{\sum X_i}{\sum X_i+\sum Y_i}.
> $$
>
> (c)  求 $H_0$ 为真时 $T$ 的分布.

## 提示

> [!hint]- 提示
> 本书指数参数为尺度；全样本均值是约束共同尺度估计。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 设$n,m\ge1$，$A=\sum X_i,B=\sum Y_i,N=n+m$，正尺度$\theta,\mu$。
> (a) 似然为$\theta^{-n}\mu^{-m}e^{-A/\theta-B/\mu}$。无约束MLE为$(A/n,B/m)$，原假设下共同MLE为$(A+B)/N$，所以
> $$\lambda=\frac{N^N}{n^nm^m}\frac{A^nB^m}{(A+B)^N}.$$
> 当此比值不超过临界常数$c$时拒绝。
> (b) 置$T=A/(A+B)$，得$\lambda=K T^n(1-T)^m$，$K=N^N/(n^nm^m)$。对数导数$n/T-m/(1-T)$在$n/N$两侧变号，故拒绝域为$T<a$或$T>b$，边界满足$K a^n(1-a)^m=K b^n(1-b)^m=c$。
> (c) 原假设下$A,B$独立Gamma$(n,\theta)$、Gamma$(m,\theta)$。换元总和$s=A+B$及比例$t$的Jacobian为$s$，联合密度分解为Gamma$(N,\theta)$密度乘$t^{n-1}(1-t)^{m-1}/B(n,m)$，故$T\sim\operatorname{Beta}(n,m)$。它不含干扰尺度，用$P(T<a)+P(T>b)=\alpha$及相同比值边界确定精确大小$\alpha$的LRT。

## 相关概念

- [[02 - 数理统计/概念/假设检验|假设检验（hypothesis testing）]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[01 - 概率论/概念/条件概率|条件概率]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 完整原题已逐页对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=358|印刷327／PDF物理358]]；原题无星号。教材信息及归档进度见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 引用输入实际核对页：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=114|印刷83／PDF物理114]]；解答已重述所需假设及结果。
- 来源已核对与独立解答写成不等于个人已完成练习；学习状态保留`not-started`。未实测Obsidian界面渲染。
