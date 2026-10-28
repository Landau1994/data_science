---
title: "习题 DL069：等间距ReLU折点的固定参数"
topic: "deep-learning"
topic_label: "深度学习"
difficulty: "intermediate"
status: "not-started"
tags:
  - exercise
  - deep-learning
source: "Understanding Deep Learning（2026-02-08修订稿），Problem 8.2，印刷136／PDF物理150"
source_id: "DS001"
source_chapter: 8
source_exercise: "8.2"
source_refs: ["DS001 Problem 8.2，印刷136/PDF150", "DS001 图8.4及固定折点说明，印刷120–121/PDF134–135"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-10-28"
---

# 习题 DL069：等间距ReLU折点的固定参数

## 题目

### 英文原题

> [!question] 英文原题
> **Problem 8.2** What values should we choose for the three weights and biases in the first layer of the model in figure 8.4a so that the hidden unit’s responses are as depicted in figures 8.4b–d?

### 中文转述

> [!question] 中文转述
> 选择图8.4a第一层的三个权重和三个偏置，使三个隐藏激活分别具有图8.4b–d的响应。

![[附件/习题图/DS001/原图-8.4.png]]

## 提示

> [!hint]- 提示
> 图中三个正斜率都为1，折点为0、1/3、2/3。

## 解答

> [!success]- 解答
> **独立推导。** 按$h_j=\operatorname{ReLU}(\theta_{0j}+\theta_{1j}x)$记号，取
> $$
> (\theta_{11},\theta_{12},\theta_{13})=(1,1,1),\qquad
> (\theta_{01},\theta_{02},\theta_{03})=(0,-1/3,-2/3).
> $$
> 于是
> $$
> h_1=\max(0,x),\quad h_2=\max(0,x-1/3),\quad h_3=\max(0,x-2/3).
> $$
> 每个函数在相应折点左侧为零，右侧斜率为1，恰为图示。这里第一层参数是预先固定的，不属于随后拟合的四个输出层参数。

## 相关概念

- [[06 - 深度学习/概念/神经网络|神经网络]]

## 备注

- 原题已逐页核对：[[附件/books/UnderstandingDeepLearning_02_09_26_C.pdf#page=150|印刷136／PDF150]]。来源核对仅覆盖本题原文和已列定位，学习状态不随归档改变。
