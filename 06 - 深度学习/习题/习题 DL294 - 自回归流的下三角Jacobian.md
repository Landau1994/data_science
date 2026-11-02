---
title: 习题 DL294：自回归流的下三角Jacobian
topic: deep-learning
topic_label: 深度学习
difficulty: intermediate
status: not-started
tags:
- exercise
- deep-learning
source: '[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Deep Learning: Foundations and Concepts（DS003）]]'
source_id: DS003
source_chapter: 18
source_exercise: '18.4'
source_stars: 2
source_refs:
- DS003 Exercise 18.4，印刷559/PDF571
- DS003 式(18.16)–(18.18)及三角说明，印刷553/PDF565
source_status: verified
solution_status: independently-derived
created: '2026-11-02'
---

# 习题 DL294：自回归流的下三角Jacobian

## 题目

### 英文原题

> [!question] 英文原题
> **Exercise 18.4（★★）** Show that the Jacobian of the autoregressive normalizing flow transformation given by (18.18) is a lower triangular matrix. The determinant of such a matrix is given by the product of the terms on the leading diagonal and is therefore easily evaluated.

### 中文转述

> [!question] 中文转述
> **原题18.4。** 证明(18.18)的自回归归一化流（autoregressive normalizing flow）逆变换Jacobian为下三角，其行列式为主对角元的乘积，因此易于计算。

## 提示

> [!hint]- 提示 1
> 写出 $z_i=h^{-1}(x_i,g_i(x_{1:i-1},w_i))$，它不依赖 $x_j$（$j>i$）。

## 解答

> [!success]- 解答
> **独立推导。** 正文(18.18)为 $z_i=h^{-1}(x_i,g_i(x_{1:i-1},w_i))$。这里 $h^{-1}$ 只对 $h$ 的第一个参数求逆，而条件函数 $g_i$ 仅使用前 $i-1$ 个观测分量。因而
> $$J_{ij}=\partial_{x_j}z_i=0\quad(j>i),\qquad J_{ii}=\partial_1h^{-1}(x_i,g_i(x_{<i},w_i)).$$
> 所以 $J$ 为下三角，$\det J=\prod_iJ_{ii}$。若 $h$ 对第一参数可微且导数非零，则逆函数定理给 $J_{ii}=1/\partial_1h(z_i,g_i(x_{<i},w_i))$；于是
> $$\ln|\det J|=-\sum_i\ln|\partial_1h(z_i,g_i(x_{<i},w_i))|.$$
> 例如 $h(z_i,c_i)=\exp(s_i)z_i+b_i$ 时，$J_{ii}=\exp(-s_i)$，对数行列式为 $-\sum_i s_i$。非对角项可以复杂，但不影响行列式。
>
> 正文PDF565将同一Jacobian称作“upper-triangular”，与其依赖关系相反；本题题面要求的“lower triangular”正确。

## 相关概念

- [[06 - 深度学习/概念/归一化流|归一化流]]
- [[03 - 线性代数与优化/概念/链式法则|链式法则]]

## 备注

- 原题及星数：[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=571|印刷559／PDF571]]；题页及引用正文已实际查看原PDF图像，精确定位见 `source_refs`。
- 正文上下三角措辞冲突已公开说明，未改写英文题面。
- `source_status: verified` 仅指本题及所列实际核对范围；解答独立推导，不构成用户已完成学习，状态保持 `not-started`。
