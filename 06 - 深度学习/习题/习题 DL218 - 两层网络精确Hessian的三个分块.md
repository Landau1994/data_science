---
title: "习题 DL218：两层网络精确Hessian的三个分块"
topic: deep-learning
topic_label: 深度学习
difficulty: advanced
status: not-started
tags: [exercise, deep-learning]
source: "[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Bishop《深度学习：基础与概念》（DS003）]]"
source_id: DS003
source_chapter: 8
source_exercise: "8.6"
source_stars: 3
source_refs: ["DS003 Exercise 8.6，印刷251／PDF物理268", "DS003 §8.1.6，式(8.36)–(8.41)，印刷242–244/PDF259–261", "DS003 §8.1.3，两层网络式(8.18)–(8.20)，印刷238/PDF255"]
source_status: verified
solution_status: independently-derived
created: 2026-11-02
---

# 习题 DL218：两层网络精确Hessian的三个分块

## 题目

### 英文原题

> [!question] 英文原题
> **8.6 (★★★)** Consider a two-layer neural network, and define the quantities
> $$
> \delta_k=\frac{\partial E_n}{\partial a_k},\qquad M_{kk'}\equiv\frac{\partial^2E_n}{\partial a_k\partial a_{k'}}.\tag{8.77}
> $$
> Derive expressions for the elements of the Hessian matrix expressed in terms of $\delta_k$ and $M_{kk'}$ for elements in which (i) both weights are in the second layer, (ii) both weights are in the first layer, and (iii) one weight is in each layer.

### 中文转述

> [!question] 中文转述
> 两层网络定义输出预激活的一阶导数 $\delta_k=\partial E_n/\partial a_k$ 及二阶导数 $M_{kk'}=\partial^2E_n/(\partial a_k\partial a_{k'})$。分别推导Hessian中：(i) 两权重均在第二层；(ii) 均在第一层；(iii) 一个位于各层的元素公式，结果以 $\delta$ 与 $M$ 表示。

## 提示

> [!hint]- 提示
> 先写通用二阶链式法则：$H_{pq}=\sum_{kl}M_{kl}A_{k,p}A_{l,q}+\sum_k\delta_kA_{k,pq}$。混合层分块不可遗漏第二项。

## 解答

> [!success]- 解答
> **证明范围：独立推导。**
> 固定一个样本，写 $a_j=\sum_iU_{ji}x_i$、$z_j=h(a_j)$、$A_k=\sum_jV_{kj}z_j$。用大写 $A_k$ 区分输出预激活，题面 $\delta_k=E_{,A_k}$、$M_{kl}=E_{,A_kA_l}$，假设相关映射二阶可微且损失不显式依赖权重。记 $h'_j=h'(a_j)$、$h''_j=h''(a_j)$，隐藏单元索引 $j,m$ 不含固定偏置节点。
>
> 对任意参数 $p,q$，二阶链式法则给
> $$
> E_{,pq}=\sum_{k,l}M_{kl}A_{k,p}A_{l,q}+\sum_k\delta_kA_{k,pq}.
> $$
> **(i) 第二层—第二层。** $A_{r,V_{kj}}=\delta_{rk}z_j$ 且对两个 $V$ 的二阶导数为0，所以
> $$
> E_{,V_{kj}V_{lm}}=M_{kl}z_jz_m.
> $$
> **(ii) 第一层—第一层。** 有 $A_{k,U_{ji}}=V_{kj}h'_jx_i$ 及 $A_{k,U_{ji}U_{mp}}=\delta_{jm}V_{kj}h''_jx_ix_p$，因此
> $$
> E_{,U_{ji}U_{mp}}=x_ix_p\left[h'_jh'_m\sum_{k,l}V_{kj}M_{kl}V_{lm}
> +\delta_{jm}h''_j\sum_k\delta_kV_{kj}\right].
> $$
> **(iii) 第二层—第一层。** $A_{r,V_{kj}U_{mi}}=\delta_{rk}\delta_{jm}h'_jx_i$，故
> $$
> E_{,V_{kj}U_{mi}}=x_i\left[z_jh'_m\sum_lM_{kl}V_{lm}+\delta_{jm}\delta_kh'_j\right].
> $$
> 反向分块由对称性得到。这些是精确式，残差导数 $\delta$ 乘网络二阶导数的项没有丢弃。总误差 $\sum_nE_n$ 的Hessian对样本求和。第一层偏置可取 $x_0=1$；输出偏置 $V_{k0}$ 取 $z_0=1$、对任何 $U$ 的导数为0，因此其混合式只保留第一项。

## 相关概念

- [[06 - 深度学习/概念/反向传播|反向传播]]
- [[03 - 线性代数与优化/概念/链式法则|链式法则]]
- [[03 - 线性代数与优化/概念/梯度与驻点|梯度与驻点]]

## 备注

- 原题已实际查看 [[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=268|印刷251／PDF物理268]]；所列依赖正文亦逐页核对，精确位置见 `source_refs`。
- 解答未使用配套答案册。`source_status: verified` 指本题原文与所列依赖的核对范围；独立推导不代表个人学习完成，状态保持 `not-started`。
