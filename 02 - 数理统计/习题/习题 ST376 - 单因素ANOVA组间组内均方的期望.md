---
title: "习题 ST376：单因素ANOVA组间组内均方的期望"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第11章习题11.22，印刷页459／PDF物理页490"
source_id: "DS011"
source_chapter: 11
source_exercise: "11.22"
source_stars: 0
source_refs: ["DS011 Exercise 11.22，印刷459／PDF物理490", "DS011 ANOVA平方和分解与均方定义，印刷433／PDF物理464"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST376：单因素ANOVA组间组内均方的期望

## 题目

### 英文原题

> [!question] 英文原题
> **11.22** Calculate the expected values of MSB and MSW given in the oneway ANOVA table. (Such expectations are formally known as expected mean squares and can be used to help identify $F$ tests in complicated ANOVAs. An algorithm exists for calculating expected mean squares. See, for example, Kirk (1982) for details about the algorithm.)

### 中文转述

> [!question] 中文转述
> **原题11.22。** 计算单因素ANOVA表中MSB与MSW的期望. （这些期望正式称为期望均方，expected mean squares，可用于帮助确定复杂ANOVA中的$F$检验. 有算法可计算期望均方，算法细节例如可见Kirk，1982.）

## 提示

> [!hint]- 提示
> 将每个组均值分解为真实均值与零均值抽样误差。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 设$Y_{ij}=\theta_i+\varepsilon_{ij}$独立、误差均值0方差$\sigma^2$，$k\ge2,N>k$。令$\theta_w=\sum_i n_i\theta_i/N$、$\bar{\bar Y}=\sum_i n_i\bar Y_i/N$。
>
> 组内平方和$W=\sum_{ij}(Y_{ij}-\bar Y_i)^2$在第$i$组期望为$(n_i-1)\sigma^2$，故$E\operatorname{MSW}=EW/(N-k)=\sigma^2$。
>
> 写$\bar Y_i=\theta_i+U_i$、$\bar{\bar Y}=\theta_w+U_w$，则组间平方和$B$展开后，交叉项期望为0，
> $$
> EB=\sum_i n_i(\theta_i-\theta_w)^2+\sum_i n_iE(U_i-U_w)^2.
> $$
> 其中$\operatorname{Var}(U_i-U_w)=\sigma^2(1/n_i-1/N)$，所以误差部分为$(k-1)\sigma^2$。于是
> $$
> E\operatorname{MSB}=\sigma^2+\frac{\sum_i n_i(\theta_i-\theta_w)^2}{k-1},\qquad
> E\operatorname{MSW}=\sigma^2.
> $$
> 均值全等时两者都无偏估计$\sigma^2$；不等时只有组间均方增加非负的处理差异项。这些期望只需独立/不相关同方差及有限二阶矩，精确F分布才进一步需要正态性。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=490|印刷第459页／PDF物理第490页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 英文原文、中文转述与本库独立解答分别保留；实际核对正文位置列于`source_refs`。题内文献引用不表示已查阅其原文。`source_status: verified`只指本题及所列位置的核对范围，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
