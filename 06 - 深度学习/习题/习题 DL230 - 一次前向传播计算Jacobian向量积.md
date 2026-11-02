---
title: "习题 DL230：一次前向传播计算Jacobian向量积"
topic: deep-learning
topic_label: 深度学习
difficulty: intermediate
status: not-started
tags: [exercise, deep-learning]
source: "[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Bishop《深度学习：基础与概念》（DS003）]]"
source_id: DS003
source_chapter: 8
source_exercise: "8.18"
source_stars: 2
source_refs: ["DS003 Exercise 8.18，印刷252／PDF物理269", "DS003 §8.2.1，式(8.57)、(8.66)–(8.67)，印刷247–249/PDF264–266"]
source_status: verified
solution_status: independently-derived
created: 2026-11-02
---

# 习题 DL230：一次前向传播计算Jacobian向量积

## 题目

### 英文原题

> [!question] 英文原题
> **8.18 (★★)** By expressing an arbitrary vector $\mathbf r=(r_1,\ldots,r_D)^{\mathsf T}$ as a linear combination of the unit vectors $\mathbf e_i$, where $i=1,\ldots,D$, show that the product of the Jacobian of a function with $\mathbf r$ in the form (8.67) can be evaluated using a single pass of forward-mode automatic differentiation by setting $\dot{\mathbf x}=\mathbf r$.

### 中文转述

> [!question] 中文转述
> 将任意向量 $r=(r_1,\ldots,r_D)^{\mathsf T}$ 展开为单位向量 $e_i$ 的线性组合，证明(8.67)的Jacobian向量积可通过一次前向模式自动微分计算，只需设置输入切变量 $\dot x=r$。

## 提示

> [!hint]- 提示
> 固定原变量的求值点时，每个切变量递推都对输入种子线性。

## 解答

> [!success]- 解答
> **证明范围：独立推导。**
> 设 $f:\mathbb R^D\to\mathbb R^K$ 在输入 $x$ 及所执行计算轨迹上可微，Jacobian $J_{ki}=\partial f_k/\partial x_i$。由于 $r=\sum_ir_ie_i$，线性映射的性质给
> $$
> Jr=\sum_ir_iJe_i=\sum_ir_i\frac{\partial f}{\partial x_i}.
> $$
> 构造路径 $x(t)=x+tr$，则 $\dot x(0)=r$。对每个中间节点 $v_j=\phi_j((v_i)_{i\in\operatorname{pa}(j)})$，前向链式法则为
> $$
> \dot v_j=\sum_{i\in\operatorname{pa}(j)}\frac{\partial\phi_j}{\partial v_i}\dot v_i.
> $$
> 固定所有原变量后，这一递推对种子 $r$ 线性。沿图归纳，输出切变量就是 $df(x+tr)/dt|_{t=0}=Jr$，故一次前向传播足够。无需先分别求全部 $D$ 列再相加；只需每个节点保存一个方向切变量。
>
> 原书(8.67)左侧误印为 $J$，但右侧是 $K\times D$ 矩阵乘 $D$ 维向量，正确左侧应为 $Jr$。结论也不表示一次方向传播可恢复完整Jacobian：一般完整矩阵仍需 $D$ 个线性独立种子或同时传播 $D$ 维切变量。

## 相关概念

- [[06 - 深度学习/概念/自动微分|自动微分]]
- [[03 - 线性代数与优化/概念/链式法则|链式法则]]

## 备注

- 原题已实际查看 [[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=269|印刷252／PDF物理269]]；所列依赖正文亦逐页核对，精确位置见 `source_refs`。
- (8.67)左侧矩阵/向量维数的源误已在解答说明；英文原题保留其引用。
- 解答未使用配套答案册。`source_status: verified` 指本题原文与所列依赖的核对范围；独立推导不代表个人学习完成，状态保持 `not-started`。
