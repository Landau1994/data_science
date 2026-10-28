---
title: "习题 DL099：AlexNet前三卷积层的感受野"
topic: "deep-learning"
topic_label: "深度学习"
difficulty: "intermediate"
status: "not-started"
tags:
  - exercise
  - deep-learning
source: "Understanding Deep Learning（2026-02-08修订稿），Problem 10.17，印刷185/PDF物理199"
source_id: "DS001"
source_chapter: 10
source_exercise: "10.17"
source_refs: ["DS001 Problem 10.17，印刷185/PDF199", "DS001 图10.16及紧接正文，印刷176/PDF190"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-10-28"
---

# 习题 DL099：AlexNet前三卷积层的感受野

## 题目

### 英文原题

> [!question] 英文原题
> **Problem 10.17** What is the receptive field size at each of the first three layers of AlexNet (i.e., the first three orange blocks in figure 10.16)?

### 中文转述

> [!question] 中文转述
> 求图10.16中前三个橙色块，也就是前三个卷积隐藏层，在原图像上的感受野大小；应把中间池化也计入传播。
>
> ![[附件/习题图/DS001/原图-10.16.png]]
> 原图：印刷176／PDF190，保留原图注。

## 提示

> [!hint]- 提示
> 同时追踪感受野边长$r$与输入坐标步距$j$。前两次池化都会增加$r$并增大后续卷积的步距。

## 解答

> [!success]- 解答
> **独立推导。** 令$r_\ell$为第$\ell$层单元在原输入上的理论覆盖跨度，$j_\ell$为相邻单元中心在原输入上的间隔。初始$r_0=j_0=1$；核大小$k_\ell$、步幅$s_\ell$、膨胀率$d_\ell$给出
> $$
> r_\ell=r_{\ell-1}+(k_\ell-1)d_\ell j_{\ell-1},\qquad
> j_\ell=s_\ell j_{\ell-1}.
> $$
>
> 对二维方核，此递推分别应用于两个空间轴。图明确给第一卷积$11\times11$、步幅4，第二卷积$5\times5$，第三卷积$3\times3$；后两卷积取步幅1。**按AlexNet通常采用的两次$3\times3$、步幅2池化补充约定**，逐层计算为：
>
> |操作|$k,s$|$r$|$j$|
> |---|---|---:|---:|
> |输入|—|1|1|
> |卷积1（橙色1）|11,4|11|4|
> |池化1|3,2|19|8|
> |卷积2（橙色2）|5,1|51|8|
> |池化2|3,2|67|16|
> |卷积3（橙色3）|3,1|99|16|
>
> 因此所求为$\boxed{11\times11,\ 51\times51,\ 99\times99}$。不能把池化块当成题目指定的第二个橙色块而回答11、19、51。
> **来源未定之处。** 本书图和紧接正文没有明写池化核大小；上面的数值对所列补充约定成立，并非仅凭图中尺寸就唯一推出。若两次池化核边长为$p_1,p_2$且步幅仍为2，则前三卷积感受野边长一般为
> $$
> r_1=11,\quad r_2=43+4(p_1-1),\quad
> r_3=75+4(p_1-1)+8(p_2-1).
> $$
> 例如改用两次$2\times2$池化则为11、47、87。以上均为结构上的理论感受野；边缘会涉及补零，特定权重或最大池化实际选中的路径可以更少。

## 相关概念

- [[06 - 深度学习/概念/神经网络|神经网络]]

- [[06 - 深度学习/概念/卷积神经网络|卷积神经网络]]

## 备注

- 原题：[[附件/books/UnderstandingDeepLearning_02_09_26_C.pdf#page=199|主书印刷185／PDF199]]；来源记录见 [[00 - 首页/教材归档/DS001 - Understanding Deep Learning|DS001]]。
- 原图未列池化窗口；数值答案明确附加两次3×3、stride2池化约定，并给一般公式。
- verified只覆盖本题实际核对的来源；解答独立撰写，学习状态不因归档改变。
