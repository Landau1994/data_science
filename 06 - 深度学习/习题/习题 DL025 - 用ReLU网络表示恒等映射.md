---
title: "习题 DL025：用ReLU网络表示恒等映射"
topic: deep-learning
topic_label: 深度学习
difficulty: beginner
status: not-started
tags:
  - exercise
  - deep-learning
source: "Understanding Deep Learning（2026-02-08修订稿），Problem 4.7，印刷55／PDF物理69"
source_id: DS001
source_chapter: 4
source_exercise: "4.7"
source_refs: ["DS001 Problem 4.7，印刷55/PDF69", "DS001 式(3.1)–(3.2)，印刷25/PDF39"]
source_status: verified
solution_status: independently-derived
created: 2026-10-28
---

# 习题 DL025：用ReLU网络表示恒等映射

## 题目

### 英文原题

> [!question] 英文原题
> **Problem 4.7** Choose values for the parameters $\phi=\{\phi_0,\phi_1,\phi_2,\phi_3,\theta_{10},\theta_{11},\theta_{20},\theta_{21},\theta_{30},\theta_{31}\}$ for the shallow neural network in equation 3.1 (with ReLU activation functions) that will define an identity function over a finite range $x\in[a,b]$.

### 中文转述

> [!question] 中文转述
> **UDL 原题 4.7。** 为式 (3.1) 中使用 ReLU 的浅层网络选择参数
> $$
> \phi=\{\phi_0,\phi_1,\phi_2,\phi_3,\theta_{10},\theta_{11},\theta_{20},\theta_{21},\theta_{30},\theta_{31}\},
> $$
> 使它在有限区间 $x\in[a,b]$ 上表示恒等函数（identity function）$f(x)=x$。

## 提示

> [!hint]- 提示 1
> 单个 $\operatorname{ReLU}(x)$ 会丢掉负半轴。能否用另一个单元表示负部，再作相减？

## 解答

> [!success]- 解答
> **独立构造。** 对任意有限实数 $a\le b$，以下同一组参数都适用：
> $$
> (\phi_0,\phi_1,\phi_2,\phi_3,\theta_{10},\theta_{11},
> \theta_{20},\theta_{21},\theta_{30},\theta_{31})
> =(0,1,-1,0,0,1,0,-1,0,0).
> $$
> 于是
> $$
> h_1=\operatorname{ReLU}(x),\qquad
> h_2=\operatorname{ReLU}(-x),\qquad h_3=\operatorname{ReLU}(0)=0,
> $$
> $$
> f(x)=h_1-h_2=\operatorname{ReLU}(x)-\operatorname{ReLU}(-x).
> $$
> 若 $x\ge0$，右边为 $x-0=x$；若 $x<0$，右边为 $0-(-x)=x$。所以它在整个实线上都等于 $x$，尤其在任意给定有限区间 $[a,b]$ 上成立，也覆盖负数区间、跨零区间及 $a=b$ 的单点情形。第三个隐藏单元可以保留而不参与输出，符合原题的三单元模型。

## 相关概念

- [[06 - 深度学习/概念/神经网络|神经网络]]：全连接层、ReLU 与仿射输出。

## 备注

- 原题：[[附件/books/UnderstandingDeepLearning_02_09_26_C.pdf#page=69|UDL 印刷55／PDF物理69]]；来源记录见 [[00 - 首页/教材归档/DS001 - Understanding Deep Learning|DS001]]。
- 这是较题目要求更强的全实线构造，不需要假设输入非负，也没有把区间端点当成训练数据。
- 来源状态 verified 仅覆盖本题原文与所列定位；解答为独立推导，学习状态保持 not-started。
