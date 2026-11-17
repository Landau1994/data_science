---
title: 习题 ST330：M估计量渐近夹心方差的Slutsky推导
topic: mathematical-statistics
topic_label: 数理统计
difficulty: intermediate
status: not-started
tags:
- exercise
- mathematical-statistics
source: George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第10章习题10.24，印刷页412／PDF物理页443
source_id: DS011
source_chapter: 10
source_exercise: '10.24'
source_stars: 0
source_refs:
- DS011 Exercise 10.24，印刷412／PDF物理443
- DS011题内依赖核对：印刷392／PDF物理423
source_status: verified
solution_status: independently-derived
created: '2026-11-13'
---

# 习题 ST330：M估计量渐近夹心方差的Slutsky推导

## 题目

### 英文原题

> [!question] 英文原题
> **10.24** Assuming that $\theta_0$ satisfies $E_{\theta_0}\psi(X-\theta_0)=0$, show that (10.2.4) and (10.2.5) imply (10.2.6).

### 中文转述

> [!question] 中文转述
> **原题10.24。** 假设$\theta_0$满足$E_{\theta_0}\psi(X-\theta_0)=0$，证明式(10.2.4)与式(10.2.5)蕴含式(10.2.6).

## 提示

> [!hint]- 提示
> 分子CLT、分母依概率趋于非零常数，还须具备M估计量的渐近线性展开。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 记$A=E_{\theta_0}\psi'(X-\theta_0)\ne0$、$B=E_{\theta_0}\psi(X-\theta_0)^2<\infty$。原式(10.2.4)为$-n^{-1/2}\sum\psi(X_i-\theta_0)\Rightarrow N(0,B)$；(10.2.5)为$n^{-1}\sum\psi'(X_i-\theta_0)\to_pA$。若沿用原文的线性化表达，二者相除由Slutsky得到$N(0,B/A^2)$，即(10.2.6)。
>
> 严格地说，需先有相合根$\hat\theta_M$及$o_p(1)$余项的线性关系。按$\psi'$是对其自变量求导的通常记号，正确Taylor展开为
> $$
> 0=\sum_i\psi(X_i-\theta_0)-(\hat\theta_M-\theta_0)\sum_i\psi'(X_i-\theta_0)+o_p(\sqrt n).
> $$
> 因此$\sqrt n(\hat\theta_M-\theta_0)=[n^{-1/2}\sum\psi]/[n^{-1}\sum\psi']+o_p(1)\Rightarrow N(0,B/A^2)$。原正文线性项符号相反，但中心正态及平方分母使最终方差相同。仅有两个平均量收敛而没有这条估计量展开，不能逻辑上推出任何任意估计量的极限；本题在正文正则线性化范围内成立。

## 相关概念

- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/期望|期望]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[02 - 数理统计/概念/参数估计|参数估计]]

## 备注

- 来源：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=443|印刷第412页／PDF物理第443页]]；版本与归档见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 式(10.2.4)–(10.2.6)实读印刷392／PDF423；显式列出非零分母、有限二阶矩及余项范围。
- 已实读本题所用正文：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=423|印刷392／PDF物理423]]；其余题内外部文献仅保留原引用，未声称查阅。
- 英文原题逐题对照PDF原始页面，保留原分题、提示、引用及可见疑误；原题无星号。题内引用补充与独立解答不混入原文；未查阅答案册或题内外部文献。
- 来源核对不表示个人学习完成，学习状态保持not-started。公式、链接与元数据检查不等于Obsidian实际渲染检查。
