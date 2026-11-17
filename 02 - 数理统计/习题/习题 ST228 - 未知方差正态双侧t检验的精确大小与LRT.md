---
title: "习题 ST228：未知方差正态双侧t检验的精确大小与LRT"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第8章习题8.38，印刷页331／PDF物理页362"
source_id: "DS011"
source_chapter: 8
source_exercise: "8.38"
source_stars: 0
source_refs: ["DS011 Exercise 8.38，印刷页331／PDF物理页362"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST228：未知方差正态双侧t检验的精确大小与LRT

## 题目

### 英文原题

> [!question] 英文原题
> **8.38** Let $X_1,\ldots,X_n$ be iid n$(\theta,\sigma^2)$, where $\theta_0$ is a specified value of $\theta$, and $\sigma^2$ is unknown. We are interested in testing
> $$H_0:\theta=\theta_0\quad\text{versus}\quad H_1:\theta\ne\theta_0.$$
> (a) Show that the test that rejects $H_0$ when $|\bar X-\theta_0|>t_{n-1,\alpha/2}\sqrt{S^2/n}$ is a test of size $\alpha$.
> (b) Show that the test in part (a) can be derived as an LRT.

### 中文转述

> [!question] 中文转述
> **原题8.38。**
> 设 $X_1,\ldots,X_n$ 独立同分布于 $\mathrm n(\theta,\sigma^2)$，$\theta_0$ 为 $\theta$ 的指定值，$\sigma^2$ 未知. 希望检验
>
> $$
> H_0:\theta=\theta_0\quad\text{对}\quad H_1:\theta\ne\theta_0.
> $$
>
> (a)  证明在
>
> $$
> |\bar X-\theta_0|>t_{n-1,\alpha/2}\sqrt{S^2/n}
> $$
>
> 时拒绝 $H_0$ 的检验，大小为 $\alpha$.
>
> (b)  证明(a) 中的检验可由似然比检验导出.

## 提示

> [!hint]- 提示
> 自由与约束残差平方和的比值是$t^2$的单调函数。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 取$n\ge2$、$\sigma>0$，记$\nu=n-1,Q=\sum_i(X_i-\bar X)^2=\nu S^2$。
> (a) 在原假设下$Z=\sqrt n(\bar X-\theta_0)/\sigma\sim N(0,1)$，$V=Q/\sigma^2\sim\chi^2_\nu$且独立。因此$T=Z/\sqrt{V/\nu}\sim t_\nu$，与未知$\sigma$无关。两尾各$\alpha/2$，拒绝$|T|>t_{\nu,\alpha/2}$有大小$\alpha$。
> (b) 全MLE为$\hat\theta=\bar X,\hat\sigma^2=Q/n$；原假设方差MLE为$[Q+n(\bar X-\theta_0)^2]/n$。代入正态似然并相除得$\lambda=[Q/(Q+n(\bar X-\theta_0)^2)]^{n/2}=[1+T^2/\nu]^{-n/2}$，关于$|T|$严格递减。取$c=[1+t_{\nu,\alpha/2}^2/\nu]^{-n/2}$即为题列LRT；$Q=0$的零概率点另定义，不影响大小。

## 相关概念

- [[02 - 数理统计/概念/假设检验|假设检验（hypothesis testing）]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[01 - 概率论/概念/条件概率|条件概率]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 完整原题已逐页对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=362|印刷331／PDF物理362]]；原题无星号。教材信息及归档进度见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 来源已核对与独立解答写成不等于个人已完成练习；学习状态保留`not-started`。未实测Obsidian界面渲染。
