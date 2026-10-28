---
title: "习题 DL034：双vonMises混合的网络输出"
topic: "deep-learning"
topic_label: "深度学习"
difficulty: "intermediate"
status: "not-started"
tags:
  - exercise
  - deep-learning
source: "Understanding Deep Learning（2026-02-08修订稿），Problem 5.5，印刷75／PDF物理89"
source_id: "DS001"
source_chapter: 5
source_exercise: "5.5"
source_refs: ["DS001 Problem 5.5，印刷75/PDF89"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-10-28"
---

# 习题 DL034：双vonMises混合的网络输出

## 题目

### 英文原题

> [!question] 英文原题
> **Problem 5.5** Consider extending the model from problem 5.3 to predict the wind direction using a mixture of two von Mises distributions. Write an expression for the likelihood $Pr(y\mid\theta)$ for this model. How many outputs will the network need to produce?

### 中文转述

> [!question] 中文转述
> 将5.3扩展为两个von Mises分布的混合来预测风向。写似然 $Pr(y\mid\theta)$，并说明网络输出数。



## 提示

> [!hint]- 提示
> 两个分量各有方向与集中度，加一个混合权重；同时说明是否沿用前题固定集中度。

## 解答

> [!success]- 解答
> **独立推导。** 一般模型为
> $$
> p(y\mid\theta)=\lambda\frac{e^{\kappa_1\cos(y-\mu_1)}}{2\pi I_0(\kappa_1)}
> +(1-\lambda)\frac{e^{\kappa_2\cos(y-\mu_2)}}{2\pi I_0(\kappa_2)}.
> $$
> $I_0=\operatorname{Bessel}_0$，$\lambda\in[0,1]$、$\kappa_j\ge0$。若两个集中度也由输入预测，需要五个标量输出：一个权重、两个方向、两个集中度；可用sigmoid约束权重、指数约束正集中度。若严格沿用5.3“集中度已知固定”的约定，则只预测 $\lambda,\mu_1,\mu_2$，需要三个输出。两种计数的区别是模型假设，并非把固定量也算作网络输出。方向直接作实数输出再模 $2\pi$ 即可。

## 相关概念

- [[06 - 深度学习/概念/神经网络|神经网络]]

## 备注

- 原题已逐页核对：[[附件/books/UnderstandingDeepLearning_02_09_26_C.pdf#page=89|印刷75／PDF89]]。来源核对仅覆盖本题原文和已列定位，学习状态不随归档改变。
