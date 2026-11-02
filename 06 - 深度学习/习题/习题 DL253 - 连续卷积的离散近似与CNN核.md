---
title: "习题 DL253：连续卷积的离散近似与CNN核"
topic: deep-learning
topic_label: 深度学习
difficulty: beginner
status: not-started
tags: [exercise, deep-learning]
source: "[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Bishop《深度学习：基础与概念》（DS003）]]"
source_id: DS003
source_chapter: 10
source_exercise: "10.5"
source_stars: 1
source_refs: ["DS003 Exercise 10.5，印刷322／PDF物理338", "DS003 §10.2.2，式(10.2)，印刷292/PDF308"]
source_status: verified
solution_status: independently-derived
created: 2026-11-02
---

# 习题 DL253：连续卷积的离散近似与CNN核

## 题目

### 英文原题

> [!question] 英文原题
> **10.5 (★)** In mathematics, a convolution for a continuous variable $x$ is defined by
> $$
> F(x)=\int_{-\infty}^{\infty}G(y)k(x-y)\,\mathrm dy\tag{10.21}
> $$
> where $k(x-y)$ is the kernel function. By considering a discrete approximation to the integral, explain the relationship to a convolutional layer, defined by (10.19), in a CNN.

### 中文转述

> [!question] 中文转述
> 连续卷积按(10.21)定义为 $F(x)=\int G(y)k(x-y)dy$。通过积分的离散近似，解释它与CNN数学卷积形式(10.19)之间的关系。

## 提示

> [!hint]- 提示
> 把积分变为等间距Riemann和，令 $x=i\Delta$、$y=j\Delta$，再重新命名索引。

## 解答

> [!success]- 解答
> **证明范围：独立推导。**
> 设函数及核有适当可积性与规则性，使有限截断后的Riemann和及截断极限收敛；例如连续且紧支撑的 $G,k$ 即足够。取网格间距 $\Delta>0$，在 $x=i\Delta$ 处有
> $$
> F(i\Delta)\approx\Delta\sum_{j\in\mathbb Z}G(j\Delta)k((i-j)\Delta).
> $$
> 记 $G_j=G(j\Delta)$、$K_l=\Delta k(l\Delta)$，并以 $l=i-j$ 换元，得到 $F_i\approx\sum_lG_{i-l}K_l$。核若有限支撑，只需有限个移位项。这是一维离散数学卷积，二维张量积网格同理给 $C(j,k)=\sum_{lm}I(j-l,k-m)K(l,m)$，即(10.19)，网格面积因子可吸收进核参数。
>
> CNN卷积层将这些局部线性组合在各空间位置复用相同核系数，另可加入偏置、多个通道与非线性激活；这些附加操作不属于原连续线性卷积积分本身。实际主书的CNN实现式(10.2)采用互相关约定，需要先翻转离散核才能等同(10.19)。学习核时翻转只改变参数排列，但在固定核的数值计算中必须明确约定。

## 相关概念

- [[06 - 深度学习/概念/卷积神经网络|卷积神经网络]]
- [[06 - 深度学习/概念/前向传播|前向传播]]

## 备注

- 原题已实际查看 [[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=338|印刷322／PDF物理338]]；所列依赖正文亦逐页核对，精确位置见 `source_refs`。
- 解答未使用配套答案册。`source_status: verified` 指本题原文与所列依赖的核对范围；独立推导不代表个人学习完成，状态保持 `not-started`。
