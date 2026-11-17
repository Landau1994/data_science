---
title: 习题 ST058：均匀变量对数的卡方Gamma与Beta生成
topic: mathematical-statistics
topic_label: 数理统计
difficulty: intermediate
status: not-started
tags:
- exercise
- mathematical-statistics
source: George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第5章习题5.47，印刷页214／PDF物理页245
source_id: DS011
source_chapter: 5
source_exercise: '5.47'
source_stars: 0
source_refs:
- DS011 Exercise 5.47，印刷214／PDF物理245
- DS011题内依赖核对：印刷202／PDF物理233
source_status: verified
solution_status: independently-derived
created: '2026-11-13'
---

# 习题 ST058：均匀变量对数的卡方Gamma与Beta生成

## 题目

### 英文原题

> [!question] 英文原题
> **5.47** Verify the distributions of the random variables in (5.6.5).

### 中文转述

> [!question] 中文转述
> **原题5.47。** 验证式(5.6.5)中各随机变量的分布.

### 题内引用与条件

式(5.6.5)：$-2\sum_{j=1}^{\nu}\log U_j\sim\chi^2_{2\nu}$；$-\beta\sum_{j=1}^a\log U_j\sim\operatorname{Gamma}(a,\beta)$；$\sum_{j=1}^a\log U_j/\sum_{j=1}^{a+b}\log U_j\sim\operatorname{Beta}(a,b)$。$\nu,a,b$为正整数，$\beta>0$。

## 提示

> [!hint]- 提示
> −log U为尺度1指数；两个独立Gamma和的比例给Beta。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 设所有$U_j$独立$U(0,1)$。对$x\ge0$，$P(-\log U_j>x)=P(U_j<e^{-x})=e^{-x}$，故$E_j=-\log U_j\sim\operatorname{Exp}(1)$。其MGF为$(1-t)^{-1}$，独立和的MGF为$(1-t)^{-k}$，即Gamma$(k,1)$。
>
> 因此对正整数$\nu$，$-2\sum_{j=1}^\nu\log U_j=2\sum E_j\sim\operatorname{Gamma}(\nu,2)=\chi^2_{2\nu}$。对正整数$a$、$\beta>0$，$-\beta\sum_{j=1}^a\log U_j\sim\operatorname{Gamma}(a,\beta)$。
>
> 最后令$A=\sum_{j=1}^aE_j,B=\sum_{j=a+1}^{a+b}E_j$，$a,b$正整数。二者因使用不相交的均匀变量而独立，分别为Gamma$(a,1)$与Gamma$(b,1)$。变换$r=A/(A+B),s=A+B$，Jacobian$s$，联合密度为
> $$
> \frac{r^{a-1}(1-r)^{b-1}}{B(a,b)}\frac{s^{a+b-1}e^{-s}}{\Gamma(a+b)},\quad0<r<1,s>0.
> $$
> 故$\sum_{j=1}^a\log U_j/\sum_{j=1}^{a+b}\log U_j=A/(A+B)\sim\operatorname{Beta}(a,b)$。负号在比例中相消。

## 相关概念

- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/期望|期望]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[02 - 数理统计/概念/参数估计|参数估计]]

## 备注

- 来源：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=245|印刷第214页／PDF物理第245页]]；版本与归档见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 实读式(5.6.5)：印刷202／PDF233；原式三项及正整数求和范围在此补全。
- 已实读本题所用正文：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=233|印刷202／PDF物理233]]；其余题内外部文献仅保留原引用，未声称查阅。
- 英文原题逐题对照PDF原始页面，保留原分题、提示、引用及可见疑误；原题无星号。题内引用补充与独立解答不混入原文；未查阅答案册或题内外部文献。
- 来源核对不表示个人学习完成，学习状态保持not-started。公式、链接与元数据检查不等于Obsidian实际渲染检查。
