---
title: 习题 ST056：Gamma元件寿命的极小二项尾概率
topic: mathematical-statistics
topic_label: 数理统计
difficulty: intermediate
status: not-started
tags:
- exercise
- mathematical-statistics
source: George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第5章习题5.45，印刷页214／PDF物理页245
source_id: DS011
source_chapter: 5
source_exercise: '5.45'
source_stars: 0
source_refs:
- DS011 Exercise 5.45，印刷214／PDF物理245
- DS011题内依赖核对：印刷200／PDF物理231
source_status: verified
solution_status: independently-derived
created: '2026-11-13'
---

# 习题 ST056：Gamma元件寿命的极小二项尾概率

## 题目

### 英文原题

> [!question] 英文原题
> **5.45** For the situation of Example 5.6.1, calculate the probability that at least 75% of the components last 150 hours when
>
> (a) $c=300$, $X\sim\operatorname{gamma}(a,b)$, $a=4,b=5$.
>
> (b) $c=100$, $X\sim\operatorname{gamma}(a,b)$, $a=20,b=5$.
>
> (c) $c=100$, $X\sim\operatorname{gamma}(a,b)$, $a=20.7,b=5$.
>
> Hint: In parts (a) and (b) it is possible to evaluate the gamma integral in closed form, although it probably isn't worth the effort in (b). There is no closed form expression for the integral in part (c), which has to be evaluated either through numerical integration or simulation.

### 中文转述

> [!question] 中文转述
> **原题5.45。** 在例5.6.1的情形中，计算至少75\%的元件寿命达到150小时的概率，分别取：
>
> (a)  $c=300$，$X\sim\operatorname{gamma}(a,b)$，$a=4,b=5$.
>
> (b)  $c=100$，$X\sim\operatorname{gamma}(a,b)$，$a=20,b=5$.
>
> (c)  $c=100$，$X\sim\operatorname{gamma}(a,b)$，$a=20.7,b=5$.
> 提示：(a)、(b)的gamma积分可求闭式，尽管(b)可能不值得这样费力.(c)的积分没有闭式，须用数值积分或模拟计算.

### 题内引用与条件

例5.6.1中$c$为独立元件总数，先以单个生存概率$p_1=P(X\ge h)$求至少$t$个存活的二项尾和。本题以Gamma寿命替换例中的指数寿命，$h=150$。

## 提示

> [!hint]- 提示
> b是尺度；先求单个寿命生存概率，再算至少ceil(.75c)次成功的二项尾。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 例5.6.1假定元件寿命独立；这里Gamma采用形状$a$、尺度$b$。记$p_a=P(X\ge150)=\Gamma(a,30)/\Gamma(a)$，$K\sim\operatorname{Bin}(c,p_a)$。所求精确表达为
> $$
> P(K\ge t)=\sum_{k=t}^c\binom ck p_a^k(1-p_a)^{c-k},\quad t=\lceil.75c\rceil.
> $$
> 整数$a$时分部积分递推给$p_a=e^{-30}\sum_{j=0}^{a-1}30^j/j!$；非整数使用上不完全Gamma积分。实际用70位十进制运算求该积分及有限和，得到
>
> |分题|$t$|单个生存概率$p_a$|所求二项尾概率|
> |---|---:|---:|---:|
> |(a)|225|$4.66103200078\times10^{-10}$|$2.50905486275\times10^{-2028}$|
> |(b)|75|$.0218734684414$|$4.38178996957\times10^{-102}$|
> |(c)|75|$.0307162144174$|$4.01000720062\times10^{-91}$|
>
> 这些量远小于通常直接Monte Carlo可分辨的频率，本解答以高精度积分和精确有限二项求和计算，没有把模拟中零次成功当成真实概率0。

## 相关概念

- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/期望|期望]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[02 - 数理统计/概念/参数估计|参数估计]]

## 备注

- 来源：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=245|印刷第214页／PDF物理第245页]]；版本与归档见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 实读例5.6.1：印刷200／PDF231。实际数值实现及环境见[[work/DS011/ch05/computations.py|本章独立计算]]、[[work/DS011/ch05/results.json|实际结果]]；mpmath 1.3.0，70位运算。
- 已实读本题所用正文：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=231|印刷200／PDF物理231]]；其余题内外部文献仅保留原引用，未声称查阅。
- 英文原题逐题对照PDF原始页面，保留原分题、提示、引用及可见疑误；原题无星号。题内引用补充与独立解答不混入原文；未查阅答案册或题内外部文献。
- 来源核对不表示个人学习完成，学习状态保持not-started。公式、链接与元数据检查不等于Obsidian实际渲染检查。
