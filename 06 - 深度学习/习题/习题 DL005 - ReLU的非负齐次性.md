---
title: "习题 DL005：ReLU的非负齐次性"
topic: deep-learning
topic_label: 深度学习
difficulty: beginner
status: not-started
tags:
  - exercise
  - deep-learning
source: "[[00 - 首页/教材归档/DS001 - Understanding Deep Learning|Understanding Deep Learning（DS001）]]"
source_id: DS001
source_chapter: 3
source_exercise: "3.5"
source_refs: ["DS001 Problem 3.5，式(3.14)，印刷39/PDF53","DS001 §3.1，ReLU定义式(3.2)，印刷25/PDF39"]
source_status: verified
solution_status: independently-derived
created: 2026-10-25
---

# 习题 DL005：ReLU的非负齐次性

## 题目

### 英文原题

> [!question] 英文原题
> **Problem 3.5** Prove that the following property holds for $\alpha\in\mathbb R^+$:
> $$
> \operatorname{ReLU}[\alpha\cdot z]=\alpha\cdot\operatorname{ReLU}[z].\tag{3.14}
> $$
> This is known as the non-negative homogeneity property of the ReLU function.

### 中文转述

> [!question] 中文转述
> **UDL 原题 3.5。** 证明：对 $\alpha\in\mathbb R^+$，
> $$
> \operatorname{ReLU}(\alpha z)=\alpha\operatorname{ReLU}(z).
> $$
> 这称为 ReLU 函数的非负齐次性（non-negative homogeneity）。

## 提示

> [!hint]- 提示
> 使用 $\operatorname{ReLU}(z)=\max(0,z)$，按 $z\ge0$ 和 $z<0$ 分别检查；正数缩放不会改变 $z$ 的符号。

## 解答

> [!success]- 解答
> **独立证明。** 设 $z\in\mathbb R$、$\alpha>0$。若 $z\ge0$，则 $\alpha z\ge0$，故
> $$
> \operatorname{ReLU}(\alpha z)=\alpha z
> =\alpha\operatorname{ReLU}(z).
> $$
> 若 $z<0$，则 $\alpha z<0$，等式两边都为零。因此等式对任意实数 $z$ 成立。
>
> 若把“非负”中的边界 $\alpha=0$ 也纳入，左右两边仍都为零，所以结论可扩展为 $\alpha\ge0$。负数缩放一般不满足此式：例如 $\alpha=-1,z=1$ 时，左边为 $0$，右边为 $-1$。

## 相关概念

- [[06 - 深度学习/概念/神经网络|神经网络]]：ReLU 激活及其分段定义。
- [[06 - 深度学习/概念/激活函数|激活函数]]

## 备注

- 原题和式 (3.14)：[[附件/books/UnderstandingDeepLearning_02_09_26_C.pdf#page=53|印刷 39／PDF 53]]；ReLU 定义：[[附件/books/UnderstandingDeepLearning_02_09_26_C.pdf#page=39|式 (3.2)，印刷 25／PDF 39]]。
- 英文保留原题 $\mathbb R^+$ 记号；解答先证明正数情形，再独立说明零值扩展，避免依赖这一记号是否包含零的约定。

