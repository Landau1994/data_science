---
title: 习题 ST334：Huber损失及一阶导数的连续拼接
topic: mathematical-statistics
topic_label: 数理统计
difficulty: intermediate
status: not-started
tags:
- exercise
- mathematical-statistics
source: George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第10章习题10.28，印刷页413／PDF物理页444
source_id: DS011
source_chapter: 10
source_exercise: '10.28'
source_stars: 0
source_refs:
- DS011 Exercise 10.28，印刷413／PDF物理444
- DS011题内依赖核对：印刷391／PDF物理422
source_status: verified
solution_status: independently-derived
created: '2026-11-13'
---

# 习题 ST334：Huber损失及一阶导数的连续拼接

## 题目

### 英文原题

> [!question] 英文原题
> **10.28** Show that if $\rho$ is defined by (10.2.2), then both $\rho$ and $\rho'$ are continuous.

### 中文转述

> [!question] 中文转述
> **原题10.28。** 证明：若$\rho$由式(10.2.2)定义，则$\rho$与$\rho'$均连续.

### 题内引用与条件

式(10.2.2)定义$\rho(u)=u^2/2$（$|u|\le k$）、$k|u|-k^2/2$（$|u|\ge k$），通常$k>0$。

## 提示

> [!hint]- 提示
> 只需额外检查两个拼接点±k的函数值与左右导数。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 取$k>0$，$\rho(u)=u^2/2$（$|u|\le k$），$\rho(u)=k|u|-k^2/2$（$|u|\ge k$）。分段内部均光滑；在$u=\pm k$，两段函数值都为$k^2/2$，故连续。导数为
> $$
> \rho'(u)=\begin{cases}-k,&u<-k,\\u,&-k\le u\le k,\\k,&u>k.\end{cases}
> $$
> 在$-k$左右导数都为$-k$，在$k$都为$k$，所以导数存在且连续，$\rho\in C^1(\mathbb R)$。二阶导数在内部为1、外部为0，拼接点不连续且一般不存在，因此不称$\rho\in C^2$。$k=0$的退化函数恒0也连续，但不再识别位置参数。

## 相关概念

- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/期望|期望]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[02 - 数理统计/概念/参数估计|参数估计]]

## 备注

- 来源：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=444|印刷第413页／PDF物理第444页]]；版本与归档见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 式(10.2.2)实读印刷391／PDF422，独立验证两端拼接。
- 已实读本题所用正文：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=422|印刷391／PDF物理422]]；其余题内外部文献仅保留原引用，未声称查阅。
- 英文原题逐题对照PDF原始页面，保留原分题、提示、引用及可见疑误；原题无星号。题内引用补充与独立解答不混入原文；未查阅答案册或题内外部文献。
- 来源核对不表示个人学习完成，学习状态保持not-started。公式、链接与元数据检查不等于Obsidian实际渲染检查。
