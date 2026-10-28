---
title: "习题 DL070：固定ReLU特征的闭式最小二乘"
topic: "deep-learning"
topic_label: "深度学习"
difficulty: "intermediate"
status: "not-started"
tags:
  - exercise
  - deep-learning
source: "Understanding Deep Learning（2026-02-08修订稿），Problem 8.3，印刷136／PDF物理150"
source_id: "DS001"
source_chapter: 8
source_exercise: "8.3"
source_refs: ["DS001 Problem 8.3，印刷136/PDF150", "DS001 图8.4及固定第一层设定，印刷120–121/PDF134–135"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-10-28"
---

# 习题 DL070：固定ReLU特征的闭式最小二乘

## 题目

### 英文原题

> [!question] 英文原题
> **Problem 8.3\*** Given a training dataset consisting of $I$ input/output pairs $\{x_i,y_i\}$, show how the parameters $\{\beta,\omega_1,\omega_2,\omega_3\}$ for the model in figure 8.4a using the least squares loss function can be found in closed form.

### 中文转述

> [!question] 中文转述
> 对I个训练样本和图8.4a的固定第一层，给出四个输出参数的闭式最小二乘解。

![[附件/习题图/DS001/原图-8.4.png]]

## 提示

> [!hint]- 提示
> 第一层固定后，模型关于四个待拟合参数是线性的。把常数1和三个隐藏响应作为设计矩阵的列。

## 解答

> [!success]- 解答
> **独立推导。** 令$t=(\beta,\omega_1,\omega_2,\omega_3)^T$，设计矩阵$X\in\mathbb R^{I\times4}$第$i$行为
> $$
> X_{i,:}=(1,h_1(x_i),h_2(x_i),h_3(x_i)),
> $$
> 其中$h_1(x)=\max(0,x)$、$h_2(x)=\max(0,x-1/3)$、$h_3(x)=\max(0,x-2/3)$。于是预测向量$Xt$，损失$L(t)=\|Xt-y\|_2^2$，梯度为$2X^T(Xt-y)$。驻点满足正规方程
> $$
> X^TXt=X^Ty.
> $$
> 若$\operatorname{rank}X=4$，则$X^TX$正定，唯一全局解为
> $$
> \hat t=(X^TX)^{-1}X^Ty.
> $$
> 若训练输入不足以辨识四列，逆矩阵不能使用；仍可用Moore–Penrose伪逆给最小范数解$\hat t=X^+y$，全部最优解为
> $$
> t=X^+y+(I_4-X^+X)v,\qquad v\in\mathbb R^4.
> $$
> 其理由是$XX^+y$为$y$到$X$列空间的正交投影，加入$X$的零空间向量不改变预测。故不论是否满秩，都有闭式全局最小二乘解。

## 相关概念

- [[06 - 深度学习/概念/神经网络|神经网络]]
- [[03 - 线性代数与优化/概念/正规方程|正规方程]]

- [[06 - 深度学习/概念/激活函数|激活函数]]

## 备注

- 原题已逐页核对：[[附件/books/UnderstandingDeepLearning_02_09_26_C.pdf#page=150|印刷136／PDF150]]。来源核对仅覆盖本题原文和已列定位，学习状态不随归档改变。
