---
title: "习题 DL055：二元交叉熵对logit的导数"
topic: "deep-learning"
topic_label: "深度学习"
difficulty: "intermediate"
status: "not-started"
tags:
  - exercise
  - deep-learning
source: "Understanding Deep Learning（2026-02-08修订稿），Problem 7.5，印刷115／PDF物理129"
source_id: "DS001"
source_chapter: 7
source_exercise: "7.5"
source_refs: ["DS001 Problem 7.5，印刷115/PDF129"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-10-28"
---

# 习题 DL055：二元交叉熵对logit的导数

## 题目

### 英文原题

> [!question] 英文原题
> **Problem 7.5** Calculate the derivative $\partial\ell_i/\partial f[x_i,\phi]$ for the binary classification loss function:
> $$
> \ell_i=-(1-y_i)\log\!\left[1-\operatorname{sig}[f[x_i,\phi]]\right]-y_i\log\!\left[\operatorname{sig}[f[x_i,\phi]]\right],\tag{7.37}
> $$
> where the function $\operatorname{sig}[\bullet]$ is the logistic sigmoid and is defined as:
> $$
> \operatorname{sig}[z]=\frac{1}{1+\exp[-z]}.\tag{7.38}
> $$

### 中文转述

> [!question] 中文转述
> 对式(7.37)的二元分类交叉熵，求关于Sigmoid之前模型输出的导数；Sigmoid定义见式(7.38)。



## 提示

> [!hint]- 提示
> 先对预测概率求导，再乘Sigmoid的导数。

## 解答

> [!success]- 解答
> **独立推导。** 记$t=f[x_i,\phi]$、$p=\operatorname{sig}[t]$。有限$t$下$0<p<1$，且$p'=p(1-p)$。因此
> $$
> \frac{\partial\ell_i}{\partial t}
> =\left(\frac{1-y_i}{1-p}-\frac{y_i}{p}\right)p(1-p)
> =(1-y_i)p-y_i(1-p)=p-y_i.
> $$
> 故所求为$\operatorname{sig}[f[x_i,\phi]]-y_i$。这是对logit的导数；对概率$p$的导数没有最后的约简形式。

## 相关概念

- [[06 - 深度学习/概念/神经网络|神经网络]]
- [[06 - 深度学习/概念/激活函数|激活函数]]
- [[03 - 线性代数与优化/概念/链式法则|链式法则]]

## 备注

- 原题已逐页核对：[[附件/books/UnderstandingDeepLearning_02_09_26_C.pdf#page=129|印刷115／PDF129]]。来源核对仅覆盖本题原文和已列定位，学习状态不随归档改变。
