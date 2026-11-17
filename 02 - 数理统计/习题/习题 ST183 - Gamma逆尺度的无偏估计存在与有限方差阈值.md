---
title: "习题 ST183：Gamma逆尺度的无偏估计存在与有限方差阈值"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "advanced"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第7章习题7.60，印刷页296／PDF物理页327"
source_id: "DS011"
source_chapter: 7
source_exercise: "7.60"
source_stars: 0
source_refs: ["DS011 Exercise 7.60，印刷296／PDF物理327", "DS011 Gamma尺度密度式(3.3.6)，印刷81／PDF物理112", "DS011 完备指数族定理6.2.25，印刷234／PDF物理265", "DS011 定理7.3.23，印刷280／PDF物理311"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST183：Gamma逆尺度的无偏估计存在与有限方差阈值

## 题目

### 英文原题

> [!question] 英文原题
> **7.60** Let $X_1,\ldots,X_n$ be iid gamma$(\alpha,\beta)$ with $\alpha$ known. Find the best unbiased estimator of $1/\beta$.

### 中文转述

> [!question] 中文转述
> **原题7.60。** 设$X_1,\ldots,X_n$独立同分布于$\operatorname{gamma}(\alpha,\beta)$，$\alpha$已知.求$1/\beta$的最佳无偏估计量.

## 提示

> [!hint]- 提示
> 计算Gamma负矩前检查形状是否足够大；完备性也能排除有限方差替代方案。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 本书$\beta$为尺度。令$a=n\alpha$、$T=\sum_iX_i$，则$T\sim\operatorname{gamma}(a,\beta)$，且由联合密度因子分解充分；其自然参数$-1/\beta$遍历开区间，满指数族准则给完备性，也可用Laplace变换唯一性直接证明。
>
> 当$a>1$，Gamma负矩积分给$ET^{-1}=1/[\beta(a-1)]$，所以唯一的可积无偏充分量函数为
> $$
> \widehat{1/\beta}=\frac{a-1}{T}=\frac{n\alpha-1}{\sum_iX_i}.
> $$
> 当$a>2$，$ET^{-2}=1/[\beta^2(a-1)(a-2)]$，因此该估计方差为$1/[\beta^2(a-2)]$，由完备充分性为UMVU。
>
> 若$1<a\le2$，同一估计虽无偏可积，但二阶矩无穷；任何有限方差无偏估计若存在，对$T$条件化必须等于该函数，Jensen不等式会迫使其二阶矩有限，矛盾。所以此区间没有有限方差无偏估计，不应把无穷方差的公式当作通常意义的“最佳有限方差”。
>
> 若$a\le1$，甚至不存在可积无偏估计。否则充分性条件化后有可积函数$h(T)$，写$s=1/\beta$，无偏方程成为
> $$
> \int_0^\infty h(t)t^{a-1}e^{-st}dt=\Gamma(a)s^{1-a},\quad s>0.
> $$
> 固定$s_0>0$，绝对可积性使左端对$s\ge s_0$被$|h(t)|t^{a-1}e^{-s_0t}$支配，且逐点趋0，故支配收敛给左端$s\to\infty$趋0；右端在$a=1$为正常数、$a<1$发散，矛盾。原题没有给样本量与形状的阈值，必须分别说明。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=327|印刷第296页／PDF物理第327页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 原题未限定nα，解答分别处理a>2、1<a≤2与a≤1，避免在不存在矩时机械套公式。
- 英文原文、中文转述与本库独立解答分别保留；实际核对正文位置列于`source_refs`。题内文献引用不表示已查阅其原文。`source_status: verified`只指本题及所列位置的核对范围，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
