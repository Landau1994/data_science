---
title: "习题 DL221：条件均值处总体平方风险的Hessian"
topic: deep-learning
topic_label: 深度学习
difficulty: intermediate
status: not-started
tags: [exercise, deep-learning]
source: "[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Bishop《深度学习：基础与概念》（DS003）]]"
source_id: DS003
source_chapter: 8
source_exercise: "8.9"
source_stars: 2
source_refs: ["DS003 Exercise 8.9，印刷251／PDF物理268", "DS003 §8.1.6，式(8.36)–(8.41)，印刷242–244/PDF259–261", "DS003 式(4.37)，印刷121/PDF140"]
source_status: verified
solution_status: independently-derived
created: 2026-11-02
---

# 习题 DL221：条件均值处总体平方风险的Hessian

## 题目

### 英文原题

> [!question] 英文原题
> **8.9 (★★)** Consider a squared-loss function of the form
> $$
> E(\mathbf w)=\frac12\iint\{y(\mathbf x,\mathbf w)-t\}^2p(\mathbf x,t)\,\mathrm d\mathbf x\,\mathrm dt\tag{8.78}
> $$
> where $y(\mathbf x,\mathbf w)$ is a parametric function such as a neural network. The result (4.37) shows that the function $y(\mathbf x,\mathbf w)$ that minimizes this error is given by the conditional expectation of $t$ given $\mathbf x$. Use this result to show that the second derivative of $E$ with respect to two elements $w_r$ and $w_s$ of the vector $\mathbf w$, is given by
> $$
> \frac{\partial^2E}{\partial w_r\partial w_s}=\int\frac{\partial y}{\partial w_r}\frac{\partial y}{\partial w_s}p(\mathbf x)\,\mathrm d\mathbf x.\tag{8.79}
> $$
> Note that, for a finite sample from $p(\mathbf x)$, we obtain (8.40).

### 中文转述

> [!question] 中文转述
> 考虑总体平方损失(8.78)，其中 $y(\mathbf x,\mathbf w)$ 是神经网络等参数化函数。结果(4.37)说明，使该误差最小的函数是 $t$ 给定 $\mathbf x$ 的条件期望。利用这一结果，证明 $E$ 关于任意两个参数 $w_r,w_s$ 的二阶导数为(8.79)所给出的输入分布下导数外积积分。用来自 $p(\mathbf x)$ 的有限样本表示该积分时，得到(8.40)。

## 提示

> [!hint]- 提示
> 求导后还有 $(y-t)y_{rs}$ 一项。它是在何种参数处平均为零？

## 解答

> [!success]- 解答
> **证明范围：独立推导。**
> 设 $m(x)=\mathbb E[T\mid X=x]$ 存在，相关风险和导数积分有限，且 $y$ 二阶可微并有可积控制函数允许交换两次求导与积分。记 $y_r=\partial_ry$、$y_{rs}=\partial_{rs}y$。直接求导与条件平均给
> $$
> \partial_{rs}E=\mathbb E[y_ry_s+(y-T)y_{rs}]
> =\int[y_ry_s+(y-m(x))y_{rs}]p(x)\,dx.
> $$
> 若在所考察参数 $w^\star$，模型确实实现 $y(x,w^\star)=m(x)$（$p$几乎处处），第二项精确消失，得到(8.79)。因此无需另假定残差与二阶导数不相关；条件均值为零已足够。
>
> 仅是某个受限参数模型的最优点，不能保证它能表达条件均值，也不保证第二项为0。例如无有效输入、$T=-1$ 恒定、$y(w)=w^2$，最优参数 $w=0$，风险 $E=\tfrac12(w^2+1)^2$ 的二阶导数为2，而右侧 $\mathbb E(y')^2=0$。这说明必须保留可实现性和评价点条件。
>
> 用样本近似总体期望得到 $N^{-1}\sum_n g_ng_n^{\mathsf T}$。若训练误差定义为**总和**而非均值，需乘回 $N$，才是(8.40)的 $\sum_n\nabla a_n\nabla a_n^{\mathsf T}$（线性输出 $a_n=y_n$）。对任意有限训练样本，残差二阶项一般不会恰好相消，故样本版仍为近似。

## 相关概念

- [[01 - 概率论/概念/期望|期望]]
- [[01 - 概率论/概念/条件概率|条件概率]]
- [[04 - 统计学习/概念/损失函数与经验风险|损失函数与经验风险]]
- [[03 - 线性代数与优化/概念/梯度与驻点|梯度与驻点]]

## 备注

- 原题已实际查看 [[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=268|印刷251／PDF物理268]]；所列依赖正文亦逐页核对，精确位置见 `source_refs`。
- (8.79)须在模型实现条件均值的参数处解释；有限样本的总和与平均的归一化差异已明确。
- 解答未使用配套答案册。`source_status: verified` 指本题原文与所列依赖的核对范围；独立推导不代表个人学习完成，状态保持 `not-started`。
