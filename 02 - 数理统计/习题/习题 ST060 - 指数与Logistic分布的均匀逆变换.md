---
title: 习题 ST060：指数与Logistic分布的均匀逆变换
topic: mathematical-statistics
topic_label: 数理统计
difficulty: intermediate
status: not-started
tags:
- exercise
- mathematical-statistics
source: George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第5章习题5.49，印刷页214／PDF物理页245
source_id: DS011
source_chapter: 5
source_exercise: '5.49'
source_stars: 0
source_refs:
- DS011 Exercise 5.49，印刷214／PDF物理245
source_status: verified
solution_status: independently-derived
created: '2026-11-13'
---

# 习题 ST060：指数与Logistic分布的均匀逆变换

## 题目

### 英文原题

> [!question] 英文原题
> **5.49** Let $U\sim\operatorname{uniform}(0,1)$.
>
> (a) Show that both $-\log U$ and $-\log(1-U)$ are exponential random variables.
>
> (b) Show that $X=\log\frac u{1-u}$ is a logistic$(0,1)$ random variable.
>
> (c) Show how to generate a logistic$(\mu,\beta)$ random variable.

### 中文转述

> [!question] 中文转述
> **原题5.49。** 设$U\sim\operatorname{uniform}(0,1)$.
>
> (a)  证明$-\log U$与$-\log(1-U)$都是指数随机变量.
>
> (b)  证明$X=\log\frac u{1-u}$是$\operatorname{logistic}(0,1)$随机变量.
>
> (c)  说明如何生成$\operatorname{logistic}(\mu,\beta)$随机变量.

## 提示

> [!hint]- 提示
> 逆变换求CDF，Logistic位置尺度变换只需仿射组合。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** **(a)** 对$x\ge0$，$P(-\log U\le x)=P(U\ge e^{-x})=1-e^{-x}$；同理$P(-\log(1-U)\le x)=P(U\le1-e^{-x})=1-e^{-x}$。两者均尺度1指数，但同一个$U$产生的两者并不独立。
>
> **(b)** 将原式的小写$u$解释为随机$U$，$U/(1-U)$严格递增，故$P(X\le x)=P(U\le e^x/(1+e^x))=1/(1+e^{-x})$。求导为$e^{-x}/(1+e^{-x})^2$，即标准Logistic密度。
>
> **(c)** 对位置$\mu\in\mathbb R$、尺度$\beta>0$，独立抽取新的$U$并令$Y=\mu+\beta\log[U/(1-U)]$。其CDF为$[1+\exp(-(y-\mu)/\beta)]^{-1}$，所以$Y\sim\operatorname{Logistic}(\mu,\beta)$。

## 相关概念

- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/期望|期望]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[02 - 数理统计/概念/参数估计|参数估计]]

## 备注

- 来源：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=245|印刷第214页／PDF物理第245页]]；版本与归档见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 英文原题逐题对照PDF原始页面，保留原分题、提示、引用及可见疑误；原题无星号。题内引用补充与独立解答不混入原文；未查阅答案册或题内外部文献。
- 来源核对不表示个人学习完成，学习状态保持not-started。公式、链接与元数据检查不等于Obsidian实际渲染检查。
