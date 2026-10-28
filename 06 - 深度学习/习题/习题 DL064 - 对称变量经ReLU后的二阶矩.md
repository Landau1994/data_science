---
title: "习题 DL064：对称变量经ReLU后的二阶矩"
topic: "deep-learning"
topic_label: "深度学习"
difficulty: "intermediate"
status: "not-started"
tags:
  - exercise
  - deep-learning
source: "Understanding Deep Learning（2026-02-08修订稿），Problem 7.14，印刷117／PDF物理131"
source_id: "DS001"
source_chapter: 7
source_exercise: "7.14"
source_refs: ["DS001 Problem 7.14，印刷117/PDF131"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-10-28"
---

# 习题 DL064：对称变量经ReLU后的二阶矩

## 题目

### 英文原题

> [!question] 英文原题
> **Problem 7.14** Consider a random variable $a$ with variance $\operatorname{Var}[a]=\sigma^2$ and a symmetrical distribution around the mean $\mathbb E[a]=0$. Prove that if we pass this variable through the ReLU function:
> $$
> b=\operatorname{ReLU}[a]=
> \begin{cases}0&a<0\\a&a\ge0,\end{cases}\tag{7.48}
> $$
> then the second moment of the transformed variable is $\mathbb E[b^2]=\sigma^2/2$.

### 中文转述

> [!question] 中文转述
> 零均值对称随机变量a的方差为σ²，证明其ReLU变换b的二阶矩为σ²/2。



## 提示

> [!hint]- 提示
> 对称性使正半轴与负半轴的平方贡献相等，零点的平方没有贡献。

## 解答

> [!success]- 解答
> **独立推导。** 由$\mathbb E[a]=0$，$\mathbb E[a^2]=\sigma^2$。对称性$a\overset d=-a$给出
> $$
> \mathbb E[a^2\mathbb I(a>0)]
> =\mathbb E[a^2\mathbb I(a<0)].
> $$
> $a=0$处平方为零，即使分布在零点有原子也不影响，所以两者之和为$\sigma^2$，各为$\sigma^2/2$。又$b^2=a^2\mathbb I(a>0)$，即得$\mathbb E[b^2]=\sigma^2/2$。一般$\mathbb E[b]>0$，因此$\operatorname{Var}(b)=\sigma^2/2-(\mathbb E[b])^2$，题目结论是二阶矩而非方差。

## 相关概念

- [[06 - 深度学习/概念/神经网络|神经网络]]

## 备注

- 原题已逐页核对：[[附件/books/UnderstandingDeepLearning_02_09_26_C.pdf#page=131|印刷117／PDF131]]。来源核对仅覆盖本题原文和已列定位，学习状态不随归档改变。
