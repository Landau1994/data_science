---
title: 习题 ST332：Huber得分的期望夹心方差与导数符号
topic: mathematical-statistics
topic_label: 数理统计
difficulty: intermediate
status: not-started
tags:
- exercise
- mathematical-statistics
source: George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第10章习题10.26，印刷页412／PDF物理页443
source_id: DS011
source_chapter: 10
source_exercise: '10.26'
source_stars: 0
source_refs:
- DS011 Exercise 10.26，印刷412／PDF物理443
- DS011题内依赖核对：印刷392／PDF物理423；印刷393／PDF物理424
source_status: verified
solution_status: independently-derived
created: '2026-11-13'
---

# 习题 ST332：Huber得分的期望夹心方差与导数符号

## 题目

### 英文原题

> [!question] 英文原题
> **10.26** Here we look at some details in the calculations in Example 10.2.6.
>
> (a) Verify the expressions for $E_\theta\psi'(X-\theta)$ and $E_\theta[\psi(X-\theta)]^2$, and hence verify the formula for the variance of $\hat\theta_M$.
>
> (b) When calculating the expected value of $\psi'$, we noted that $\psi$ was not differentiable, but we could work with the differentiable portion. Another approach is to realize that the expected value of $\psi$ is differentiable, and that in (10.2.5) we could write
> $$
> \frac1n\sum_{i=1}^n\psi'(x_i-\theta_0)\to\left.\frac d{d\theta_0}E_\theta\psi(X-\theta_0)\right|_{\theta_0=\theta}.
> $$
> Show that this is the same limit as in (10.2.5).

### 中文转述

> [!question] 中文转述
> **原题10.26。** 考察例10.2.6计算的若干细节.
>
> (a)  验证$E_\theta\psi'(X-\theta)$与$E_\theta[\psi(X-\theta)]^2$的表达式，从而验证$\hat\theta_M$的方差公式.
>
> (b)  计算$\psi'$的期望时，注意到$\psi$并非处处可微，但可处理其中可微的部分. 另一种做法是注意$\psi$的期望可微，在式(10.2.5)中可以写为
>
> $$
> \frac1n\sum_{i=1}^n\psi'(x_i-\theta_0)\longrightarrow\left.\frac d{d\theta_0}E_\theta\psi(X-\theta_0)\right|_{\theta_0=\theta}.
> $$
>
> 证明这与式(10.2.5)的极限相同.

## 提示

> [!hint]- 提示
> ψ_k(u)=clip(u,−k,k)，导数在内部为1、外部为0；对位置θ_0求导要带负号。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 设$X-\theta\sim f$，$f$关于0对称且连续，$k>0$，$\psi_k(u)=\max(-k,\min(k,u))$。
>
> **(a)** 除$u=\pm k$两个零概率点外，$\psi_k'(u)=I(|u|<k)$，因此$A=E\psi_k'(X-\theta)=P_0(|X|<k)$。平方在内部为$u^2$、外部为$k^2$，故
> $$
> B=E\psi_k(X-\theta)^2=\int_{-k}^ku^2f(u)du+k^2P_0(|X|>k).
> $$
> 对称性给$E\psi_k=0$。若$A>0$并满足相合根的正则条件，$\sqrt n(\hat\theta_M-\theta)\Rightarrow N(0,B/A^2)$，估计量本身的常规方差近似$B/(nA^2)$。有界$\psi$保证$B<\infty$，即使总体$X$没有二阶矩也可适用。
>
> **(b)** $\psi_k$是1-Lipschitz，差商绝对值不超过1；在两折点外，关于$t$求导为$-I(|X-t|<k)$。支配收敛给
> $$
> \frac d{dt}E_\theta\psi_k(X-t)=-P_\theta(|X-t|<k),\quad \left.\frac d{dt}E_\theta\psi_k(X-t)\right|_{t=\theta}=-A.
> $$
> 而原左边WLLN极限为$+A$。所以题(b)显示式缺少负号，按通常$\psi'$自变量导数约定不能“相同”；正确应为$-\frac d{dt}E_\theta\psi(X-t)|_{t=\theta}=A$。折点的存在不妨碍期望可微，符号错误却不能忽略。

## 相关概念

- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/期望|期望]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[02 - 数理统计/概念/参数估计|参数估计]]

## 备注

- 来源：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=443|印刷第412页／PDF物理第443页]]；版本与归档见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 例10.2.6及其方差计算实读印刷392–393／PDF423–424；原(b)负号疑误完整保留。
- 已实读本题所用正文：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=423|印刷392／PDF物理423]]；[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=424|印刷393／PDF物理424]]；其余题内外部文献仅保留原引用，未声称查阅。
- 英文原题逐题对照PDF原始页面，保留原分题、提示、引用及可见疑误；原题无星号。题内引用补充与独立解答不混入原文；未查阅答案册或题内外部文献。
- 来源核对不表示个人学习完成，学习状态保持not-started。公式、链接与元数据检查不等于Obsidian实际渲染检查。
