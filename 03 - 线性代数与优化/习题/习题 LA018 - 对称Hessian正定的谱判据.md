---
title: "习题 LA018：对称Hessian正定的谱判据"
topic: linear-algebra-optimization
topic_label: 线性代数与优化
difficulty: beginner
status: not-started
tags: [exercise, linear-algebra-optimization]
source: "[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Bishop《深度学习：基础与概念》（DS003）]]"
source_id: DS003
source_chapter: 7
source_exercise: "7.2"
source_stars: 1
source_refs: ["DS003 Exercise 7.2，印刷230／PDF物理247", "DS003 §7.1.1，式(7.3)–(7.14)，印刷211–213/PDF228–230"]
source_status: verified
solution_status: independently-derived
created: 2026-11-02
---

# 习题 LA018：对称Hessian正定的谱判据

## 题目

### 英文原题

> [!question] 英文原题
> **7.2 (★)** Consider a Hessian matrix $\mathbf H$ with eigenvector equation (7.8). By setting the vector $\mathbf v$ in (7.14) equal to each of the eigenvectors $\mathbf u_i$ in turn, show that $\mathbf H$ is positive definite if, and only if, all its eigenvalues are positive.

### 中文转述

> [!question] 中文转述
> 设Hessian满足(7.8)。在(7.14)中依次令 $v$ 为各特征向量，证明实对称 $H$ 正定当且仅当所有特征值为正。

## 提示

> [!hint]- 提示
> 必要性用一个特征向量；充分性需要把任意非零向量展开成完整特征基。

## 解答

> [!success]- 解答
> **证明范围：独立推导。**
> 这里正定（positive definite）约定为对每个 $v\ne0$ 都有 $v^{\mathsf T}Hv>0$，零向量必须排除。设 $Hu_i=\lambda_i u_i$、$u_i^{\mathsf T}u_j=\delta_{ij}$，完整实正交特征基是已核对正文的输入。
>
> 若 $H\succ0$，代入非零单位向量 $v=u_i$ 得 $u_i^{\mathsf T}Hu_i=\lambda_i>0$。
>
> 反过来，若每个 $\lambda_i>0$，对任意 $v=\sum_i c_i u_i\ne0$，至少一个 $c_i\ne0$，于是
> $$
> v^{\mathsf T}Hv=\sum_i\lambda_i c_i^2>0.\tag{7.14}
> $$
> 故两条件等价。该结论使用实对称性；对任意非对称矩阵仅检查特征值符号不足以判断二次型正定。

## 相关概念

- [[03 - 线性代数与优化/概念/梯度与驻点|梯度与驻点]]
- [[03 - 线性代数与优化/概念/最优性条件|最优性条件]]

## 备注

- 原题已实际查看 [[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=247|印刷230／PDF物理247]]；所列依赖正文亦逐页核对，精确位置见 `source_refs`。
- 正文(7.12)把范围写作“for all v”，应排除零向量；解答已明确约定。
- 解答未使用配套答案册。`source_status: verified` 指本题原文与所列依赖的核对范围；独立推导不代表个人学习完成，状态保持 `not-started`。
