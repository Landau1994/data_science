---
title: "习题 ST086：双参数Gamma族的和与对数和充分性"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第6章习题6.6，印刷页244／PDF物理页275"
source_id: "DS011"
source_chapter: 6
source_exercise: "6.6"
source_stars: 0
source_refs: ["DS011 Exercise 6.6，印刷244／PDF物理275", "DS011 Theorem 6.2.6，印刷225／PDF256"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST086：双参数Gamma族的和与对数和充分性

## 题目

### 英文原题

> [!question] 英文原题
> **6.6** Let $X_1,\ldots,X_n$ be a random sample from a gamma$(\alpha,\beta)$ population. Find a two-dimensional sufficient statistic for $(\alpha,\beta)$.

### 中文转述

> [!question] 中文转述
> **原题6.6。**
> 设$X_1,\ldots,X_n$为来自$\operatorname{gamma}(\alpha,\beta)$总体的随机样本.求$(\alpha,\beta)$的二维充分统计量.

## 提示

> [!hint]- 提示 1
> 把$x_i^{\alpha-1}$的乘积写为对数和的指数。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 教材输入与补充假设另行标明。
>
> 采用本书的尺度参数表示，$\alpha,\beta>0$，
> $$
> f(x\mid\alpha,\beta)=\frac{x^{\alpha-1}e^{-x/\beta}}{\Gamma(\alpha)\beta^\alpha}\mathbf1_{\{x>0\}}.
> $$
> 于是
> $$
> L=\Gamma(\alpha)^{-n}\beta^{-n\alpha}
>  \exp\!\left((\alpha-1)\sum_i\log x_i-\frac1\beta\sum_ix_i\right)
>  \prod_i\mathbf1_{\{x_i>0\}}.
> $$
> 故$T=(\sum_iX_i,\sum_i\log X_i)$充分；一一等价的$(\sum_iX_i,\prod_iX_i)$也充分，因为所有样本均为正。即使另一约定把$\beta$写作率参数，仍得到同样的两个样本统计量，但似然中的$\beta$位置应相应改变。

## 相关概念

- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[01 - 概率论/概念/概率模型|概率模型]]

## 备注

- 统一来源见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011教材台账]]；原题位于[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=275|印刷244／PDF物理275]]。已对照原始页面核对完整英文、分题与定位，原题无星号。
- 解答为独立推导；引用的教材结论按source_refs核对，不使用答案册代替证明。
- 来源核对、归档与个人学习分别记录；verified只指所列来源核对范围，学习状态保持not-started。未实测Obsidian渲染。
