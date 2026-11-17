---
title: "习题 P169：半正态分布的矩与平方Gamma变换"
topic: "probability-theory"
topic_label: "概率论"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "probability-theory"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第3章习题3.20，印刷页107／PDF物理页138"
source_id: "DS011"
source_chapter: 3
source_exercise: "3.20"
source_stars: 0
source_refs: ["DS011 Exercise 3.20，印刷107／PDF物理138", "DS011 Gamma尺度参数化，印刷81／PDF物理112"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 P169：半正态分布的矩与平方Gamma变换

## 题目

### 英文原题

> [!question] 英文原题
> **3.20** Let the random variable $X$ have the pdf
> $$
> f(x)=\frac2{\sqrt{2\pi}}e^{-x^2/2},\qquad0<x<\infty.
> $$
> (a) Find the mean and variance of $X$. (This distribution is sometimes called a folded normal.)
>
> (b) If $X$ has the folded normal distribution, find the transformation $g(X)=Y$, and values of $\alpha$ and $\beta$, so that $Y\sim\operatorname{gamma}(\alpha,\beta)$.

### 中文转述

> [!question] 中文转述
> **原题3.20。** 设随机变量$X$具有pdf
>
> $$
> f(x)=\frac2{\sqrt{2\pi}}e^{-x^2/2},\qquad0<x<\infty.
> $$
>
> (a)  求$X$的均值和方差. （这个分布有时称为折叠正态分布，folded normal.）
>
> (b)  若$X$具有折叠正态分布，求变换$g(X)=Y$及$\alpha,\beta$的值，使$Y\sim\operatorname{gamma}(\alpha,\beta)$.

## 提示

> [!hint]- 提示
> 用x²/2换元求一阶矩；平方变量的Jacobian带入y^-1/2。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** **(a)** 换元$u=x^2/2$给
> $$
> EX=\sqrt{2/\pi}\int_0^\infty xe^{-x^2/2}dx=\sqrt{2/\pi}.
> $$
> 利用对称标准正态的二阶矩，或对$\int_0^\infty x^2e^{-x^2/2}dx$分部积分，得到$EX^2=1$，故$\operatorname{Var}X=1-2/\pi$。
>
> **(b)** 取$Y=X^2$。$x=\sqrt y$、Jacobian为$1/(2\sqrt y)$，于是
> $$
> f_Y(y)=\frac1{\sqrt{2\pi}}y^{-1/2}e^{-y/2},\quad y>0,
> $$
> 与形状$\alpha=1/2$、尺度$\beta=2$的Gamma密度相同。此题是均值0基础正态的绝对值，即半正态；一般非零均值的折叠正态不能照用这两个矩。

## 相关概念

- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/期望|期望]]
- [[01 - 概率论/概念/概率模型|概率模型]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=138|印刷第107页／PDF物理第138页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 英文原文、中文转述与本库独立解答分别保留；所用正文实际核对位置列于`source_refs`。题内文献只保留原题引用，不表示已查阅原文献。`source_status: verified`只指本题及所列位置核对，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
