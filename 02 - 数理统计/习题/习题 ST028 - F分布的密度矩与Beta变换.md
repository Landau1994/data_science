---
title: 习题 ST028：F分布的密度矩与Beta变换
topic: mathematical-statistics
topic_label: 数理统计
difficulty: intermediate
status: not-started
tags:
- exercise
- mathematical-statistics
source: George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第5章习题5.17，印刷页210／PDF物理页241
source_id: DS011
source_chapter: 5
source_exercise: '5.17'
source_stars: 0
source_refs:
- DS011 Exercise 5.17，印刷210／PDF物理241
source_status: verified
solution_status: independently-derived
created: '2026-11-13'
---

# 习题 ST028：F分布的密度矩与Beta变换

## 题目

### 英文原题

> [!question] 英文原题
> **5.17** Let $X$ be a random variable with an $F_{p,q}$ distribution.
>
> (a) Derive the pdf of $X$.
>
> (b) Derive the mean and variance of $X$.
>
> (c) Show that $1/X$ has an $F_{q,p}$ distribution.
>
> (d) Show that $(p/q)X/[1+(p/q)X]$ has a beta distribution with parameters $p/2$ and $q/2$.

### 中文转述

> [!question] 中文转述
> **原题5.17。** 设随机变量$X$服从$F_{p,q}$分布.
>
> (a)  推导$X$的pdf.
>
> (b)  推导$X$的均值与方差.
>
> (c)  证明$1/X$服从$F_{q,p}$分布.
>
> (d)  证明$(p/q)X/[1+(p/q)X]$服从参数为$p/2$和$q/2$的beta分布.

## 提示

> [!hint]- 提示
> 从独立卡方U,V出发，X=(U/p)/(V/q)。矩化成Gamma矩。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 设$p,q>0$，$U\sim\chi^2_p,V\sim\chi^2_q$独立，$X=qU/(pV)$。
>
> **(a)** 用$u=pxv/q$、Jacobian$pv/q$积分掉$v$，Gamma积分给
> $$
> f_X(x)=\frac{(p/q)^{p/2}}{B(p/2,q/2)}\frac{x^{p/2-1}}{(1+px/q)^{(p+q)/2}},\quad x>0,
> $$
> 支持外为0。具体被积式为$\frac{(p/q)^{p/2}x^{p/2-1}}{2^{(p+q)/2}\Gamma(p/2)\Gamma(q/2)}v^{(p+q)/2-1}e^{-(1+px/q)v/2}$，积分即上式。
>
> **(b)** 独立性与Gamma积分给
> $$
> EX^r=(q/p)^r\frac{\Gamma(p/2+r)\Gamma(q/2-r)}{\Gamma(p/2)\Gamma(q/2)},\quad -p/2<r<q/2.
> $$
> 取$r=1,2$并相减，得$EX=q/(q-2)$（$q>2$），$\operatorname{Var}X=2q^2(p+q-2)/[p(q-2)^2(q-4)]$（$q>4$）。当$q\le2$时均值为$\infty$；$2<q\le4$时方差为$\infty$；均值无限时通常不定义方差。
>
> **(c)** 交换$U,V$即$1/X=(V/q)/(U/p)\sim F_{q,p}$。
>
> **(d)** $B=U/(U+V)$。变换$s=U+V,b=U/s$，Jacobian$s$，联合密度分解为$\operatorname{Beta}(p/2,q/2)$密度与$\operatorname{Gamma}((p+q)/2,2)$密度，故所求变换确为Beta。

## 相关概念

- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/期望|期望]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[02 - 数理统计/概念/参数估计|参数估计]]

## 备注

- 来源：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=241|印刷第210页／PDF物理第241页]]；版本与归档见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 英文原题逐题对照PDF原始页面，保留原分题、提示、引用及可见疑误；原题无星号。题内引用补充与独立解答不混入原文；未查阅答案册或题内外部文献。
- 来源核对不表示个人学习完成，学习状态保持not-started。公式、链接与元数据检查不等于Obsidian实际渲染检查。
