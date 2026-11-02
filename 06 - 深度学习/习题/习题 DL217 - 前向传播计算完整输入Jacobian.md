---
title: "习题 DL217：前向传播计算完整输入Jacobian"
topic: deep-learning
topic_label: 深度学习
difficulty: advanced
status: not-started
tags: [exercise, deep-learning]
source: "[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Bishop《深度学习：基础与概念》（DS003）]]"
source_id: DS003
source_chapter: 8
source_exercise: "8.5"
source_stars: 3
source_refs: ["DS003 Exercise 8.5，印刷251／PDF物理268", "DS003 §8.1.5，式(8.26)–(8.35)，印刷240–242/PDF257–259"]
source_status: verified
solution_status: independently-derived
created: 2026-11-02
---

# 习题 DL217：前向传播计算完整输入Jacobian

## 题目

### 英文原题

> [!question] 英文原题
> **8.5 (★★★)** In Section 8.1.5, we derived a procedure for evaluating the Jacobian matrix of a neural network using a backpropagation procedure. Derive an alternative formalism for finding the Jacobian based on forward propagation equations.

### 中文转述

> [!question] 中文转述
> §8.1.5通过反向传播计算网络Jacobian。推导基于前向传播方程的另一套计算方法。

## 提示

> [!hint]- 提示
> 对每个节点附带其关于所有输入的导数向量；输入节点从单位矩阵开始。

## 解答

> [!success]- 解答
> **证明范围：独立推导。**
> 设前馈图每个节点满足 $a_j=\sum_iw_{ji}z_i$、$z_j=h_j(a_j)$，参数在本题求输入导数时固定，激活在所取点可微。对每个输入坐标 $x_p$ 定义 $F_{jp}=\partial z_j/\partial x_p$。输入节点初始化 $F_{ip}=\delta_{ip}$，常数偏置节点的导数为0。按拓扑顺序前向计算
> $$
> \frac{\partial a_j}{\partial x_p}=\sum_iw_{ji}F_{ip},\qquad
> F_{jp}=h_j'(a_j)\sum_iw_{ji}F_{ip}.
> $$
> 因此到达输出节点时，$J_{kp}=\partial y_k/\partial x_p$ 就是相应 $F_{kp}$。该递推由节点链式法则直接成立，按拓扑顺序归纳即覆盖所有路径，也适用于跳连。
>
> 分层形式令 $F^{(0)}=I_D$，逐层有
> $$
> F^{(l)}=D_lW^{(l)}F^{(l-1)},\quad
> J=D_LW^{(L)}\cdots D_1W^{(1)}.
> $$
> 其中 $D_l$ 为逐坐标激活导数对角阵；耦合输出用完整激活Jacobian替换。可一次传播所有 $D$ 列，也可分别以单位方向作 $D$ 次前向模式传播。若边数为 $W$，完整Jacobian的导数运算量通常为 $O(DW)$，输入少、输出多时有优势。

## 相关概念

- [[06 - 深度学习/概念/自动微分|自动微分]]
- [[06 - 深度学习/概念/前向传播|前向传播]]
- [[03 - 线性代数与优化/概念/链式法则|链式法则]]

## 备注

- 原题已实际查看 [[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=268|印刷251／PDF物理268]]；所列依赖正文亦逐页核对，精确位置见 `source_refs`。
- 解答未使用配套答案册。`source_status: verified` 指本题原文与所列依赖的核对范围；独立推导不代表个人学习完成，状态保持 `not-started`。
