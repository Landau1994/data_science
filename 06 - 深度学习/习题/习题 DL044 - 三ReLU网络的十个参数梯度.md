---
title: "习题 DL044：三ReLU网络的十个参数梯度"
topic: "deep-learning"
topic_label: "深度学习"
difficulty: "intermediate"
status: "not-started"
tags:
  - exercise
  - deep-learning
source: "Understanding Deep Learning（2026-02-08修订稿），Problem 6.5，印刷95／PDF物理109"
source_id: "DS001"
source_chapter: 6
source_exercise: "6.5"
source_refs: ["DS001 Problem 6.5，印刷95/PDF109"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-10-28"
---

# 习题 DL044：三ReLU网络的十个参数梯度

## 题目

### 英文原题

> [!question] 英文原题
> **Problem 6.5\*** Compute the derivatives of the least squares loss with respect to the ten parameters of the simple neural network model introduced in equation 3.1:
> $$
> f[x,\phi]=\phi_0+\phi_1a[\theta_{10}+\theta_{11}x]+\phi_2a[\theta_{20}+\theta_{21}x]+\phi_3a[\theta_{30}+\theta_{31}x].\tag{6.23}
> $$
> Think carefully about what the derivative of the ReLU function $a[\bullet]$ will be.

### 中文转述

> [!question] 中文转述
> 对式(6.23)三ReLU模型求平方损失关于全部十个参数的导数，仔细说明ReLU折点的导数。



## 提示

> [!hint]- 提示
> 用 $z_{ij}=\theta_{j0}+\theta_{j1}x_i$ 和激活指示函数分组表达十个分量。

## 解答

> [!success]- 解答
> **独立推导。** 令 $L=\sum_i(f(x_i)-y_i)^2$、$z_{ij}=\theta_{j0}+\theta_{j1}x_i$、$r_i=f(x_i)-y_i$、$h_{ij}=\max(0,z_{ij})$。在所有 $z_{ij}\ne0$ 的参数位置，链式法则给
> $$
> \frac{\partial L}{\partial\phi_0}=2\sum_i r_i,\qquad
> \frac{\partial L}{\partial\phi_j}=2\sum_i r_i h_{ij}\quad(j=1,2,3),
> $$
> $$
> \frac{\partial L}{\partial\theta_{j0}}=2\sum_i r_i\phi_j{\bf1}_{z_{ij}>0},\qquad
> \frac{\partial L}{\partial\theta_{j1}}=2\sum_i r_i\phi_j x_i{\bf1}_{z_{ij}>0}.
> $$
> 这是 $1+3+3+3=10$ 个导数。ReLU在零点没有普通双侧导数；程序常选零作为反向传播约定。代入这一约定可实现更新，但不能将约定冒称为零点的经典导数。某些退化组合中总损失恰好可微，需另行检查。

## 相关概念

- [[06 - 深度学习/概念/神经网络|神经网络]]

## 备注

- 原题已逐页核对：[[附件/books/UnderstandingDeepLearning_02_09_26_C.pdf#page=109|印刷95／PDF109]]。来源核对仅覆盖本题原文和已列定位，学习状态不随归档改变。
