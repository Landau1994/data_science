---
title: "习题 DL057：Sigmoid激活的饱和导数"
topic: "deep-learning"
topic_label: "深度学习"
difficulty: "intermediate"
status: "not-started"
tags:
  - exercise
  - deep-learning
source: "Understanding Deep Learning（2026-02-08修订稿），Problem 7.7，印刷115／PDF物理129"
source_id: "DS001"
source_chapter: 7
source_exercise: "7.7"
source_refs: ["DS001 Problem 7.7，印刷115/PDF129"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-10-28"
---

# 习题 DL057：Sigmoid激活的饱和导数

## 题目

### 英文原题

> [!question] 英文原题
> **Problem 7.7** Consider the case where we use the logistic sigmoid (see equation 7.38) as an activation function, so $h=\operatorname{sig}[f]$. Compute the derivative $\partial h/\partial f$ for this activation function. What happens to the derivative when the input takes (i) a large positive value and (ii) a large negative value?

### 中文转述

> [!question] 中文转述
> 以Sigmoid作为激活函数，求其导数，并说明输入很大为正或很小为负时的行为。



## 提示

> [!hint]- 提示
> 把指数形式的导数重新用h表示。

## 解答

> [!success]- 解答
> **独立推导。** 由$h=(1+e^{-f})^{-1}$，
> $$
> \frac{\partial h}{\partial f}
> =\frac{e^{-f}}{(1+e^{-f})^2}=h(1-h).
> $$
> 当$f\to+\infty$时$h\to1$，导数趋零；当$f\to-\infty$时$h\to0$，导数也趋零。两侧都是饱和区，会压缩反向梯度。又因$0<h<1$，$h(1-h)\le1/4$，仅在$f=0$取最大值$1/4$。

## 相关概念

- [[06 - 深度学习/概念/神经网络|神经网络]]

## 备注

- 原题已逐页核对：[[附件/books/UnderstandingDeepLearning_02_09_26_C.pdf#page=129|印刷115／PDF129]]。来源核对仅覆盖本题原文和已列定位，学习状态不随归档改变。
