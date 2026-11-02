---
title: 习题 ML060：PPCA均值对数似然的严格凹性
topic: statistical-learning
topic_label: 统计学习
difficulty: intermediate
status: not-started
tags:
- exercise
- statistical-learning
source: '[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Deep Learning: Foundations and Concepts（DS003）]]'
source_id: DS003
source_chapter: 16
source_exercise: '16.10'
source_stars: 2
source_refs:
- DS003 Exercise 16.10，印刷529/PDF543
- DS003 对数似然(16.44)，印刷509/PDF523；均值最大值说明，印刷510/PDF524
source_status: verified
solution_status: independently-derived
created: '2026-11-02'
---

# 习题 ML060：PPCA均值对数似然的严格凹性

## 题目

### 英文原题

> [!question] 英文原题
> **Exercise 16.10（★★）** By evaluating the second derivatives of the log likelihood function (16.44) for the probabilistic PCA model with respect to the parameter $\boldsymbol\mu$, show that the stationary point $\boldsymbol\mu_{\mathrm{ML}}=\overline{\mathbf x}$ represents the unique maximum.

### 中文转述

> [!question] 中文转述
> **原题16.10。** 对PPCA对数似然(16.44)的均值参数求二阶导数，证明样本均值驻点是唯一最大点。

## 提示

> [!hint]- 提示 1
> 梯度为 $NC^{-1}(\bar x-\mu)$，所以Hessian为 $-NC^{-1}$。

## 解答

> [!success]- 解答
> **独立推导。** 固定 $W,\sigma^2>0$，$C=WW^T+\sigma^2I\succ0$。由(16.44)，
> $$\frac{\partial\ell}{\partial\mu_i}=\sum_{n,j}(C^{-1})_{ij}(x_{nj}-\mu_j),\qquad\frac{\partial^2\ell}{\partial\mu_i\partial\mu_j}=-N(C^{-1})_{ij}.$$
> 因此对任意非零向量 $h$，$h^T\nabla_\mu^2\ell\,h=-Nh^TC^{-1}h<0$。对数似然在整个 $\mathbb R^D$ 严格凹。驻点由 $NC^{-1}(\bar x-\mu)=0$ 得 $\mu=\bar x$；严格凹性使其为唯一全局最大点。
>
> 这里的唯一性只针对固定合法协方差时的均值优化。若令噪声为零导致 $C$ 奇异，原普通高斯对数密度已不成立，不能直接用同一个Hessian论证。

## 相关概念

- [[04 - 统计学习/概念/无监督学习|无监督学习]]
- [[05 - 概率模型与推断/概念/潜变量|潜变量]]
- [[03 - 线性代数与优化/概念/凸函数|凸函数]]
- [[03 - 线性代数与优化/概念/最优性条件|最优性条件]]

## 备注

- 原题及星数：[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=543|印刷529／PDF543]]；题页及引用正文已实际查看原PDF图像，精确定位见 `source_refs`。
- `source_status: verified` 仅指本题及所列实际核对范围；解答独立推导，不构成用户已完成学习，状态保持 `not-started`。
