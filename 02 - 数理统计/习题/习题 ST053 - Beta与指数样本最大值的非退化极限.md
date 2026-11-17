---
title: 习题 ST053：Beta与指数样本最大值的非退化极限
topic: mathematical-statistics
topic_label: 数理统计
difficulty: intermediate
status: not-started
tags:
- exercise
- mathematical-statistics
source: George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第5章习题5.42，印刷页214／PDF物理页245
source_id: DS011
source_chapter: 5
source_exercise: '5.42'
source_stars: 0
source_refs:
- DS011 Exercise 5.42，印刷214／PDF物理245
- DS011题内依赖核对：印刷192／PDF物理223
source_status: verified
solution_status: independently-derived
created: '2026-11-13'
---

# 习题 ST053：Beta与指数样本最大值的非退化极限

## 题目

### 英文原题

> [!question] 英文原题
> **5.42** Similar to Example 5.5.11, let $X_1,X_2,\ldots$ be iid $f$ and $X_{(n)}=\max_{1\le i\le n}X_i$.
>
> (a) If $f$ is beta$(1,\beta)$, find a value of $\nu$ so that $n^\nu(1-X_{(n)})$ converges in distribution.
>
> (b) If $f$ is exponential$(1)$, find a sequence $a_n$ so that $X_{(n)}-a_n$ converges in distribution.

### 中文转述

> [!question] 中文转述
> **原题5.42。** 类似例5.5.11，设$X_1,X_2,\ldots$为iid $f$，$X_{(n)}=\max_{1\le i\le n}X_i$.
>
> (a)  若$f$为$\operatorname{beta}(1,\beta)$，求使$n^\nu(1-X_{(n)})$依分布收敛的$\nu$.
>
> (b)  若$f$为$\operatorname{exponential}(1)$，求使$X_{(n)}-a_n$依分布收敛的序列$a_n$.

## 提示

> [!hint]- 提示
> 先写最大值CDF为F(x)^n，再找使尾概率是1/n量级的缩放。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** **(a)** $\beta>0$时$F(x)=1-(1-x)^\beta$，$0<x<1$。取$\nu=1/\beta$，对$t\ge0$，充分大$n$时
> $$
> P(n^{1/\beta}(1-X_{(n)})>t)=[1-t^\beta/n]^n\to e^{-t^\beta}.
> $$
> 故极限CDF在$t\ge0$为$1-e^{-t^\beta}$，在$t<0$为0，即形状$\beta$的Weibull分布。若$\nu<1/\beta$会退化到0，若$\nu>1/\beta$则逃向正无穷，因此所选值给非退化极限。
>
> **(b)** 指数尺度1的$F(x)=1-e^{-x}$。取$a_n=\log n$，对固定实$t$，充分大$n$时
> $$
> P(X_{(n)}-\log n\le t)=(1-e^{-t}/n)^n\to\exp(-e^{-t}),
> $$
> 即标准Gumbel分布。

## 相关概念

- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/期望|期望]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[02 - 数理统计/概念/参数估计|参数估计]]

## 备注

- 来源：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=245|印刷第214页／PDF物理第245页]]；版本与归档见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 已实读本题所用正文：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=223|印刷192／PDF物理223]]；其余题内外部文献仅保留原引用，未声称查阅。
- 英文原题逐题对照PDF原始页面，保留原分题、提示、引用及可见疑误；原题无星号。题内引用补充与独立解答不混入原文；未查阅答案册或题内外部文献。
- 来源核对不表示个人学习完成，学习状态保持not-started。公式、链接与元数据检查不等于Obsidian实际渲染检查。
