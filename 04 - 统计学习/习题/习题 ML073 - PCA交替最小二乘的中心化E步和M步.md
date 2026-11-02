---
title: 习题 ML073：PCA交替最小二乘的中心化E步和M步
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
source_exercise: '16.23'
source_stars: 2
source_refs:
- DS003 Exercise 16.23，印刷530、531/PDF544、545
- DS003 PCA E/M迭代(16.70)–(16.71)及矩阵维度，印刷520/PDF534
source_status: verified
solution_status: independently-derived
created: '2026-11-02'
---

# 习题 ML073：PCA交替最小二乘的中心化E步和M步

## 题目

### 英文原题

> [!question] 英文原题
> **Exercise 16.23（★★）** Let $\mathbf W$ be a $D\times M$ matrix whose columns define a linear subspace of dimensionality $M$ embedded within a data space of dimensionality $D$, and let $\boldsymbol\mu$ be a $D$-dimensional vector. Given a data set $\{\mathbf x_n\}$ where $n=1,\ldots,N$, we can approximate the data points using a linear mapping from a set of $M$-dimensional vectors $\{\mathbf z_n\}$, so that $\mathbf x_n$ is approximated by $\mathbf W\mathbf z_n+\boldsymbol\mu$. The associated sum-of-squares reconstruction cost is given by
> $$J=\sum_{n=1}^N\|\mathbf x_n-\boldsymbol\mu-\mathbf W\mathbf z_n\|^2.\tag{16.90}$$
> First show that minimizing $J$ with respect to $\boldsymbol\mu$ leads to an analogous expression with $\mathbf x_n$ and $\mathbf z_n$ replaced by zero-mean variables $\mathbf x_n-\overline{\mathbf x}$ and $\mathbf z_n-\overline{\mathbf z}$, respectively, where $\overline{\mathbf x}$ and $\overline{\mathbf z}$ denote sample means. Then show that minimizing $J$ with respect to $\mathbf z_n$, where $\mathbf W$ is kept fixed, gives rise to the PCA E step (16.70), and that minimizing $J$ with respect to $\mathbf W$, where $\{\mathbf z_n\}$ is kept fixed, gives rise to the PCA M step (16.71).

### 中文转述

> [!question] 中文转述
> **原题16.23。** 用 $Wz_n+\mu$ 近似 $D$ 维样本，其中 $W$ 为满列秩 $D\times M$ 矩阵。对于平方重构误差(16.90)，先对 $\mu$ 最小化，证明可把观测与潜坐标都中心化；再固定 $W$ 对潜坐标最小化得到PCA E步(16.70)，固定潜坐标对 $W$ 最小化得到M步(16.71)。

## 提示

> [!hint]- 提示 1
> 对均值求导先得到 $\mu=\bar x-W\bar z$。

> [!hint]- 提示 2
> 对两个矩阵块分别使用正规方程，并留意数据矩阵在正文中按行储存样本。

## 解答

> [!success]- 解答
> **独立推导。** 对固定 $W,z_n$，$\nabla_\mu J=-2\sum_n(x_n-\mu-Wz_n)$，故唯一最优均值为 $\mu=\bar x-W\bar z$。代入得
> $$J=\sum_n\|(x_n-\bar x)-W(z_n-\bar z)\|^2.$$
> 记 $y_n=x_n-\bar x$、$h_n=z_n-\bar z$，以后使用中心化坐标。固定满列秩 $W$，每个平方误差的正规方程为 $W^TWh_n=W^Ty_n$，因此
> $$h_n=(W^TW)^{-1}W^Ty_n.$$
> 其样本均值为零，符合中心化约束。若 $Y$ 为第 $n$ 行是 $y_n^T$ 的 $N\times D$ 矩阵、$\Omega$ 为第 $n$ 列是 $h_n$ 的 $M\times N$ 矩阵，则
> $$\Omega=(W_{\mathrm{old}}^TW_{\mathrm{old}})^{-1}W_{\mathrm{old}}^TY^T,$$
> 即(16.70)。固定 $\Omega$，$J=\|Y^T-W\Omega\|_F^2$，求导得 $W\Omega\Omega^T=Y^T\Omega^T$；若 $\Omega\Omega^T$ 可逆，
> $$W_{\mathrm{new}}=Y^T\Omega^T(\Omega\Omega^T)^{-1},$$
> 即(16.71)。两步分别精确最小化一个变量块，所以每步误差不增加。
>
> 若某矩阵秩亏，最小二乘解仍存在，可用Moore–Penrose伪逆给一个解，零空间方向可产生多解；不能无条件套普通逆。该交替算法与零噪声PPCA极限一致，但其目标一般非联合凸，单步误差下降本身不证明任意初始化都到达唯一全局PCA解。

## 相关概念

- [[04 - 统计学习/概念/无监督学习|无监督学习]]
- [[05 - 概率模型与推断/概念/潜变量|潜变量]]
- [[03 - 线性代数与优化/概念/正规方程|正规方程]]

## 备注

- 原题及星数：[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=544|印刷530、531／PDF544、545]]；题页及引用正文已实际查看原PDF图像，精确定位见 `source_refs`。
- `source_status: verified` 仅指本题及所列实际核对范围；解答独立推导，不构成用户已完成学习，状态保持 `not-started`。
