---
title: "习题 ST146：样本方差观测的倒Gamma共轭后验与均值条件"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第7章习题7.23，印刷页290／PDF物理页321"
source_id: "DS011"
source_chapter: 7
source_exercise: "7.23"
source_stars: 0
source_refs: ["DS011 Exercise 7.23，印刷290／PDF物理321"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST146：样本方差观测的倒Gamma共轭后验与均值条件

## 题目

### 英文原题

> [!question] 英文原题
> **7.23** If $S^2$ is the sample variance based on a sample of size $n$ from a normal population, we know that $(n-1)S^2/\sigma^2$ has a $\chi^2_{n-1}$ distribution. The conjugate prior for $\sigma^2$ is the inverted gamma pdf, IG$(\alpha,\beta)$, given by
> $$
> \pi(\sigma^2)=\frac1{\Gamma(\alpha)\beta^\alpha}\frac1{(\sigma^2)^{\alpha+1}}e^{-1/(\beta\sigma^2)},\qquad0<\sigma^2<\infty,
> $$
> where $\alpha$ and $\beta$ are positive constants. Show that the posterior distribution of $\sigma^2$ is IG$(\alpha+\frac{n-1}{2},[\frac{(n-1)S^2}{2}+\frac1\beta]^{-1})$. Find the mean of this distribution, the Bayes estimator of $\sigma^2$.

### 中文转述

> [!question] 中文转述
> **原题7.23。** 若$S^2$是正态总体中大小为$n$的样本的样本方差，已知$(n-1)S^2/\sigma^2$服从$\chi_{n-1}^2$分布.$\sigma^2$的共轭先验是逆gamma pdf，记为$\operatorname{IG}(\alpha,\beta)$：
>
> $$
> \pi(\sigma^2)=\frac1{\Gamma(\alpha)\beta^\alpha}\frac1{(\sigma^2)^{\alpha+1}}e^{-1/(\beta\sigma^2)},\qquad0<\sigma^2<\infty,
> $$
>
> 其中$\alpha$和$\beta$为正常数.说明$\sigma^2$的后验分布为
>
> $$
> \operatorname{IG}\left(\alpha+\frac{n-1}2,\left[\frac{(n-1)S^2}2+\frac1\beta\right]^{-1}\right).
> $$
>
> 求此分布的均值，即$\sigma^2$的Bayes估计量.

## 提示

> [!hint]- 提示
> 先把方差本身记作$q$，检查倒Gamma的尺度约定与负矩存在条件。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 本题按**只观测$S^2$**的似然计算，而非对未知正态均值另添未说明的先验。令$\nu=n-1>0$、$q=\sigma^2$，缩放卡方密度对$q$的核为$q^{-\nu/2}\exp[-\nu s^2/(2q)]$。乘先验后为
> $$
> q^{-(A+1)}e^{-B/q},\quad A=\alpha+\nu/2,\quad B=1/\beta+\nu s^2/2.
> $$
> 由代换$u=B/q$，积分为$\Gamma(A)/B^A$，所以完整后验为$B^Aq^{-A-1}e^{-B/q}/\Gamma(A)$，即本题记号的$IG(A,1/B)$。
>
> 再积分$q$倍的后验，得到
> $$
> E(q\mid s^2)=\frac{B\Gamma(A-1)}{\Gamma(A)}=
> \frac{1/\beta+(n-1)s^2/2}{\alpha+(n-1)/2-1},\qquad A>1.
> $$
> 若$A\le1$，后验均值发散，不能把同一分式当成有限Bayes点估计。平方损失下若还要求每个有限行动的后验损失有限，需$A>2$保证后验二阶矩；$1<A\le2$时后验均值虽有限，但普通平方风险比较全为无穷，应注明这一决策理论边界。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=321|印刷第290页／PDF物理第321页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 英文原文、中文转述与本库独立解答分别保留；实际核对正文位置列于`source_refs`。题内文献引用不表示已查阅其原文。`source_status: verified`只指本题及所列位置的核对范围，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
