---
title: "习题 ST240：Laplace先验下正态后验尾概率及扩散极限"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "advanced"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第8章习题8.50，印刷页334／PDF物理页365"
source_id: "DS011"
source_chapter: 8
source_exercise: "8.50"
source_stars: 0
source_refs: ["DS011 Exercise 8.50，印刷页334／PDF物理页365"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST240：Laplace先验下正态后验尾概率及扩散极限

## 题目

### 英文原题

> [!question] 英文原题
> **8.50** Let $X_1,\ldots,X_n$ be iid n$(\theta,\sigma^2)$, $\sigma^2$ known, and let $\theta$ have a double exponential distribution, that is, $\pi(\theta)=e^{-|\theta|/a}/(2a)$, $a$ known. A Bayesian test of the hypotheses $H_0:\theta\le0$ versus $H_1:\theta>0$ will decide in favor of $H_1$ if its posterior probability is large.
> (a) For a given constant $K$, calculate the posterior probability that $\theta>K$, that is, $P(\theta>K\mid x_1,\ldots,x_n,a)$.
> (b) Find an expression for $\lim_{a\to\infty}P(\theta>K\mid x_1,\ldots,x_n,a)$.
> (c) Compare your answer in part (b) to the p-value associated with the classical hypothesis test.

### 中文转述

> [!question] 中文转述
> **原题8.50。**
> 设 $X_1,\ldots,X_n$ 独立同分布于 $\mathrm n(\theta,\sigma^2)$，$\sigma^2$ 已知，$\theta$ 服从双指数分布，即 $\pi(\theta)=e^{-|\theta|/a}/(2a)$，$a$ 已知. 检验 $H_0:\theta\le0$ 对 $H_1:\theta>0$ 的贝叶斯检验，在 $H_1$ 的后验概率较大时支持 $H_1$.
>
> (a)  对给定常数 $K$，计算 $\theta>K$ 的后验概率，即 $P(\theta>K\mid x_1,\ldots,x_n,a)$.
>
> (b)  求 $\lim_{a\to\infty}P(\theta>K\mid x_1,\ldots,x_n,a)$ 的表达式.
>
> (c)  将(b) 的答案与经典假设检验对应的 $p$ 值比较.

## 提示

> [!hint]- 提示
> 把后验按正负半轴各配成一个正态核。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 设$a>0,v=\sigma^2/n>0,s=\sqrt v,m=\bar x$。后验核为$e^{-(\theta-m)^2/(2v)-|\theta|/a}$。令$\mu_+=m-v/a,\mu_-=m+v/a$，并定义
> $$D=e^{-m/a}\Phi(\mu_+/s)+e^{m/a}\Phi(-\mu_-/s)>0.$$
> 配方后正半轴核为$e^{-m/a+v/(2a^2)}e^{-(\theta-\mu_+)^2/(2v)}$，负半轴类似为$e^{m/a+v/(2a^2)}e^{-(\theta-\mu_-)^2/(2v)}$，公共积分因子抵消。
> (a) 若$K\ge0$，后验尾概率为$e^{-m/a}[1-\Phi((K-\mu_+)/s)]/D$。若$K<0$，则为
> $$\frac{e^{-m/a}\Phi(\mu_+/s)+e^{m/a}[\Phi(-\mu_-/s)-\Phi((K-\mu_-)/s)]}{D}.$$
> 两式在0连续，已包含全部半轴。
> (b) $a\to\infty$时$\mu_\pm\to m$，$D\to\Phi(m/s)+\Phi(-m/s)=1$，故极限为$1-\Phi((K-m)/s)$。
> (c) 原题检验的经典单侧$p$值为$1-\Phi(m/s)$。取对应边界$K=0$，(b)是$1-p$，即备择后验概率；原假设后验概率的极限才等于$p$。一般$K$对应检验$\theta\le K$，有同样互补关系。不能把备择概率本身误写成经典$p$值，也不把不正规平坦先验当作某个有限$a$的先验密度。

## 相关概念

- [[02 - 数理统计/概念/假设检验|假设检验（hypothesis testing）]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[01 - 概率论/概念/条件概率|条件概率]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 完整原题已逐页对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=365|印刷334／PDF物理365]]；原题无星号。教材信息及归档进度见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 来源已核对与独立解答写成不等于个人已完成练习；学习状态保留`not-started`。未实测Obsidian界面渲染。
