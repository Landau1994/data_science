---
title: "习题 DL050：百万参数Hessian的形状"
topic: "deep-learning"
topic_label: "深度学习"
difficulty: "beginner"
status: "not-started"
tags:
  - exercise
  - deep-learning
source: "Understanding Deep Learning（2026-02-08修订稿），Problem 6.11，印刷95／PDF物理109"
source_id: "DS001"
source_chapter: 6
source_exercise: "6.11"
source_refs: ["DS001 Problem 6.11，印刷95/PDF109"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-10-28"
---

# 习题 DL050：百万参数Hessian的形状

## 题目

### 英文原题

> [!question] 英文原题
> **Problem 6.11** What dimensions will the Hessian have if the model has one million parameters?

### 中文转述

> [!question] 中文转述
> 模型有一百万个参数，Hessian的维数是多少？



## 提示

> [!hint]- 提示
> 每个参数对每个参数都有一个二阶偏导数。

## 解答

> [!success]- 解答
> **独立推导。** 将参数展为长度 $P=10^6$ 的向量，Hessian为 $P\times P=10^6\times10^6$ 的方阵，有 $10^{12}$ 个条目；不是百万阶张量。若密集使用float32存储，条目本身需 $4\times10^{12}$ 字节，约4TB（不含额外开销）；这解释为什么常用Hessian向量积而不显式保存矩阵。

## 相关概念

- [[06 - 深度学习/概念/神经网络|神经网络]]

## 备注

- 原题已逐页核对：[[附件/books/UnderstandingDeepLearning_02_09_26_C.pdf#page=109|印刷95／PDF109]]。来源核对仅覆盖本题原文和已列定位，学习状态不随归档改变。
