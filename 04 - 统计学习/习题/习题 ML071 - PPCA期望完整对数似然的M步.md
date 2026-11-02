---
title: 习题 ML071：PPCA期望完整对数似然的M步
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
source_exercise: '16.21'
source_stars: 2
source_refs:
- DS003 Exercise 16.21，印刷530/PDF544
- DS003 完整数据期望与E步(16.64)–(16.67)，印刷518/PDF532；M步(16.68)–(16.69)，印刷519/PDF533
source_status: verified
solution_status: independently-derived
created: '2026-11-02'
---

# 习题 ML071：PPCA期望完整对数似然的M步

## 题目

### 英文原题

> [!question] 英文原题
> **Exercise 16.21（★★）** Derive the M-step equations (16.68) and (16.69) for the probabilistic PCA model by maximizing the expected complete-data log likelihood function given by (16.65).

### 中文转述

> [!question] 中文转述
> **原题16.21。** 最大化期望完整数据对数似然(16.65)，推导PPCA的M步载荷更新(16.68)和噪声方差更新(16.69)。

## 提示

> [!hint]- 提示 1
> 在M步固定旧后验矩 $m_n=\mathrm E[z_n]$、$R_n=\mathrm E[z_nz_n^T]$，对 $W$ 和 $\sigma^2$ 分别求导。

## 解答

> [!success]- 解答
> **独立推导。** 先取 $\mu=\bar x$，$y_n=x_n-\bar x$；E步使用旧参数计算 $m_n,R_n$，M步中二者均视为常量。除去参数无关项，(16.65)为
> $$Q(W,v)=-\frac{ND}2\ln v-\frac1{2v}\sum_n[\|y_n\|^2-2m_n^TW^Ty_n+\operatorname{Tr}(R_nW^TW)],\quad v=\sigma^2.$$
> 令 $A=\sum_ny_nm_n^T$、$B=\sum_nR_n$。由于 $R_n$ 对称，$\nabla_WQ=v^{-1}(A-WB)$。当 $B\succ0$，得到唯一载荷M步
> $$W_{\mathrm{new}}=AB^{-1}=\left[\sum_n(x_n-\bar x)\mathrm E[z_n]^T\right]\left[\sum_n\mathrm E[z_nz_n^T]\right]^{-1},$$
> 即(16.68)。正噪声下每个后验协方差正定，所以 $N\geq1$ 时 $B\succ0$。
>
> 设残差平方和期望为 $R(W)$，则 $\partial_vQ=-ND/(2v)+R(W)/(2v^2)$，故
> $$\sigma_{\mathrm{new}}^2=\frac1{ND}\sum_n[\|x_n-\bar x\|^2-2m_n^TW_{\mathrm{new}}^T(x_n-\bar x)+\operatorname{Tr}(R_nW_{\mathrm{new}}^TW_{\mathrm{new}})],$$
> 即(16.69)。$R(W)$ 是非负平方的期望；若严格为正，该标量驻点为最大值，因为导数在其前为正、其后为负。若残差恰为零，最优仅在 $v\downarrow0$ 的边界，不可在严格正噪声空间宣称正的内点解。两式共同完成期望重构误差的最小化及噪声估计。

## 相关概念

- [[04 - 统计学习/概念/无监督学习|无监督学习]]
- [[05 - 概率模型与推断/概念/潜变量|潜变量]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[03 - 线性代数与优化/概念/正规方程|正规方程]]

## 备注

- 原题及星数：[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=544|印刷530／PDF544]]；题页及引用正文已实际查看原PDF图像，精确定位见 `source_refs`。
- `source_status: verified` 仅指本题及所列实际核对范围；解答独立推导，不构成用户已完成学习，状态保持 `not-started`。
