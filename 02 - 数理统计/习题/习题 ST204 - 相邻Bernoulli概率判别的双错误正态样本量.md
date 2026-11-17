---
title: "习题 ST204：相邻Bernoulli概率判别的双错误正态样本量"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第8章习题8.14，印刷页328／PDF物理页359"
source_id: "DS011"
source_chapter: 8
source_exercise: "8.14"
source_stars: 0
source_refs: ["DS011 Exercise 8.14，印刷页328／PDF物理页359"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST204：相邻Bernoulli概率判别的双错误正态样本量

## 题目

### 英文原题

> [!question] 英文原题
> **8.14** For a random sample $X_1,\ldots,X_n$ of Bernoulli$(p)$ variables, it is desired to test
> $$H_0:p=.49\quad\text{versus}\quad H_1:p=.51.$$
> Use the Central Limit Theorem to determine, approximately, the sample size needed so that the two probabilities of error are both about .01. Use a test function that rejects $H_0$ if $\sum_{i=1}^nX_i$ is large.

### 中文转述

> [!question] 中文转述
> **原题8.14。**
> 对 $\operatorname{Bernoulli}(p)$ 随机变量的随机样本 $X_1,\ldots,X_n$，希望检验
>
> $$
> H_0:p=.49\quad\text{对}\quad H_1:p=.51.
> $$
>
> 利用中心极限定理，近似确定使两类错误概率都约为 $.01$ 所需的样本量. 采用在 $\sum_{i=1}^nX_i$ 较大时拒绝 $H_0$ 的检验函数.

## 提示

> [!hint]- 提示
> 两假设的方差相同，临界点可放在两个总数均值中间。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 记$S=\sum_iX_i$。两假设下均值分别$.49n,.51n$，方差同为$.49\cdot.51n=.2499n$。采用$S>.5n$，忽略格点连续性修正时，两类错误都近似$1-\Phi(.01\sqrt n/\sqrt{.2499})$。令该值为$.01$得
> $$n\approx\frac{z_{.01}^2(.2499)}{.01^2}\approx13524.324,$$
> 因此约需$13525$次试验。阈值取最接近$n/2$的整数并按指定不等式执行；在该大样本下两错误约为$.01$。这是中心极限定理近似设计，不宣称有限二项格点能使两类错误严格同时等于$.01$；需要时可用精确二项尾和重新标定。

## 相关概念

- [[02 - 数理统计/概念/假设检验|假设检验（hypothesis testing）]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[01 - 概率论/概念/条件概率|条件概率]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 完整原题已逐页对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=359|印刷328／PDF物理359]]；原题无星号。教材信息及归档进度见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 来源已核对与独立解答写成不等于个人已完成练习；学习状态保留`not-started`。未实测Obsidian界面渲染。
