---
title: "习题 LA021：逻辑回归Hessian的符号与秩条件"
topic: linear-algebra-optimization
topic_label: 线性代数与优化
difficulty: intermediate
status: not-started
tags: [exercise, linear-algebra-optimization]
source: "[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Bishop《深度学习：基础与概念》（DS003）]]"
source_id: DS003
source_chapter: 7
source_exercise: "7.5"
source_stars: 2
source_refs: ["DS003 Exercise 7.5，印刷230–231／PDF物理247–248", "DS003 §7.1.1，式(7.3)–(7.14)，印刷211–213/PDF228–230", "DS003 逻辑Sigmoid定义式(6.13)，印刷183/PDF201"]
source_status: verified
solution_status: independently-derived
created: 2026-11-02
---

# 习题 LA021：逻辑回归Hessian的符号与秩条件

## 题目

### 英文原题

> [!question] 英文原题
> **7.5 (★★)** Consider a single-layer classification model with a single input variable $x$ and a single output variable $y$ of the form
> $$
> y(x,w,b)=\sigma(wx+b)\tag{7.63}
> $$
> where $\sigma(\cdot)$ is the logistic sigmoid function defined by (5.42) together with a cross-entropy error function given by
> $$
> E(w,b)=\sum_{n=1}^N\{t_n\ln y(x_n,w,b)+(1-t_n)\ln(1-y(x_n,w,b))\}.\tag{7.64}
> $$
> Derive expressions for the elements of the $2\times2$ Hessian matrix given by the second derivatives of the error function with respect to the weight parameter $w$ and bias parameter $b$. Show that the trace and the determinant of this Hessian are both positive. Since the trace represents the sum of the eigenvalue and the determinant corresponds to the product of the eigenvalues, then both eigenvalues are positive and hence the stationary point of the error function is a minimum.

### 中文转述

> [!question] 中文转述
> 考虑单输入、单输出的单层分类模型(7.63)：$y(x,w,b)=\sigma(wx+b)$，其中 $\sigma$ 是(5.42)定义的逻辑Sigmoid函数；误差函数由(7.64)给出：
> $$
> E(w,b)=\sum_{n=1}^N\{t_n\ln y(x_n,w,b)+(1-t_n)\ln(1-y(x_n,w,b))\}.
> $$
> 推导误差关于权重 $w$、偏置 $b$ 的二阶导数，给出 $2\times2$ Hessian的各元素。证明其迹和行列式都为正；由于迹是特征值之和、行列式是特征值之积，两个特征值均为正，从而误差驻点为极小点。

## 提示

> [!hint]- 提示
> 先核对(7.64)是负对数似然还是对数似然。对正确的负对数似然，其Hessian为 $X^{\mathsf T}RX$。

## 解答

> [!success]- 解答
> **证明范围：独立推导。**
> **先处理原式符号。** 原题(7.64)没有负号，实际写的是伯努利对数似然。令 $L=-E$ 为要最小化的交叉熵，$a_n=wx_n+b$、$y_n=\sigma(a_n)=1/(1+e^{-a_n})$、$r_n=y_n(1-y_n)$。有限参数保证 $r_n>0$，且链式法则给出
> $$
> \nabla L=\sum_n(y_n-t_n)\binom{x_n}{1},\qquad
> H_L=\begin{pmatrix}\sum_nr_nx_n^2&\sum_nr_nx_n\\\sum_nr_nx_n&\sum_nr_n\end{pmatrix}.
> $$
> 因此 $\operatorname{tr}H_L=\sum_nr_n(x_n^2+1)>0$（$N\ge1$）。令 $R=\sum_nr_n$、$\bar x_r=\sum_nr_nx_n/R$，则
> $$
> \det H_L=R\sum_nr_n(x_n-\bar x_r)^2.
> $$
> 若至少两个输入不同，此值严格为正，故两个特征值均正，$L$严格凸；任何有限驻点为唯一全局最小。若输入全相同，则行列式为0，$L$仅凸而非关于两参数严格凸。
>
> 按原式 $E$ 本身求导，$H_E=-H_L$：迹严格**负**；满秩时行列式仍正，而两个特征值均负，驻点为极大点。因此原题要求的正迹和极小结论无法由所印(7.64)得到，须先添加负号。
>
> 严格凸不保证有限驻点存在。例如严格可分数据可让分类正确概率趋1，使 $L\downarrow0$ 而有限参数始终 $L>0$；参数会逃向无穷。这里判定的是“若有限驻点存在”时的性质。

## 相关概念

- [[04 - 统计学习/概念/交叉熵|交叉熵]]
- [[06 - 深度学习/概念/激活函数|激活函数]]
- [[03 - 线性代数与优化/概念/梯度与驻点|梯度与驻点]]
- [[03 - 线性代数与优化/概念/凸函数|凸函数]]

## 备注

- 原题已实际查看 [[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=247|印刷230–231／PDF物理247–248]]；所列依赖正文亦逐页核对，精确位置见 `source_refs`。
- 原题跨印刷230–231/PDF247–248。式(7.64)漏负号且未给设计秩条件；已保留原式并分别解释。
- 解答未使用配套答案册。`source_status: verified` 指本题原文与所列依赖的核对范围；独立推导不代表个人学习完成，状态保持 `not-started`。
