---
title: "习题 PM059：后验处ELBO与对数似然的切向梯度"
topic: probabilistic-models
topic_label: 概率模型与推断
difficulty: beginner
status: not-started
tags:
  - exercise
  - probabilistic-models
source: "[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Bishop 深度学习（DS003）]]"
source_id: DS003
source_chapter: 15
source_exercise: "15.22"
source_stars: 1
source_refs:
  - "DS003 Exercise 15.22，印刷493/PDF508"
  - "DS003 §15.4，式15.51–15.54，印刷485/PDF500"
  - "DS003 §15.4.2，式15.56，印刷487/PDF502"
source_status: verified
solution_status: independently-derived
created: 2026-11-02
---

# 习题 PM059：后验处ELBO与对数似然的切向梯度

## 题目

### 英文原题

> [!question] 英文原题
> **15.22 (★)** Show that the lower bound $\mathcal L(q,\boldsymbol\theta)$ given by (15.53), with $q(\mathbf Z)=p(\mathbf Z\mid\mathbf X,\boldsymbol\theta^{(\mathrm{old})})$, has the same gradient with respect to $\boldsymbol\theta$ as the log likelihood function $\ln p(\mathbf X\mid\boldsymbol\theta)$ at the point $\boldsymbol\theta=\boldsymbol\theta^{(\mathrm{old})}$.

### 中文转述

> [!question] 中文转述
> 在(15.53)中取分布$q(\mathbf Z)=p(\mathbf Z\mid\mathbf X,\boldsymbol\theta^{(\mathrm{old})})$。证明当$\boldsymbol\theta=\boldsymbol\theta^{(\mathrm{old})}$时，下界$\mathcal L(q,\boldsymbol\theta)$对$\boldsymbol\theta$的梯度等于对数似然$\ln p(\mathbf X\mid\boldsymbol\theta)$的梯度。

## 提示

> [!hint]- 提示 1
> 求导时$q$保持固定。直接对边缘似然求导，再除以边缘似然。

## 解答

> [!success]- 解答
> **独立推导。**
>
> 设$\theta_0=\theta^{\mathrm{old}}$为可微参数域内点，附近有共同支持，$p(X\mid\theta_0)>0$，并可交换求导与对潜变量的求和或积分。有限潜状态且相关联合概率在邻域内正、可微，是充分条件之一。固定$q_0(Z)=p(Z\mid X,\theta_0)$。
>
> 熵项$-\sum_Zq_0\log q_0$不依赖$\theta$，所以
> $$
> \left.\nabla_\theta\mathcal L(q_0,\theta)\right|_{\theta_0}
> =\sum_Zq_0(Z)\left.\nabla_\theta\log p(X,Z\mid\theta)\right|_{\theta_0}.
> $$
> 另一方面，
> $$
> \left.\nabla_\theta\log p(X\mid\theta)\right|_{\theta_0}
> =\frac{\sum_Z\left.\nabla_\theta p(X,Z\mid\theta)\right|_{\theta_0}}{p(X\mid\theta_0)}
> $$
> $$
> =\sum_Z\frac{p(X,Z\mid\theta_0)}{p(X\mid\theta_0)}
> \left.\nabla_\theta\log p(X,Z\mid\theta)\right|_{\theta_0},
> $$
> 与前式相同。这也是Fisher恒等式在当前参数处的形式。
>
> 由(15.52)还可理解为KL项在后验匹配处取到零的可微内点最小值，故其梯度为零；但这需要可微性，不能只用“数值相等”推出“梯度相等”。本题求导不能把$q_0$随待优化$\theta$更新；M步中它固定为旧参数后验。参数边界、支持随参数变化或不可交换微分积分时，普通梯度推导可能失效，需单独处理方向导数或边界条件。

## 相关概念

- [[05 - 概率模型与推断/概念/变分推断|变分推断]]
- [[03 - 线性代数与优化/概念/梯度与驻点|梯度与驻点]]
- [[05 - 概率模型与推断/概念/潜变量|潜变量]]

## 备注

- 原题已核对 DS003 印刷493页／PDF物理508页；正文引用的实际核对范围见 `source_refs`。
- 解答为独立推导；归档与个人学习状态分开，学习状态保持 `not-started`。
