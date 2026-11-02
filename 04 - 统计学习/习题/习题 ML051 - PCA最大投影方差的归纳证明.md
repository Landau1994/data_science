---
title: 习题 ML051：PCA最大投影方差的归纳证明
topic: statistical-learning
topic_label: 统计学习
difficulty: intermediate
status: not-started
tags:
- exercise
- statistical-learning
source: '[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Deep Learning: Foundations and Concepts（DS003）]]'
source_id: DS003
source_chapter: 16
source_exercise: '16.1'
source_stars: 2
source_refs:
- DS003 Exercise 16.1，印刷527、528/PDF541、542
- DS003 §16.1.1，式(16.2)–(16.6)，印刷498/PDF512
source_status: verified
solution_status: independently-derived
created: '2026-11-02'
---

# 习题 ML051：PCA最大投影方差的归纳证明

## 题目

### 英文原题

> [!question] 英文原题
> **Exercise 16.1（★★）** In this exercise, we use proof by induction to show that the linear projection onto an $M$-dimensional subspace that maximizes the variance of the projected data is defined by the $M$ eigenvectors of the data covariance matrix $\mathbf S$, given by (16.3), corresponding to the $M$ largest eigenvalues. In Section 16.1, this result was proven for $M=1$. Now suppose the result holds for some general value of $M$ and show that it consequently holds for dimensionality $M+1$. To do this, first set the derivative of the variance of the projected data with respect to a vector $\mathbf u_{M+1}$ defining the new direction in data space equal to zero. This should be done subject to the constraints that $\mathbf u_{M+1}$ are orthogonal to the existing vectors $\mathbf u_1,\ldots,\mathbf u_M$, and also that it is normalized to unit length. Use Lagrange multipliers to enforce these constraints. Then make use of the orthonormality properties of the vectors $\mathbf u_1,\ldots,\mathbf u_M$ to show that the new vector $\mathbf u_{M+1}$ is an eigenvector of $\mathbf S$. Finally, show that the variance is maximized if the eigenvector is chosen to be the one corresponding to eigenvalue $\lambda_{M+1}$ where the eigenvalues have been ordered in decreasing value.

### 中文转述

> [!question] 中文转述
> **原题16.1。** 用归纳法证明：主成分分析（principal component analysis，PCA）中，最大化投影方差的 $M$ 维子空间由协方差矩阵 $S$ 的前 $M$ 大特征值的特征向量张成。已知 $M=1$，假定 $M$ 维结论成立，对新方向 $u_{M+1}$ 加上单位长度及与已有方向正交的约束，用拉格朗日乘子求驻点；再利用已有方向的正交性证明它是 $S$ 的特征向量，最后说明应取按降序排列的 $\lambda_{M+1}$。

## 提示

> [!hint]- 提示 1
> 设拉格朗日函数为 $u^TSu-\lambda(u^Tu-1)-2\sum_i\gamma_i u_i^Tu$，左乘已有 $u_j^T$ 消去乘子。

## 解答

> [!success]- 解答
> **独立推导。** $S=N^{-1}\sum_n(x_n-\bar x)(x_n-\bar x)^T$ 为实对称半正定矩阵。取正交特征基 $v_i$，$\lambda_1\geq\cdots\geq\lambda_D$。一维情况由Rayleigh商最大值 $\lambda_1$ 成立。
>
> 假设已取 $u_i=v_i$（$i\leq M$），新方向 $u$ 约束为 $u^Tu=1,u_i^Tu=0$。新增投影方差是 $u^TSu$，原先各方向的方差不变。驻点条件为
> $$Su=\lambda u+\sum_{i=1}^M\gamma_i u_i.$$
> 左乘 $u_j^T$，由 $u_j^TSu=\lambda_j u_j^Tu=0$ 和正交性得 $\gamma_j=0$，所以 $Su=\lambda u$。任一可行 $u=\sum_{i>M}c_iv_i$ 满足 $\sum c_i^2=1$，故 $u^TSu=\sum_{i>M}\lambda_i c_i^2\leq\lambda_{M+1}$，取 $u=v_{M+1}$ 达到。
>
> 为保证这也给出**所有** $(M+1)$ 维子空间的全局最大值，任取正交列矩阵 $U$，记 $a_i=\|U^Tv_i\|^2$，则 $0\leq a_i\leq1$、$\sum_i a_i=M+1$，总方差 $\operatorname{Tr}(U^TSU)=\sum_i\lambda_i a_i\leq\sum_{i=1}^{M+1}\lambda_i$。上述归纳构造恰达到界，结论成立。重特征值时可在对应特征空间中任取正交基；若截断处有并列值，最优子空间可能不唯一。

## 相关概念

- [[04 - 统计学习/概念/无监督学习|无监督学习]]
- [[05 - 概率模型与推断/概念/潜变量|潜变量]]
- [[03 - 线性代数与优化/概念/最优性条件|最优性条件]]

## 备注

- 原题及星数：[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=541|印刷527、528／PDF541、542]]；题页及引用正文已实际查看原PDF图像，精确定位见 `source_refs`。
- `source_status: verified` 仅指本题及所列实际核对范围；解答独立推导，不构成用户已完成学习，状态保持 `not-started`。
