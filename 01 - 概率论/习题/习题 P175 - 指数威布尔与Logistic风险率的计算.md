---
title: "习题 P175：指数威布尔与Logistic风险率的计算"
topic: "probability-theory"
topic_label: "概率论"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "probability-theory"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第3章习题3.26，印刷页108／PDF物理页139"
source_id: "DS011"
source_chapter: 3
source_exercise: "3.26"
source_stars: 0
source_refs: ["DS011 Exercise 3.26，印刷108／PDF物理139", "DS011 Weibull密度式(3.3.12)及参数顺序，印刷83／PDF物理114"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 P175：指数威布尔与Logistic风险率的计算

## 题目

### 英文原题

> [!question] 英文原题
> **3.26** Verify that the following pdfs have the indicated hazard functions (see Exercise 3.25).
>
> (a) If $T\sim\operatorname{exponential}(\beta)$, then $h_T(t)=1/\beta$.
>
> (b) If $T\sim\operatorname{Weibull}(\gamma,\beta)$, then $h_T(t)=(\gamma/\beta)t^{\gamma-1}$.
>
> (c) If $T\sim\operatorname{logistic}(\mu,\beta)$, that is,
> $$
> F_T(t)=\frac1{1+e^{-(t-\mu)/\beta}},
> $$
> then $h_T(t)=(1/\beta)F_T(t)$.

### 中文转述

> [!question] 中文转述
> **原题3.26。** 验证下列pdf具有所给出的风险函数（见习题3.25）.
>
> (a)  若$T\sim\operatorname{exponential}(\beta)$，则$h_T(t)=1/\beta$.
>
> (b)  若$T\sim\operatorname{Weibull}(\gamma,\beta)$，则$h_T(t)=(\gamma/\beta)t^{\gamma-1}$.
>
> (c)  若$T\sim\operatorname{logistic}(\mu,\beta)$，即
>
> $$
> F_T(t)=\frac1{1+e^{-(t-\mu)/\beta}},
> $$
>
> 则$h_T(t)=(1/\beta)F_T(t)$.

## 提示

> [!hint]- 提示
> 每题先写生存函数，消去共同指数因子。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 在密度存在且生存概率为正处使用$h=f/(1-F)$，参数尺度均为正。
>
> **(a)** $t>0$时生存函数$S(t)=e^{-t/\beta}$、密度$S(t)/\beta$，故$h=1/\beta$。
>
> **(b)** 依习题3.24(a)的参数化，$S(t)=e^{-t^\gamma/\beta}$，$f(t)=(\gamma/\beta)t^{\gamma-1}S(t)$，所以$h=(\gamma/\beta)t^{\gamma-1}$，$t>0$。$\gamma<1$时在0附近风险率无界不违反概率公理。
>
> **(c)** 令$F$为给定Logistic CDF，求导得$f(t)=F(t)(1-F(t))/\beta$，故$h(t)=F(t)/\beta$，$t\in\mathbb R$。Logistic支持包括负数，若把它作为真正非负寿命模型还需截断或改模型；本题只是给定分布的数学风险率。

## 相关概念

- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/期望|期望]]
- [[01 - 概率论/概念/概率模型|概率模型]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=139|印刷第108页／PDF物理第139页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 英文原文、中文转述与本库独立解答分别保留；所用正文实际核对位置列于`source_refs`。题内文献只保留原题引用，不表示已查阅原文献。`source_status: verified`只指本题及所列位置核对，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
