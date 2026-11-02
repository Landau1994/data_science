---
title: 习题 DL321：标量势函数得分的对称Jacobian
topic: deep-learning
topic_label: 深度学习
difficulty: beginner
status: not-started
tags:
- exercise
- deep-learning
source: '[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Bishop《深度学习：基础与概念》（DS003）]]'
source_id: DS003
source_chapter: 20
source_exercise: '20.14'
source_stars: 1
source_refs:
- DS003 Exercise 20.14，印刷605/PDF615
- DS003 §20.3–20.3.2，式(20.42)–(20.50)，印刷594–596/PDF604–606
source_status: verified
solution_status: independently-derived
created: '2026-11-02'
---

# 习题 DL321：标量势函数得分的对称Jacobian

## 题目

### 英文原题

> [!question] 英文原题
> **20.14 (★)** The score function is defined by $\mathbf s(\mathbf x)=\nabla_{\mathbf x}p(\mathbf x\mid\mathbf w)$ and is therefore a vector of the same dimensionality as the input vector $\mathbf x$. Consider a matrix whose elements are given by
> $$
> M_{ij}=\frac{\partial s_i}{\partial x_j}-\frac{\partial s_j}{\partial x_i}.\tag{20.64}
> $$
> Show that if the score function is defined by taking the gradient $\mathbf s=\nabla_{\mathbf x}\phi(\mathbf x)$ of the output of a neural network with a single output variable $\phi(\mathbf x)$, then all the matrix elements $M_{ij}=0$ for all pairs $i,j$. Note that if the score function $\mathbf s(\mathbf x)=\nabla_{\mathbf x}p(\mathbf x\mid\mathbf w)$ is instead represented directly by a deep neural network with the same number of outputs as inputs, then only the diagonal matrix elements $M_{ii}=0$, and so the output of the network does not in general correspond to the gradient of any scalar function.

### 中文转述

> [!question] 中文转述
> **原题20.14。** 得分函数定义为 $\mathbf s(\mathbf x)=\nabla_{\mathbf x}p(\mathbf x\mid\mathbf w)$，其维数与输入相同。令
> $$
> M_{ij}=\frac{\partial s_i}{\partial x_j}-\frac{\partial s_j}{\partial x_i}
> $$
> 如(20.64)。若使用单输出神经网络的标量输出 $\phi(\mathbf x)$，并取 $\mathbf s=\nabla_{\mathbf x}\phi(\mathbf x)$，证明对所有 $i,j$ 都有 $M_{ij}=0$。若改用输入、输出维数相同的网络直接表示得分，则只有对角元 $M_{ii}=0$，网络输出一般不对应任何标量函数的梯度。

## 提示

> [!hint]- 提示
> 使用二阶混合偏导交换；直接向量场可构造非零旋度的二维例子。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 若 $\phi\in C^2$，$s_i=\partial_i\phi$，则由混合偏导交换定理，
> $$
> M_{ij}=\partial_j\partial_i\phi-\partial_i\partial_j\phi=0.
> $$
> 对任意可微向量场，对角元 $M_{ii}=0$ 都是恒等式，但非对角元不受约束。例如二维网络可表达 $\mathbf s(x_1,x_2)=(-x_2,x_1)$，其 $M_{12}=-1-1=-2$，因此不能在任何开邻域表示成 $C^2$ 标量函数的梯度。原文“only the diagonal”应理解为只**保证**对角为零，而非断言每一个非对角元必非零。
>
> 标准得分按正文(20.42)应为 $\nabla\ln p$，原题两次写成 $\nabla p$，此处没有修改英文。无论对密度还是对数密度取梯度，上述对称性证明都成立，但它们是数值不同的向量场。若网络采用ReLU，经典二阶偏导需在可微区域讨论或改用弱导数；不能在折点直接套用 $C^2$ 定理。对称Jacobian只给局部可积性的条件，全球存在势函数还与定义域拓扑有关，且存在势也不自动保证 $e^\phi$ 可归一化为密度。

## 相关概念

- [[06 - 深度学习/概念/扩散模型|扩散模型]]
- [[06 - 深度学习/概念/得分匹配|得分匹配]]
- [[03 - 线性代数与优化/概念/链式法则|链式法则]]

## 备注

- 原题已实际对照[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=615|印刷605／PDF615]]；正文引用范围见 `source_refs`。
- 英文原题与中文转述分列，原文疑误另注；未使用配套答案册。`source_status: verified` 仅表示本题及所列公式的实际核对范围；解答写成不表示个人学习完成，状态保持 `not-started`。
