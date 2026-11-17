---
title: "习题 ST367：单因素ANOVA似然比检验与F检验的等价"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第11章习题11.13，印刷页458／PDF物理页489"
source_id: "DS011"
source_chapter: 11
source_exercise: "11.13"
source_stars: 0
source_refs: ["DS011 Exercise 11.13，印刷458／PDF物理489", "DS011 ANOVA F检验式(11.2.14)，印刷431／PDF物理462", "DS011 平方和分解定理11.2.11，印刷433／PDF物理464"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST367：单因素ANOVA似然比检验与F检验的等价

## 题目

### 英文原题

> [!question] 英文原题
> **11.13** Under the oneway ANOVA assumptions, show that the likelihood ratio test of $H_0:\theta_1=\theta_2=\cdots=\theta_k$ is given by the $F$ test of (11.2.14).

### 中文转述

> [!question] 中文转述
> **原题11.13。** 在单因素ANOVA假设下，证明$H_0:\theta_1=\theta_2=\cdots=\theta_k$的似然比检验就是式11.2.14的$F$检验.

## 提示

> [!hint]- 提示
> 分别在全模型和共同均值模型下最小化残差平方和。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 设独立$Y_{ij}\sim n(\theta_i,\sigma^2)$、$k\ge2,N>k$。令$W=\sum_{ij}(y_{ij}-\bar y_i)^2$、$B=\sum_i n_i(\bar y_i-\bar{\bar y})^2$，总平方和$T=W+B$。通常$W>0$几乎必然。
>
> 无约束下，各均值MLE为$\bar y_i$，方差MLE为$W/N$；原假设下共同均值MLE为加权总均值$\bar{\bar y}$，方差MLE为$T/N$。最大正态似然与残差平方和的$-N/2$次幂成正比，因此似然比为
> $$
> \Lambda=\left(\frac WT\right)^{N/2}
> =\left[1+\frac{k-1}{N-k}F\right]^{-N/2},
> \quad F=\frac{B/(k-1)}{W/(N-k)}.
> $$
> 它严格随$F$下降，故小似然比拒绝域恰为大$F$拒绝域。原假设下$B/\sigma^2\sim\chi^2_{k-1}$，$W/\sigma^2\sim\chi^2_{N-k}$且独立（组均值与残差的正交正态分解），所以$F\sim F_{k-1,N-k}$。水平$\alpha$时在$F>F_{k-1,N-k,\alpha}$拒绝，就是(11.2.14)。$W=0$的特殊数据在正方差模型下有无界似然，不能把方差MLE0当内点；这不影响通常连续样本的几乎必然检验结论。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=489|印刷第458页／PDF物理第489页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 英文原文、中文转述与本库独立解答分别保留；实际核对正文位置列于`source_refs`。题内文献引用不表示已查阅其原文。`source_status: verified`只指本题及所列位置的核对范围，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
