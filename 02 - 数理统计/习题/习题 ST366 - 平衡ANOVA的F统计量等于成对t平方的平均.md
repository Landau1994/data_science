---
title: "习题 ST366：平衡ANOVA的F统计量等于成对t平方的平均"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第11章习题11.12，印刷页457／PDF物理页488"
source_id: "DS011"
source_chapter: 11
source_exercise: "11.12"
source_stars: 0
source_refs: ["DS011 Exercise 11.12，印刷457／PDF物理488"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST366：平衡ANOVA的F统计量等于成对t平方的平均

## 题目

### 英文原题

> [!question] 英文原题
> **11.12** Suppose that we have a oneway ANOVA with equal numbers of observations on each treatment, that is, $n_i=n$, $i=1,\ldots,k$. In this case the $F$ test can be considered an average $t$ test.
>
> (a) Show that a $t$ test of $H_0:\theta_i=\theta_{i'}$ versus $H_1:\theta_i\ne\theta_{i'}$ can be based on the statistic
> $$
> t_{ii'}^2=\frac{(\bar Y_{i\cdot}-\bar Y_{i'\cdot})^2}{S_p^2(2/n)}.
> $$
> (b) Show that
> $$
> \frac1{k(k-1)}\sum_{i,i'}t_{ii'}^2=F,
> $$
> where $F$ is the usual ANOVA $F$ statistic. (Hint: See Exercise 5.8a.) (Communicated by George McCabe, who learned it from John Tukey.)

### 中文转述

> [!question] 中文转述
> **原题11.12。** 假设单因素ANOVA中每个处理的观测数相同，即$n_i=n$，$i=1,\ldots,k$. 此时$F$检验可看成平均的$t$检验.
>
> (a)  证明，$H_0:\theta_i=\theta_{i'}$对$H_1:\theta_i\ne\theta_{i'}$的$t$检验可以基于统计量
>
> $$
> t_{ii'}^2=\frac{(\bar Y_{i\cdot}-\bar Y_{i'\cdot})^2}{S_p^2(2/n)}.
> $$
>
> (b)  证明
>
> $$
> \frac1{k(k-1)}\sum_{i,i'}t_{ii'}^2=F,
> $$
>
> 其中$F$为通常的ANOVA $F$统计量. （提示：见习题5.8(a).）（由George McCabe提供，他从John Tukey处获知此结果.）

## 提示

> [!hint]- 提示
> 先明确求和包含两个方向的成对差，再展开平方差总和。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 取$k\ge2,n\ge2$，$S_p^2$是全部组内残差除以$k(n-1)$。
>
> **(a)** 两个独立组均值之差在相等原假设下为$n(0,2\sigma^2/n)$，独立于$S_p^2$，故带符号比值$T_{ii'}=(\bar Y_i-\bar Y_{i'})/[S_p\sqrt{2/n}]$服从$t_{k(n-1)}$。双侧检验只取决于它的平方，得到所给统计量（其零假设分布为$F_{1,k(n-1)}$）。
>
> **(b)** 对任意数$z_i$，有有序对恒等式
> $$
> \sum_{i,i'}(z_i-z_{i'})^2=2k\sum_i(z_i-\bar z)^2.
> $$
> 证明是展开左端为$2k\sum_i z_i^2-2(\sum_i z_i)^2$。因此
> $$
> \frac{\sum_{i,i'}t_{ii'}^2}{k(k-1)}
> =\frac{n\sum_i(\bar Y_i-\bar{\bar Y})^2/(k-1)}{S_p^2}=F.
> $$
> 原求和是**有序对**，对角项为0；若改为无序$i<i'$，分母应为$k(k-1)/2$。这是每份数据都成立的代数恒等式，不要求原假设为真；但各成对$t$统计量共用分母且互相依赖，不是独立检验的平均。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=488|印刷第457页／PDF物理第488页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 英文原文、中文转述与本库独立解答分别保留；实际核对正文位置列于`source_refs`。题内文献引用不表示已查阅其原文。`source_status: verified`只指本题及所列位置的核对范围，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
