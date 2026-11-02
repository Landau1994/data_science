---
title: "习题 DL223：Softmax交叉熵的广义GaussNewton矩阵"
topic: deep-learning
topic_label: 深度学习
difficulty: intermediate
status: not-started
tags: [exercise, deep-learning]
source: "[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Bishop《深度学习：基础与概念》（DS003）]]"
source_id: DS003
source_chapter: 8
source_exercise: "8.11"
source_stars: 2
source_refs: ["DS003 Exercise 8.11，印刷252／PDF物理269", "DS003 §8.1.6，式(8.36)–(8.41)，印刷242–244/PDF259–261", "DS003 softmax定义式(6.37)，印刷197/PDF215"]
source_status: verified
solution_status: independently-derived
created: 2026-11-02
---

# 习题 DL223：Softmax交叉熵的广义GaussNewton矩阵

## 题目

### 英文原题

> [!question] 英文原题
> **8.11 (★★)** Derive an expression for the outer product approximation of a Hessian matrix for a network having $K$ outputs with a softmax output-unit activation function and a cross-entropy error function, corresponding to the result (8.40) for the sum-of-squares error function.

### 中文转述

> [!question] 中文转述
> 网络有 $K$ 个softmax输出，使用交叉熵损失。推导对应平方误差(8.40)的Hessian外积近似。

## 提示

> [!hint]- 提示
> 输出预激活上的Hessian是 $\operatorname{diag}(y)-yy^{\mathsf T}$，类别之间有交叉项。

## 解答

> [!success]- 解答
> **证明范围：独立推导。**
> 对样本 $n$，令预激活向量 $a_n\in\mathbb R^K$，$y_{nk}=e^{a_{nk}}/\sum_le^{a_{nl}}$，标签 $t_{nk}\ge0$ 且 $\sum_kt_{nk}=1$。交叉熵 $E_n=-\sum_kt_{nk}\ln y_{nk}$ 给
> $$
> \nabla_{a_n}E_n=y_n-t_n,\qquad B_n=\nabla_{a_n}^2E_n=\operatorname{diag}(y_n)-y_ny_n^{\mathsf T}.
> $$
> 记 $J_n=\partial a_n/\partial w$，二阶链式法则给出精确式
> $$
> H=\sum_nJ_n^{\mathsf T}B_nJ_n+\sum_{n,k}(y_{nk}-t_{nk})\nabla_w^2a_{nk}.
> $$
> 忽略后项得到所求近似
> $$
> G=\sum_n\left[\sum_ky_{nk}g_{nk}g_{nk}^{\mathsf T}
> -\left(\sum_ky_{nk}g_{nk}\right)\left(\sum_ly_{nl}g_{nl}\right)^{\mathsf T}\right],\quad g_{nk}=\nabla_wa_{nk}.
> $$
> 对任意 $v$，$v^{\mathsf T}J_n^{\mathsf T}B_nJ_nv$ 是类别分布 $y_n$ 下数值 $g_{nk}^{\mathsf T}v$ 的方差，故非负。这也说明不能把各输出当独立Sigmoid而丢掉类别交叉项。若预激活对参数仿射，式子精确；若条件类别概率拟合正确，残差项在标签上条件平均为0。softmax共同平移不变会引入零方向，因此非负不代表正定或可逆。

## 相关概念

- [[04 - 统计学习/概念/交叉熵|交叉熵]]
- [[03 - 线性代数与优化/概念/链式法则|链式法则]]
- [[06 - 深度学习/概念/激活函数|激活函数]]

## 备注

- 原题已实际查看 [[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=269|印刷252／PDF物理269]]；所列依赖正文亦逐页核对，精确位置见 `source_refs`。
- 解答未使用配套答案册。`source_status: verified` 指本题原文与所列依赖的核对范围；独立推导不代表个人学习完成，状态保持 `not-started`。
