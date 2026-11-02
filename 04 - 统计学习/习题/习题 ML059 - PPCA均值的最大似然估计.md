---
title: 习题 ML059：PPCA均值的最大似然估计
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
source_exercise: '16.9'
source_stars: 1
source_refs:
- DS003 Exercise 16.9，印刷529/PDF543
- DS003 对数似然(16.44)，印刷509/PDF523
source_status: verified
solution_status: independently-derived
created: '2026-11-02'
---

# 习题 ML059：PPCA均值的最大似然估计

## 题目

### 英文原题

> [!question] 英文原题
> **Exercise 16.9（★）** Verify that maximizing the log likelihood (16.44) for the probabilistic PCA model with respect to the parameter $\boldsymbol\mu$ gives the result $\boldsymbol\mu_{\mathrm{ML}}=\overline{\mathbf x}$ where $\overline{\mathbf x}$ is the mean of the data vectors.

### 中文转述

> [!question] 中文转述
> **原题16.9。** 对PPCA对数似然(16.44)中的均值参数 $\mu$ 最大化，验证最大似然估计为样本均值 $\bar x$。

## 提示

> [!hint]- 提示 1
> 固定 $W,\sigma^2$，协方差 $C=WW^T+\sigma^2I$ 不含 $\mu$。

## 解答

> [!success]- 解答
> **独立推导。** 假设 $N\geq1$、$\sigma^2>0$，固定协方差 $C=WW^T+\sigma^2I\succ0$。对数似然关于 $\mu$ 为
> $$\ell(\mu)=\text{常数}-\frac12\sum_n(x_n-\mu)^TC^{-1}(x_n-\mu).$$
> 利用 $C^{-1}$ 对称，$\nabla_\mu\ell=\sum_n C^{-1}(x_n-\mu)=NC^{-1}(\bar x-\mu)$。可逆性给唯一驻点 $\mu=\bar x$。
>
> 又有平方分解
> $$\sum_n(x_n-\mu)^TC^{-1}(x_n-\mu)=\sum_n(x_n-\bar x)^TC^{-1}(x_n-\bar x)+N(\mu-\bar x)^TC^{-1}(\mu-\bar x).$$
> 最后一项仅在 $\mu=\bar x$ 时为零，其他地方严格为正，所以该驻点是关于均值的唯一全局最大值。这不声称 $W,\sigma^2$ 的联合最大值唯一，潜空间旋转仍导致参数非可辨识。

## 相关概念

- [[04 - 统计学习/概念/无监督学习|无监督学习]]
- [[05 - 概率模型与推断/概念/潜变量|潜变量]]
- [[01 - 概率论/概念/概率模型|概率模型]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题及星数：[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=543|印刷529／PDF543]]；题页及引用正文已实际查看原PDF图像，精确定位见 `source_refs`。
- `source_status: verified` 仅指本题及所列实际核对范围；解答独立推导，不构成用户已完成学习，状态保持 `not-started`。
