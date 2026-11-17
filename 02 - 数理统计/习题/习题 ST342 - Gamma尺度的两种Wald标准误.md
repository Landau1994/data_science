---
title: 习题 ST342：Gamma尺度的两种Wald标准误
topic: mathematical-statistics
topic_label: 数理统计
difficulty: intermediate
status: not-started
tags:
- exercise
- mathematical-statistics
source: George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第10章习题10.36，印刷页415／PDF物理页446
source_id: DS011
source_chapter: 10
source_exercise: '10.36'
source_stars: 0
source_refs:
- DS011 Exercise 10.36，印刷415／PDF物理446
- DS011题内依赖核对：印刷398／PDF物理429
source_status: verified
solution_status: independently-derived
created: '2026-11-13'
---

# 习题 ST342：Gamma尺度的两种Wald标准误

## 题目

### 英文原题

> [!question] 英文原题
> **10.36** Let $X_1,\ldots,X_n$ be a random sample from a gamma$(\alpha,\beta)$ population. Assume $\alpha$ is known and $\beta$ is unknown. Consider testing $H_0:\beta=\beta_0$.
>
> (a) What is the MLE of $\beta$?
>
> (b) Derive a Wald statistic for testing $H_0$, using the MLE both in the numerator and denominator of the statistic.
>
> (c) Repeat part (b) but using the sample standard deviation in the standard error.

### 中文转述

> [!question] 中文转述
> **原题10.36。** 设$X_1,\ldots,X_n$为gamma$(\alpha,\beta)$总体的随机样本，假设$\alpha$已知、$\beta$未知. 考虑检验$H_0:\beta=\beta_0$.
>
> (a)  $\beta$的MLE是什么？
>
> (b)  导出检验$H_0$的Wald统计量，在统计量的分子与分母中都使用MLE.
>
> (c)  重做(b)，但在标准误中使用样本标准差.

## 提示

> [!hint]- 提示
> β是尺度，EX=αβ、Var X=αβ²。MLE是均值除以α。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 设$\alpha,\beta_0>0$。**(a)** 对数似然关于$\beta$为$-n\alpha\log\beta-\sum_iX_i/\beta+\mathrm{const}$，导数$-n\alpha/\beta+\sum_iX_i/\beta^2$，所以$\hat\beta=\bar X/\alpha$；导数由正变负，给全局MLE。
>
> **(b)** 总信息$I_n(\beta)=n\alpha/\beta^2$，MLE标准误为$\hat\beta/\sqrt{n\alpha}$，所以
> $$
> Z_W=\sqrt{n\alpha}\frac{\hat\beta-\beta_0}{\hat\beta}=\frac{\sqrt n(\bar X-\alpha\beta_0)}{\bar X/\sqrt\alpha}.
> $$
> **(c)** 因$\operatorname{sd}(\hat\beta)=\operatorname{sd}(\bar X)/\alpha=\sigma_X/(\alpha\sqrt n)$，以样本$S$估计$\sigma_X$，得$Z_{W,S}=\sqrt n(\bar X-\alpha\beta_0)/S$。iid Gamma具有有限二阶矩且$S\to_p\sqrt\alpha\beta$，因此两个统计量在$H_0$均趋于标准正态；以$|Z|>z_{\alpha_{\rm test}/2}$拒绝。检验显著性水平与Gamma形状同用字母时应分清，这里用$\alpha_{\rm test}$标记水平。

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
