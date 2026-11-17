---
title: 习题 ST349：Wald区间端点补正与覆盖长度权衡
topic: mathematical-statistics
topic_label: 数理统计
difficulty: intermediate
status: not-started
tags:
- exercise
- mathematical-statistics
source: George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第10章习题10.43，印刷页416／PDF物理页447
source_id: DS011
source_chapter: 10
source_exercise: '10.43'
source_stars: 0
source_refs:
- DS011 Exercise 10.43，印刷416／PDF物理447
- DS011题内依赖核对：印刷406／PDF物理437
source_status: verified
solution_status: independently-derived
created: '2026-11-13'
---

# 习题 ST349：Wald区间端点补正与覆盖长度权衡

## 题目

### 英文原题

> [!question] 英文原题
> **10.43** In Example 10.4.7, two modifications were made to the Wald interval.
>
> (a) At $y=0$ the upper interval endpoint was changed to $1-(\alpha/2)^{1/n}$, and at $y=n$ the lower interval endpoint was changed to $(\alpha/2)^{1/n}$. Justify the choice of these endpoints. (Hint: Section 9.2.3.)
>
> (b) The second modification was to truncate all intervals to be within $[0,1]$. Show that this change, together with the one in part (a), results in an improvement over the original Wald interval.

### 中文转述

> [!question] 中文转述
> **原题10.43。** 在例10.4.7中，对Wald区间作了两项修正.
>
> (a)  当$y=0$时，将上端点改为$1-(\alpha/2)^{1/n}$；当$y=n$时，将下端点改为$(\alpha/2)^{1/n}$. 说明选取这些端点的理由. （提示：第9.2.3节.）
>
> (b)  第二项修正是将所有区间截断在$[0,1]$内. 证明这个改变结合(a)的改变，改进了原Wald区间.

## 提示

> [!hint]- 提示
> y=0与y=n时原标准误0；反演单侧精确二项尾可以补出非零长度端点。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 设$Y\sim\operatorname{Bin}(n,p)$，$0<\alpha<1$。
>
> **(a)** 若观察$Y=0$，等尾精确上端点$u$满足$P_u(Y=0)=(1-u)^n=\alpha/2$，故$u=1-(\alpha/2)^{1/n}$，下端0。若$Y=n$，下端$l$满足$P_l(Y=n)=l^n=\alpha/2$，故$l=(\alpha/2)^{1/n}$，上端1。这些是反演两侧各分配$\alpha/2$的精确单侧尾概率边界；原Wald在极端观测分别退化为$[0,0]$、$[1,1]$，会漏掉全部内部参数。
>
> **(b)** 对每个真实$p\in[0,1]$，$p\in C\cap[0,1]$当且仅当$p\in C$，因此截断不改变覆盖概率，且逐次实现长度不增、排除无效参数值。端点观测处(a)扩张了原退化区间，其他观测不变，所以对每个$p$总覆盖概率弱增加，在某些内部$p$严格增加。两改动使参数范围合法，并缓解边界欠覆盖，构成这种意义的改进。
>
> 不能声称同时对所有样本都缩短长度：(a)本来就把零长度改成正长度；也不能由该局部修正推出全参数覆盖至少$1-\alpha$，中间计数的Wald区间仍可能欠覆盖。故“改进”的准确结论是截断不损覆盖而缩去无效长度，加上端点扩张弱增覆盖；并非完整有限样本置信系数保证。

## 相关概念

- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/期望|期望]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[02 - 数理统计/概念/参数估计|参数估计]]

## 备注

- 来源：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=447|印刷第416页／PDF物理第447页]]；版本与归档见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 实读例10.4.7与其两项修正：印刷406／PDF437。
- 已实读本题所用正文：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=437|印刷406／PDF物理437]]；其余题内外部文献仅保留原引用，未声称查阅。
- 英文原题逐题对照PDF原始页面，保留原分题、提示、引用及可见疑误；原题无星号。题内引用补充与独立解答不混入原文；未查阅答案册或题内外部文献。
- 来源核对不表示个人学习完成，学习状态保持not-started。公式、链接与元数据检查不等于Obsidian实际渲染检查。
