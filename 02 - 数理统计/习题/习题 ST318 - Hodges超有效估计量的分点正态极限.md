---
title: 习题 ST318：Hodges超有效估计量的分点正态极限
topic: mathematical-statistics
topic_label: 数理统计
difficulty: intermediate
status: not-started
tags:
- exercise
- mathematical-statistics
source: George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第10章习题10.12，印刷页409／PDF物理页440
source_id: DS011
source_chapter: 10
source_exercise: '10.12'
source_stars: 0
source_refs:
- DS011 Exercise 10.12，印刷409／PDF物理440
- DS011题内依赖核对：印刷417／PDF物理448
source_status: verified
solution_status: independently-derived
created: '2026-11-13'
---

# 习题 ST318：Hodges超有效估计量的分点正态极限

## 题目

### 英文原题

> [!question] 英文原题
> **10.12** Verify that the superefficient estimator $d_n$ of Miscellanea 10.6.1 is asymptotically normal with variance $v(\theta)=1$ when $\theta\ne0$ and $v(\theta)=a^2$ when $\theta=0$. (See Lehmann and Casella 1998, Section 6.2, for more on superefficient estimators.)

### 中文转述

> [!question] 中文转述
> **原题10.12。** 验证杂录10.6.1的超有效估计量$d_n$渐近正态，其方差在$\theta\ne0$时为$v(\theta)=1$，在$\theta=0$时为$v(\theta)=a^2$. （超有效估计量的更多内容见Lehmann和Casella，1998，第6.2节.）

### 题内引用与条件

杂录10.6.1给$X_i\sim N(\theta,1)$和上述阈值估计量，讨论在$\theta=0$处的超有效性。

## 提示

> [!hint]- 提示
> θ≠0时阈值区间最终不包含真值；θ=0时√n乘阈值趋于无穷。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 模型$X_i\sim N(\theta,1)$ iid，原估计量
> $$
> d_n=\begin{cases}\bar X_n,&|\bar X_n|\ge n^{-1/4},\\a\bar X_n,&|\bar X_n|<n^{-1/4}.\end{cases}
> $$
> 若$\theta\ne0$，对足够大$n$有$n^{-1/4}<|\theta|/2$，所以$P(|\bar X_n|<n^{-1/4})\le P(|\bar X_n-\theta|>|\theta|/2)\to0$。因此$\sqrt n(d_n-\theta)$与$\sqrt n(\bar X_n-\theta)\sim N(0,1)$以趋于1的概率相等，得到极限$N(0,1)$。
>
> 若$\theta=0$，$\sqrt n\bar X_n\sim N(0,1)$，且$P(|\bar X_n|\ge n^{-1/4})=P(|Z|\ge n^{1/4})\to0$。故$\sqrt n d_n$与$a\sqrt n\bar X_n$以趋于1的概率相等，极限为$N(0,a^2)$。$a=0$时是退化0。超有效要求$|a|<1$，原杂录仅写$a<1$不足以保证$a^2<1$。这是每个固定$\theta$的点态结论，不是对接近0的局部参数序列统一优于均值的保证。

## 相关概念

- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/期望|期望]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[02 - 数理统计/概念/参数估计|参数估计]]

## 备注

- 来源：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=440|印刷第409页／PDF物理第440页]]；版本与归档见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 实读杂录10.6.1：印刷417／PDF448；原题所引外部文献未查阅。
- 已实读本题所用正文：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=448|印刷417／PDF物理448]]；其余题内外部文献仅保留原引用，未声称查阅。
- 英文原题逐题对照PDF原始页面，保留原分题、提示、引用及可见疑误；原题无星号。题内引用补充与独立解答不混入原文；未查阅答案册或题内外部文献。
- 来源核对不表示个人学习完成，学习状态保持not-started。公式、链接与元数据检查不等于Obsidian实际渲染检查。
