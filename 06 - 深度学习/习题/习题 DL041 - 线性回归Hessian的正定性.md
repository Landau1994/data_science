---
title: "习题 DL041：线性回归Hessian的正定性"
topic: "deep-learning"
topic_label: "深度学习"
difficulty: "intermediate"
status: "not-started"
tags:
  - exercise
  - deep-learning
source: "Understanding Deep Learning（2026-02-08修订稿），Problem 6.2，印刷94／PDF物理108"
source_id: "DS001"
source_chapter: 6
source_exercise: "6.2"
source_refs: ["DS001 Problem 6.2，印刷94/PDF108"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-10-28"
---

# 习题 DL041：线性回归Hessian的正定性

## 题目

### 英文原题

> [!question] 英文原题
> **Problem 6.2** A surface is guaranteed to be convex if the eigenvalues of the Hessian $\mathbf H[\phi]$ are positive everywhere. In this case, the surface has a unique minimum, and optimization is easy. Find an algebraic expression for the Hessian matrix,
> $$
> \mathbf H[\phi]=\begin{pmatrix}
> \frac{\partial^2L}{\partial\phi_0^2}&\frac{\partial^2L}{\partial\phi_0\partial\phi_1}\\
> \frac{\partial^2L}{\partial\phi_1\partial\phi_0}&\frac{\partial^2L}{\partial\phi_1^2}
> \end{pmatrix},\tag{6.20}
> $$
> for the linear regression model (equation 6.5). Prove that this function is convex when there are at least two different samples $x_i$ by showing that the eigenvalues are always positive. This can be done by showing that both the trace and the determinant of the matrix are positive.

### 中文转述

> [!question] 中文转述
> 为式(6.5)线性回归损失求Hessian；当至少两个输入值不同时，用迹、行列式证明特征值均正，从而证明凸性。原文关于唯一极小值的一般措辞保留，解答区分存在性。



## 提示

> [!hint]- 提示
> 对上一题梯度再求导，并将行列式写成中心化平方和。

## 解答

> [!success]- 解答
> **独立推导。** 令 $I\ge2$、$\bar x=I^{-1}\sum_i x_i$。二次求导得
> $$
> H=2\begin{pmatrix}I&\sum_i x_i\\\sum_i x_i&\sum_i x_i^2\end{pmatrix}.
> $$
> 迹为 $2(I+\sum x_i^2)>0$；行列式为
> $$
> 4\left[I\sum x_i^2-(\sum x_i)^2\right]
> =4I\sum_i(x_i-\bar x)^2>0.
> $$
> $H$ 对称，故特征值实数；乘积正、和正迫使两者都正。损失是具有正定二次项的严格凸二次函数，且趋向无穷时也趋向无穷，所以唯一极小解存在，满足正规方程。全部 $x_i$ 相同时仍为凸但Hessian退化，参数一般不唯一。原文泛称“处处正Hessian必有唯一minimum”缺少存在性条件，如 $e^x$ 没有有限极小点；本题正定二次型则确有唯一解。

## 相关概念

- [[06 - 深度学习/概念/神经网络|神经网络]]
- [[03 - 线性代数与优化/概念/链式法则|链式法则]]

## 备注

- 原题已逐页核对：[[附件/books/UnderstandingDeepLearning_02_09_26_C.pdf#page=108|印刷94／PDF108]]。来源核对仅覆盖本题原文和已列定位，学习状态不随归档改变。
