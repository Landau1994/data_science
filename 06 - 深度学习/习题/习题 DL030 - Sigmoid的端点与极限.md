---
title: "习题 DL030：Sigmoid的端点与极限"
topic: "deep-learning"
topic_label: "深度学习"
difficulty: "beginner"
status: "not-started"
tags:
  - exercise
  - deep-learning
source: "Understanding Deep Learning（2026-02-08修订稿），Problem 5.1，印刷74／PDF物理88"
source_id: "DS001"
source_chapter: 5
source_exercise: "5.1"
source_refs: ["DS001 Problem 5.1，印刷74/PDF88"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-10-28"
---

# 习题 DL030：Sigmoid的端点与极限

## 题目

### 英文原题

> [!question] 英文原题
> **Problem 5.1** Show that the logistic sigmoid function $\operatorname{sig}[z]$ becomes 0 as $z\to-\infty$, is 0.5 when $z=0$, and becomes 1 when $z\to\infty$, where:
> $$
> \operatorname{sig}[z]=\frac{1}{1+\exp[-z]}.\tag{5.32}
> $$

### 中文转述

> [!question] 中文转述
> 证明逻辑 Sigmoid（logistic sigmoid）在负无穷处趋于0、零点取1/2、正无穷处趋于1，定义如式(5.32)。



## 提示

> [!hint]- 提示
> 分别考虑分母中 $e^{-z}$ 的极限。

## 解答

> [!success]- 解答
> **独立推导。** 对任意实数 $z$，$e^{-z}>0$，故 $0<\operatorname{sig}(z)<1$。当 $z\to-\infty$，$e^{-z}\to\infty$，倒数趋于0；当 $z=0$，分母为2；当 $z\to\infty$，$e^{-z}\to0$，倒数趋于1。两个端值都是极限，有限 $z$ 不会取到0或1。

## 相关概念

- [[06 - 深度学习/概念/神经网络|神经网络]]
- [[06 - 深度学习/概念/激活函数|激活函数]]

## 备注

- 原题已逐页核对：[[附件/books/UnderstandingDeepLearning_02_09_26_C.pdf#page=88|印刷74／PDF88]]。来源核对仅覆盖本题原文和已列定位，学习状态不随归档改变。
