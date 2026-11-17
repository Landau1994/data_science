---
title: 习题 ST027：由异参数正态构造卡方t与F统计量
topic: mathematical-statistics
topic_label: 数理统计
difficulty: intermediate
status: not-started
tags:
- exercise
- mathematical-statistics
source: George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第5章习题5.16，印刷页210／PDF物理页241
source_id: DS011
source_chapter: 5
source_exercise: '5.16'
source_stars: 0
source_refs:
- DS011 Exercise 5.16，印刷210／PDF物理241
source_status: verified
solution_status: independently-derived
created: '2026-11-13'
---

# 习题 ST027：由异参数正态构造卡方t与F统计量

## 题目

### 英文原题

> [!question] 英文原题
> **5.16** Let $X_i$, $i=1,2,3$, be independent with $\operatorname n(i,i^2)$ distributions. For each of the following situations, use the $X_i$s to construct a statistic with the indicated distribution.
>
> (a) Chi squared with 3 degrees of freedom.
>
> (b) $t$ distribution with 2 degrees of freedom.
>
> (c) $F$ distribution with 1 and 2 degrees of freedom.

### 中文转述

> [!question] 中文转述
> **原题5.16。** 设$X_i$（$i=1,2,3$）独立且各服从$n(i,i^2)$分布.在每种情形中，用$X_i$构造具有指定分布的统计量.
>
> (a)  自由度为3的卡方分布.
>
> (b)  自由度为2的$t$分布.
>
> (c)  自由度为1和2的$F$分布.

## 提示

> [!hint]- 提示
> 先把三个变量分别标准化。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 令$Z_1=X_1-1,Z_2=(X_2-2)/2,Z_3=(X_3-3)/3$，则三者独立$N(0,1)$。
>
> **(a)** $Q=Z_1^2+Z_2^2+Z_3^2\sim\chi^2_3$。
>
> **(b)** $T=Z_1/\sqrt{(Z_2^2+Z_3^2)/2}\sim t_2$，因为分子为标准正态，分母平方是独立$\chi^2_2/2$。
>
> **(c)** $F=Z_1^2/[(Z_2^2+Z_3^2)/2]\sim F_{1,2}$，同理由独立卡方比定义。分母为0的概率为0。

## 相关概念

- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/期望|期望]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[02 - 数理统计/概念/参数估计|参数估计]]

## 备注

- 来源：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=241|印刷第210页／PDF物理第241页]]；版本与归档见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 英文原题逐题对照PDF原始页面，保留原分题、提示、引用及可见疑误；原题无星号。题内引用补充与独立解答不混入原文；未查阅答案册或题内外部文献。
- 来源核对不表示个人学习完成，学习状态保持not-started。公式、链接与元数据检查不等于Obsidian实际渲染检查。
