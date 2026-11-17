---
title: "习题 ST365：ANOVA线性对比的加权内积协方差"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第11章习题11.11，印刷页457／PDF物理页488"
source_id: "DS011"
source_chapter: 11
source_exercise: "11.11"
source_stars: 0
source_refs: ["DS011 Exercise 11.11，印刷457／PDF物理488"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST365：ANOVA线性对比的加权内积协方差

## 题目

### 英文原题

> [!question] 英文原题
> **11.11** For any sets of constants $\mathbf a=(a_1,\ldots,a_k)$ and $\mathbf b=(b_1,\ldots,b_k)$, show that under the oneway ANOVA assumptions
> $$
> \operatorname{Cov}\left(\sum a_i\bar Y_{i\cdot},\sum b_i\bar Y_{i\cdot}\right)=\sigma^2\sum\frac{a_ib_i}{n_i}.
> $$
> Hence, in the oneway ANOVA, contrasts are uncorrelated (orthogonal) if $\sum a_ib_i/n_i=0$.

### 中文转述

> [!question] 中文转述
> **原题11.11。** 对任意常数组$\boldsymbol a=(a_1,\ldots,a_k)$和$\boldsymbol b=(b_1,\ldots,b_k)$，证明在单因素ANOVA假设下
>
> $$
> \operatorname{Cov}\left(\sum a_i\bar Y_{i\cdot},\sum b_i\bar Y_{i\cdot}\right)
> =\sigma^2\sum\frac{a_ib_i}{n_i}.
> $$
>
> 因此，单因素ANOVA中，若$\sum a_ib_i/n_i=0$，则对比互不相关（正交）.

## 提示

> [!hint]- 提示
> 把双重协方差和中的异组项全部消去。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 独立同方差正态ANOVA下，各组均值独立且$\operatorname{Var}\bar Y_i=\sigma^2/n_i$。由协方差双线性，
> $$
> \operatorname{Cov}\left(\sum_i a_i\bar Y_i,\sum_j b_j\bar Y_j\right)
> =\sum_{i,j}a_i b_j\operatorname{Cov}(\bar Y_i,\bar Y_j)
> =\sum_i a_i b_i\frac{\sigma^2}{n_i}.
> $$
> 故$\sum_i a_i b_i/n_i=0$时不相关；$\sigma^2>0$下这也是不相关的充要条件。若两线性组合联合正态，零协方差还推出独立；即便不要求正态，只要组均值不相关且有这些方差，协方差等式仍成立，但独立结论不能随意保留。样本量不等时应使用权$1/n_i$的内积，不能只检查普通向量内积。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=488|印刷第457页／PDF物理第488页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 英文原文、中文转述与本库独立解答分别保留；实际核对正文位置列于`source_refs`。题内文献引用不表示已查阅其原文。`source_status: verified`只指本题及所列位置的核对范围，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
