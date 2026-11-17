---
title: 习题 ST341：正态均值与标准差的Wald统计量
topic: mathematical-statistics
topic_label: 数理统计
difficulty: intermediate
status: not-started
tags:
- exercise
- mathematical-statistics
source: George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第10章习题10.35，印刷页415／PDF物理页446
source_id: DS011
source_chapter: 10
source_exercise: '10.35'
source_stars: 0
source_refs:
- DS011 Exercise 10.35，印刷415／PDF物理446
- DS011题内依赖核对：印刷398／PDF物理429
source_status: verified
solution_status: independently-derived
created: '2026-11-13'
---

# 习题 ST341：正态均值与标准差的Wald统计量

## 题目

### 英文原题

> [!question] 英文原题
> **10.35** Let $X_1,\ldots,X_n$ be a random sample from a $\operatorname n(\mu,\sigma^2)$ population.
>
> (a) If $\mu$ is unknown and $\sigma^2$ is known, show that $Z=\sqrt n(\bar X-\mu_0)/\sigma$ is a Wald statistic for testing $H_0:\mu=\mu_0$.
>
> (b) If $\sigma^2$ is unknown and $\mu$ is known, find a Wald statistic for testing $H_0:\sigma=\sigma_0$.

### 中文转述

> [!question] 中文转述
> **原题10.35。** 设$X_1,\ldots,X_n$为$\mathrm n(\mu,\sigma^2)$总体的随机样本.
>
> (a)  若$\mu$未知、$\sigma^2$已知，证明$Z=\sqrt n(\bar X-\mu_0)/\sigma$是检验$H_0:\mu=\mu_0$的Wald统计量.
>
> (b)  若$\sigma^2$未知、$\mu$已知，求检验$H_0:\sigma=\sigma_0$的Wald统计量.

## 提示

> [!hint]- 提示
> Wald用参数估计减零假设值，除以在估计值处的标准误。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** **(a)** $\hat\mu=\bar X$，每观测信息$I_\mu=1/\sigma^2$，标准误$\sigma/\sqrt n$，故$Z_W=(\hat\mu-\mu_0)/(\sigma/\sqrt n)$即原$Z$。正态模型下它在$H_0$精确$N(0,1)$，不仅渐近。
>
> **(b)** 写$Q=\sum_i(X_i-\mu)^2$，MLE$\hat\sigma=\sqrt{Q/n}$。关于$\sigma$，得分$-n/\sigma+Q/\sigma^3$、总信息$2n/\sigma^2$，故以MLE代入标准误$\hat\sigma/\sqrt{2n}$，得到
> $$
> Z_W=\sqrt{2n}\frac{\hat\sigma-\sigma_0}{\hat\sigma}\Rightarrow N(0,1)\quad(H_0).
> $$
> 要求$\sigma_0>0$。若改把参数定义为$v=\sigma^2$，另一个合法Wald统计量为$(\hat v-\sigma_0^2)/[\hat v\sqrt{2/n}]$；两者一阶渐近等价，有限样本不相同，Wald不具一般有限样本重参数化不变性。

## 相关概念

- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/期望|期望]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/假设检验|假设检验]]

## 备注

- 来源：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=446|印刷第415页／PDF物理第446页]]；版本与归档见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 已实读本题所用正文：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=429|印刷398／PDF物理429]]；其余题内外部文献仅保留原引用，未声称查阅。
- 英文原题逐题对照PDF原始页面，保留原分题、提示、引用及可见疑误；原题无星号。题内引用补充与独立解答不混入原文；未查阅答案册或题内外部文献。
- 来源核对不表示个人学习完成，学习状态保持not-started。公式、链接与元数据检查不等于Obsidian实际渲染检查。
