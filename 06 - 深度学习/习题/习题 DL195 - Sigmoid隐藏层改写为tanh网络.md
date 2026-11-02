---
title: "习题 DL195：Sigmoid隐藏层改写为tanh网络"
topic: "deep-learning"
topic_label: "深度学习"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "deep-learning"]
source: "[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Bishop《深度学习：基础与概念》（DS003）]]"
source_id: "DS003"
source_chapter: 6
source_exercise: "6.4"
source_stars: 2
source_refs: ["DS003 Exercise 6.4及式(6.60)，印刷205/PDF223", "DS003 §6.2–6.2.1，式(6.7)–(6.11)，印刷180–181/PDF198–199", "DS003 §6.2.3，tanh定义式(6.14)，印刷184/PDF202"]
source_status: "verified"
solution_status: "independently-derived"
created: 2026-11-02
---

# 习题 DL195：Sigmoid隐藏层改写为tanh网络

## 题目

### 英文原题

> [!question] 英文原题
> **6.4 (★★)** Consider a two-layer network function of the form (6.11) in which the hidden-unit nonlinear activation functions $h(\cdot)$ are given by logistic sigmoid functions of the form
> $$
> \sigma(a)=\{1+\exp(-a)\}^{-1}.\tag{6.60}
> $$
> Show that there exists an equivalent network, which computes exactly the same function, but with hidden-unit activation functions given by $\tanh(a)$ where the tanh function is defined by (6.14). Hint: first find the relation between $\sigma(a)$ and $\tanh(a)$, and then show that the parameters of the two networks differ by linear transformations.

### 中文转述

> [!question] 中文转述
> **Bishop 原题 6.4。** 考虑式(6.11)的两层网络，隐藏单元的非线性激活函数（activation function）为式(6.60)的逻辑 Sigmoid。证明存在一个计算完全相同函数、隐藏单元激活改为式(6.14)的 tanh 的等价网络。原题提示：先求 Sigmoid 与 tanh 的关系，再证明两网络的参数通过线性变换相联系。

## 提示

> [!hint]- 提示 1
> 利用 $\sigma(a)=\{1+\tanh(a/2)\}/2$，对隐藏层的输入权重、偏置与下一层的权重、偏置同时作变换。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 将原书式(6.7)–(6.11)的偏置显式写出：
> $$
> a_j=\sum_{i=1}^Dw_{ji}^{(1)}x_i+w_{j0}^{(1)},\quad
> z_j=\sigma(a_j),\quad
> b_k=\sum_{j=1}^Mw_{kj}^{(2)}z_j+w_{k0}^{(2)},\quad y_k=f(b_k).
> $$
> 这里保留相同的输出激活 $f$。由指数定义直接可得 $\tanh(a/2)=2\sigma(a)-1$，所以 $z_j=\frac12(1+\tanh(a_j/2))$。
>
> 定义新网络的参数为
> $$
> u_{ji}^{(1)}=\frac12w_{ji}^{(1)}\quad(i=1,\ldots,D),\qquad
> u_{j0}^{(1)}=\frac12w_{j0}^{(1)},
> $$
> $$
> u_{kj}^{(2)}=\frac12w_{kj}^{(2)}\quad(j=1,\ldots,M),\qquad
> u_{k0}^{(2)}=w_{k0}^{(2)}+\frac12\sum_{j=1}^Mw_{kj}^{(2)}.
> $$
> 其隐藏输出为 $\widetilde z_j=\tanh(a_j/2)=2z_j-1$，于是新的输出预激活是
> $$
> \begin{aligned}
> \widetilde b_k
> &=\sum_{j=1}^M\frac{w_{kj}^{(2)}}2(2z_j-1)
> +w_{k0}^{(2)}+\frac12\sum_{j=1}^Mw_{kj}^{(2)}\\
> &=\sum_{j=1}^Mw_{kj}^{(2)}z_j+w_{k0}^{(2)}=b_k.
> \end{aligned}
> $$
> 因此对所有输入均有 $f(\widetilde b_k)=f(b_k)$，即输出函数完全相同。由于整个预激活向量不变，这也适用于采用向量形式输出激活的情形。
>
> 上述变换在全部权重和偏置组成的参数向量上是线性的，并且可逆：第一层权重、偏置和第二层非偏置权重均乘以2；第二层原偏置则由
> $$
> w_{k0}^{(2)}=u_{k0}^{(2)}-\sum_{j=1}^Mu_{kj}^{(2)}
> $$
> 恢复。隐藏层的常数偏置节点始终是1，不能把它当作一个普通 Sigmoid 单元一起变换。
>
> 这证明函数表示的等价性；采用相同数值初始化、步长或未变换的参数惩罚时，两个训练过程并不因此相同。

## 相关概念

- [[06 - 深度学习/概念/神经网络|神经网络]]
- [[06 - 深度学习/概念/激活函数|激活函数]]
- [[06 - 深度学习/概念/前向传播|前向传播]]

## 备注

- 原题定位：[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=223|印刷205／PDF物理223]]；所用正文公式的实际位置见 `source_refs`。
- 输出激活函数保持原样，调整包括隐藏层偏置与输出层偏置，不只调整非偏置权重。
- 此题将已归档的[[04 - 统计学习/习题/习题 ML017 - Sigmoid与tanh基函数的等价参数化|固定基函数版本4.3]]推广到具有可学习隐藏层参数的网络。
- 题干、星号、引用公式与定位已实际对照原页；`source_status: verified` 仅限本题实际核对范围。解答为独立推导，未使用配套答案册；个人学习状态保持 `not-started`。
