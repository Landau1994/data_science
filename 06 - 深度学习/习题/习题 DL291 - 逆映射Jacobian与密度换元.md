---
title: 习题 DL291：逆映射Jacobian与密度换元
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
source_exercise: '18.1'
source_stars: 2
source_refs:
- DS003 Exercise 18.1，印刷559/PDF571
- DS003 式(18.1)–(18.2)，印刷548/PDF560
source_status: verified
solution_status: independently-derived
created: '2026-11-02'
---

# 习题 DL291：逆映射Jacobian与密度换元

## 题目

### 英文原题

> [!question] 英文原题
> **Exercise 18.1（★★）** Consider a transformation $\mathbf x=\mathbf f(\mathbf z)$ along with its inverse $\mathbf z=\mathbf g(\mathbf x)$. By differentiating $\mathbf x=\mathbf f(\mathbf g(\mathbf x))$, show that
> $$\mathbf J\mathbf K=\mathbf I\tag{18.31}$$
> where $\mathbf I$ is the identity matrix, and $\mathbf J$ and $\mathbf K$ are matrices with elements
> $$J_{ij}=\frac{\partial g_i}{\partial x_j},\qquad K_{ij}=\frac{\partial f_i}{\partial z_j}.\tag{18.32}$$
> Using the result that the determinant of a product of matrices is the product of their determinants, show that
> $$\det(\mathbf J)=\frac1{\det(\mathbf K)}.\tag{18.33}$$
> Hence, show that the formula (18.1) for the transformation of a density under a change of variables can be rewritten as
> $$p_{\mathbf x}(\mathbf x)=p_{\mathbf z}(\mathbf g(\mathbf x))|\det\mathbf K|^{-1}\tag{18.34}$$
> where $\mathbf K$ is evaluated at $\mathbf z=\mathbf g(\mathbf x)$.

### 中文转述

> [!question] 中文转述
> **原题18.1。** 给定互逆变换 $x=f(z)$、$z=g(x)$，对复合恒等式求导，证明由(18.32)定义的两Jacobian互为逆矩阵；利用乘积行列式得到(18.33)，再将密度换元公式写成(18.34)。注意 $K$ 应在 $z=g(x)$ 处求值。

## 提示

> [!hint]- 提示 1
> 对 $f(g(x))$ 求导先得到 $KJ=I$；方阵左逆与右逆相同。

## 解答

> [!success]- 解答
> **独立推导。** 设 $f,g$ 为同维欧氏开集之间的 $C^1$ 微分同胚，$J=Dg(x),K=Df(g(x))$。链式法则逐分量给出
> $$\delta_{ij}=\sum_k\frac{\partial f_i}{\partial z_k}\frac{\partial g_k}{\partial x_j}=(KJ)_{ij}.$$
> 方阵乘积为单位矩阵说明两矩阵可逆，故也有 $JK=I$，即原题(18.31)。取行列式得 $\det K\det J=1$，于是(18.33)成立。
>
> 对小体积元，$\mathrm dz=|\det Dg(x)|\mathrm dx$。概率质量守恒给 $p_x(x)\mathrm dx=p_z(g(x))\mathrm dz$，因此
> $$p_x(x)=p_z(g(x))|\det J|=p_z(g(x))|\det K(g(x))|^{-1}.$$
> 绝对值不能省去，方向翻转也须保持密度非负。上述推导依赖非奇异的同维可逆变换；降维映射需其他测度公式。

## 相关概念

- [[06 - 深度学习/概念/归一化流|归一化流]]
- [[03 - 线性代数与优化/概念/链式法则|链式法则]]

## 备注

- 原题及星数：[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=571|印刷559／PDF571]]；题页及引用正文已实际查看原PDF图像，精确定位见 `source_refs`。
- `source_status: verified` 仅指本题及所列实际核对范围；解答独立推导，不构成用户已完成学习，状态保持 `not-started`。
