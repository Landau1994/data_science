---
title: 习题 P126：幂密度与Cauchy分布的中位数
topic: probability-theory
topic_label: 概率论
difficulty: beginner
status: not-started
tags:
- exercise
- probability-theory
source: George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第2章习题2.17，印刷页64／PDF物理页95
source_id: DS011
source_chapter: 2
source_exercise: '2.17'
source_stars: 0
source_refs:
- DS011 Exercise 2.17，印刷64／PDF物理95
source_status: verified
solution_status: independently-derived
created: '2026-11-13'
---

# 习题 P126：幂密度与Cauchy分布的中位数

## 题目

### 英文原题

> [!question] 英文原题
> **2.17** A median of a distribution is a value $m$ such that $P(X\le m)\ge\frac12$ and $P(X\ge m)\ge\frac12$. (If $X$ is continuous, $m$ satisfies $\int_{-\infty}^mf(x)\,dx=\int_m^\infty f(x)\,dx=\frac12$.) Find the median of the following distributions.
>
> (a) $f(x)=3x^2$, $0<x<1$
>
> (b) $f(x)=\dfrac1{\pi(1+x^2)}$, $-\infty<x<\infty$

### 中文转述

> [!question] 中文转述
> **原题2.17。** 分布的中位数（median）是满足 $P(X\le m)\ge\frac12$ 且 $P(X\ge m)\ge\frac12$ 的数 $m$. （若 $X$ 连续，则 $m$ 满足 $\int_{-\infty}^m f(x)\,dx=\int_m^\infty f(x)\,dx=\frac12$.）求下列分布的中位数.
>
> (a)  $f(x)=3x^2$，$0<x<1$.
>
> (b)  $f(x)=1/[\pi(1+x^2)]$，$-\infty<x<\infty$.

## 提示

> [!hint]- 提示
> 对连续分布解$F(m)=1/2$；中位数存在不要求均值存在。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** **(a)** 支持内$F(x)=\int_0^x3t^2dt=x^3$，严格递增，故唯一中位数为$m=2^{-1/3}$。
>
> **(b)** $F(x)=1/2+\arctan(x)/\pi$，严格递增，$F(0)=1/2$，故唯一中位数为0。该分布的均值不存在，但这不影响中位数的定义与上述计算。两题在中位点均无原子，因此左右闭半轴概率都恰为$1/2$。

## 相关概念

- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/概率模型|概率模型]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 来源：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=95|印刷第64页／PDF物理第95页]]；版本与归档见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 已逐题查看原始页面，英文原题、全部分题与原附提示／引用照录；原题无星号。所列正文定位已经实读，题内补充、原文及独立推导分开。未查阅题内外部文献或答案册。
- 来源核对状态不表示个人学习完成；学习状态保持not-started。公式与链接检查不等于Obsidian实际渲染检查。
