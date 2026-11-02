---
title: "习题 DL219：含跳连网络的精确Hessian扩展"
topic: deep-learning
topic_label: 深度学习
difficulty: advanced
status: not-started
tags: [exercise, deep-learning]
source: "[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Bishop《深度学习：基础与概念》（DS003）]]"
source_id: DS003
source_chapter: 8
source_exercise: "8.7"
source_stars: 3
source_refs: ["DS003 Exercise 8.7，印刷251／PDF物理268", "DS003 §8.1.6，式(8.36)–(8.41)，印刷242–244/PDF259–261", "DS003 §8.1.3，两层网络式(8.18)–(8.20)，印刷238/PDF255"]
source_status: verified
solution_status: independently-derived
created: 2026-11-02
---

# 习题 DL219：含跳连网络的精确Hessian扩展

## 题目

### 英文原题

> [!question] 英文原题
> **8.7 (★★★)** Extend the results of Exercise 8.6 for the exact Hessian of a two-layer network to include skip-layer connections that go directly from inputs to outputs.

### 中文转述

> [!question] 中文转述
> 将习题8.6的两层网络精确Hessian公式扩展到含输入至输出直接跳连的情形。

## 提示

> [!hint]- 提示
> 新增 $A_k$ 中的线性项 $\sum_iS_{ki}x_i$，它关于隐藏权重的二阶导数为0。

## 解答

> [!success]- 解答
> **证明范围：独立推导。**
> 固定样本，明确网络为 $a_j=\sum_iU_{ji}x_i$、$z_j=h(a_j)$、$A_k=\sum_jV_{kj}z_j+\sum_iS_{ki}x_i$，并定义 $\delta_k=E_{,A_k}$、$M_{kl}=E_{,A_kA_l}$。对任意参数 $p,q$ 仍有精确恒等式
> $$
> E_{,pq}=\sum_{kl}M_{kl}A_{k,p}A_{l,q}+\sum_k\delta_kA_{k,pq}.
> $$
> 原有三个分块（所有 $\delta,M$ 必须用含跳连的新输出计算）完整写为
> $$
> E_{,V_{kj}V_{lm}}=M_{kl}z_jz_m,
> $$
> $$
> E_{,U_{ji}U_{mp}}=x_ix_p\left[h'_jh'_m\sum_{kl}V_{kj}M_{kl}V_{lm}
> +\delta_{jm}h''_j\sum_k\delta_kV_{kj}\right],
> $$
> $$
> E_{,V_{kj}U_{mi}}=x_i\left[z_jh'_m\sum_lM_{kl}V_{lm}+\delta_{jm}\delta_kh'_j\right].
> $$
> 这里 $h'_j=h'(a_j)$。新增参数导数为 $A_{r,S_{ki}}=\delta_{rk}x_i$，且它与所有参数的二阶导数为0。所以新三个分块为
> $$
> E_{,S_{ki}S_{lp}}=M_{kl}x_ix_p,\qquad
> E_{,S_{ki}V_{lj}}=M_{kl}x_iz_j,
> $$
> $$
> E_{,S_{ki}U_{jp}}=x_ix_ph'_j\sum_lM_{kl}V_{lj}.
> $$
> 对称位置交换参数索引即可。每个式子均由上述链式法则中代入一阶导数得到，新增分块没有额外 $\delta$ 项，因为 $A_{,S q}=0$。隐藏偏置用 $x_0=1$ 处理，固定隐藏常数节点导数为0；若同时用直连常数与原输出偏置，应合并它们，避免重复参数化。

## 相关概念

- [[06 - 深度学习/概念/反向传播|反向传播]]
- [[03 - 线性代数与优化/概念/链式法则|链式法则]]
- [[06 - 深度学习/概念/残差网络|残差网络]]

## 备注

- 原题已实际查看 [[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=268|印刷251／PDF物理268]]；所列依赖正文亦逐页核对，精确位置见 `source_refs`。
- 解答未使用配套答案册。`source_status: verified` 指本题原文与所列依赖的核对范围；独立推导不代表个人学习完成，状态保持 `not-started`。
