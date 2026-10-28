---
title: "习题 DL098：AlexNet逐层参数的完整计数"
topic: "deep-learning"
topic_label: "深度学习"
difficulty: "intermediate"
status: "not-started"
tags:
  - exercise
  - deep-learning
source: "Understanding Deep Learning（2026-02-08修订稿），Problem 10.16，印刷185/PDF物理199"
source_id: "DS001"
source_chapter: 10
source_exercise: "10.16"
source_refs: ["DS001 Problem 10.16*，印刷185/PDF199", "DS001 图10.16及紧接正文，印刷176/PDF190"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-10-28"
---

# 习题 DL098：AlexNet逐层参数的完整计数

## 题目

### 英文原题

> [!question] 英文原题
> **Problem 10.16\*** Consider the AlexNet network (figure 10.16). How many parameters are used in each convolutional and fully connected layer? What is the total number of parameters?

### 中文转述

> [!question] 中文转述
> 按图10.16的AlexNet结构，分别数每个卷积层、全连接层的参数，并求总数。
>
> ![[附件/习题图/DS001/原图-10.16.png]]
> 原图：印刷176／PDF190，保留原图注。

## 提示

> [!hint]- 提示
> 卷积层用$k^2C_{\rm in}C_{\rm out}+C_{\rm out}$，全连接层用$D_{\rm in}D_{\rm out}+D_{\rm out}$；最后池化后的展开维数为$6\cdot6\cdot256$。

## 解答

> [!success]- 解答
> **独立推导。** 按本书图中的普通全通道卷积计数，每输出通道一个偏置；池化、ReLU、softmax均无可训练参数。图示五层通道为$3\to96\to256\to384\to384\to256$，核为11、5、3、3、3；最后池化输出$6\times6\times256=9216$，随后全连接$9216\to4096\to4096\to1000$。
> |层|输入→输出|核|权重|偏置|合计|
> |---|---|---|---:|---:|---:|
> |conv1|3→96|$11\times11$|34848|96|34944|
> |conv2|96→256|$5\times5$|614400|256|614656|
> |conv3|256→384|$3\times3$|884736|384|885120|
> |conv4|384→384|$3\times3$|1327104|384|1327488|
> |conv5|384→256|$3\times3$|884736|256|884992|
> |fc1|9216→4096|全连接|37748736|4096|37752832|
> |fc2|4096→4096|全连接|16777216|4096|16781312|
> |fc3|4096→1000|全连接|4096000|1000|4097000|
>
> 相加得
> $$
> \boxed{P=62378344}.
> $$
> 表中数值已通过整数运算实际重算。空间大小决定全连接层的输入宽度，但卷积参数在各空间位置共享，不乘输出图像面积。
> 这是书中所画连接方式的计数。若另行规定分组卷积，权重应改为$k^2C_{\rm in}C_{\rm out}/g$，数量会变化；图中没有给分组标记，不能无说明采用别处AlexNet实现的参数总数。

## 相关概念

- [[06 - 深度学习/概念/神经网络|神经网络]]

## 备注

- 原题：[[附件/books/UnderstandingDeepLearning_02_09_26_C.pdf#page=199|主书印刷185／PDF199]]；来源记录见 [[00 - 首页/教材归档/DS001 - Understanding Deep Learning|DS001]]。
- verified只覆盖本题实际核对的来源；解答独立撰写，学习状态不因归档改变。
