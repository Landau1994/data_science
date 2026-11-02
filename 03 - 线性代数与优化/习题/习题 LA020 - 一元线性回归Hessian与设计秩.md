---
title: "习题 LA020：一元线性回归Hessian与设计秩"
topic: linear-algebra-optimization
topic_label: 线性代数与优化
difficulty: intermediate
status: not-started
tags: [exercise, linear-algebra-optimization]
source: "[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Bishop《深度学习：基础与概念》（DS003）]]"
source_id: DS003
source_chapter: 7
source_exercise: "7.4"
source_stars: 2
source_refs: ["DS003 Exercise 7.4，印刷230／PDF物理247", "DS003 §7.1.1，式(7.3)–(7.14)，印刷211–213/PDF228–230"]
source_status: verified
solution_status: independently-derived
created: 2026-11-02
---

# 习题 LA020：一元线性回归Hessian与设计秩

## 题目

### 英文原题

> [!question] 英文原题
> **7.4 (★★)** Consider a linear regression model with a single input variable $x$ and a single output variable $y$ of the form
> $$
> y(x,w,b)=wx+b\tag{7.61}
> $$
> together with a sum-of-squares error function given by
> $$
> E(w,b)=\frac12\sum_{n=1}^N\{y(x_n,w,b)-t_n\}^2.\tag{7.62}
> $$
> Derive expressions for the elements of the $2\times2$ Hessian matrix given by the second derivatives of the error function with respect to the weight parameter $w$ and bias parameter $b$. Show that the trace and the determinant of this Hessian are both positive. Since the trace represents the sum of the eigenvalue and the determinant corresponds to the product of the eigenvalues, then both eigenvalues are positive and hence the stationary point of the error function is a minimum.

### 中文转述

> [!question] 中文转述
> 考虑式(7.61)的单输入、单输出线性模型 $y(x,w,b)=wx+b$，及平方和误差(7.62)。推导误差关于权重 $w$、偏置 $b$ 的二阶导数，给出 $2\times2$ Hessian的各元素。证明其迹和行列式都为正；由于迹是特征值之和、行列式是特征值之积，两个特征值均为正，从而误差驻点为极小点。

## 提示

> [!hint]- 提示
> 行列式可写成 $N\sum_n(x_n-\bar x)^2$。所有输入相同时会发生什么？

## 解答

> [!success]- 解答
> **证明范围：独立推导。**
> 设 $N\ge1$，对参数顺序 $(w,b)$ 直接求导，得到
> $$
> H=\begin{pmatrix}\sum_n x_n^2&\sum_n x_n\\\sum_n x_n&N\end{pmatrix},\quad
> \operatorname{tr}H=\sum_nx_n^2+N>0,
> $$
> $$
> \det H=N\sum_nx_n^2-(\sum_nx_n)^2=N\sum_n(x_n-\bar x)^2\ge0.
> $$
> 因此行列式**严格为正需要至少两个不同的输入值**，亦即带截距设计矩阵 $X=[x,\mathbf1]$ 满列秩。该条件下，实特征值乘积正、和正，故两者均正；$H=X^{\mathsf T}X\succ0$，误差为严格凸二次函数，唯一驻点就是唯一全局极小点。
>
> 若所有 $x_n=c$，预测仅依赖 $cw+b$，Hessian秩为1，行列式为0。最小值仍存在，由 $cw+b=\bar t$ 的整条直线取得；若 $N=1$ 亦如此。一般地，因误差等于 $\tfrac12\|X\theta-t\|^2$，任意驻点 $X^{\mathsf T}(X\theta-t)=0$ 满足
> $$
> E(\theta+h)-E(\theta)=\tfrac12\|Xh\|^2\ge0,
> $$
> 无须正定即可判定为全局极小。故原题未说明输入变异时，“determinant positive”需补假设。

## 相关概念

- [[03 - 线性代数与优化/概念/正规方程|正规方程]]
- [[03 - 线性代数与优化/概念/梯度与驻点|梯度与驻点]]
- [[03 - 线性代数与优化/概念/凸函数|凸函数]]

## 备注

- 原题已实际查看 [[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=247|印刷230／PDF物理247]]；所列依赖正文亦逐页核对，精确位置见 `source_refs`。
- 原题未给设计满秩条件；秩亏边界已在解答中单独处理。
- 解答未使用配套答案册。`source_status: verified` 指本题原文与所列依赖的核对范围；独立推导不代表个人学习完成，状态保持 `not-started`。
