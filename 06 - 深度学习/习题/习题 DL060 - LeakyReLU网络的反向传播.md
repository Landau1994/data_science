---
title: "习题 DL060：LeakyReLU网络的反向传播"
topic: "deep-learning"
topic_label: "深度学习"
difficulty: "intermediate"
status: "not-started"
tags:
  - exercise
  - deep-learning
source: "Understanding Deep Learning（2026-02-08修订稿），Problem 7.10，印刷116／PDF物理130"
source_id: "DS001"
source_chapter: 7
source_exercise: "7.10"
source_refs: ["DS001 Problem 7.10，印刷116/PDF130"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-10-28"
---

# 习题 DL060：LeakyReLU网络的反向传播

## 题目

### 英文原题

> [!question] 英文原题
> **Problem 7.10\*** Derive the equations for the backward pass of the backpropagation algorithm for a network that uses leaky ReLU activations, which are defined as:
> $$
> a[z]=\operatorname{ReLU}[z]=
> \begin{cases}\alpha\cdot z&z<0\\z&z\ge0,\end{cases}\tag{7.43}
> $$
> where $\alpha$ is a small positive constant (typically 0.1).

### 中文转述

> [!question] 中文转述
> 推导使用Leaky ReLU的网络的完整反向传播递推，负半轴斜率α为固定正小常数，通常取0.1。



## 提示

> [!hint]- 提示
> 权重和偏置梯度仍是仿射层公式；只需把激活门在负半轴的零换成α。

## 解答

> [!success]- 解答
> **独立推导。** 用$h_0=x$、$z_k=b_k+W_kh_{k-1}$、$h_k=a[z_k]$表示$k=1,\ldots,K$个隐藏层，输出为$f=b_{K+1}+W_{K+1}h_K$。定义门向量
> $$
> q_{k,j}=\begin{cases}\alpha&z_{k,j}<0\\1&z_{k,j}>0.\end{cases}
> $$
> 先根据损失计算输出梯度$g=\nabla_f\ell$。输出层有
> $$
> \nabla_{b_{K+1}}\ell=g,\quad
> \nabla_{W_{K+1}}\ell=gh_K^T,\quad
> \delta_K=q_K\odot(W_{K+1}^Tg).
> $$
> 对$k=K,K-1,\ldots,1$，依次计算
> $$
> \nabla_{b_k}\ell=\delta_k,\qquad
> \nabla_{W_k}\ell=\delta_kh_{k-1}^T,
> $$
> 且在$k>1$时递推
> $$
> \delta_{k-1}=q_{k-1}\odot(W_k^T\delta_k).
> $$
> 输入梯度为$\nabla_x\ell=W_1^T\delta_1$。这些公式由仿射层链式法则和逐坐标激活导数相乘得到；小批量时对样本梯度按损失的求和或平均约定聚合。当$\alpha\ne1$时零点不可微，程序必须另选约定，例如与原题$z\ge0$分支一致取$q=1$；这不是零点普通导数。原文式(7.43)把Leaky ReLU记作ReLU，此处保留该排印记号。

## 相关概念

- [[06 - 深度学习/概念/神经网络|神经网络]]
- [[06 - 深度学习/概念/激活函数|激活函数]]
- [[03 - 线性代数与优化/概念/链式法则|链式法则]]

## 备注

- 原题已逐页核对：[[附件/books/UnderstandingDeepLearning_02_09_26_C.pdf#page=130|印刷116／PDF130]]。来源核对仅覆盖本题原文和已列定位，学习状态不随归档改变。
