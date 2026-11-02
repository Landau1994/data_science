---
title: 习题 ML062：PPCA后验均值的谱收缩
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
source_exercise: '16.12'
source_stars: 2
source_refs:
- DS003 Exercise 16.12，印刷529/PDF543
- DS003 后验与M定义(16.42)–(16.43)，印刷509/PDF523；收缩讨论与投影式(16.49)–(16.51)，印刷511–512/PDF525–526
source_status: verified
solution_status: independently-derived
created: '2026-11-02'
---

# 习题 ML062：PPCA后验均值的谱收缩

## 题目

### 英文原题

> [!question] 英文原题
> **Exercise 16.12（★★）** For $\sigma^2>0$ show that the posterior mean in the probabilistic PCA model is shifted towards the origin relative to the orthogonal projection.

### 中文转述

> [!question] 中文转述
> **原题16.12。** 当噪声方差严格为正时，证明PPCA后验均值相对于无噪声正交投影向原点收缩。

## 提示

> [!hint]- 提示 1
> 对 $W$ 作奇异值分解，逐个潜方向比较 $s/(s^2+\sigma^2)$ 与 $1/s$。

## 解答

> [!success]- 解答
> **独立推导。** 设满列秩 $W=U\operatorname{diag}(s_i)V^T$，$s_i>0$，令 $y=x-\mu$。无噪声最小二乘潜坐标与后验均值为
> $$z_0=V\operatorname{diag}(s_i^{-1})U^Ty,\qquad m_\sigma=V\operatorname{diag}\left(\frac{s_i}{s_i^2+\sigma^2}\right)U^Ty.$$
> 在正交潜基 $V$ 中，后验均值各分量等于 $z_0$ 的相应分量乘 $r_i=s_i^2/(s_i^2+\sigma^2)\in(0,1)$。所以
> $$\|m_\sigma\|^2=\sum_i r_i^2(V^Tz_0)_i^2\leq\|z_0\|^2,$$
> 非零 $z_0$ 时严格小于。不同 $r_i$ 可以不同，故一般不是沿同一条径向直线等比例缩小；“向原点”应理解为各正交主方向收缩与范数减小。
>
> 数据空间中 $Wm_\sigma=U\operatorname{diag}(r_i)U^Ty$，而正交投影为 $UU^Ty$，同样逐方向收缩。加回均值后，是向 $\mu$（最大似然时 $\bar x$）收缩，而不是向未中心化数据的数值零点。零潜方向可用伪逆表述，其后验均值为零。

## 相关概念

- [[04 - 统计学习/概念/无监督学习|无监督学习]]
- [[05 - 概率模型与推断/概念/潜变量|潜变量]]
- [[04 - 统计学习/概念/正则化|正则化]]

## 备注

- 原题及星数：[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=543|印刷529／PDF543]]；题页及引用正文已实际查看原PDF图像，精确定位见 `source_refs`。
- `source_status: verified` 仅指本题及所列实际核对范围；解答独立推导，不构成用户已完成学习，状态保持 `not-started`。
