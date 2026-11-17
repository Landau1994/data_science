---
title: 习题 ST314：似然得分CLT与观测信息大数定律
topic: mathematical-statistics
topic_label: 数理统计
difficulty: advanced
status: not-started
tags:
- exercise
- mathematical-statistics
source: George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第10章习题10.8，印刷页409／PDF物理页440
source_id: DS011
source_chapter: 10
source_exercise: '10.8'
source_stars: 0
source_refs:
- DS011 Exercise 10.8，印刷409／PDF物理440
- DS011题内依赖核对：印刷381／PDF物理412；印刷417／PDF物理448；印刷418／PDF物理449
source_status: verified
solution_status: independently-derived
created: '2026-11-13'
---

# 习题 ST314：似然得分CLT与观测信息大数定律

## 题目

### 英文原题

> [!question] 英文原题
> **10.8** Finish the proof of Theorem 10.1.6 by establishing the two convergence results in (10.1.6).
>
> (a) Show that
> $$
> \frac1{\sqrt n}l'(\theta_0\mid X)=\sqrt n\left[\frac1n\sum_iW_i\right],
> $$
> where $W_i=\frac{\frac d{d\theta}f(X_i\mid\theta)}{f(X_i\mid\theta)}$ has mean 0 and variance $I(\theta_0)$. Now use the CLT to establish the convergence to $\operatorname n[0,I(\theta_0)]$.
>
> (b) Show that
> $$
> -\frac1n l''(\theta_0\mid X)=\frac1n\sum_iW_i^2-\frac1n\sum_i\frac{\frac{d^2}{d\theta^2}f(X_i\mid\theta)}{f(X_i\mid\theta)},
> $$
> and that the mean of the first piece is $I(\theta_0)$ and the mean of the second piece is 0. Apply the WLLN.

### 中文转述

> [!question] 中文转述
> **原题10.8。** 通过建立式(10.1.6)中的两个收敛结果，完成定理10.1.6的证明.
>
> (a)  证明
>
> $$
> \frac1{\sqrt n}l'(\theta_0\mid\boldsymbol X)=\sqrt n\left[\frac1n\sum_iW_i\right],
> $$
>
> 其中$W_i=\frac{\frac d{d\theta}f(X_i\mid\theta)}{f(X_i\mid\theta)}$均值为0、方差为$I(\theta_0)$. 再用中心极限定理建立向$\mathrm n[0,I(\theta_0)]$的收敛.
>
> (b)  证明
>
> $$
> -\frac1n l''(\theta_0\mid\boldsymbol X)=\frac1n\sum_iW_i^2-\frac1n\sum_i\frac{\frac{d^2}{d\theta^2}f(X_i\mid\theta)}{f(X_i\mid\theta)},
> $$
>
> 且第一部分均值为$I(\theta_0)$，第二部分均值为0. 应用弱大数定律.

## 提示

> [!hint]- 提示
> 所有导数在θ_0代入，积分与求导交换需明确正则性；观测信息带负号。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 设iid观测来自真密度$f(\cdot\mid\theta_0)$，共同支持，在真值处可两次求导并可交换积分求导，$0<I(\theta_0)=E_{\theta_0}(f'/f)^2<\infty$，且$E|f''/f|<\infty$。
>
> **(a)** 对数似然导数为$\sum_iW_i$，$W_i=f'(X_i\mid\theta_0)/f(X_i\mid\theta_0)$。$EW_i=\int f'(x\mid\theta_0)dx=\partial_\theta\int f(x\mid\theta)dx|_{\theta_0}=0$，所以方差为$EW_i^2=I(\theta_0)$。iid CLT给$n^{-1/2}\sum_iW_i\Rightarrow N(0,I(\theta_0))$；负得分也有相同中心正态极限。
>
> **(b)** 逐项求导$\partial_\theta^2\log f=f''/f-(f'/f)^2$即题式。第一项均值$I(\theta_0)$，第二项均值$\int f''(x\mid\theta_0)dx=\partial_\theta^2 1=0$。有限一阶矩WLLN给$-l''(\theta_0)/n\to_p I(\theta_0)$。两式组合才提供通常MLE正态极限；若扩展到随机中间点还须局部一致性及Taylor余项控制，本题未用点态WLLN冒充该额外步骤。
>
> 题目所引式(10.1.6)实际位于定理10.1.12的证明，非定理10.1.6的证明。原正文该式第二行将$l''/n$写成正信息也漏了负号；这里按题(b)的正确$-l''/n$证明。

## 相关概念

- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/期望|期望]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[02 - 数理统计/概念/参数估计|参数估计]]

## 备注

- 来源：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=440|印刷第409页／PDF物理第440页]]；版本与归档见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 实读式(10.1.6)：印刷381／PDF412。题目引理编号、导数代入点和信息符号分别注明，未静默修正。
- 已实读本题所用正文：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=412|印刷381／PDF物理412]]；[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=448|印刷417／PDF物理448]]；[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=449|印刷418／PDF物理449]]；其余题内外部文献仅保留原引用，未声称查阅。
- 英文原题逐题对照PDF原始页面，保留原分题、提示、引用及可见疑误；原题无星号。题内引用补充与独立解答不混入原文；未查阅答案册或题内外部文献。
- 来源核对不表示个人学习完成，学习状态保持not-started。公式、链接与元数据检查不等于Obsidian实际渲染检查。
