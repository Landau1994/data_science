---
title: "习题 ST239：二项与Poisson上尾观测的精确p值"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第8章习题8.49，印刷页334／PDF物理页365"
source_id: "DS011"
source_chapter: 8
source_exercise: "8.49"
source_stars: 0
source_refs: ["DS011 Exercise 8.49，印刷页334／PDF物理页365"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST239：二项与Poisson上尾观测的精确p值

## 题目

### 英文原题

> [!question] 英文原题
> **8.49** In each of the following situations, calculate the p-value of the observed data.
> (a) For testing $H_0:\theta\le1/2$ versus $H_1:\theta>1/2$, 7 successes are observed out of 10 Bernoulli trials.
> (b) For testing $H_0:\lambda\le1$ versus $H_1:\lambda>1$, $X=3$ is observed, where $X\sim\operatorname{Poisson}(\lambda)$.
> (c) For testing $H_0:\lambda\le1$ versus $H_1:\lambda>1$, $X_1=3,X_2=5,$ and $X_3=1$ is observed, where $X_i\sim\operatorname{Poisson}(\lambda)$, independent.

### 中文转述

> [!question] 中文转述
> **原题8.49。**
> 在以下各情形中，计算已观察数据的 $p$ 值.
>
> (a)  检验 $H_0:\theta\le1/2$ 对 $H_1:\theta>1/2$，在 $10$ 次伯努利试验中观察到 $7$ 次成功.
>
> (b)  检验 $H_0:\lambda\le1$ 对 $H_1:\lambda>1$，观测到 $X=3$，其中 $X\sim\operatorname{Poisson}(\lambda)$.
>
> (c)  检验 $H_0:\lambda\le1$ 对 $H_1:\lambda>1$，观测到 $X_1=3,X_2=5,X_3=1$，其中 $X_i\sim\operatorname{Poisson}(\lambda)$，相互独立.

## 提示

> [!hint]- 提示
> 有利于大参数的统计量用包含观察点的右尾，复合原假设最坏在边界。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 三例上尾均随参数增加，所以$p$值上确界在原假设上端点。
> (a) $p=P_{1/2}(S\ge7)=\sum_{k=7}^{10}\binom{10}k2^{-10}=176/1024=.171875$。
> (b) $p=P_1(X\ge3)=1-e^{-1}(1+1+1/2)\approx.0803013971$。
> (c) 总数$S=9$，在边界$S\sim\operatorname{Pois}(3)$，故$p=1-e^{-3}\sum_{k=0}^8 3^k/k!\approx.0038029921$。这里用完整独立样本的充分总数，不分别计算三个$p$值后任意合并；尾概率包含等于观察统计量的点。

## 相关概念

- [[02 - 数理统计/概念/假设检验|假设检验（hypothesis testing）]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[01 - 概率论/概念/条件概率|条件概率]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 完整原题已逐页对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=365|印刷334／PDF物理365]]；原题无星号。教材信息及归档进度见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 来源已核对与独立解答写成不等于个人已完成练习；学习状态保留`not-started`。未实测Obsidian界面渲染。
