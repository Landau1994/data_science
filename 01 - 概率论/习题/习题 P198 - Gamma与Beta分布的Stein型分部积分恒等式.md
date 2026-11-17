---
title: "习题 P198：Gamma与Beta分布的Stein型分部积分恒等式"
topic: "probability-theory"
topic_label: "概率论"
difficulty: "advanced"
status: "not-started"
tags: ["exercise", "probability-theory"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第3章习题3.49，印刷页111／PDF物理页142"
source_id: "DS011"
source_chapter: 3
source_exercise: "3.49"
source_stars: 0
source_refs: ["DS011 Exercise 3.49，印刷111／PDF物理142", "DS011 Gamma尺度密度，印刷81／PDF物理112", "DS011 Stein相关上下文，印刷103／PDF物理134"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 P198：Gamma与Beta分布的Stein型分部积分恒等式

## 题目

### 英文原题

> [!question] 英文原题
> **3.49** Prove the following analogues to Stein’s Lemma, assuming appropriate conditions on the function $g$.
>
> (a) If $X\sim\operatorname{gamma}(\alpha,\beta)$, then
> $$
> E(g(X)(X-\alpha\beta))=\beta E(Xg'(X)).
> $$
> (b) If $X\sim\operatorname{beta}(\alpha,\beta)$, then
> $$
> E\left[g(X)\left(\beta-(\alpha-1)\frac{1-X}{X}\right)\right]=E((1-X)g'(X)).
> $$

### 中文转述

> [!question] 中文转述
> **原题3.49。** 在假定函数$g$满足适当条件的前提下，证明下列Stein引理的对应结果.
>
> (a)  若$X\sim\operatorname{gamma}(\alpha,\beta)$，则
>
> $$
> E(g(X)(X-\alpha\beta))=\beta E(Xg'(X)).
> $$
>
> (b)  若$X\sim\operatorname{beta}(\alpha,\beta)$，则
>
> $$
> E\left[g(X)\left(\beta-(\alpha-1)\frac{1-X}X\right)\right]=E((1-X)g'(X)).
> $$

## 提示

> [!hint]- 提示
> 找出带密度的乘积导数，再让边界项消失。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 给出足够条件：$g$在支持内部局部绝对连续，两边被积函数绝对可积，下述积分边界项均为0。特别地，$g\in C_c^1$且紧支集落在支持内部时这些条件自动满足。
>
> **(a)** Gamma密度$f=x^{\alpha-1}e^{-x/\beta}/[\Gamma(\alpha)\beta^\alpha]$，直接求导得$(xf)'=(\alpha-x/\beta)f$。若$[xg(x)f(x)]_{0}^{\infty}=0$，则
> $$
> E[g(X)(X-\alpha\beta)]
> =-\beta\int_0^\infty g(x)(xf(x))'dx
> =\beta\int_0^\infty xg'(x)f(x)dx.
> $$
> **(b)** 对Beta密度，
> $$
> ((1-x)f(x))'=\left[(\alpha-1)\frac{1-x}x-\beta\right]f(x).
> $$
> 若$[(1-x)g(x)f(x)]_0^1=0$，负号乘上此式并分部积分，便得到
> $$
> \int_0^1g(x)\left[\beta-(\alpha-1)\frac{1-x}x\right]f(x)dx
> =\int_0^1(1-x)g'(x)f(x)dx.
> $$
> 当$\alpha\le1$时，含$1/X$的项及0端边界尤其不能省略检查；不是任意可微$g$都满足结论。上述条件把原题“appropriate conditions”具体化，未假装原书为所有函数断言成立。

## 相关概念

- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/期望|期望]]
- [[01 - 概率论/概念/概率模型|概率模型]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=142|印刷第111页／PDF物理第142页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 英文原文、中文转述与本库独立解答分别保留；所用正文实际核对位置列于`source_refs`。题内文献只保留原题引用，不表示已查阅原文献。`source_status: verified`只指本题及所列位置核对，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
