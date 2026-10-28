---
title: "习题 DL042：Gabor模型的平方损失梯度"
topic: "deep-learning"
topic_label: "深度学习"
difficulty: "intermediate"
status: "not-started"
tags:
  - exercise
  - deep-learning
source: "Understanding Deep Learning（2026-02-08修订稿），Problem 6.3，印刷94／PDF物理108"
source_id: "DS001"
source_chapter: 6
source_exercise: "6.3"
source_refs: ["DS001 Problem 6.3，印刷94/PDF108", "DS001 式(6.8)–(6.9)，印刷80/PDF94"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-10-28"
---

# 习题 DL042：Gabor模型的平方损失梯度

## 题目

### 英文原题

> [!question] 英文原题
> **Problem 6.3** Compute the derivatives of the least squares loss $L[\phi]$ with respect to the parameters $\phi_0$ and $\phi_1$ for the Gabor model (equation 6.8).

### 中文转述

> [!question] 中文转述
> 对式(6.8)的Gabor模型，求平方损失关于 $\phi_0,\phi_1$ 的导数。



## 提示

> [!hint]- 提示
> 先令 $u_i=\phi_0+0.06\phi_1x_i$，同时对正弦与包络求导。

## 解答

> [!success]- 解答
> **独立推导。** 原模型是 $f_i=\sin u_i\,e^{-u_i^2/32}$，$L=\sum_i(f_i-y_i)^2$。乘积法则给
> $$
> q_i=\frac{\partial f_i}{\partial u_i}
> =e^{-u_i^2/32}\left(\cos u_i-\frac{u_i}{16}\sin u_i\right).
> $$
> 又 $\partial u_i/\partial\phi_0=1$、$\partial u_i/\partial\phi_1=0.06x_i$，所以
> $$
> \frac{\partial L}{\partial\phi_0}=2\sum_i(f_i-y_i)q_i,\qquad
> \frac{\partial L}{\partial\phi_1}=0.12\sum_i x_i(f_i-y_i)q_i.
> $$
> 包络的导数不可漏掉，否则得到的不是原模型的梯度。

## 相关概念

- [[06 - 深度学习/概念/神经网络|神经网络]]

## 备注

- 原题已逐页核对：[[附件/books/UnderstandingDeepLearning_02_09_26_C.pdf#page=108|印刷94／PDF108]]。来源核对仅覆盖本题原文和已列定位，学习状态不随归档改变。
