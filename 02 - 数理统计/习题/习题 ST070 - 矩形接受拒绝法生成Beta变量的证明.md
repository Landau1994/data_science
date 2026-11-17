---
title: 习题 ST070：矩形接受拒绝法生成Beta变量的证明
topic: mathematical-statistics
topic_label: 数理统计
difficulty: intermediate
status: not-started
tags:
- exercise
- mathematical-statistics
source: George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第5章习题5.59，印刷页216／PDF物理页247
source_id: DS011
source_chapter: 5
source_exercise: '5.59'
source_stars: 0
source_refs:
- DS011 Exercise 5.59，印刷216／PDF物理247
- DS011题内依赖核对：印刷204／PDF物理235；印刷205／PDF物理236
source_status: verified
solution_status: independently-derived
created: '2026-11-13'
---

# 习题 ST070：矩形接受拒绝法生成Beta变量的证明

## 题目

### 英文原题

> [!question] 英文原题
> **5.59** Prove that the algorithm of Example 5.6.7 generates a beta$(a,b)$ random variable.

### 中文转述

> [!question] 中文转述
> **原题5.59。** 证明例5.6.7的算法生成$\operatorname{beta}(a,b)$随机变量.

### 题内引用与条件

例5.6.7设$a=2.7,b=6.3$，以$c\ge\max f$的矩形包络Beta密度；抽独立$U,V\sim U(0,1)$，若$U<f(V)/c$则输出$V$，否则重抽。

## 提示

> [!hint]- 提示
> 接受概率等于曲线下面积除以矩形面积；条件于接受后归一化。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 例5.6.7的算法每轮独立生成$U,V\sim U(0,1)$，令$A=\{U<f(V)/c\}$，其中$f(v)=v^{a-1}(1-v)^{b-1}/B(a,b)$且$c\ge\sup f<\infty$；接受时输出$V$，否则重抽。对任意Borel集$B\subset(0,1)$，
> $$
> P(V\in B,A)=\int_B\frac{f(v)}c\,dv,\qquad P(A)=1/c.
> $$
> 因此$P(V\in B\mid A)=\int_Bf(v)dv$。不同轮独立，首次接受轮的无条件输出概率为$\sum_{k=1}^\infty(1-1/c)^{k-1}\int_B f(v)dv/c=\int_Bf(v)dv$；接受概率正使几乎必然终止，平均轮数$c$。
>
> 对原例$a=2.7,b=6.3$，最大值在$(a-1)/(a+b-2)=1.7/7$，$c=f(1.7/7)\approx2.669$有限，所以证明适用。一般$a,b\ge1$时Beta密度有界；若$a<1$或$b<1$，端点发散，有限矩形包络不存在，原均匀矩形算法不可直接使用，需换重尾于端点的候选密度。

## 相关概念

- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/期望|期望]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/重采样|重采样]]

## 备注

- 来源：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=247|印刷第216页／PDF物理第247页]]；版本与归档见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 实读例5.6.7及算法：印刷204–205／PDF235–236；这里证明条件分布并用几何级数明确首次接受输出，不只引用一般定理。
- 已实读本题所用正文：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=235|印刷204／PDF物理235]]；[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=236|印刷205／PDF物理236]]；其余题内外部文献仅保留原引用，未声称查阅。
- 英文原题逐题对照PDF原始页面，保留原分题、提示、引用及可见疑误；原题无星号。题内引用补充与独立解答不混入原文；未查阅答案册或题内外部文献。
- 来源核对不表示个人学习完成，学习状态保持not-started。公式、链接与元数据检查不等于Obsidian实际渲染检查。
