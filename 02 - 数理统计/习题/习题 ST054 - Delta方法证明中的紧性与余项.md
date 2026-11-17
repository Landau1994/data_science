---
title: 习题 ST054：Delta方法证明中的紧性与余项
topic: mathematical-statistics
topic_label: 数理统计
difficulty: intermediate
status: not-started
tags:
- exercise
- mathematical-statistics
source: George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第5章习题5.43，印刷页214／PDF物理页245
source_id: DS011
source_chapter: 5
source_exercise: '5.43'
source_stars: 0
source_refs:
- DS011 Exercise 5.43，印刷214／PDF物理245
- DS011题内依赖核对：印刷195／PDF物理226；印刷197／PDF物理228
source_status: verified
solution_status: independently-derived
created: '2026-11-13'
---

# 习题 ST054：Delta方法证明中的紧性与余项

## 题目

### 英文原题

> [!question] 英文原题
> **5.43** Fill in the details in the proof of Theorem 5.5.24.
>
> (a) Show that if $\sqrt n(Y_n-\mu)\to\operatorname n(0,\sigma^2)$ in distribution, then $Y_n\to\mu$ in probability.
>
> (b) Give the details for the application of Slutsky's Theorem (Theorem 5.5.17).

### 中文转述

> [!question] 中文转述
> **原题5.43。** 补全定理5.5.24证明的细节.
>
> (a)  证明若$\sqrt n(Y_n-\mu)\to n(0,\sigma^2)$（依分布），则$Y_n\to\mu$（依概率）.
>
> (b)  给出应用Slutsky定理（定理5.5.17）的细节.

### 题内引用与条件

定理5.5.24（Delta方法）假设$\sqrt n(Y_n-\mu)\Rightarrow N(0,\sigma^2)$及$g'(\mu)$存在且非0，结论为$\sqrt n[g(Y_n)-g(\mu)]\Rightarrow N(0,\sigma^2[g'(\mu)]^2)$。

## 提示

> [!hint]- 提示
> 弱收敛的标准化序列紧；可微余项必须是o(Y_n−µ)，不能只知它趋于0。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** **(a)** 记$Z_n=\sqrt n(Y_n-\mu)$。分布收敛到有限正态变量保证紧性：对任意$\eta>0$可选$M$使充分大$n$时$P(|Z_n|>M)<\eta$。当$\epsilon\sqrt n>M$时，$P(|Y_n-\mu|>\epsilon)\le P(|Z_n|>M)<\eta$，故$Y_n\to_p\mu$。
>
> **(b)** 假设$g$在$\mu$可微，定义
> $$
> r(y)=\begin{cases}[g(y)-g(\mu)]/(y-\mu)-g'(\mu),&y\ne\mu,\\0,&y=\mu.\end{cases}
> $$
> 可微性给$r(y)\to0$当$y\to\mu$；(a)给$r(Y_n)\to_p0$。因此
> $$
> \sqrt n[g(Y_n)-g(\mu)]=[g'(\mu)+r(Y_n)]Z_n\Rightarrow g'(\mu)Z\sim N(0,\sigma^2[g'(\mu)]^2).
> $$
> 这里Slutsky应用于依概率趋于常数的第一因子与依分布收敛的第二因子，不要求二者独立。也可用紧性直接证明$r(Y_n)Z_n\to_p0$：其尾概率不超过$P(|Z_n|>M)+P(|r(Y_n)|>\epsilon/M)$。若$g'(\mu)=0$，此尺度给退化0，需高阶展开才有非退化极限。仅说未缩放的Taylor余项趋于0不足以推出结论。

## 相关概念

- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/期望|期望]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[02 - 数理统计/概念/参数估计|参数估计]]

## 备注

- 来源：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=245|印刷第214页／PDF物理第245页]]；版本与归档见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 实读定理5.5.24：印刷197／PDF228。补足原简写中缩放余项的必要阶数。
- 已实读本题所用正文：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=226|印刷195／PDF物理226]]；[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=228|印刷197／PDF物理228]]；其余题内外部文献仅保留原引用，未声称查阅。
- 英文原题逐题对照PDF原始页面，保留原分题、提示、引用及可见疑误；原题无星号。题内引用补充与独立解答不混入原文；未查阅答案册或题内外部文献。
- 来源核对不表示个人学习完成，学习状态保持not-started。公式、链接与元数据检查不等于Obsidian实际渲染检查。
