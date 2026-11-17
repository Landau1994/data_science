---
title: "习题 ST374：原假设下组间均方无偏与ANOVA独立方差比"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第11章习题11.20，印刷页459／PDF物理页490"
source_id: "DS011"
source_chapter: 11
source_exercise: "11.20"
source_stars: 0
source_refs: ["DS011 Exercise 11.20，印刷459／PDF物理490", "DS011 定理11.2.8的卡方中心化，印刷430／PDF物理461", "DS011 ANOVA F检验式(11.2.14)，印刷431／PDF物理462", "DS011 例5.3.5的独立方差比，印刷182–183／PDF物理213,214"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST374：原假设下组间均方无偏与ANOVA独立方差比

## 题目

### 英文原题

> [!question] 英文原题
> **11.20** Show that if the oneway ANOVA null hypothesis is true, then
>
> (a) $\sum n_i(\bar Y_{i\cdot}-\bar{\bar Y})^2/(k-1)$ gives an unbiased estimate of $\sigma^2$.
>
> (b) Show how to use the method of Example 5.3.5 to derive the ANOVA $F$ test.

### 中文转述

> [!question] 中文转述
> **原题11.20。** 证明：若单因素ANOVA原假设成立，则
>
> (a)  $\sum n_i(\bar Y_{i\cdot}-\bar{\bar Y})^2/(k-1)$是$\sigma^2$的无偏估计量.
>
> (b)  说明如何用例5.3.5的方法推导ANOVA $F$检验.

## 提示

> [!hint]- 提示
> 组间与组内平方和给两个独立卡方量，原假设下它们估计同一方差。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 假定独立同方差正态ANOVA、$k\ge2,N>k$，且全部处理均值相等。
>
> **(a)** 令$B=\sum_i n_i(\bar Y_i-\bar{\bar Y})^2$。中心化的加权均值残差卡方分解给$B/\sigma^2\sim\chi_{k-1}^2$，故$E[B/(k-1)]=\sigma^2$。也可不依赖分布直接算：$\operatorname{Var}(\bar Y_i-\bar{\bar Y})=\sigma^2(1/n_i-1/N)$，所以$EB=\sum_i n_i\sigma^2(1/n_i-1/N)=(k-1)\sigma^2$。
>
> **(b)** 组内平方和$W=\sum_{ij}(Y_{ij}-\bar Y_i)^2$满足$W/\sigma^2\sim\chi_{N-k}^2$，且与组均值函数$B$独立。因此两个无偏方差估计的比值
> $$
> F=\frac{B/(k-1)}{W/(N-k)}
> =\frac{\chi_{k-1}^2/(k-1)}{\chi_{N-k}^2/(N-k)}\sim F_{k-1,N-k}.
> $$
> 均值不等会增加组间平方和而不改变组内误差模型，故在$F>F_{k-1,N-k,\alpha}$拒绝全等原假设，得到水平$\alpha$的ANOVA检验。这里用的正是独立正态样本方差比产生F分布的做法。独立性与两个自由度均不能省去。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=490|印刷第459页／PDF物理第490页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 英文原文、中文转述与本库独立解答分别保留；实际核对正文位置列于`source_refs`。题内文献引用不表示已查阅其原文。`source_status: verified`只指本题及所列位置的核对范围，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
