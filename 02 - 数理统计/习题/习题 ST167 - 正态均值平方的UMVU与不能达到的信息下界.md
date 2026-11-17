---
title: "习题 ST167：正态均值平方的UMVU与不能达到的信息下界"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "advanced"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第7章习题7.44，印刷页294／PDF物理页325"
source_id: "DS011"
source_chapter: 7
source_exercise: "7.44"
source_stars: 0
source_refs: ["DS011 Exercise 7.44，印刷294／PDF物理325", "DS011 完备指数族准则定理6.2.25，印刷234／PDF物理265", "DS011 Stein引理3.6.5，印刷102／PDF物理133", "DS011 定理7.3.23完备充分量的最优性，印刷280／PDF物理311"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST167：正态均值平方的UMVU与不能达到的信息下界

## 题目

### 英文原题

> [!question] 英文原题
> **7.44** Let $X_1,\ldots,X_n$ be iid $n(\theta,1)$. Show that the best unbiased estimator of $\theta^2$ is $\bar X^2-(1/n)$. Calculate its variance (use Stein’s Identity from Section 3.6), and show that it is greater than the Cramér–Rao Lower Bound.

### 中文转述

> [!question] 中文转述
> **原题7.44。** 设$X_1,\ldots,X_n$独立同分布于$n(\theta,1)$.说明$\theta^2$的最佳无偏估计量为$\bar X^2-1/n$.计算其方差（使用节3.6的Stein恒等式），并说明它大于Cramér--Rao下界.

## 提示

> [!hint]- 提示
> 均值平方先减去已知方差；Stein恒等式递推出四阶矩。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 令$Z=\bar X\sim n(\theta,v)$、$v=1/n$。$EZ^2=\theta^2+v$，故$T=Z^2-v$无偏。样本联合密度的参数部分是$\exp[n\theta Z-n\theta^2/2]$，$Z$充分；其自然参数$n\theta$遍历开区间$\mathbb R$，由满秩指数族完备性准则，$Z$完备。因此$T$为完备充分量的无偏函数，Rao–Blackwell与完备性给它为唯一最佳无偏估计（不另行把该指数族完备性定理归为本题独立重证）。
>
> 按题意用Stein恒等式$E[(Z-\theta)g(Z)]=vEg'(Z)$。取$g(z)=z^2$得$EZ^3=\theta EZ^2+2vEZ=\theta^3+3\theta v$；取$g(z)=z^3$得$EZ^4=\theta EZ^3+3vEZ^2=\theta^4+6\theta^2v+3v^2$。这些多项式在高斯下绝对可积、边界项消失，所以恒等式适用。因此
> $$
> \operatorname{Var}T=EZ^4-(EZ^2)^2=4\theta^2/n+2/n^2.
> $$
> 信息$I_n=n$，目标$g(\theta)=\theta^2$导数$2\theta$，故Cramér–Rao下界为$4\theta^2/n$，严格差$2/n^2>0$，包括$\theta=0$。最佳无偏并不意味着一定达到这个下界。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=325|印刷第294页／PDF物理第325页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 英文原文、中文转述与本库独立解答分别保留；实际核对正文位置列于`source_refs`。题内文献引用不表示已查阅其原文。`source_status: verified`只指本题及所列位置的核对范围，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
