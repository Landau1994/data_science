---
title: "习题 DL224：逐样本更新外积Hessian的逆矩阵"
topic: deep-learning
topic_label: 深度学习
difficulty: advanced
status: not-started
tags: [exercise, deep-learning]
source: "[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Bishop《深度学习：基础与概念》（DS003）]]"
source_id: DS003
source_chapter: 8
source_exercise: "8.12"
source_stars: 3
source_refs: ["DS003 Exercise 8.12，印刷252／PDF物理269", "DS003 §8.1.6，式(8.36)–(8.41)，印刷242–244/PDF259–261"]
source_status: verified
solution_status: independently-derived
created: 2026-11-02
---

# 习题 DL224：逐样本更新外积Hessian的逆矩阵

## 题目

### 英文原题

> [!question] 英文原题
> **8.12 (★★★)** Consider the matrix identity
> $$
> (\mathbf M+\mathbf v\mathbf v^{\mathsf T})^{-1}=\mathbf M^{-1}-\frac{(\mathbf M^{-1}\mathbf v)(\mathbf v^{\mathsf T}\mathbf M^{-1})}{1+\mathbf v^{\mathsf T}\mathbf M^{-1}\mathbf v},\tag{8.80}
> $$
> which is simply a special case of the Woodbury identity (A.7). By applying (8.80) to the outer product approximation (8.40) for a Hessian matrix, derive a formula that allows the inverse of the Hessian matrix to be computed by making one pass through the training data and updating the inverse Hessian with each data point. Note that the algorithm can initialized using $\mathbf H=\alpha\mathbf I$ where $\alpha$ is a small constant, and that the results are not particularly sensitive to the precise value of $\alpha$.

### 中文转述

> [!question] 中文转述
> 矩阵恒等式(8.80)是Woodbury公式(A.7)的特例。把它应用于Hessian的外积近似(8.40)，推导一次遍历训练数据、随每个数据点逐步更新Hessian逆矩阵的公式。算法可以从 $\mathbf H=\alpha\mathbf I$ 初始化，其中 $\alpha$ 为小常数，结果对其精确取值不特别敏感。

## 提示

> [!hint]- 提示
> 设 $H_n=\alpha I+\sum_{i\le n}g_ig_i^{\mathsf T}$，真正保存的是 $P_n=H_n^{-1}$；初始化应为 $P_0=I/\alpha$。

## 解答

> [!success]- 解答
> **证明范围：独立推导。**
> 固定同一参数位置的梯度 $g_n=\nabla_wa_n$，取 $\alpha>0$。定义
> $$
> H_0=\alpha I,\quad P_0=\alpha^{-1}I,\qquad H_n=H_{n-1}+g_ng_n^{\mathsf T}.
> $$
> 逐步把题给(8.80)中的 $M,v$ 替换为 $H_{n-1},g_n$，得到
> $$
> u_n=P_{n-1}g_n,\qquad
> P_n=P_{n-1}-\frac{u_nu_n^{\mathsf T}}{1+g_n^{\mathsf T}P_{n-1}g_n}.
> $$
> 因为 $H_{n-1}\succ0$，分母至少为1，恒等式适用；归纳给出一次遍历后
> $$
> P_N=\left(\alpha I+\sum_{n=1}^Ng_ng_n^{\mathsf T}\right)^{-1}.
> $$
> 这是**带对角阻尼的外积近似矩阵**的精确逆，不是一般完整Hessian的精确逆。每个样本只需一次矩阵向量乘与秩一更新，约 $O(W^2)$ 运算，存储 $O(W^2)$，总计 $O(NW^2)$；无需在每步重新做 $O(W^3)$ 的一般求逆。若遍历中同时改变网络权重，则梯度来自不同参数点，最终不再是一个固定点的Hessian近似。
>
> 原题关于小 $\alpha$ 不敏感的说法有条件。若 $G=\sum_ng_ng_n^{\mathsf T}\succ0$ 且 $\alpha\ll\lambda_{\min}(G)$，逆特征值由 $1/\lambda_i$ 改成 $1/(\lambda_i+\alpha)$，相对变化为 $\alpha/(\lambda_i+\alpha)$，可控。若 $G$ 奇异，其零空间上的逆为 $1/\alpha$，对 $\alpha$ 极敏感且 $\alpha\downarrow0$ 发散；不能宣称一般不敏感，亦不能把极限当成伪逆。

## 相关概念

- [[03 - 线性代数与优化/概念/梯度与驻点|梯度与驻点]]
- [[06 - 深度学习/概念/反向传播|反向传播]]

## 备注

- 原题已实际查看 [[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=269|印刷252／PDF物理269]]；所列依赖正文亦逐页核对，精确位置见 `source_refs`。
- 原文“can initialized”语法照录；初始化H与初始化其逆的区别、α的条件和奇异边界已说明。
- 解答未使用配套答案册。`source_status: verified` 指本题原文与所列依赖的核对范围；独立推导不代表个人学习完成，状态保持 `not-started`。
