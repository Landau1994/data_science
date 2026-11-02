---
title: 习题 ML061：PPCA零噪声极限的正交投影与潜坐标
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
source_exercise: '16.11'
source_stars: 2
source_refs:
- DS003 Exercise 16.11，印刷529/PDF543
- DS003 后验(16.43)，印刷509/PDF523；最大似然载荷(16.46)，印刷510/PDF524；投影及极限(16.49)–(16.51)，印刷511–512/PDF525–526
source_status: verified
solution_status: independently-derived
created: '2026-11-02'
---

# 习题 ML061：PPCA零噪声极限的正交投影与潜坐标

## 题目

### 英文原题

> [!question] 英文原题
> **Exercise 16.11（★★）** Show that in the limit $\sigma^2\to0$, the posterior mean for the probabilistic PCA model becomes an orthogonal projection onto the principal subspace, as in conventional PCA.

### 中文转述

> [!question] 中文转述
> **原题16.11。** 证明PPCA在噪声方差趋零时，后验均值对应传统PCA的主子空间正交投影。

## 提示

> [!hint]- 提示 1
> 先求潜坐标 $(W^TW)^{-1}W^T(x-\mu)$，再乘 $W$ 并加回均值，得到数据空间投影。

## 解答

> [!success]- 解答
> **独立推导与维度说明。** 设 $W\in\mathbb R^{D\times M}$ 满列秩，暂时固定 $W$。后验均值为 $m_\sigma=(W^TW+\sigma^2I)^{-1}W^T(x-\mu)$。连续性给
> $$m_\sigma\longrightarrow m_0=(W^TW)^{-1}W^T(x-\mu).$$
> $m_0$ 是 $M$ 维潜坐标；它本身不是作用于 $D$ 维空间的正交投影矩阵。对应的重构为
> $$\widehat x_0=\mu+Wm_0=\mu+P_W(x-\mu),\qquad P_W=W(W^TW)^{-1}W^T.$$
> 直接计算 $P_W^T=P_W,P_W^2=P_W$，且 $W^T[(x-\mu)-P_W(x-\mu)]=0$，故它是到仿射子空间 $\mu+\operatorname{col}W$ 的正交投影。
>
> 在最大似然PPCA解，$\operatorname{col}W$ 是前 $M$ 个主成分张成的空间，且 $\mu=\bar x$，因此得到传统PCA重构。若用 $W=U_M(\Lambda_M-\sigma^2I)^{1/2}R$ 随噪声变化，并保留正特征值，投影矩阵同样趋于 $U_MU_M^T$；潜坐标可能含尺度和旋转，未必等于标准PCA坐标 $U_M^T(x-\bar x)$。
>
> 后验协方差 $\sigma^2(W^TW+\sigma^2I)^{-1}\to0$。若 $W$ 秩亏，须在有效子空间用伪逆，未被观测约束的潜方向后验方差不趋零，不能无条件使用满秩结论。

## 相关概念

- [[04 - 统计学习/概念/无监督学习|无监督学习]]
- [[05 - 概率模型与推断/概念/潜变量|潜变量]]

## 备注

- 原题及星数：[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=543|印刷529／PDF543]]；题页及引用正文已实际查看原PDF图像，精确定位见 `source_refs`。
- 区分潜空间坐标和数据空间正交投影，避免把不同维向量直接认作同一个投影。
- `source_status: verified` 仅指本题及所列实际核对范围；解答独立推导，不构成用户已完成学习，状态保持 `not-started`。
