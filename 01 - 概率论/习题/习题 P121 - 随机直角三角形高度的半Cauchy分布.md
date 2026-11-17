---
title: 习题 P121：随机直角三角形高度的半Cauchy分布
topic: probability-theory
topic_label: 概率论
difficulty: intermediate
status: not-started
tags:
- exercise
- probability-theory
source: George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第2章习题2.12，印刷页63/64／PDF物理页94/95
source_id: DS011
source_chapter: 2
source_exercise: '2.12'
source_stars: 0
source_refs:
- DS011 Exercise 2.12，印刷63/64／PDF物理94/95
source_status: verified
solution_status: independently-derived
created: '2026-11-13'
---

# 习题 P121：随机直角三角形高度的半Cauchy分布

## 题目

### 英文原题

> [!question] 英文原题
> **2.12** A random right triangle can be constructed in the following manner. Let $X$ be a random angle whose distribution is uniform on $(0,\pi/2)$. For each $X$, construct a triangle as pictured below. Here, $Y=$ height of the random triangle. For a fixed constant $d$, find the distribution of $Y$ and $\mathrm EY$.
>
> ![[附件/习题图/DS011/原图-习题2.12.png]]

### 中文转述

> [!question] 中文转述
> **原题2.12。** 可以按下列方式构造随机直角三角形. 设 $X$ 是在 $(0,\pi/2)$ 上均匀分布的随机角. 对每个 $X$，如下图构造三角形，其中 $Y$ 为该随机三角形的高. 对固定常数 $d$，求 $Y$ 的分布和 $\mathrm EY$.
>
> 原图见英文原题。

## 提示

> [!hint]- 提示
> 从图中得到$Y=d\tan X$。不能因为角度有界就断言高度的期望有限。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 按原图，$d>0$为固定的水平直角边长，$\tan X=Y/d$，故$Y=d\tan X$。对$y\ge0$，
> $$
> F_Y(y)=P\!\left(X\le\arctan\frac yd\right)
> =\frac2\pi\arctan\frac yd.
> $$
> $y<0$时CDF为0；对正半轴求导得
> $$
> f_Y(y)=\frac{2d}{\pi(d^2+y^2)},\quad y>0,
> $$
> 这就是尺度为$d$的半Cauchy分布（half-Cauchy distribution）。该密度的积分由反正切在无穷处趋于$\pi/2$而为1。
>
> 由于高度非负，期望允许扩展值。对$R>0$，
> $$
> \int_0^Ryf_Y(y)dy
> =\frac d\pi\log\!\left(1+\frac{R^2}{d^2}\right)\longrightarrow+\infty.
> $$
> 所以$\mathrm EY=+\infty$；它没有有限均值。图中常数作为非退化边长必须为正，若$d=0$会变成另一个退化几何模型，不能套用此密度。

## 相关概念

- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/概率模型|概率模型]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 来源：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=94|印刷第63/64页／PDF物理第94/95页]]；版本与归档见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 原题文字在PDF94，三角形原图在PDF95；忠实裁切中的x、(d,y)、d标签完整保留。d>0来自所画非退化边长，解答明示该几何条件。
- 已逐题查看原始页面，英文原题、全部分题与原附提示／引用照录；原题无星号。所列正文定位已经实读，题内补充、原文及独立推导分开。未查阅题内外部文献或答案册。
- 来源核对状态不表示个人学习完成；学习状态保持not-started。公式与链接检查不等于Obsidian实际渲染检查。
