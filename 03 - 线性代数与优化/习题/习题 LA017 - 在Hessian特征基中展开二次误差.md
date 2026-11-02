---
title: "习题 LA017：在Hessian特征基中展开二次误差"
topic: linear-algebra-optimization
topic_label: 线性代数与优化
difficulty: beginner
status: not-started
tags: [exercise, linear-algebra-optimization]
source: "[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Bishop《深度学习：基础与概念》（DS003）]]"
source_id: DS003
source_chapter: 7
source_exercise: "7.1"
source_stars: 1
source_refs: ["DS003 Exercise 7.1，印刷230／PDF物理247", "DS003 §7.1.1，式(7.3)–(7.14)，印刷211–213/PDF228–230"]
source_status: verified
solution_status: independently-derived
created: 2026-11-02
---

# 习题 LA017：在Hessian特征基中展开二次误差

## 题目

### 英文原题

> [!question] 英文原题
> **7.1 (★)** By substituting (7.10) into (7.7) and using (7.8) and (7.9), show that the error function (7.7) can be written in the form (7.11).

### 中文转述

> [!question] 中文转述
> 把式(7.10)的位移特征向量展开代入二次误差(7.7)，利用特征方程(7.8)及正交归一式(7.9)，证明误差可写成(7.11)。

## 提示

> [!hint]- 提示
> 先写出双重求和，再用 $u_i^{\mathsf T}Hu_j=\lambda_j\delta_{ij}$ 消去交叉项。

## 解答

> [!success]- 解答
> **证明范围：独立推导。**
> 令实对称Hessian $H$ 的正交归一特征基为 $u_i$，满足 $Hu_i=\lambda_i u_i$、$u_i^{\mathsf T}u_j=\delta_{ij}$。式(7.7)、(7.10)分别是
> $$
> E(w)=E(w^\star)+\tfrac12(w-w^\star)^{\mathsf T}H(w-w^\star),\qquad
> w-w^\star=\sum_i\alpha_i u_i.
> $$
> 代入并逐项相乘得
> $$
> E(w)-E(w^\star)=\frac12\sum_{i,j}\alpha_i\alpha_j u_i^{\mathsf T}Hu_j
> =\frac12\sum_{i,j}\alpha_i\alpha_j\lambda_j\delta_{ij}
> =\frac12\sum_i\lambda_i\alpha_i^2.\tag{7.11}
> $$
> 这对精确二次函数是恒等式；若(7.7)只代表一般误差的局部Taylor二次模型，则此处亦是该模型的表达，不能把遗漏的高阶项当作恒为零。

## 相关概念

- [[03 - 线性代数与优化/概念/梯度与驻点|梯度与驻点]]
- [[03 - 线性代数与优化/概念/最优性条件|最优性条件]]

## 备注

- 原题已实际查看 [[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=247|印刷230／PDF物理247]]；所列依赖正文亦逐页核对，精确位置见 `source_refs`。
- 解答未使用配套答案册。`source_status: verified` 指本题原文与所列依赖的核对范围；独立推导不代表个人学习完成，状态保持 `not-started`。
