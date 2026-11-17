---
title: "习题 ST421：有界设计的收敛反例与LAD次梯度残差"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "advanced"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第12章习题12.26，印刷页492／PDF物理页523"
source_id: "DS011"
source_chapter: 12
source_exercise: "12.26"
source_stars: 0
source_refs: ["DS011 Exercise 12.26，印刷页492／PDF物理页523", "DS011 所引正文，印刷485／PDF物理516", "DS011 所引正文，印刷486／PDF物理517"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST421：有界设计的收敛反例与LAD次梯度残差

## 题目

### 英文原题

> [!question] 英文原题
> **12.26** Exercises 12.26–12.28 will look at some of the details of Example 12.4.3.
> (a) Throughout Example 12.4.3 we assumed that $n^{-1}\sum_{i=1}^nx_i^2\to\sigma_x^2<\infty$. Show that this condition is satisfied by (i) $x_i=1$ (the case of ordinary median) and (ii) $|x_i|\le1$ (the case of bounded $x_i$).
> (b) Show that under the conditions on $x_i$ in part (a), $n^{-1}\sum_{i=1}^n\psi(y_i-\hat\beta_Lx_i)\to0$ in probability.

### 中文转述

> [!question] 中文转述
> **原题12.26。**
> (a)  例12.4.3始终假定$\frac1n\sum_{i=1}^nx_i^2\to\sigma_x^2<\infty$. 证明以下情形满足此条件：(i) $x_i=1$，即普通中位数的情形；(ii) $|x_i|\le1$，即$x_i$有界的情形.
>
> (b)  证明在(a)关于$x_i$的条件下，$\frac1n\sum_{i=1}^n\psi(y_i-\hat\beta_Lx_i)\to0$依概率成立.

## 提示

> [!hint]- 提示
> 原文$\psi$已含$x_i$权重；有界性不自动保证Cesàro平方均值收敛。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 原例定义$\psi_i(y_i-bx_i)=x_iI(y_i>bx_i)-x_iI(y_i<bx_i)$，零残差时取0；下面沿用这个含下标权重的定义。
> (a)(i) $x_i=1$时平方均值恒1，结论成立。(ii) 原断言不成立：令第$k$块长度$L_k=2^{2^k}$，奇数块全取0、偶数块全取1。因$L_k/\sum_{j<k}L_j\to\infty$，在奇数块末平方均值趋0，在偶数块末趋1，虽$|x_i|\le1$却无极限。正确结论只是平方均值有界；若另外假设它有极限，才满足原例条件。
> (b) 对LAD目标$Q(b)=\sum_i|y_i-bx_i|$，最优点有$0\in\partial Q(\hat\beta_L)$。在非零残差处，负次梯度恰为$\psi_i$；在零残差处可取任意$[-|x_i|,|x_i|]$以使总和0。假设原例独立连续误差且设计固定、忽略$x_i=0$的恒定项，则不同非零$x_i$的比值$Y_i/x_i$几乎处处无并列，所以任一拟合斜率至多一个非零权重残差恰为0。因而$|\sum_i\psi_i(Y_i-\hat\beta_Lx_i)|\le\max_{i\le n}|x_i|$几乎处处。
> 在$|x_i|\le1$下，除以$n$的绝对值不超过$1/n$，甚至几乎处处趋0；$x_i=1$同理。更一般若平方均值有界，$\max|x_i|/n\le\sqrt{\sum x_i^2}/n=O(n^{-1/2})\to0$。因此(b)可成立而不必硬证错误的(a)(ii)。若误差有原子产生大量并列，需保留次梯度选择而不能无说明地把所有零残差都当作同一可微得分。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计（parameter estimation）]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]
- [[01 - 概率论/概念/随机变量|随机变量]]

## 备注

- 完整原题已逐页对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=523|印刷492／PDF物理523]]；原题无星号。教材信息与归档进度见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 实际引用输入核对页：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=516|印刷485／PDF物理516]]、[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=517|印刷486／PDF物理517]]；所需模型、公式、数据在解答重述。
- 来源已核对与解答写成不表示个人学习已完成；学习状态保留`not-started`。未实测Obsidian界面渲染。
