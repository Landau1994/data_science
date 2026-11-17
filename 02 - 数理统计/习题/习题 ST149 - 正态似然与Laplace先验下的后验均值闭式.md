---
title: "习题 ST149：正态似然与Laplace先验下的后验均值闭式"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "advanced"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第7章习题7.26，印刷页291／PDF物理页322"
source_id: "DS011"
source_chapter: 7
source_exercise: "7.26"
source_stars: 0
source_refs: ["DS011 Exercise 7.26，印刷291／PDF物理322", "DS011 例7.2.16共轭正态模型，印刷263／PDF物理294"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST149：正态似然与Laplace先验下的后验均值闭式

## 题目

### 英文原题

> [!question] 英文原题
> **7.26** In Example 7.2.16, we saw that the normal distribution is its own conjugate family. It is sometimes the case, however, that a conjugate prior does not accurately reflect prior knowledge, and a different prior is sought. Let $X_1,\ldots,X_n$ be iid $n(\theta,\sigma^2)$, and let $\theta$ have a double exponential distribution, that is, $\pi(\theta)=e^{-|\theta|/a}/(2a)$, $a$ known. Find the mean of the posterior distribution of $\theta$.

### 中文转述

> [!question] 中文转述
> **原题7.26。** 在例7.2.16中，看到正态分布是自身的共轭族.不过，有时共轭先验不能准确反映先验知识，需要寻找不同的先验.设$X_1,\ldots,X_n$独立同分布于$n(\theta,\sigma^2)$，$\theta$服从双指数分布，即$\pi(\theta)=e^{-|\theta|/a}/(2a)$，$a$已知.求$\theta$的后验分布的均值.

## 提示

> [!hint]- 提示
> 按参数正负分段配方，后验成为两个截断正态的混合。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 设$a>0,\sigma^2>0$，令$z=\bar x$、$v=\sigma^2/n$、$s=\sqrt v$，用$\phi,\Phi$表示标准正态密度与CDF。后验核为$\exp[-(\theta-z)^2/(2v)-|\theta|/a]$。
>
> 在$\theta\ge0$与$\theta<0$两段分别配方，得到均值参数$m_+=z-v/a$、$m_-=z+v/a$的两个截断正态核，其未归一化段质量（去掉共同常数）是
> $$
> A_+=e^{-z/a}\Phi(m_+/s),\qquad A_-=e^{z/a}\Phi(-m_-/s).
> $$
> 完整后验是$A_+/(A_++A_-)$权重的$n(m_+,v)$在$[0,\infty)$截断分布，加上$A_-/(A_++A_-)$权重的$n(m_-,v)$在$(-\infty,0)$截断分布。
>
> 通过$\phi'(u)=-u\phi(u)$积分，两个段的条件均值分别为$m_++s\phi(m_+/s)/\Phi(m_+/s)$和$m_--s\phi(m_-/s)/\Phi(-m_-/s)$。所以
> $$
> E(\theta\mid\mathbf x)=\frac{A_+m_++A_-m_-+s[e^{-z/a}\phi(m_+/s)-e^{z/a}\phi(m_-/s)]}{A_++A_-}.
> $$
> 方括号恰为0，因为两项指数均为$-z^2/(2v)-v/(2a^2)$。最终可简写为
> $$
> E(\theta\mid\mathbf x)=z+\frac va\frac{A_--A_+}{A_++A_-}.
> $$
> 分母严格正、后验有高斯尾，故全部矩有限；$z=0$时两段对称，均值为0。极端$z$的数值实现宜使用对数正态尾函数避免上下溢，但这里给出的是解析公式。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=322|印刷第291页／PDF物理第322页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 英文原文、中文转述与本库独立解答分别保留；实际核对正文位置列于`source_refs`。题内文献引用不表示已查阅其原文。`source_status: verified`只指本题及所列位置的核对范围，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
