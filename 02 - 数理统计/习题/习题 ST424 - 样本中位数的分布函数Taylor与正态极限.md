---
title: "习题 ST424：样本中位数的分布函数Taylor与正态极限"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "advanced"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第12章习题12.29，印刷页492／PDF物理页523"
source_id: "DS011"
source_chapter: 12
source_exercise: "12.29"
source_stars: 0
source_refs: ["DS011 Exercise 12.29，印刷页492／PDF物理页523", "DS011 所引正文，印刷485／PDF物理516", "DS011 所引正文，印刷486／PDF物理517"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST424：样本中位数的分布函数Taylor与正态极限

## 题目

### 英文原题

> [!question] 英文原题
> **12.29** Using a Taylor series argument as in Example 12.4.3, derive the asymptotic distribution of the median in iid sampling.

### 中文转述

> [!question] 中文转述
> **原题12.29。**
> 用例12.4.3那样的Taylor级数论证，推导独立同分布抽样中中位数的渐近分布.

## 提示

> [!hint]- 提示
> 对总体CDF在唯一中位数处展开，用二项计数CLT代替不可微样本指标的Taylor。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 设iid样本总体CDF为$F$，唯一中位数$m$，$F(m)=1/2$，$F$在$m$附近有连续密度且$f(m)>0$。先取奇数$n$，样本中位数$M_n=Y_{((n+1)/2)}$。对固定实$t$，令$a_n=m+t/\sqrt n$；Taylor展开给$p_n=F(a_n)=1/2+f(m)t/\sqrt n+o(n^{-1/2})$。计数$B_n=\sum I(Y_i\le a_n)\sim\operatorname{Bin}(n,p_n)$，且$\{M_n\le a_n\}=\{B_n\ge(n+1)/2\}$。
> 二项三角阵列CLT给$(B_n-np_n)/\sqrt{np_n(1-p_n)}\Rightarrow N(0,1)$，临界标准化值趋$-2f(m)t$，因此$P(\sqrt n(M_n-m)\le t)\to\Phi(2f(m)t)$，即
> $$\sqrt n(M_n-m)\Rightarrow N\left(0,\frac1{4f(m)^2}\right).$$
> 偶数样本的两个中央次序统计量只对应阈值索引相差1，作同样计算有相同极限；其间任意中位数选择由夹逼也同极限。这个Taylor作用于光滑的总体CDF，并完整解释随机计数极限；对含原子、平坦中位区间或$f(m)=0$的总体，给定正态方差结论不自动成立。无需误差均值或方差存在。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计（parameter estimation）]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]
- [[01 - 概率论/概念/随机变量|随机变量]]

## 备注

- 完整原题已逐页对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=523|印刷492／PDF物理523]]；原题无星号。教材信息与归档进度见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 实际引用输入核对页：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=516|印刷485／PDF物理516]]、[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=517|印刷486／PDF物理517]]；所需模型、公式、数据在解答重述。
- 来源已核对与解答写成不表示个人学习已完成；学习状态保留`not-started`。未实测Obsidian界面渲染。
