---
title: "习题 DL220：多输出平方损失的外积Hessian近似"
topic: deep-learning
topic_label: 深度学习
difficulty: intermediate
status: not-started
tags: [exercise, deep-learning]
source: "[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Bishop《深度学习：基础与概念》（DS003）]]"
source_id: DS003
source_chapter: 8
source_exercise: "8.8"
source_stars: 2
source_refs: ["DS003 Exercise 8.8，印刷251／PDF物理268", "DS003 §8.1.6，式(8.36)–(8.41)，印刷242–244/PDF259–261"]
source_status: verified
solution_status: independently-derived
created: 2026-11-02
---

# 习题 DL220：多输出平方损失的外积Hessian近似

## 题目

### 英文原题

> [!question] 英文原题
> **8.8 (★★)** The outer product approximation to the Hessian matrix for a neural network using a sum-of-squares error function is given by (8.40). Extend this result for multiple outputs.

### 中文转述

> [!question] 中文转述
> 式(8.40)给出平方和损失网络的Hessian外积近似（outer product approximation）。把它推广到多输出情形。

## 提示

> [!hint]- 提示
> 先对每个样本、每个输出的平方残差求两次导数，再指出近似丢掉哪一项。

## 解答

> [!success]- 解答
> **证明范围：独立推导。**
> 设 $y_n(w)\in\mathbb R^K$，$E=\tfrac12\sum_{n,k}(y_{nk}-t_{nk})^2$，每个输出二阶可微。记 $g_{nk}=\nabla_w y_{nk}$，则直接求导得到精确Hessian
> $$
> H=\sum_{n,k}\left[g_{nk}g_{nk}^{\mathsf T}+(y_{nk}-t_{nk})\nabla_w^2y_{nk}\right].
> $$
> 外积（Gauss–Newton）近似舍去第二项，得到
> $$
> H\simeq G=\sum_{n,k}g_{nk}g_{nk}^{\mathsf T}=\sum_nJ_n^{\mathsf T}J_n,
> $$
> 其中 $J_n\in\mathbb R^{K\times W}$ 为输出对参数的Jacobian。对线性输出激活 $y_{nk}=a_{nk}$，这正是(8.40)的多输出版。任意 $v$ 满足 $v^{\mathsf T}Gv=\sum_n\|J_nv\|^2\ge0$，但未必正定，故不能保证可逆。
>
> 若每个训练残差为0，或输出对参数是仿射函数，则舍去项精确为0。其他情形只是近似；误差范数满足 $\|H-G\|\le\sum_{nk}|y_{nk}-t_{nk}|\,\|\nabla^2y_{nk}\|$，所以“小残差”仍需相应二阶导数受控。若损失取样本平均，所有式子相应除以 $N$。

## 相关概念

- [[06 - 深度学习/概念/反向传播|反向传播]]
- [[03 - 线性代数与优化/概念/梯度与驻点|梯度与驻点]]

## 备注

- 原题已实际查看 [[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=268|印刷251／PDF物理268]]；所列依赖正文亦逐页核对，精确位置见 `source_refs`。
- 解答未使用配套答案册。`source_status: verified` 指本题原文与所列依赖的核对范围；独立推导不代表个人学习完成，状态保持 `not-started`。
