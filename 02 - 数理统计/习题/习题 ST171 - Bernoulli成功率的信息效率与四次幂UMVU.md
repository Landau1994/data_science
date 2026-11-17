---
title: "习题 ST171：Bernoulli成功率的信息效率与四次幂UMVU"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第7章习题7.48，印刷页295／PDF物理页326"
source_id: "DS011"
source_chapter: 7
source_exercise: "7.48"
source_stars: 0
source_refs: ["DS011 Exercise 7.48，印刷295／PDF物理326", "DS011 完备充分量的最佳无偏性与条件化方法，印刷280／PDF物理311", "DS011 例7.3.24的二项条件分布做法，印刷281／PDF物理312"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST171：Bernoulli成功率的信息效率与四次幂UMVU

## 题目

### 英文原题

> [!question] 英文原题
> **7.48** Suppose that $X_i$, $i=1,\ldots,n$, are iid Bernoulli$(p)$.
>
> (a) Show that the variance of the MLE of $p$ attains the Cramér–Rao Lower Bound.
>
> (b) For $n\ge4$, show that the product $X_1X_2X_3X_4$ is an unbiased estimator of $p^4$, and use this fact to find the best unbiased estimator of $p^4$.

### 中文转述

> [!question] 中文转述
> **原题7.48。** 假设$X_i$，$i=1,\ldots,n$，独立同分布于$\operatorname{Bernoulli}(p)$.
>
> (a)  说明$p$的MLE的方差达到Cramér--Rao下界.
>
> (b)  对$n\ge4$，说明乘积$X_1X_2X_3X_4$是$p^4$的无偏估计量，并利用这一事实求$p^4$的最佳无偏估计量.

## 提示

> [!hint]- 提示
> 先用四个独立指示变量造一个简单无偏估计，再给定总成功数。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** **(a)** 写$S=\sum_iX_i$。二项似然最大点为$\widehat p=S/n$，端点也包含在参数空间$[0,1]$。对$0<p<1$，得分$(S-np)/[p(1-p)]$给$I_n=n/[p(1-p)]$；而$E\widehat p=p$、$\operatorname{Var}\widehat p=p(1-p)/n$，等于下界。端点分布退化，方差为0，最优性直接成立。
>
> **(b)** 独立性给$E(X_1X_2X_3X_4)=p^4$。条件于$S=s$，所有含$s$个1的二元序列等可能。前四位全为1的条件概率为$\binom{n-4}{s-4}/\binom ns=\binom s4/\binom n4$（$s<4$时为0），所以Rao–Blackwell化得到
> $$
> T(S)=\frac{S(S-1)(S-2)(S-3)}{n(n-1)(n-2)(n-3)}=\frac{\binom S4}{\binom n4}.
> $$
> $S$充分，且完备性可直接验证：若$\sum_{s=0}^nh(s)\binom ns p^s(1-p)^{n-s}=0$对$0<p<1$成立，除以$(1-p)^n$，令$t=p/(1-p)$，得到对所有$t>0$为零的多项式，故每个系数$h(s)\binom ns=0$。因此$T(S)$为唯一最佳无偏估计，包括闭区间端点。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=326|印刷第295页／PDF物理第326页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 英文原文、中文转述与本库独立解答分别保留；实际核对正文位置列于`source_refs`。题内文献引用不表示已查阅其原文。`source_status: verified`只指本题及所列位置的核对范围，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
