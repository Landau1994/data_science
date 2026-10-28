---
title: "习题 DL114：饱和softmax的全部偏导数"
topic: "deep-learning"
topic_label: "深度学习"
difficulty: "intermediate"
status: "not-started"
tags:
  - exercise
  - deep-learning
source: "Understanding Deep Learning（2026-02-08修订稿），Problem 12.4，印刷239/PDF物理253"
source_id: "DS001"
source_chapter: 12
source_exercise: "12.4"
source_refs: ["DS001 Problem 12.4，印刷239/PDF253"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-10-28"
---

# 习题 DL114：饱和softmax的全部偏导数

## 题目

### 英文原题

> [!question] 英文原题
> **Problem 12.4** Consider the softmax operation:
> $$
> y_i=\operatorname{softmax}_i[\mathbf z]=\frac{\exp[z_i]}{\sum_{j=1}^5\exp[z_j]},\tag{12.19}
> $$
> in the case where there are five inputs with values: $z_1=-3,z_2=1,z_3=100,z_4=5,z_5=-1$. Compute the 25 derivatives, $\partial y_i/\partial z_j$ for all $i,j\in\{1,2,3,4,5\}$. What do you conclude?

### 中文转述

> [!question] 中文转述
> 对五维softmax，输入(-3,1,100,5,-1)，计算全部25个偏导并解释。

## 提示

> [!hint]- 提示
> 先推导J=diag(y)−yyᵀ。数值上先减去最大logit；对占优类别的对角项，应通过其他类别概率之和计算，避免1−y3舍入为0。

## 解答

> [!success]- 解答
> **独立推导。** 商法则给出
> $$
> J_{ij}=y_i(\delta_{ij}-y_j),\qquad J=\operatorname{diag}(y)-yy^T.
> $$
> 将所有logit减100不改变概率。用Python Decimal、110位十进制精度实际计算指数及归一化，$y$ 约为
> $$
> (1.85211677\!\times10^{-45},\,1.01122149\!\times10^{-43},\,
> 1-5.637742\!\times10^{-42},\,5.52108228\!\times10^{-42},\,
> 1.36853947\!\times10^{-44})^T.
> $$
> 全部偏导（行是输出i，列是输入j）为：
>
> | | $z_1$ | $z_2$ | $z_3$ | $z_4$ | $z_5$ |
> | --- | --- | --- | --- | --- | --- |
> | $y_1$ | $1.85212\times10^{-45}$ | $-1.87290\times10^{-88}$ | $-1.85212\times10^{-45}$ | $-1.02257\times10^{-86}$ | $-2.53469\times10^{-89}$ |
> | $y_2$ | $-1.87290\times10^{-88}$ | $1.01122\times10^{-43}$ | $-1.01122\times10^{-43}$ | $-5.58304\times10^{-85}$ | $-1.38390\times10^{-87}$ |
> | $y_3$ | $-1.85212\times10^{-45}$ | $-1.01122\times10^{-43}$ | $5.63774\times10^{-42}$ | $-5.52108\times10^{-42}$ | $-1.36854\times10^{-44}$ |
> | $y_4$ | $-1.02257\times10^{-86}$ | $-5.58304\times10^{-85}$ | $-5.52108\times10^{-42}$ | $5.52108\times10^{-42}$ | $-7.55582\times10^{-86}$ |
> | $y_5$ | $-2.53469\times10^{-89}$ | $-1.38390\times10^{-87}$ | $-1.36854\times10^{-44}$ | $-7.55582\times10^{-86}$ | $1.36854\times10^{-44}$ |
>
> 表中是近似值而非精确零。softmax已极度饱和于第3类，整个Jacobian量级至多约 $10^{-42}$，局部梯度传递会很弱。精确Jacobian每行和为0，反映所有logit加同一常数不变。单独softmax梯度很小不意味着交叉熵对logit的融合梯度必为零；后者为y减目标。
> 复现：取Decimal精度110，算 $e_i=\exp(z_i-100), y_i=e_i/\sum e$；非对角项为 $-y_iy_j$，对角项用 $y_i\sum_{k\ne i}y_k$。这次有限计算只对应本题五个输入。

## 相关概念

- [[06 - 深度学习/概念/神经网络|神经网络]]

- [[06 - 深度学习/概念/自注意力|自注意力]]
- [[03 - 线性代数与优化/概念/链式法则|链式法则]]

## 备注

- 原题：[[附件/books/UnderstandingDeepLearning_02_09_26_C.pdf#page=253|主书印刷239／PDF253]]；来源记录见 [[00 - 首页/教材归档/DS001 - Understanding Deep Learning|DS001]]。
- verified只覆盖本题实际核对的来源；解答独立撰写，学习状态不因归档改变。
