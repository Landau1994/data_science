---
title: "习题 ST357：BoxCox变换的连续极限与稳定方差族"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第11章习题11.3，印刷页456／PDF物理页487"
source_id: "DS011"
source_chapter: 11
source_exercise: "11.3"
source_stars: 0
source_refs: ["DS011 Exercise 11.3，印刷456／PDF物理487"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST357：BoxCox变换的连续极限与稳定方差族

## 题目

### 英文原题

> [!question] 英文原题
> **11.3** The Box–Cox family of power transformations (Box and Cox 1964) is defined by
> $$
> g_\lambda^*(y)=\begin{cases}(y^\lambda-1)/\lambda&\text{if }\lambda\ne0,\\\log y&\text{if }\lambda=0,\end{cases}
> $$
> where $\lambda$ is a free parameter.
>
> (a) Show that, for each $y$, $g_\lambda^*(y)$ is continuous in $\lambda$. In particular, show that
> $$
> \lim_{\lambda\to0}(y^\lambda-1)/\lambda=\log y.
> $$
> (b) Find the function $v(\theta)$, the approximate variance of $Y$, that $g_\lambda^*(y)$ stabilizes. (Note that $v(\theta)$ will most likely also depend on $\lambda$.)
>
> Analysis of transformed data in general, and the Box–Cox power transformation in particular, has been the topic of some controversy in the statistical literature. See Bickel and Doksum (1981), Box and Cox (1982), and Hinkley and Runger (1984).

### 中文转述

> [!question] 中文转述
> **原题11.3。** Box--Cox幂变换族（Box和Cox，1964）定义为
>
> $$
> g_\lambda^*(y)=\begin{cases}(y^\lambda-1)/\lambda,&\lambda\ne0,\\\log y,&\lambda=0,\end{cases}
> $$
>
> 其中$\lambda$为自由参数.
>
> (a)  证明，对每个$y$，$g_\lambda^*(y)$关于$\lambda$连续. 特别地，证明
>
> $$
> \lim_{\lambda\to0}(y^\lambda-1)/\lambda=\log y.
> $$
>
> (b)  求函数$v(\theta)$，即由$g_\lambda^*(y)$稳定的$Y$的近似方差. （注意$v(\theta)$很可能还依赖$\lambda$.）
>
> 变换后数据的分析，特别是Box--Cox幂变换，在统计文献中曾引起一些争论. 见Bickel和Doksum（1981）、Box和Cox（1982），以及Hinkley和Runger（1984）.

## 提示

> [!hint]- 提示
> 把$y^\lambda$写成指数函数；对$y$求导后反解方差函数。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 定义域取$y>0$，均值$\theta>0$。
>
> **(a)** 固定$y>0$，$y^\lambda=e^{\lambda\log y}$，所以$(e^{\lambda\log y}-1)/\lambda\to\log y$，包括$y=1$时两边均为0。在$\lambda\ne0$处由指数函数及商的连续性成立，因此分段定义在全部实数$\lambda$连续。也可写$g_\lambda^*(y)=\log y\int_0^1e^{s\lambda\log y}ds$，直接展示跨零连续性。
>
> **(b)** $\partial_y g_\lambda^*(y)=y^{\lambda-1}$，该式在$\lambda=0$也给$1/y$。若希望线性化后方差为任意正常数$C$，则要求$\theta^{2\lambda-2}v(\theta)=C$，即
> $$
> v(\theta)=C\theta^{2-2\lambda}.
> $$
> $\lambda=0$对应方差与均值平方成比例，$\lambda=1/2$对应方差与均值成比例，$\lambda=1$对应常方差。该关系指定的是被稳定的均值方差族；它不保证任意具有该均值方差关系的分布都满足良好的Taylor余项条件。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=487|印刷第456页／PDF物理第487页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 英文原文、中文转述与本库独立解答分别保留；实际核对正文位置列于`source_refs`。题内文献引用不表示已查阅其原文。`source_status: verified`只指本题及所列位置的核对范围，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
