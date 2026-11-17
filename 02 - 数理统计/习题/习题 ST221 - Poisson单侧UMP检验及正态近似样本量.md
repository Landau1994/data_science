---
title: "习题 ST221：Poisson单侧UMP检验及正态近似样本量"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第8章习题8.31，印刷页330／PDF物理页361"
source_id: "DS011"
source_chapter: 8
source_exercise: "8.31"
source_stars: 0
source_refs: ["DS011 Exercise 8.31，印刷页330／PDF物理页361"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST221：Poisson单侧UMP检验及正态近似样本量

## 题目

### 英文原题

> [!question] 英文原题
> **8.31** Let $X_1,\ldots,X_n$ be iid Poisson$(\lambda)$.
> (a) Find a UMP test of $H_0:\lambda\le\lambda_0$ versus $H_1:\lambda>\lambda_0$.
> (b) Consider the specific case $H_0:\lambda\le1$ versus $H_1:\lambda>1$. Use the Central Limit Theorem to determine the sample size $n$ so a UMP test satisfies $P(\text{reject }H_0\mid\lambda=1)=.05$ and $P(\text{reject }H_0\mid\lambda=2)=.9$.

### 中文转述

> [!question] 中文转述
> **原题8.31。**
> 设 $X_1,\ldots,X_n$ 独立同分布于 $\operatorname{Poisson}(\lambda)$.
>
> (a)  求 $H_0:\lambda\le\lambda_0$ 对 $H_1:\lambda>\lambda_0$ 的一个一致最强检验.
>
> (b)  考虑具体情形 $H_0:\lambda\le1$ 对 $H_1:\lambda>1$. 利用中心极限定理确定样本量 $n$，使一致最强检验满足 $P(\text{拒绝 }H_0\mid\lambda=1)=.05$ 和 $P(\text{拒绝 }H_0\mid\lambda=2)=.9$.

## 提示

> [!hint]- 提示
> 总数为Poisson，精确大小一般需要临界格点随机化。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** (a) 充分统计量$S=\sum X_i\sim\operatorname{Pois}(n\lambda)$，任意较大参数相对$\lambda_0$的似然比为常数乘$(\lambda/\lambda_0)^S$，随$S$增加。因此选择整数$k$及$0\le\gamma\le1$，在$S>k$时拒绝、$S=k$时以$\gamma$拒绝，使$P_{n\lambda_0}(S>k)+\gamma P_{n\lambda_0}(S=k)=\alpha$。尾概率随参数增加，所以原假设最坏在边界；NP引理对每个较大参数成立，故UMP。若拒绝随机化，取相邻尾域使大小不超过$\alpha$，但通常不精确等于它。
> (b) CLT把临界总数近似写为$n+z_{.05}\sqrt n$，在备择2达到功效$.9$需要它也等于$2n-z_{.10}\sqrt{2n}$。故$\sqrt n\approx z_{.05}+\sqrt2z_{.10}$，$n\approx11.95$，得到近似设计$n=12$。这是题目要求的CLT设计，而不是两项有限样本等式的严格解；Poisson格点和偏斜会造成差异。若要求有限样本第一类错误恰为$.05$，应按(a)实际标定边界随机化，再检查备择功效；精确等于$.9$也不一定能由某个整数$n$同时取得。后附有限核验记录会分别报告该近似设计的精确表现，不把近似当作等式证明。 实际精确核验：$n=12$时在$S>18$必拒绝、$S=18$以约$.4925090151$拒绝，大小恰为$.05$但在$\lambda=2$的功效约$.8919891593$；取$n=13$，在$S>19$必拒绝、$S=19$以约$.2698859401$拒绝，则大小$.05$、功效约$.9118672084\ge.9$。因此若把功效要求解释为至少$.9$，$n=13$提供有限样本可实施修正；在$n=1,\ldots,12$逐一精确标定与计算也均低于$.9$。

## 相关概念

- [[02 - 数理统计/概念/假设检验|假设检验（hypothesis testing）]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[01 - 概率论/概念/条件概率|条件概率]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 完整原题已逐页对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=361|印刷330／PDF物理361]]；原题无星号。教材信息及归档进度见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 来源已核对与独立解答写成不等于个人已完成练习；学习状态保留`not-started`。未实测Obsidian界面渲染。
