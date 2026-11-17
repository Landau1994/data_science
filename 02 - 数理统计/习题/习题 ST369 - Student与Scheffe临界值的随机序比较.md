---
title: "习题 ST369：Student与Scheffe临界值的随机序比较"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第11章习题11.15，印刷页458／PDF物理页489"
source_id: "DS011"
source_chapter: 11
source_exercise: "11.15"
source_stars: 0
source_refs: ["DS011 Exercise 11.15，印刷458／PDF物理489", "DS011 定理11.2.10及临界值比较，印刷432／PDF物理463", "DS011 区间宽度与功效讨论，印刷433／PDF物理464"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST369：Student与Scheffe临界值的随机序比较

## 题目

### 英文原题

> [!question] 英文原题
> **11.15** (a) Show that for the $t$ and $F$ distributions, for any $\nu,\alpha$, and $k$,
> $$
> t_{\nu,\alpha/2}\le\sqrt{(k-1)F_{k-1,\nu,\alpha}}.
> $$
> (Recall the relation between the $t$ and the $F$. This inequality is a consequence of the fact that the distributions $kF_{k,\nu}$ are stochastically increasing in $k$ for fixed $\nu$, but is actually a weaker statement. See Exercise 5.19.)
>
> (b) Explain how the above inequality shows that the simultaneous Scheffé intervals are always wider than the single-contrast intervals.
>
> (c) Show that it also follows from the above inequality that Scheffé tests are less powerful than $t$ tests.

### 中文转述

> [!question] 中文转述
> **原题11.15。** (a)  证明，对$t$分布和$F$分布，以及任意$\nu,\alpha,k$，
>
> $$
> t_{\nu,\alpha/2}\le\sqrt{(k-1)F_{k-1,\nu,\alpha}}.
> $$
>
> （回顾$t$与$F$的关系. 固定$\nu$时，$kF_{k,\nu}$的分布随$k$随机递增，该不等式是其推论，但实际上是一个较弱的陈述. 见习题5.19.）
>
> (b)  解释上述不等式如何说明，同时Scheffé区间总比单个对比区间宽.
>
> (c)  证明，由上述不等式还可得到Scheffé检验的功效低于$t$检验.

## 提示

> [!hint]- 提示
> 用同一个分母，把一个正态平方扩充成多个平方和，直接得到随机序。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 合法范围为$\nu>0,0<\alpha<1$、整数$k\ge2$，分位数均按右尾概率记。
>
> **(a)** 取相互独立的$Z_1,\ldots,Z_{k-1}\sim n(0,1)$和$V\sim\chi_\nu^2$。则$Z_1^2/(V/\nu)\sim F_{1,\nu}$，$\sum_{j=1}^{k-1}Z_j^2/(V/\nu)\sim(k-1)F_{k-1,\nu}$，前者逐点不大于后者。因此其右尾$\alpha$分位数满足$F_{1,\nu,\alpha}\le(k-1)F_{k-1,\nu,\alpha}$。又$t_\nu^2\sim F_{1,\nu}$，所以$F_{1,\nu,\alpha}=t_{\nu,\alpha/2}^2$，开根即得。$k=2$为等号，$k>2$时非退化连续分布给严格更大的临界值。
>
> **(b)** 两种区间中心及标准误相同，半宽仅将Student临界值换成Scheffé的$\sqrt{(k-1)F}$，故同时区间不窄；$k=2$等宽，不能把“always wider”理解为无条件严格。
>
> **(c)** 对同一固定对比与同一名义$\alpha$，Scheffé单项拒绝域$\{|T|>\sqrt{(k-1)F}\}$包含于Student拒绝域$\{|T|>t\}$，所以对每个备择其拒绝概率不大于后者。这是同时保护带来的单项功效代价；不能把未校正的单项水平与同时总体水平当作同一个保证。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=489|印刷第458页／PDF物理第489页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 英文原文、中文转述与本库独立解答分别保留；实际核对正文位置列于`source_refs`。题内文献引用不表示已查阅其原文。`source_status: verified`只指本题及所列位置的核对范围，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
