---
title: 习题 DL295：残差网络小步长极限与神经ODE
topic: deep-learning
topic_label: 深度学习
difficulty: beginner
status: not-started
tags:
- exercise
- deep-learning
source: '[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Deep Learning: Foundations and Concepts（DS003）]]'
source_id: DS003
source_chapter: 18
source_exercise: '18.5'
source_stars: 1
source_refs:
- DS003 Exercise 18.5，印刷559/PDF571
- DS003 式(18.21)–(18.22)，印刷554/PDF566；积分式(18.23)，印刷555/PDF567
source_status: verified
solution_status: independently-derived
created: '2026-11-02'
---

# 习题 DL295：残差网络小步长极限与神经ODE

## 题目

### 英文原题

> [!question] 英文原题
> **Exercise 18.5（★）** Consider the forward propagation equation for a residual network given by (18.21) in which we consider a small increment $\epsilon$ in the ‘time’ variable $t$:
> $$\mathbf z^{(t+\epsilon)}=\mathbf z^{(t)}+\epsilon\mathbf f(\mathbf z^{(t)},\mathbf w).\tag{18.38}$$
> Here the additive contribution from the neural network is scaled by $\epsilon$. Note that (18.21) corresponds to the case $\epsilon=1$. By taking the limit $\epsilon\to0$, derive the forward propagation differential equation given by (18.22).

### 中文转述

> [!question] 中文转述
> **原题18.5。** 将残差网络（residual network）更新中的增量乘以小步长 $\epsilon$，得到(18.38)；原(18.21)对应步长1。令 $\epsilon\to0$，推导神经常微分方程（neural ODE）的前向传播公式(18.22)。

## 提示

> [!hint]- 提示 1
> 移项后除以 $\epsilon$，辨认差商。

## 解答

> [!success]- 解答
> **独立推导。** 由(18.38)，
> $$\frac{z(t+\epsilon)-z(t)}{\epsilon}=f(z(t),w).$$
> 若离散轨迹收敛为可微函数且 $f$ 连续，左边趋于 $z'(t)$，得到
> $$\frac{\mathrm dz(t)}{\mathrm dt}=f(z(t),w),\qquad z(0)=z_0.$$
> 这是(18.22)。反过来，对于光滑ODE解，Taylor展开 $z(t+\epsilon)=z(t)+\epsilon f(z(t),w)+O(\epsilon^2)$，说明(18.38)为显式Euler一步。若 $f$ 对 $z$ Lipschitz且足够光滑，在固定有限时间区间上，Euler法通常具有一阶全局误差；因此这里的连续极限不是声称有限步残差网络等于精确ODE流。
>
> 积分形式应为 $z(T)=z(0)+\int_0^T f(z(t),w)\,\mathrm dt$。正文(18.23)少写了 $z(0)$，除非初始值恰为零；初值在网络中通常就是输入，不能省略。

## 相关概念

- [[06 - 深度学习/概念/归一化流|归一化流]]
- [[03 - 线性代数与优化/概念/链式法则|链式法则]]
- [[06 - 深度学习/概念/残差网络|残差网络]]

## 备注

- 原题及星数：[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=571|印刷559／PDF571]]；题页及引用正文已实际查看原PDF图像，精确定位见 `source_refs`。
- 独立推导补充连续极限的光滑性与初值条件，并标明相邻正文的积分初值漏项。
- `source_status: verified` 仅指本题及所列实际核对范围；解答独立推导，不构成用户已完成学习，状态保持 `not-started`。
