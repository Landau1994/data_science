---
title: "习题 ST227：正态均值单侧z与t检验的大小和似然比"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "advanced"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第8章习题8.37，印刷页331／PDF物理页362"
source_id: "DS011"
source_chapter: 8
source_exercise: "8.37"
source_stars: 0
source_refs: ["DS011 Exercise 8.37，印刷页331／PDF物理页362"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST227：正态均值单侧z与t检验的大小和似然比

## 题目

### 英文原题

> [!question] 英文原题
> **8.37** Let $X_1,\ldots,X_n$ be a random sample from a n$(\theta,\sigma^2)$ population. Consider testing
> $$H_0:\theta\le\theta_0\quad\text{versus}\quad H_1:\theta>\theta_0.$$
> (a) If $\sigma^2$ is known, show that the test that rejects $H_0$ when $\bar X>\theta_0+z_\alpha\sqrt{\sigma^2/n}$ is a test of size $\alpha$. Show that the test can be derived as an LRT.
> (b) Show that the test in part (a) is a UMP test.
> (c) If $\sigma^2$ is unknown, show that the test that rejects $H_0$ when $\bar X>\theta_0+t_{n-1,\alpha}\sqrt{S^2/n}$ is a test of size $\alpha$. Show that the test can be derived as an LRT.

### 中文转述

> [!question] 中文转述
> **原题8.37。**
> 设 $X_1,\ldots,X_n$ 是来自 $\mathrm n(\theta,\sigma^2)$ 总体的随机样本. 考虑检验
>
> $$
> H_0:\theta\le\theta_0\quad\text{对}\quad H_1:\theta>\theta_0.
> $$
>
> (a)  若 $\sigma^2$ 已知，证明在
>
> $$
> \bar X>\theta_0+z_\alpha\sqrt{\sigma^2/n}
> $$
>
> 时拒绝 $H_0$ 的检验，大小为 $\alpha$. 证明它可由似然比检验导出.
>
> (b)  证明(a) 中的检验是一致最强检验.
>
> (c)  若 $\sigma^2$ 未知，证明在
>
> $$
> \bar X>\theta_0+t_{n-1,\alpha}\sqrt{S^2/n}
> $$
>
> 时拒绝 $H_0$ 的检验，大小为 $\alpha$. 证明它可由似然比检验导出.

## 提示

> [!hint]- 提示
> 本书临界值下标为右尾概率；单侧LRT存在原假设内平顶。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 令$z_\alpha$及$t_{\nu,\alpha}$表示右尾概率$\alpha$的分位点。通常显著性范围取$0<\alpha<1/2$，使两个临界值正；这也是下述字面LRT对应范围。
> (a) $Z=\sqrt n(\bar X-\theta_0)/\sigma$在边界为标准正态，向负的均值偏移只减少右尾，故复合原假设大小$\alpha$。全MLE均值为$\bar X$，约束MLE为$\min(\bar X,\theta_0)$，故$\lambda=1$若$\bar X\le\theta_0$，否则$e^{-Z^2/2}$。取$c=e^{-z_\alpha^2/2}$得到题列拒绝域。
> (b) 相对边界$\theta_0$的似然比对$\bar X$随任意正备择均严格递增，NP引理使同一上尾域对每个备择最强；又任意复合水平竞争检验在边界也水平$\alpha$，所以为UMP。
> (c) 取$n\ge2$，$Q=\sum(X_i-\bar X)^2=(n-1)S^2>0$。自由MLE方差为$Q/n$；若$\bar X>\theta_0$，原假设MLE均值为$\theta_0$、方差为$[Q+n(\bar X-\theta_0)^2]/n$。故$\lambda=1$若$\bar X\le\theta_0$，否则$[1+T^2/(n-1)]^{-n/2}$，$T=\sqrt n(\bar X-\theta_0)/S$。边界处$T\sim t_{n-1}$，其分布由独立标准正态分子与$\chi^2_{n-1}/(n-1)$分母平方根得到。若$\theta\le\theta_0$，写$T=[Z+\sqrt n(\theta-\theta_0)/\sigma]/\sqrt{V/(n-1)}$，固定正分母后尾事件减小，故原假设上确界在任一边界$(\theta_0,\sigma)$取得$\alpha$。选择$c=[1+t_{n-1,\alpha}^2/(n-1)]^{-n/2}$即得到LRT。
> 对$\alpha\ge1/2$，右尾检验仍有所列大小及(a)的UMP性，但字面$\lambda\le c$的平顶限制使它不必是未经额外平顶选取的LRT；这与习题8.24的边界相同。

## 相关概念

- [[02 - 数理统计/概念/假设检验|假设检验（hypothesis testing）]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[01 - 概率论/概念/条件概率|条件概率]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 完整原题已逐页对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=362|印刷331／PDF物理362]]；原题无星号。教材信息及归档进度见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 来源已核对与独立解答写成不等于个人已完成练习；学习状态保留`not-started`。未实测Obsidian界面渲染。
