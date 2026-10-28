---
title: "习题 DL056：仿射层的转置Jacobian约定"
topic: "deep-learning"
topic_label: "深度学习"
difficulty: "intermediate"
status: "not-started"
tags:
  - exercise
  - deep-learning
source: "Understanding Deep Learning（2026-02-08修订稿），Problem 7.6，印刷115／PDF物理129"
source_id: "DS001"
source_chapter: 7
source_exercise: "7.6"
source_refs: ["DS001 Problem 7.6，印刷115/PDF129"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-10-28"
---

# 习题 DL056：仿射层的转置Jacobian约定

## 题目

### 英文原题

> [!question] 英文原题
> **Problem 7.6\*** Show that for $z=\beta+\Omega h$:
> $$
> \frac{\partial z}{\partial h}=\Omega^T,\tag{7.39}
> $$
> where $\partial z/\partial h$ is a matrix containing the term $\partial z_i/\partial h_j$ in its $i^{th}$ column and $j^{th}$ row. To do this, first find an expression for the constituent elements $\partial z_i/\partial h_j$, and then consider the form that the matrix $\partial z/\partial h$ must take.

### 中文转述

> [!question] 中文转述
> 按本书“输出编号为列、输入编号为行”的矩阵导数约定，证明仿射层关于输入的导数是权重矩阵转置。先求元素导数，再确定矩阵形状。



## 提示

> [!hint]- 提示
> 展开zi；特别注意题目指定的行列位置。

## 解答

> [!success]- 解答
> **独立推导。** 设$h\in\mathbb R^n$、$z,\beta\in\mathbb R^m$、$\Omega\in\mathbb R^{m\times n}$。逐分量有
> $$
> z_i=\beta_i+\sum_{k=1}^n\Omega_{ik}h_k,\qquad
> \frac{\partial z_i}{\partial h_j}=\Omega_{ij}.
> $$
> 题设矩阵$M=\partial z/\partial h$的第$j$行、第$i$列放入该导数，故$M_{ji}=\Omega_{ij}=(\Omega^T)_{ji}$，从而$M=\Omega^T\in\mathbb R^{n\times m}$。若采用通常“输出为行”的Jacobian约定，则矩阵为$\Omega$；两种记法的元素导数完全相同。

## 相关概念

- [[06 - 深度学习/概念/神经网络|神经网络]]

## 备注

- 原题已逐页核对：[[附件/books/UnderstandingDeepLearning_02_09_26_C.pdf#page=129|印刷115／PDF129]]。来源核对仅覆盖本题原文和已列定位，学习状态不随归档改变。
