---
title: "习题 ST213：单观测Beta形状族的UMP单侧检验"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第8章习题8.23，印刷页329／PDF物理页360"
source_id: "DS011"
source_chapter: 8
source_exercise: "8.23"
source_stars: 0
source_refs: ["DS011 Exercise 8.23，印刷页329／PDF物理页360"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST213：单观测Beta形状族的UMP单侧检验

## 题目

### 英文原题

> [!question] 英文原题
> **8.23** Suppose $X$ is one observation from a population with beta$(\theta,1)$ pdf.
> (a) For testing $H_0:\theta\le1$ versus $H_1:\theta>1$, find the size and sketch the power function of the test that rejects $H_0$ if $X>1/2$.
> (b) Find the most powerful level $\alpha$ test of $H_0:\theta=1$ versus $H_1:\theta=2$.
> (c) Is there a UMP test of $H_0:\theta\le1$ versus $H_1:\theta>1$? If so, find it. If not, prove so.

### 中文转述

> [!question] 中文转述
> **原题8.23。**
> 设 $X$ 是来自密度为 $\operatorname{beta}(\theta,1)$ 的总体的一次观测.
>
> (a)  对检验 $H_0:\theta\le1$ 对 $H_1:\theta>1$，求在 $X>1/2$ 时拒绝 $H_0$ 的检验的大小，并画出功效函数.
>
> (b)  求 $H_0:\theta=1$ 对 $H_1:\theta=2$ 的水平 $\alpha$ 最强检验.
>
> (c)  是否存在 $H_0:\theta\le1$ 对 $H_1:\theta>1$ 的一致最强检验？若存在，求出；否则证明不存在.

## 提示

> [!hint]- 提示
> CDF为$x^\theta$；大$X$支持大形状参数。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 参数$\theta>0$，密度$\theta x^{\theta-1}$、CDF$x^\theta$，$0<x<1$。
> (a) $\beta(\theta)=1-2^{-\theta}$严格递增，故$\sup_{0<\theta\le1}\beta=1/2$。曲线见图，横轴保留完整正参数域的代表区间。
>
> ![[附件/习题图/DS011/习题8.23-Beta功效.png]]
>
> (b) 似然比$2x$严格递增，原假设均匀，所以拒绝$X>1-\alpha$恰有大小$\alpha$且最强。
> (c) 对任意$\theta_1>1$，相对于边界1的似然比$\theta_1x^{\theta_1-1}$均递增，同一个拒绝域$X>1-\alpha$在每个简单备择都最强；其在所有$\theta\le1$的拒绝概率不超过边界$\alpha$。任意复合原假设水平$\alpha$的竞争检验也在边界1有水平$\alpha$，因此受这些最强性逐一控制。故该检验UMP，功效$1-(1-\alpha)^\theta$。

## 相关概念

- [[02 - 数理统计/概念/假设检验|假设检验（hypothesis testing）]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[01 - 概率论/概念/条件概率|条件概率]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 完整原题已逐页对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=360|印刷329／PDF物理360]]；原题无星号。教材信息及归档进度见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 本题图件按解答公式独立绘制并保留[[附件/习题图/DS011/习题8.23-Beta功效.pdf|矢量PDF]]及[[附件/习题图/DS011/源码/第8章/ch08_23.tex|可编辑绘图源文件]]；数据为公式数值采样，不是随机模拟。
- 来源已核对与独立解答写成不等于个人已完成练习；学习状态保留`not-started`。未实测Obsidian界面渲染。
