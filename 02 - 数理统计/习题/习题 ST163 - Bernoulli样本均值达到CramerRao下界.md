---
title: "习题 ST163：Bernoulli样本均值达到CramerRao下界"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第7章习题7.40，印刷页294／PDF物理页325"
source_id: "DS011"
source_chapter: 7
source_exercise: "7.40"
source_stars: 0
source_refs: ["DS011 Exercise 7.40，印刷294／PDF物理325", "DS011 信息下界及正则性讨论，印刷274／PDF物理305"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST163：Bernoulli样本均值达到CramerRao下界

## 题目

### 英文原题

> [!question] 英文原题
> **7.40** Let $X_1,\ldots,X_n$ be iid Bernoulli$(p)$. Show that the variance of $\bar X$ attains the Cramér–Rao Lower Bound, and hence $\bar X$ is the best unbiased estimator of $p$.

### 中文转述

> [!question] 中文转述
> **原题7.40。** 设$X_1,\ldots,X_n$独立同分布于$\operatorname{Bernoulli}(p)$.说明$\bar X$的方差达到Cramér--Rao下界，从而$\bar X$是$p$的最佳无偏估计量.

## 提示

> [!hint]- 提示
> 样本得分与$\bar X-p$成比例，这是信息不等式取等号的情形。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 对$0<p<1$，记$S=\sum_iX_i$，对数似然为$S\log p+(n-S)\log(1-p)$。得分$U=(S-np)/[p(1-p)]$，故
> $$
> I_n(p)=EU^2=\frac{np(1-p)}{p^2(1-p)^2}=\frac n{p(1-p)}.
> $$
> 有限支持允许逐项求导，信息不等式适用。对目标$g(p)=p$，任意有限方差无偏估计$T$有$\operatorname{Var}_pT\ge[g'(p)]^2/I_n=p(1-p)/n$。而$E\bar X=p$且$\operatorname{Var}\bar X=p(1-p)/n$，恰好达到，故在所有内点同时为最佳无偏估计。
>
> 若参数空间包含0和1，这两点不直接套内点得分公式：分别全零或全一样本几乎必然，$\bar X$方差为0，不可能再改进。于是最佳无偏结论也覆盖闭区间端点。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=325|印刷第294页／PDF物理第325页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 英文原文、中文转述与本库独立解答分别保留；实际核对正文位置列于`source_refs`。题内文献引用不表示已查阅其原文。`source_status: verified`只指本题及所列位置的核对范围，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
