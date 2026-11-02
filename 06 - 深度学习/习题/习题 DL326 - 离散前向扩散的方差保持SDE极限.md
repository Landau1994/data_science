---
title: 习题 DL326：离散前向扩散的方差保持SDE极限
topic: deep-learning
topic_label: 深度学习
difficulty: intermediate
status: not-started
tags:
- exercise
- deep-learning
source: '[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Bishop《深度学习：基础与概念》（DS003）]]'
source_id: DS003
source_chapter: 20
source_exercise: '20.19'
source_stars: 2
source_refs:
- DS003 Exercise 20.19，印刷607/PDF617
- DS003 §20.1，式(20.3)，印刷583/PDF593；§20.3.4，式(20.55)，印刷598/PDF608
source_status: verified
solution_status: independently-derived
created: '2026-11-02'
---

# 习题 DL326：离散前向扩散的方差保持SDE极限

## 题目

### 英文原题

> [!question] 英文原题
> **20.19 (★★)** For discrete steps, the forward noise process in a diffusion model is defined by (20.3). Here we take the continuous-time limit and convert this to an SDE. We first introduce a continuously-changing variance function $\beta(t)$ such that $\beta_t=\beta(t)\Delta t$. By making a Taylor expansion of the square root in the first term on the right-hand-side of (20.3), show that the infinitesimal update can be written in the form
> $$
> \mathrm d\mathbf z=-\frac12\beta(t)\mathbf z\,\mathrm dt+\sqrt{\beta(t)}\,\mathrm d\mathbf v.\tag{20.70}
> $$
> We see that this is a special case of the general SDE (20.55).

### 中文转述

> [!question] 中文转述
> **原题20.19。** 令离散噪声方差为 $\beta(t)\Delta t$，对平方根展开，识别前向扩散的随机微分方程（stochastic differential equation, SDE）漂移与扩散系数。

## 提示

> [!hint]- 提示
> 标准高斯增量乘 $\sqrt{\Delta t}$ 对应布朗运动增量，不能当作普通可微速度。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 在步长 $\Delta t$ 上，更新为 $\mathbf z(t+\Delta t)=\sqrt{1-\beta(t)\Delta t}\mathbf z(t)+\sqrt{\beta(t)\Delta t}\boldsymbol\epsilon_t$。对局部有界非负 $\beta(t)$，
> $$
> \sqrt{1-\beta(t)\Delta t}=1-\tfrac12\beta(t)\Delta t+O((\Delta t)^2).
> $$
> 因此
> $$
> \Delta\mathbf z=-\tfrac12\beta(t)\mathbf z\Delta t+\sqrt{\beta(t)}\Delta\mathbf v+O((\Delta t)^2\|\mathbf z\|),
> $$
> 其中独立 $\Delta\mathbf v=\sqrt{\Delta t}\boldsymbol\epsilon_t\sim\mathcal N(0,\Delta t I)$ 是布朗增量。保留漂移的一阶及噪声的平方根阶，即得到(20.70)，在(20.55)中对应 $\mathbf f(\mathbf z,t)=-\beta(t)\mathbf z/2$、$g(t)=\sqrt{\beta(t)}$。
>
> 这是对Euler–Maruyama局部增量的SDE识别。若进一步声明数值过程强／弱收敛，需要系数正则性、矩控制与具体离散耦合等条件；本题的形式极限不替代完整数值收敛定理。

## 相关概念

- [[06 - 深度学习/概念/扩散模型|扩散模型]]
- [[01 - 概率论/概念/随机变量|随机变量]]
- [[03 - 线性代数与优化/概念/梯度流|梯度流]]

## 备注

- 原题已实际对照[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=617|印刷607／PDF617]]；正文引用范围见 `source_refs`。
- 英文原题与中文转述分列，原文疑误另注；未使用配套答案册。`source_status: verified` 仅表示本题及所列公式的实际核对范围；解答写成不表示个人学习完成，状态保持 `not-started`。
