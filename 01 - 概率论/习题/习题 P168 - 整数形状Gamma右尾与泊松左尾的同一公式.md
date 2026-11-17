---
title: "习题 P168：整数形状Gamma右尾与泊松左尾的同一公式"
topic: "probability-theory"
topic_label: "概率论"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "probability-theory"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第3章习题3.19，印刷页107／PDF物理页138"
source_id: "DS011"
source_chapter: 3
source_exercise: "3.19"
source_stars: 0
source_refs: ["DS011 Exercise 3.19，印刷107／PDF物理138", "DS011 Gamma密度与Gamma函数，印刷81／PDF物理112"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 P168：整数形状Gamma右尾与泊松左尾的同一公式

## 题目

### 英文原题

> [!question] 英文原题
> **3.19** Show that
> $$
> \int_x^\infty\frac1{\Gamma(\alpha)}z^{\alpha-1}e^{-z}\,dz=\sum_{y=0}^{\alpha-1}\frac{x^ye^{-x}}{y!},\qquad\alpha=1,2,3,\ldots.
> $$
> (Hint: Use integration by parts.) Express this formula as a probabilistic relationship between Poisson and gamma random variables.

### 中文转述

> [!question] 中文转述
> **原题3.19。** 证明
>
> $$
> \int_x^\infty\frac1{\Gamma(\alpha)}z^{\alpha-1}e^{-z}\,dz=\sum_{y=0}^{\alpha-1}\frac{x^ye^{-x}}{y!},\qquad\alpha=1,2,3,\ldots.
> $$
>
> （提示：用分部积分.）把这个公式表述为Poisson随机变量与Gamma随机变量之间的概率关系.

## 提示

> [!hint]- 提示
> 对形状参数作递推，基例是指数分布尾。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 取$x\ge0$以便作概率解释，设$I_a(x)=\int_x^\infty z^{a-1}e^{-z}dz/\Gamma(a)$。$I_1(x)=e^{-x}$。对$a\ge2$分部积分及$\Gamma(a)=(a-1)\Gamma(a-1)$给出
> $$
> I_a(x)=\frac{x^{a-1}e^{-x}}{(a-1)!}+I_{a-1}(x).
> $$
> 归纳得到$I_a(x)=e^{-x}\sum_{j=0}^{a-1}x^j/j!$。因此若$G\sim\operatorname{Gamma}(a,1)$、$N\sim\operatorname{Poisson}(x)$，则$P(G>x)=P(N\le a-1)$。连续Gamma的$>$可换成$\ge$。这只比较两个边缘分布，不要求它们独立或在同一空间；若要过程解释，可把$G$视为速率1泊松过程第$a$次到达时刻。

## 相关概念

- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/期望|期望]]
- [[01 - 概率论/概念/概率模型|概率模型]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=138|印刷第107页／PDF物理第138页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 英文原文、中文转述与本库独立解答分别保留；所用正文实际核对位置列于`source_refs`。题内文献只保留原题引用，不表示已查阅原文献。`source_status: verified`只指本题及所列位置核对，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
