---
title: "习题 ST238：Fisher精确检验的超几何条件分布"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第8章习题8.48，印刷页334／PDF物理页365"
source_id: "DS011"
source_chapter: 8
source_exercise: "8.48"
source_stars: 0
source_refs: ["DS011 Exercise 8.48，印刷页334／PDF物理页365", "DS011 所引正文，印刷323／PDF物理354"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST238：Fisher精确检验的超几何条件分布

## 题目

### 英文原题

> [!question] 英文原题
> **8.48** Prove the assertion in Example 8.3.30 that the conditional distribution of $S_1$ given $S$ is hypergeometric.

### 中文转述

> [!question] 中文转述
> **原题8.48。**
> 证明例8.3.30的断言：给定 $S$ 后 $S_1$ 的条件分布为超几何分布.

## 提示

> [!hint]- 提示
> 在共同成功概率原假设下，两个二项pmf相乘再除以总成功数pmf。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 原例设$S_1\sim\operatorname{Bin}(n_1,p_1)$、$S_2\sim\operatorname{Bin}(n_2,p_2)$独立，原假设$p_1=p_2=p$，$S=S_1+S_2$。此时$S\sim\operatorname{Bin}(N,p)$，$N=n_1+n_2$。对有正条件概率的$s$，
> $$P(S_1=k\mid S=s)=\frac{\binom{n_1}k\binom{n_2}{s-k}p^s(1-p)^{N-s}}{\binom Ns p^s(1-p)^{N-s}}=\frac{\binom{n_1}k\binom{n_2}{s-k}}{\binom Ns},$$
> 支持$\max(0,s-n_2)\le k\le\min(n_1,s)$。这等价于在$N$个位置中均匀选$s$个成功，其中前$n_1$位置的成功数，故为超几何分布；Vandermonde恒等式验证总和1。未知$p$完全消去，这正是给定原假设充分总数后精确检验的依据。$p=0,1$时只对有正概率总数作相应退化条件分布。

## 相关概念

- [[02 - 数理统计/概念/假设检验|假设检验（hypothesis testing）]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[01 - 概率论/概念/条件概率|条件概率]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 完整原题已逐页对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=365|印刷334／PDF物理365]]；原题无星号。教材信息及归档进度见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 引用输入实际核对页：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=354|印刷323／PDF物理354]]；解答已重述所需假设及结果。
- 相关先修：[[02 - 数理统计/概念/充分统计量|充分统计量]]。
- 来源已核对与独立解答写成不等于个人已完成练习；学习状态保留`not-started`。未实测Obsidian界面渲染。
