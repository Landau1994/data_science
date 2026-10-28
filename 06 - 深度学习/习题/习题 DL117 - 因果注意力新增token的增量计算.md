---
title: "习题 DL117：因果注意力新增token的增量计算"
topic: "deep-learning"
topic_label: "深度学习"
difficulty: "intermediate"
status: "not-started"
tags:
  - exercise
  - deep-learning
source: "Understanding Deep Learning（2026-02-08修订稿），Problem 12.7，印刷239/PDF物理253"
source_id: "DS001"
source_chapter: 12
source_exercise: "12.7"
source_refs: ["DS001 Problem 12.7，印刷239/PDF253"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-10-28"
---

# 习题 DL117：因果注意力新增token的增量计算

## 题目

### 英文原题

> [!question] 英文原题
> **Problem 12.7** Consider adding a new token to a precomputed masked self-attention mechanism with $N$ tokens. Describe the extra computation that must be done to incorporate this new token.

### 中文转述

> [!question] 中文转述
> 给已有N个token的预计算带掩码自注意力追加一个token，描述新增计算。

## 提示

> [!hint]- 提示
> 在因果掩码下，旧位置不能看到新未来位置。已有键和值可缓存。

## 解答

> [!success]- 解答
> **独立推导。** 假设是自回归因果掩码、推理时追加末尾token，且每层已缓存旧K、V。旧输出不变，不需重算旧query的注意力行。只须：
> 1. 对新表示投影得到 $q_{N+1},k_{N+1},v_{N+1}$，并把新K、V追加缓存；
> 2. 计算新query与全部N+1个key的点积（含缩放、合法位置掩码），做一次长度N+1的softmax；
> 3. 用所得权重聚合N+1个value，再做需要的输出投影、残差和逐位置前馈。
> 单头维度D时，新增投影为 $O(D^2)$，点积与聚合各 $O(ND)$、softmax为O(N)，无需重做N²个旧交互。深层decoder逐层重复，新位置要经过各层，但旧层缓存仍可复用。若掩码允许旧位置看新位置，则旧输出也可能变化，此增量结论不适用。

## 相关概念

- [[06 - 深度学习/概念/神经网络|神经网络]]

## 备注

- 原题：[[附件/books/UnderstandingDeepLearning_02_09_26_C.pdf#page=253|主书印刷239／PDF253]]；来源记录见 [[00 - 首页/教材归档/DS001 - Understanding Deep Learning|DS001]]。
- verified只覆盖本题实际核对的来源；解答独立撰写，学习状态不因归档改变。
