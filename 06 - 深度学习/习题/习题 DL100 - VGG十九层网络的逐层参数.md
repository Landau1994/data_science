---
title: "习题 DL100：VGG十九层网络的逐层参数"
topic: "deep-learning"
topic_label: "深度学习"
difficulty: "intermediate"
status: "not-started"
tags:
  - exercise
  - deep-learning
source: "Understanding Deep Learning（2026-02-08修订稿），Problem 10.18，印刷185/PDF物理199"
source_id: "DS001"
source_chapter: 10
source_exercise: "10.18"
source_refs: ["DS001 Problem 10.18，印刷185/PDF199", "DS001 图10.17，印刷177/PDF191；VGG正文说明，印刷176/PDF190"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-10-28"
---

# 习题 DL100：VGG十九层网络的逐层参数

## 题目

### 英文原题

> [!question] 英文原题
> **Problem 10.18** How many weights and biases are there at each convolutional layer and fully connected layer in the VGG architecture (figure 10.17)?

### 中文转述

> [!question] 中文转述
> 按图10.17的VGG网络逐层列出卷积层和全连接层的权重数与偏置数。
>
> ![[附件/习题图/DS001/原图-10.17.png]]
> 原图：印刷177／PDF191，保留原图注。

## 提示

> [!hint]- 提示
> 图中五组卷积层数为2、2、4、4、4，通道64、128、256、512、512；最后池化后为$7\times7\times512$。

## 解答

> [!success]- 解答
> **独立推导。** 图示为16个$3\times3$卷积加3个全连接层。把五组卷积分别记作conv1至conv5，每组内从1编号。每层权重$9C_{\rm in}C_{\rm out}$、偏置$C_{\rm out}$；首层输入3通道。五次尺寸减半使最终池化后为$7\times7\times512=25088$，故全连接宽度为$25088\to4096\to4096\to1000$。
> |层|权重|偏置|合计|
> |---|---:|---:|---:|
> |conv1_1|1728|64|1792|
> |conv1_2|36864|64|36928|
> |conv2_1|73728|128|73856|
> |conv2_2|147456|128|147584|
> |conv3_1|294912|256|295168|
> |conv3_2|589824|256|590080|
> |conv3_3|589824|256|590080|
> |conv3_4|589824|256|590080|
> |conv4_1|1179648|512|1180160|
> |conv4_2|2359296|512|2359808|
> |conv4_3|2359296|512|2359808|
> |conv4_4|2359296|512|2359808|
> |conv5_1|2359296|512|2359808|
> |conv5_2|2359296|512|2359808|
> |conv5_3|2359296|512|2359808|
> |conv5_4|2359296|512|2359808|
> |fc1|102760448|4096|102764544|
> |fc2|16777216|4096|16781312|
> |fc3|4096000|1000|4097000|
>
> 所有卷积按普通全通道连接、每输出通道一个偏置；池化、ReLU、softmax不计参数。完整19层表已实际用整数运算逐项重算，权重总数143652544，偏置总数14696，合计
> $$
> \boxed{143667240}.
> $$
> 约1.44亿，与正文量级相符。不能把同组内第一层和后续层都按相同输入通道计数：例如conv4_1是$256\to512$，而conv4_2至conv4_4才是$512\to512$。

## 相关概念

- [[06 - 深度学习/概念/神经网络|神经网络]]

- [[06 - 深度学习/概念/卷积神经网络|卷积神经网络]]

## 备注

- 原题：[[附件/books/UnderstandingDeepLearning_02_09_26_C.pdf#page=199|主书印刷185／PDF199]]；来源记录见 [[00 - 首页/教材归档/DS001 - Understanding Deep Learning|DS001]]。
- verified只覆盖本题实际核对的来源；解答独立撰写，学习状态不因归档改变。
