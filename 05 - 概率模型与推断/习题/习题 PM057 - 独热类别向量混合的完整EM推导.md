---
title: "习题 PM057：独热类别向量混合的完整EM推导"
topic: probabilistic-models
topic_label: 概率模型与推断
difficulty: advanced
status: not-started
tags:
  - exercise
  - probabilistic-models
source: "[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Bishop 深度学习（DS003）]]"
source_id: DS003
source_chapter: 15
source_exercise: "15.20"
source_stars: 3
source_refs:
  - "DS003 Exercise 15.20，印刷493/PDF508"
  - "DS003 §15.3.3，式15.34–15.50，印刷481–483/PDF496–498"
source_status: verified
solution_status: independently-derived
created: 2026-11-02
---

# 习题 PM057：独热类别向量混合的完整EM推导

## 题目

### 英文原题

> [!question] 英文原题
> **15.20 (★★★)** Consider a $D$-dimensional variable $\mathbf x$ each of whose components $i$ is itself a multinomial variable of degree $M$ so that $\mathbf x$ is a binary vector with components $x_{ij}$ where $i=1,\ldots,D$ and $j=1,\ldots,M$, subject to the constraint that $\sum_jx_{ij}=1$ for all $i$. Suppose that the distribution of these variables is described by a mixture of the discrete multinomial distributions so that
> $$
> p(\mathbf x)=\sum_{k=1}^K\pi_kp(\mathbf x\mid\boldsymbol\mu_k)\tag{15.66}
> $$
> where
> $$
> p(\mathbf x\mid\boldsymbol\mu_k)=\prod_{i=1}^D\prod_{j=1}^M\mu_{kij}^{x_{ij}}.\tag{15.67}
> $$
> The parameters $\mu_{kij}$ represent the probabilities $p(x_{ij}=1\mid\boldsymbol\mu_k)$ and must satisfy $0\leq\mu_{kij}\leq1$ together with the constraint $\sum_j\mu_{kij}=1$ for all values of $k$ and $i$. Given an observed data set $\{\mathbf x_n\}$, where $n=1,\ldots,N$, derive the E-step and M-step equations of the EM algorithm for optimizing the mixing coefficients $\pi_k$ and the component parameters $\mu_{kij}$ of this distribution by maximum likelihood.

### 中文转述

> [!question] 中文转述
> 变量$\mathbf x$有$D$个类别坐标，每个坐标$i$是具有$M$个状态的多项类别变量，用二值独热分量$x_{ij}$表示，$i=1,\ldots,D$、$j=1,\ldots,M$，且每个$i$满足$\sum_jx_{ij}=1$。其混合分布为
> $$
> p(\mathbf x)=\sum_{k=1}^K\pi_kp(\mathbf x\mid\boldsymbol\mu_k),\qquad
> p(\mathbf x\mid\boldsymbol\mu_k)=\prod_{i=1}^D\prod_{j=1}^M\mu_{kij}^{x_{ij}}.
> $$
> 参数$\mu_{kij}=p(x_{ij}=1\mid\boldsymbol\mu_k)$满足$0\leq\mu_{kij}\leq1$及每个$k,i$的$\sum_j\mu_{kij}=1$。给定$N$个观测$\{\mathbf x_n\}$，推导用极大似然优化混合权重$\pi_k$及全部$\mu_{kij}$的E步、M步方程。

## 提示

> [!hint]- 提示 1
> 引入一个K状态独热潜标签，取完整数据对数似然；每个$k,i$都有一个独立的类别概率和约束。

## 解答

> [!success]- 解答
> **独立推导。**
>
> 令潜标签$z_{nk}\in\{0,1\}$、$\sum_kz_{nk}=1$。完整对数似然为
> $$
> \ell_c=\sum_{n,k}z_{nk}\left[\log\pi_k+\sum_{i=1}^D\sum_{j=1}^Mx_{nij}\log\mu_{kij}\right].
> $$
> E步对当前旧参数使用Bayes公式：
> $$
> \gamma_{nk}=P(z_{nk}=1\mid x_n)
> =\frac{\pi_k^{\mathrm{old}}\prod_{i,j}(\mu_{kij}^{\mathrm{old}})^{x_{nij}}}{\sum_a\pi_a^{\mathrm{old}}\prod_{i,j}(\mu_{aij}^{\mathrm{old}})^{x_{nij}}}.
> $$
> M步固定$\gamma$，定义$N_k=\sum_n\gamma_{nk}$及$S_{kij}=\sum_n\gamma_{nk}x_{nij}$。期望完整对数似然分解为
> $$
> Q=\sum_kN_k\log\pi_k+\sum_{k,i,j}S_{kij}\log\mu_{kij}.
> $$
> 混合权重约束$\sum_k\pi_k=1$给出$\pi_k^{\mathrm{new}}=N_k/N$。对固定$k,i$，在$\sum_j\mu_{kij}=1$下使用乘子，内点条件为$S_{kij}/\mu_{kij}+\lambda_{ki}=0$。因为独热编码使
> $$
> \sum_jS_{kij}=\sum_n\gamma_{nk}\sum_jx_{nij}=N_k,
> $$
> 所以$\lambda_{ki}=-N_k$，从而
> $$
> \mu_{kij}^{\mathrm{new}}=\frac{S_{kij}}{N_k}=\frac{\sum_n\gamma_{nk}x_{nij}}{\sum_n\gamma_{nk}},\qquad N_k>0.
> $$
> 这就是每类每坐标的责任度加权类别频率。凹对数目标保证各概率单纯形上的全局M步最优；$S_{kij}=0$时最优可在$\mu_{kij}=0$边界取得。空分量$N_k=0$的所有$\mu_{kij}$不识别，可保留或另行合法初始化；其权重取零。
>
> E步要求每个训练观测的混合概率正，分母为零时不能计算责任度。数值上通常用对数概率及log-sum-exp计算，零概率事件按$-\infty$处理；强制开区间参数时某些M步仅有边界上确界。这里所谓multinomial按题目独热约束是一次类别试验，并非每坐标含任意总次数的计数向量。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[01 - 概率论/概念/条件概率|条件概率]]
- [[05 - 概率模型与推断/概念/潜变量|潜变量]]
- [[05 - 概率模型与推断/概念/概率推断|概率推断]]

## 备注

- 原题已核对 DS003 印刷493页／PDF物理508页；正文引用的实际核对范围见 `source_refs`。
- 解答为独立推导；归档与个人学习状态分开，学习状态保持 `not-started`。
