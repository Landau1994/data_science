---
title: 习题 ML064：PPCA协方差参数计数的两个极端
topic: statistical-learning
topic_label: 统计学习
difficulty: beginner
status: not-started
tags:
- exercise
- statistical-learning
source: '[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Deep Learning: Foundations and Concepts（DS003）]]'
source_id: DS003
source_chapter: 16
source_exercise: '16.14'
source_stars: 1
source_refs:
- DS003 Exercise 16.14，印刷529/PDF543
- DS003 协方差参数计数(16.52)及两极端说明，印刷512–513/PDF526–527
source_status: verified
solution_status: independently-derived
created: '2026-11-02'
---

# 习题 ML064：PPCA协方差参数计数的两个极端

## 题目

### 英文原题

> [!question] 英文原题
> **Exercise 16.14（★）** The number of independent parameters in the covariance matrix for a probabilistic PCA model with an $M$-dimensional latent space and a $D$-dimensional data space is given by (16.52). Verify that for $M=D-1$, the number of independent parameters is the same as in a general covariance Gaussian, whereas for $M=0$ it is the same as for a Gaussian with an isotropic covariance.

### 中文转述

> [!question] 中文转述
> **原题16.14。** PPCA潜维为 $M$、数据维为 $D$ 时协方差的参数计数见(16.52)。验证 $M=D-1$ 时与一般协方差高斯相同，$M=0$ 时与各向同性高斯相同。

## 提示

> [!hint]- 提示 1
> 将 $M=D-1$ 和 $M=0$ 代入 $DM+1-M(M-1)/2$。

## 解答

> [!success]- 解答
> **独立验证。** PPCA协方差 $C=WW^T+\sigma^2I$ 有 $DM$ 个载荷参数和一个噪声参数；满秩常规情形扣去潜空间正交旋转的 $M(M-1)/2$ 维自由度，得 $k=DM+1-M(M-1)/2$。
>
> 当 $M=D-1$，
> $$k=D(D-1)+1-\frac{(D-1)(D-2)}2=\frac{D(D+1)}2.$$
> 这正是实对称 $D\times D$ 协方差矩阵的独立元素数。任意正定 $C=U\operatorname{diag}(\lambda_i)U^T$，取 $\sigma^2=\lambda_D$、$W=U_{1:D-1}\operatorname{diag}(\sqrt{\lambda_i-\lambda_D})$ 也可直接构造此表示（特征值重合时 $W$ 可降秩）。
>
> 当 $M=0$，没有 $W$，$C=\sigma^2I$ 只有一个自由参数，代入计数同样得1。上述只计协方差；若包括均值，再加 $D$ 个参数。

## 相关概念

- [[04 - 统计学习/概念/无监督学习|无监督学习]]
- [[05 - 概率模型与推断/概念/潜变量|潜变量]]
- [[02 - 数理统计/概念/参数估计|参数估计]]

## 备注

- 原题及星数：[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=543|印刷529／PDF543]]；题页及引用正文已实际查看原PDF图像，精确定位见 `source_refs`。
- `source_status: verified` 仅指本题及所列实际核对范围；解答独立推导，不构成用户已完成学习，状态保持 `not-started`。
