---
title: "习题 DL110：U-Net训练中图像尺寸与批处理"
topic: "deep-learning"
topic_label: "深度学习"
difficulty: "intermediate"
status: "not-started"
tags:
  - exercise
  - deep-learning
source: "Understanding Deep Learning（2026-02-08修订稿），Problem 11.9，印刷206/PDF物理220"
source_id: "DS001"
source_chapter: 11
source_exercise: "11.9"
source_refs: ["DS001 Problem 11.9，印刷206/PDF220"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-10-28"
---

# 习题 DL110：U-Net训练中图像尺寸与批处理

## 题目

### 英文原题

> [!question] 英文原题
> **Problem 11.9** The U-Net is completely convolutional and can be run with any sized image after training. Why do we not train with a collection of arbitrarily-sized images?

### 中文转述

> [!question] 中文转述
> U-Net完全由卷积式操作构成，训练后能应用于不同尺寸图像。为什么通常不直接把任意尺寸图像组成训练集合与训练批次？

## 提示

> [!hint]- 提示
> 区分“参数不依赖图像尺寸”与“一个批次能直接叠成规则张量”；同时考虑池化尺度、内存和损失权重。

## 解答

> [!success]- 解答
> **独立推导。** 卷积核的参数与空间尺寸无关，因此同一组参数可以用于多个尺寸。但常规高效训练把批次叠成$B\times C\times H\times W$规则张量；尺寸各异的图像不能直接叠放。逐张处理会降低并行效率并使显存需求、每步像素数和运行时间变化很大，大图还可能超出内存。
> U-Net还有多级下采样、上采样和跳接。尺寸不满足下采样倍数时，必须明确补边、裁切或插值对齐，才能连接对应特征；“任意尺寸”通常包含这些实现适配，并非对任意整数尺寸都无需处理。
> 若对全部像素直接平均，大图在一个混合尺寸批次中可能取得更大权重；若逐图平均则是另一训练目标。补边还会影响边缘预测、BN统计及损失，需要有效像素掩码。
> 所以常采用固定大小随机裁块、统一缩放，或按尺寸分组；也可以补边加掩码、逐图梯度累积等方式训练不同尺寸。不同尺寸训练在数学上可行，题中惯例主要由批处理效率、对齐和训练目标的一致性决定。

## 相关概念

- [[06 - 深度学习/概念/神经网络|神经网络]]

## 备注

- 原题：[[附件/books/UnderstandingDeepLearning_02_09_26_C.pdf#page=220|主书印刷206／PDF220]]；来源记录见 [[00 - 首页/教材归档/DS001 - Understanding Deep Learning|DS001]]。
- verified只覆盖本题实际核对的来源；解答独立撰写，学习状态不因归档改变。
