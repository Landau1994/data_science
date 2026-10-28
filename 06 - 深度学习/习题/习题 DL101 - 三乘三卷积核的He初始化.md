---
title: "习题 DL101：三乘三卷积核的He初始化"
topic: "deep-learning"
topic_label: "深度学习"
difficulty: "intermediate"
status: "not-started"
tags:
  - exercise
  - deep-learning
source: "Understanding Deep Learning（2026-02-08修订稿），Problem 10.19，印刷185/PDF物理199"
source_id: "DS001"
source_chapter: 10
source_exercise: "10.19"
source_refs: ["DS001 Problem 10.19*，印刷185/PDF199"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-10-28"
---

# 习题 DL101：三乘三卷积核的He初始化

## 题目

### 英文原题

> [!question] 英文原题
> **Problem 10.19\*** Consider two hidden layers of size $224\times224$ with $C_1$ and $C_2$ channels, respectively, connected by a $3\times3$ convolutional layer. Describe how to initialize the weights using He initialization.

### 中文转述

> [!question] 中文转述
> 两个隐藏层空间大小均为$224\times224$，通道分别为$C_1,C_2$，以$3\times3$卷积连接。说明如何做He初始化。

## 提示

> [!hint]- 提示
> 对一个内部输出单元，实际相加的是$9C_1$项，不能把整张输入图像的变量数都作为fan-in。

## 解答

> [!success]- 解答
> **独立推导。** 对ReLU后的前向二阶矩稳定，He初始化按扇入（fan-in）$n_{\rm in}=3\cdot3\cdot C_1=9C_1$设置独立核参数：
> $$
> \boxed{W_{o,c,p,q}\ \overset{\rm iid}{\sim}\ 
> \mathcal N\!\left(0,\frac{2}{9C_1}\right)},
> \quad
> 1\le o\le C_2,\ 1\le c\le C_1,\ 1\le p,q\le3.
> $$
> 偏置通常设为0。相同方差的均匀分布版本为
> $$
> W_{o,c,p,q}\sim
> \operatorname{Unif}\!\left[-\sqrt{\frac{6}{9C_1}},\sqrt{\frac{6}{9C_1}}\right].
> $$
> 原因是一个内部预激活$Z=\sum_{j=1}^{9C_1}W_jH_j$。在零均值独立初始化与同尺度输入的近似下，
> $$
> \mathbb E[Z^2]=(9C_1)\operatorname{Var}(W)\mathbb E[H^2].
> $$
> 当$Z$关于零对称，$\mathbb E[\operatorname{ReLU}(Z)^2]=\tfrac12\mathbb E[Z^2]$，选$\operatorname{Var}(W)=2/(9C_1)$使ReLU后的二阶矩与输入相当。这里稳定的是二阶矩近似，不能无条件把ReLU输出的方差也当作二阶矩。
> 空间位置共享同一个核，只采样$9C_1C_2$个独立核权重，然后在各位置复用；不是给展开矩阵每个非零格独立采样。224的空间尺寸不进入fan-in，$C_2$也不进入此前向扇入方差。边缘补零时有效输入项较少，标准共享核初始化不会保证所有边缘位置精确同方差。

## 相关概念

- [[06 - 深度学习/概念/神经网络|神经网络]]

## 备注

- 原题：[[附件/books/UnderstandingDeepLearning_02_09_26_C.pdf#page=199|主书印刷185／PDF199]]；来源记录见 [[00 - 首页/教材归档/DS001 - Understanding Deep Learning|DS001]]。
- verified只覆盖本题实际核对的来源；解答独立撰写，学习状态不因归档改变。
