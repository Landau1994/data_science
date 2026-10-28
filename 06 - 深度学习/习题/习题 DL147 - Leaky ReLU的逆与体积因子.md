---
title: "习题 DL147：Leaky ReLU的逆与体积因子"
topic: deep-learning
topic_label: 深度学习
difficulty: intermediate
status: not-started
tags:
  - exercise
  - deep-learning
source: "Understanding Deep Learning（2026-02-08 修订稿），Problem 16.7，印刷326／PDF物理340"
source_id: DS001
source_chapter: 16
source_exercise: "16.7"
source_refs: ["DS001 Problem 16.7，印刷326/PDF340"]
source_status: verified
solution_status: independently-derived
created: 2026-10-28
---

# 习题 DL147：Leaky ReLU的逆与体积因子

## 题目

### 英文原题

> [!question] 英文原题
> **Problem 16.7** The Leaky ReLU is defined as:
> $$
> \operatorname{LReLU}[z]=\begin{cases}0.1z&z<0,\\z&z\ge0.\end{cases}\tag{16.31}
> $$
> Write an expression for the inverse of the leaky ReLU. Write an expression for the inverse absolute determinant of the Jacobian $|\partial\mathbf f[\mathbf z]/\partial\mathbf z|^{-1}$ for an elementwise transformation $\mathbf x=\mathbf f[\mathbf z]$ of the multivariate variable $\mathbf z$ where:
> $$
> \mathbf f[\mathbf z]=[\operatorname{LReLU}[z_1],\operatorname{LReLU}[z_2],\ldots,\operatorname{LReLU}[z_D]]^T.\tag{16.32}
> $$

### 中文转述

> [!question] 中文转述
> 对式 (16.31) 的 Leaky ReLU 写出逆函数；对式 (16.32) 的逐坐标变换，求雅可比行列式绝对值的倒数。


## 提示

> [!hint]- 提示
> 变换保持符号，负半轴逆斜率为 $10$；多维雅可比为对角矩阵。

## 解答

> [!success]- 解答
> 独立推导。单变量严格递增且满射到实线，逆为
> $$
> \operatorname{LReLU}^{-1}(x)=\begin{cases}10x,&x<0,\\x,&x\ge0.\end{cases}
> $$
> 在所有 $z_j\ne0$ 处，雅可比为 $\operatorname{diag}(d_1,\ldots,d_D)$，其中负坐标的 $d_j=0.1$，正坐标的 $d_j=1$。若 $n_- =\#\{j:z_j<0\}$，则
> $$
> |\det Df(z)|=10^{-n_-},\qquad |\det Df(z)|^{-1}=10^{n_-}.
> $$
> 零坐标处经典导数不存在；上述密度换元因子按几乎处处理解，不必人为给折点指定唯一导数。

## 相关概念

- [[06 - 深度学习/概念/归一化流|归一化流]]：可逆变换、雅可比与密度变换。

## 备注

- 原题：[[附件/books/UnderstandingDeepLearning_02_09_26_C.pdf#page=340|印刷 326／PDF 340]]；教材记录见 [[00 - 首页/教材归档/DS001 - Understanding Deep Learning|DS001]]。
- 题干、公式及所引原页已核对；解答为独立推导。
