---
title: 习题 ML058：由线性高斯条件公式得到PPCA后验
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
source_exercise: '16.8'
source_stars: 2
source_refs:
- DS003 Exercise 16.8，印刷529/PDF543
- DS003 线性高斯后验(3.100)–(3.101)，印刷84/PDF103；PPCA矩阵与后验(16.42)–(16.43)，印刷509/PDF523
source_status: verified
solution_status: independently-derived
created: '2026-11-02'
---

# 习题 ML058：由线性高斯条件公式得到PPCA后验

## 题目

### 英文原题

> [!question] 英文原题
> **Exercise 16.8（★★）** By making use of the result (3.100), show that the posterior distribution $p(\mathbf z|\mathbf x)$ for the probabilistic PCA model is given by (16.43).

### 中文转述

> [!question] 中文转述
> **原题16.8。** 将PPCA的先验与条件高斯参数代入线性高斯后验公式(3.100)，证明后验为(16.43)。

## 提示

> [!hint]- 提示 1
> 在(3.100)中取先验精度 $I$、观测精度 $\sigma^{-2}I$、线性系数 $W$、偏置 $\mu$。

## 解答

> [!success]- 解答
> **独立推导。** 原公式的潜变量对应此处 $z$，观测变量对应 $x$。代入先验均值0、先验精度 $I_M$、条件均值 $Wz+\mu$ 和条件精度 $\sigma^{-2}I_D$，后验精度为
> $$V^{-1}=I+\sigma^{-2}W^TW=\sigma^{-2}M,\qquad M=W^TW+\sigma^2I.$$
> 所以 $V=\sigma^2M^{-1}$，均值为
> $$m=V\sigma^{-2}W^T(x-\mu)=M^{-1}W^T(x-\mu).$$
> 得到 $p(z|x)=\mathcal N(z|M^{-1}W^T(x-\mu),\sigma^2M^{-1})$，即(16.43)。也可直接展开负对数联合密度中的 $z$ 项：$\tfrac12z^T(I+\sigma^{-2}W^TW)z-\sigma^{-2}z^TW^T(x-\mu)$，配方后获得相同结论。$\sigma^2>0$ 保证 $M\succ0$，即使 $W$ 秩亏也可求逆；后验协方差不依赖观测值 $x$。

## 相关概念

- [[04 - 统计学习/概念/无监督学习|无监督学习]]
- [[05 - 概率模型与推断/概念/潜变量|潜变量]]
- [[01 - 概率论/概念/概率模型|概率模型]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题及星数：[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=543|印刷529／PDF543]]；题页及引用正文已实际查看原PDF图像，精确定位见 `source_refs`。
- `source_status: verified` 仅指本题及所列实际核对范围；解答独立推导，不构成用户已完成学习，状态保持 `not-started`。
