---
title: "习题 ST362：ANOVA任意线性组合的正态均值方差"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第11章习题11.8，印刷页457／PDF物理页488"
source_id: "DS011"
source_chapter: 11
source_exercise: "11.8"
source_stars: 0
source_refs: ["DS011 Exercise 11.8，印刷457／PDF物理488", "DS011 单因素ANOVA模型及分组均值，印刷422／PDF物理453"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST362：ANOVA任意线性组合的正态均值方差

## 题目

### 英文原题

> [!question] 英文原题
> **11.8** Show that under the oneway ANOVA assumptions, for any set of constants $\mathbf a=(a_1,\ldots,a_k)$, the quantity $\sum a_i\bar Y_{i\cdot}$ is normally distributed with mean $\sum a_i\theta_i$ and variance $\sigma^2\sum a_i^2/n_i$. (See Corollary 4.6.10.)

### 中文转述

> [!question] 中文转述
> **原题11.8。** 证明：在单因素ANOVA假设下，对任意常数组$\boldsymbol a=(a_1,\ldots,a_k)$，量$\sum a_i\bar Y_{i\cdot}$服从均值为$\sum a_i\theta_i$、方差为$\sigma^2\sum a_i^2/n_i$的正态分布. （见4.6.10.）

## 提示

> [!hint]- 提示
> 独立正态线性组合的mgf逐项相乘。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 组均值相互独立，且$\bar Y_i\sim n(\theta_i,\sigma^2/n_i)$。对$T=\sum_i a_i\bar Y_i$，mgf乘积为
> $$
> E e^{tT}=\prod_i\exp\left(t a_i\theta_i+\frac{t^2a_i^2\sigma^2}{2n_i}\right)
> =\exp\left(t\sum_i a_i\theta_i+\frac{t^2\sigma^2}{2}\sum_i a_i^2/n_i\right).
> $$
> 这正是均值$\sum_i a_i\theta_i$、方差$\sigma^2\sum_i a_i^2/n_i$的正态mgf。若所有$a_i=0$，统计量恒为0，应理解为退化正态；其余情形方差为正。结论适用于任意固定线性组合，不要求系数和为零；对比（contrast）只是其中系数和为零的子类。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=488|印刷第457页／PDF物理第488页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 英文原文、中文转述与本库独立解答分别保留；实际核对正文位置列于`source_refs`。题内文献引用不表示已查阅其原文。`source_status: verified`只指本题及所列位置的核对范围，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
