---
title: 习题 DL301：Hutchinson迹估计的任意样本量无偏性
topic: deep-learning
topic_label: 深度学习
difficulty: beginner
status: not-started
tags:
- exercise
- deep-learning
source: '[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Deep Learning: Foundations and Concepts（DS003）]]'
source_id: DS003
source_chapter: 18
source_exercise: '18.11'
source_stars: 1
source_refs:
- DS003 Exercise 18.11，印刷561/PDF573
- DS003 Hutchinson公式(18.29)–(18.30)及噪声矩条件，印刷558/PDF570
source_status: verified
solution_status: independently-derived
created: '2026-11-02'
---

# 习题 DL301：Hutchinson迹估计的任意样本量无偏性

## 题目

### 英文原题

> [!question] 英文原题
> **Exercise 18.11（★）** Show that the expectation of the right-hand side in the Hutchinson trace estimator (18.30) is equal to $\operatorname{Tr}(\mathbf A)$ for any value of $M$. This shows that the estimator is unbiased.

### 中文转述

> [!question] 中文转述
> **原题18.11。** 证明Hutchinson迹估计器(18.30)对于任意正整数样本数 $M$，其期望都等于 $\operatorname{Tr}(A)$，因此无偏。

## 提示

> [!hint]- 提示 1
> 逐项展开 $\epsilon^TA\epsilon=\sum_{ij}A_{ij}\epsilon_i\epsilon_j$；零均值单位协方差意味着 $\mathrm E\epsilon_i\epsilon_j=\delta_{ij}$。

## 解答

> [!success]- 解答
> **独立推导。** 正文假设 $\epsilon_m$ 零均值、单位协方差，故 $\mathrm E[\epsilon_m\epsilon_m^T]=I$。对固定实方阵 $A$，有限二阶矩足以保证各项可积，且
> $$\mathrm E[\epsilon_m^TA\epsilon_m]=\sum_{i,j}A_{ij}\mathrm E[\epsilon_{mi}\epsilon_{mj}]=\sum_iA_{ii}=\operatorname{Tr}(A).$$
> 因此对任意 $M\geq1$，
> $$\mathrm E\left[\frac1M\sum_{m=1}^M\epsilon_m^TA\epsilon_m\right]=\frac1M\sum_m\operatorname{Tr}(A)=\operatorname{Tr}(A).$$
> 不要求 $A$ 对称，因为反对称部分的二次型和迹都为零；样本间独立性也不是无偏性所必需，但会影响方差。独立且四阶矩有限时，平均的方差为单样本方差除以 $M$。
>
> 若 $A$ 是由当前状态／网络决定的随机矩阵，噪声需满足条件矩 $\mathrm E[\epsilon\epsilon^T|A]=I$（例如独立于 $A$），才有条件无偏；直接把与 $A$ 强相关的噪声代入可能失效。$M=1$ 已无偏，但不表示单次估计等于真实迹。

## 相关概念

- [[06 - 深度学习/概念/归一化流|归一化流]]
- [[03 - 线性代数与优化/概念/链式法则|链式法则]]
- [[01 - 概率论/概念/期望|期望]]
- [[06 - 深度学习/概念/自动微分|自动微分]]

## 备注

- 原题及星数：[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=573|印刷561／PDF573]]；题页及引用正文已实际查看原PDF图像，精确定位见 `source_refs`。
- `source_status: verified` 仅指本题及所列实际核对范围；解答独立推导，不构成用户已完成学习，状态保持 `not-started`。
