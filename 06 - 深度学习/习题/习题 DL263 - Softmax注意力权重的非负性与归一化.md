---
title: "习题 DL263：Softmax注意力权重的非负性与归一化"
topic: deep-learning
topic_label: 深度学习
difficulty: beginner
status: not-started
tags:
  - exercise
  - deep-learning
source: "[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Bishop 深度学习（DS003）]]"
source_id: DS003
source_chapter: 12
source_exercise: "12.2"
source_stars: 1
source_refs:
  - "DS003 Exercise 12.2，印刷404/PDF420"
  - "DS003 §12.1.2–12.1.3，式12.2–12.6，印刷362–363/PDF378–379"
source_status: verified
solution_status: independently-derived
created: 2026-11-02
---

# 习题 DL263：Softmax注意力权重的非负性与归一化

## 题目

### 英文原题

> [!question] 英文原题
> **12.2 (★)** Verify that the softmax function (12.5) satisfies the constraints (12.3) and (12.4) for any values of the vectors $\mathbf{x}_1,\ldots,\mathbf{x}_N$.

### 中文转述

> [!question] 中文转述
> 验证：对于任意向量$\mathbf x_1,\ldots,\mathbf x_N$，式(12.5)的Softmax函数都满足约束(12.3)、(12.4)。

## 提示

> [!hint]- 提示 1
> 指数项严格为正，分子之和就是分母。

## 解答

> [!success]- 解答
> **独立推导。**
>
> 设$N\geq1$，各向量坐标有限。对固定$n$，记$s_m=x_n^Tx_m$及$Z_n=\sum_{j=1}^N e^{s_j}$，则$0<Z_n<\infty$。因此
> $$
> a_{nm}=\frac{e^{s_m}}{Z_n}>0,\qquad
> \sum_{m=1}^Na_{nm}=\frac{\sum_me^{s_m}}{Z_n}=1.
> $$
> 这分别是(12.3)的非负性和(12.4)的归一化。若$N>1$，每项严格小于$1$；若$N=1$，唯一权重为$1$。计算实现可用$e^{s_m-\max_js_j}$避免指数溢出，不改变上述数学值。

## 相关概念

- [[06 - 深度学习/概念/自注意力|自注意力]]
- [[06 - 深度学习/概念/Transformer|Transformer]]

## 备注

- 原题已核对 DS003 印刷404页／PDF物理420页；正文引用的实际核对范围见 `source_refs`。
- 解答为独立推导；归档与个人学习状态分开，学习状态保持 `not-started`。
