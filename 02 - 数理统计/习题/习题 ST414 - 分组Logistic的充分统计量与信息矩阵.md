---
title: "习题 ST414：分组Logistic的充分统计量与信息矩阵"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第12章习题12.19，印刷页491／PDF物理页522"
source_id: "DS011"
source_chapter: 12
source_exercise: "12.19"
source_stars: 0
source_refs: ["DS011 Exercise 12.19，印刷页491／PDF物理页522", "DS011 所引正文，印刷482／PDF物理513"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST414：分组Logistic的充分统计量与信息矩阵

## 题目

### 英文原题

> [!question] 英文原题
> **12.19** For the logistic regression model:
> (a) Show that $\left(\sum_{j=1}^JY_j^*,\sum_{j=1}^JY_j^*x_j\right)$ is a sufficient statistic for $(\alpha,\beta)$.
> (b) Verify the formula for the logistic regression information matrix in (12.3.10).

### 中文转述

> [!question] 中文转述
> **原题12.19。**
> 对于逻辑回归模型：
>
> (a)  证明$\bigl(\sum_{j=1}^JY_j^*,\sum_{j=1}^JY_j^*x_j\bigr)$是$(\alpha,\beta)$的充分统计量.
>
> (b)  验证式12.3.10的逻辑回归信息矩阵公式.

## 提示

> [!hint]- 提示
> 把联合pmf写成二参数指数族形式，再对得分求导。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 原文分组模型为独立$Y_j^*\sim\operatorname{Bin}(n_j,\pi_j)$，$\pi_j=\Lambda(\alpha+\beta x_j)$，$x_j,n_j$已知。
> (a) 联合pmf等于$\prod_j\binom{n_j}{y_j}\exp\{\alpha\sum_jy_j+\beta\sum_jx_jy_j-\sum_jn_j\log(1+e^{\alpha+\beta x_j})\}$。样本依赖参数的部分只通过两个题列和，支持$0\le y_j\le n_j$也不依赖参数，因此因子分解定理给充分性。
> (b) 得分为$\sum_j(y_j-n_j\pi_j)(1,x_j)^T$，且$\partial\pi_j/\partial\alpha=\pi_j(1-\pi_j)$、$\partial\pi_j/\partial\beta=x_j\pi_j(1-\pi_j)$，所以负Hessian为
> $$I(\alpha,\beta)=\begin{pmatrix}\sum_jn_j\pi_j(1-\pi_j)&\sum_jn_jx_j\pi_j(1-\pi_j)\\\sum_jn_jx_j\pi_j(1-\pi_j)&\sum_jn_jx_j^2\pi_j(1-\pi_j)\end{pmatrix}.$$
> 它不含随机$Y_j^*$，所以观察信息与期望信息相同。内部参数下权重正，若至少两个不同$x_j$各有正$n_j$，矩阵正定；设计秩不足时不能取普通逆矩阵估计两个系数的方差。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计（parameter estimation）]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]
- [[01 - 概率论/概念/随机变量|随机变量]]
- [[02 - 数理统计/概念/充分统计量|充分统计量]]

## 备注

- 完整原题已逐页对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=522|印刷491／PDF物理522]]；原题无星号。教材信息与归档进度见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 实际引用输入核对页：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=513|印刷482／PDF物理513]]；所需模型、公式、数据在解答重述。
- 来源已核对与解答写成不表示个人学习已完成；学习状态保留`not-started`。未实测Obsidian界面渲染。
