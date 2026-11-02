---
title: 习题 ML048：多类交叉熵对Softmax参数的梯度
topic: statistical-learning
topic_label: 统计学习
difficulty: beginner
status: not-started
tags:
- exercise
- statistical-learning
source: '[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Deep Learning: Foundations and Concepts（DS003）]]'
source_id: DS003
source_chapter: 5
source_exercise: '5.22'
source_stars: 1
source_refs:
- DS003 Exercise 5.22，印刷169/PDF188
- DS003 §5.4.4，式(5.76)–(5.81)，印刷161–162/PDF180–181
- DS004 Solution 5.22，式(177)及链式推导，印刷58/PDF58
source_status: verified
solution_status: independently-derived
created: '2026-11-02'
---

# 习题 ML048：多类交叉熵对Softmax参数的梯度

## 题目

### 英文原题

> [!question] 英文原题
> **Exercise 5.22（★）** Using the result (5.78) for the derivatives of the softmax activation function, show that the gradients of the cross-entropy error (5.80) are given by (5.81).

### 中文转述

> [!question] 中文转述
> **原题5.22（★）。** 利用 Softmax 导数式 (5.78)，证明多类交叉熵误差（cross-entropy error）
> $$
> E(\mathbf w_1,\ldots,\mathbf w_K)=-\sum_{n=1}^N\sum_{k=1}^Kt_{nk}\ln y_{nk},\tag{5.80}
> $$
> 其中 $y_{nk}=e^{a_{nk}}/\sum_ie^{a_{ni}}$、$a_{nk}=\mathbf w_k^{\mathsf T}\boldsymbol\phi_n$，标签采用1-of-$K$编码，满足
> $$
> \nabla_{\mathbf w_j}E=\sum_{n=1}^N(y_{nj}-t_{nj})\boldsymbol\phi_n.\tag{5.81}
> $$
> 题中所用 Softmax 导数为 $\partial y_{nk}/\partial a_{nj}=y_{nk}(I_{kj}-y_{nj})$。

## 提示

> [!hint]- 提示 1
> 先只看样本 $n$：对 $a_{nj}$ 求导时，所有类别输出 $y_{nk}$ 都会变化，不能只取 $k=j$ 的一项。

> [!hint]- 提示 2
> 约掉 $y_{nk}$ 后，使用标签归一化 $\sum_kt_{nk}=1$，再对 $\mathbf w_j$ 用链式法则。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 设所有参数和固定特征为有限实数，标签 $t_{nk}\in\{0,1\}$ 且每行恰有一个1。有限 Softmax 给出 $y_{nk}>0$，故对数和中间除法均有定义。
>
> 记单样本误差为 $E_n=-\sum_kt_{nk}\ln y_{nk}$。链式法则与式 (5.78) 给出
> $$
> \begin{aligned}
> \frac{\partial E_n}{\partial a_{nj}}
> &=\sum_{k=1}^K\frac{\partial E_n}{\partial y_{nk}}\frac{\partial y_{nk}}{\partial a_{nj}}\\
> &=-\sum_{k=1}^K\frac{t_{nk}}{y_{nk}}\,y_{nk}(I_{kj}-y_{nj})\\
> &=-t_{nj}+y_{nj}\sum_{k=1}^Kt_{nk}\\
> &=y_{nj}-t_{nj}.
> \end{aligned}
> $$
> 又 $a_{nj}=\mathbf w_j^{\mathsf T}\boldsymbol\phi_n$，因此 $\nabla_{\mathbf w_j}a_{nj}=\boldsymbol\phi_n$。对每个样本的贡献求和，得到
> $$
> \nabla_{\mathbf w_j}E=\sum_{n=1}^N(y_{nj}-t_{nj})\boldsymbol\phi_n,
> $$
> 这就是式 (5.81)。按参数分量写即 $\partial E/\partial w_{ij}=\sum_n(y_{nj}-t_{nj})\phi_{ni}$，其中 $w_{ij}$ 是第 $j$ 类参数向量的第 $i$ 个分量。
>
> 同一推导对满足 $t_{nk}\geq0$、$\sum_kt_{nk}=1$ 的软标签也成立，因为唯一使用的标签代数性质是行和等于一。若标签行和不是一，导数应为 $y_{nj}\sum_kt_{nk}-t_{nj}$，不能无条件写成 $y_{nj}-t_{nj}$。原书用总和误差；平均误差的梯度需除以 $N$。

## 相关概念

- [[04 - 统计学习/概念/交叉熵|交叉熵]]
- [[04 - 统计学习/概念/损失函数与经验风险|损失函数与经验风险]]
- [[06 - 深度学习/概念/激活函数|激活函数]]
- [[03 - 线性代数与优化/概念/链式法则|链式法则]]

## 备注

- 原题与星号：[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=188|印刷169／PDF物理188]]；原题及实际引用的正文页均已对照原始PDF图像。正文精确定位见 `source_refs`。
- 已查看[[00 - 首页/教材归档/DS004 - Bishop 深度学习答案册|DS004]]印刷58／PDF58的5.22。这里独立保留类别求和及标签行归一化步骤，避免遗漏 Softmax 输出之间的耦合。
- `source_status: verified` 仅指本题及所列实际核对范围；独立解答不构成个人完成学习，状态保持 `not-started`。
