---
title: "习题 DL205：Sigmoid交叉熵对输出预激活的导数"
topic: deep-learning
topic_label: 深度学习
difficulty: beginner
status: not-started
tags:
  - exercise
  - deep-learning
source: "[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Bishop 深度学习（DS003）]]"
source_id: DS003
source_chapter: 6
source_exercise: "6.14"
source_stars: 1
source_refs: ["DS003 Exercise 6.14，印刷207/PDF225", "DS003 §6.2.3，式(6.13)，印刷183/PDF201", "DS003 §6.4.1–6.4.2，式(6.31)–(6.35)，印刷196–197/PDF214–215"]
source_status: verified
solution_status: independently-derived
created: 2026-11-02
---

# 习题 DL205：Sigmoid交叉熵对输出预激活的导数

## 题目

### 英文原题

> [!question] 英文原题
> **6.14 (★)** Show that the derivative of the error function (6.33) with respect to the pre-activation $a_k$ for an output unit having a logistic-sigmoid activation function $y_k=\sigma(a_k)$, where $\sigma(a)$ is given by (6.13), satisfies (6.31).

### 中文转述

> [!question] 中文转述
> **原题6.14。** 输出单元采用逻辑Sigmoid激活 $y_k=\sigma(a_k)$，其中 $\sigma$ 由式(6.13)定义。证明误差函数(6.33)关于该输出单元预激活（pre-activation）$a_k$ 的导数满足式(6.31)，即 $\partial E/\partial a_k=y_k-t_k$。

## 提示

> [!hint]- 提示 1
> 先固定一个样本和一个二元输出，按 $E\to y\to a$ 求导；有限预激活时 $y(1-y)>0$，可以约去。

> [!hint]- 提示 2
> 原书式(6.33)对样本编号 $n$ 求和，而 $k$ 表示输出单元。完整批量记号应保留 $a_{nk}$，不能误将每个样本的输出当成同一个独立变量。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 先对一个样本的二元交叉熵求导。设 $t\in\{0,1\}$、$a\in\mathbb R$ 有限，$y=\sigma(a)=1/(1+e^{-a})\in(0,1)$，单样本误差为
> $$
> \ell(y,t)=-t\ln y-(1-t)\ln(1-y).
> $$
> 直接计算得
> $$
> \frac{\partial\ell}{\partial y}=-\frac ty+\frac{1-t}{1-y}
> =\frac{y-t}{y(1-y)},
> $$
> $$
> \frac{dy}{da}=\frac{e^{-a}}{(1+e^{-a})^2}=y(1-y).
> $$
> 所以链式法则给出
> $$
> \frac{\partial\ell}{\partial a}
> =\frac{y-t}{y(1-y)}\,y(1-y)=y-t.
> $$
> 有限 $a$ 保证分母非零，约分合法。这就是原书式(6.31)的单样本、单输出形式。
>
> **样本与输出下标。** 对式(6.33)的单二元输出，$E=\sum_n\ell(y_n,t_n)$、$y_n=\sigma(a_n)$。把批量预激活视为独立计算图变量，则
> $$
> \frac{\partial E}{\partial a_n}=y_n-t_n,
> $$
> 不会在这个局部偏导上再多一个样本求和。若扩展到式(6.35)的 $K$ 个给定输入后独立的二元输出，使用 $a_{nk}$、$y_{nk}$、$t_{nk}$，同样有
> $$
> \frac{\partial E}{\partial a_{nk}}=y_{nk}-t_{nk}.
> $$
> 略去样本编号后才是题面的 $\partial E/\partial a_k=y_k-t_k$。若继续对共享网络权重求导，则必须将各样本、各输出的贡献按链式法则相加：
> $$
> \nabla_{\mathbf w}E=\sum_{n,k}(y_{nk}-t_{nk})\nabla_{\mathbf w}a_{nk}.
> $$
> 该导数是数学上的有限预激活结论；把数值概率先截成0或1后，不能再对含除法的中间表达直接作相同运算。

## 相关概念

- [[04 - 统计学习/概念/交叉熵|交叉熵]]
- [[06 - 深度学习/概念/激活函数|激活函数]]
- [[03 - 线性代数与优化/概念/链式法则|链式法则]]
- [[06 - 深度学习/概念/反向传播|反向传播]]

## 备注

- 原题已核对 [[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=225|印刷207／PDF物理225]]；所引正文公式的实际位置见 `source_refs`。
- 原题引用式(6.33)的单输出误差，同时沿用式(6.31)中的输出编号 $k$；解答分别列出单样本、批量和独立多输出情形，避免把输出编号与样本求和混淆。
- `source_status: verified` 只指本题原文、所列公式与定位核对，不表示整章或整书理论全部核验。解答未使用配套答案册；个人学习状态保留 `not-started`。
