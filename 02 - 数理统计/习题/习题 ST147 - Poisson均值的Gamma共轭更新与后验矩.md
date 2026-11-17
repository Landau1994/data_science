---
title: "习题 ST147：Poisson均值的Gamma共轭更新与后验矩"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第7章习题7.24，印刷页290／PDF物理页321"
source_id: "DS011"
source_chapter: 7
source_exercise: "7.24"
source_stars: 0
source_refs: ["DS011 Exercise 7.24，印刷290／PDF物理321", "DS011 Gamma尺度密度式(3.3.6)，印刷81／PDF物理112"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST147：Poisson均值的Gamma共轭更新与后验矩

## 题目

### 英文原题

> [!question] 英文原题
> **7.24** Let $X_1,\ldots,X_n$ be iid Poisson$(\lambda)$, and let $\lambda$ have a gamma$(\alpha,\beta)$ distribution, the conjugate family for the Poisson.
>
> (a) Find the posterior distribution of $\lambda$.
>
> (b) Calculate the posterior mean and variance.

### 中文转述

> [!question] 中文转述
> **原题7.24。** 设$X_1,\ldots,X_n$独立同分布于$\operatorname{Poisson}(\lambda)$，令$\lambda$服从Poisson分布的共轭族$\operatorname{gamma}(\alpha,\beta)$分布.
>
> (a)  求$\lambda$的后验分布.
>
> (b)  计算后验均值和方差.

## 提示

> [!hint]- 提示
> Poisson似然和Gamma先验分别贡献幂指数与指数衰减速率。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 本书Gamma的$\beta$是尺度。令$S=\sum_i x_i$。
>
> **(a)** 似然核为$\lambda^S e^{-n\lambda}$，先验核为$\lambda^{\alpha-1}e^{-\lambda/\beta}$。两者相乘给
> $$
> \pi(\lambda\mid\mathbf x)=\frac{B^A}{\Gamma(A)}\lambda^{A-1}e^{-B\lambda},
> \quad A=\alpha+S,\quad B=n+1/\beta,\quad\lambda>0.
> $$
> 归一化来自$\int_0^\infty\lambda^{A-1}e^{-B\lambda}d\lambda=\Gamma(A)/B^A$。所以后验为$\operatorname{gamma}(\alpha+S,\beta/(1+n\beta))$。
>
> **(b)** 同样用Gamma积分，$E\lambda=\Gamma(A+1)/[B\Gamma(A)]=A/B$，$E\lambda^2=A(A+1)/B^2$，因此
> $$
> E(\lambda\mid\mathbf x)=\frac{\alpha+S}{n+1/\beta},\qquad
> \operatorname{Var}(\lambda\mid\mathbf x)=\frac{\alpha+S}{(n+1/\beta)^2}.
> $$
> 先验$\alpha,\beta>0$使所有这些后验矩有限，包括全零数据。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=321|印刷第290页／PDF物理第321页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 英文原文、中文转述与本库独立解答分别保留；实际核对正文位置列于`source_refs`。题内文献引用不表示已查阅其原文。`source_status: verified`只指本题及所列位置的核对范围，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
