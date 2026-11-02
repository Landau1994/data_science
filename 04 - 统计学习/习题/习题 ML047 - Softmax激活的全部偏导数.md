---
title: 习题 ML047：Softmax激活的全部偏导数
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
source_exercise: '5.21'
source_stars: 1
source_refs:
- DS003 Exercise 5.21，印刷168/PDF187
- DS003 §5.4.4，式(5.76)–(5.78)，印刷161/PDF180
- DS004 Solution 5.21，印刷58/PDF58
source_status: verified
solution_status: independently-derived
created: '2026-11-02'
---

# 习题 ML047：Softmax激活的全部偏导数

## 题目

### 英文原题

> [!question] 英文原题
> **Exercise 5.21（★）** Show that the derivatives of the softmax activation function (5.76), where the $a_k$ are defined by (5.77), are given by (5.78).

### 中文转述

> [!question] 中文转述
> **原题5.21（★）。** 证明 Softmax 激活函数（softmax activation function）
> $$
> y_k=\frac{e^{a_k}}{\sum_{i=1}^Ke^{a_i}},\tag{5.76}
> \qquad a_k=\mathbf w_k^{\mathsf T}\boldsymbol\phi\tag{5.77}
> $$
> 关于各预激活量的偏导数为
> $$
> \frac{\partial y_k}{\partial a_j}=y_k(I_{kj}-y_j),\tag{5.78}
> $$
> 其中 $I_{kj}$ 为单位矩阵元素。

## 提示

> [!hint]- 提示 1
> 对商使用求导法则，并区分 $j=k$ 与 $j\ne k$。

> [!hint]- 提示 2
> 分母对任意 $a_j$ 的导数都是 $e^{a_j}$，分子只有在 $j=k$ 时才有非零导数。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 设 $K\geq1$，所有 logit $a_i$ 为有限实数，记 $Z=\sum_ie^{a_i}>0$。则
> $$
> \frac{\partial e^{a_k}}{\partial a_j}=I_{kj}e^{a_k},\qquad
> \frac{\partial Z}{\partial a_j}=e^{a_j}.
> $$
> 商法则给出
> $$
> \begin{aligned}
> \frac{\partial y_k}{\partial a_j}
> &=\frac{I_{kj}e^{a_k}Z-e^{a_k}e^{a_j}}{Z^2}\\
> &=I_{kj}\frac{e^{a_k}}Z-\frac{e^{a_k}}Z\frac{e^{a_j}}Z\\
> &=y_k(I_{kj}-y_j).
> \end{aligned}
> $$
> 即对角偏导为 $y_k(1-y_k)$，非对角偏导为 $-y_ky_j$。完整 Jacobian 可写成
> $$
> \mathbf J=\operatorname{diag}(\mathbf y)-\mathbf y\mathbf y^{\mathsf T}.
> $$
> 由于 $\sum_jy_j=1$，每行之和为零；这与给所有 $a_j$ 同加一个常数不会改变输出的性质一致。若继续对模型参数求导，由 $a_j=\mathbf w_j^{\mathsf T}\boldsymbol\phi$ 还有
> $$
> \nabla_{\mathbf w_j}y_k=y_k(I_{kj}-y_j)\boldsymbol\phi.
> $$
> 这里输入特征固定，且不同类别的参数向量分别作为独立求导变量。

## 相关概念

- [[06 - 深度学习/概念/激活函数|激活函数]]
- [[03 - 线性代数与优化/概念/链式法则|链式法则]]
- [[06 - 深度学习/概念/自注意力|自注意力]]

## 备注

- 原题与星号：[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=187|印刷168／PDF物理187]]；原题及实际引用的正文页均已对照原始PDF图像。正文精确定位见 `source_refs`。
- 已查看[[00 - 首页/教材归档/DS004 - Bishop 深度学习答案册|DS004]]印刷58／PDF58的5.21；本解答逐项给出所有偏导、矩阵形式及参数链式导数。自注意力概念中的权重归一化提供同一 Softmax 操作的应用联系。
- `source_status: verified` 仅指本题及所列实际核对范围；独立解答不构成个人完成学习，状态保持 `not-started`。
