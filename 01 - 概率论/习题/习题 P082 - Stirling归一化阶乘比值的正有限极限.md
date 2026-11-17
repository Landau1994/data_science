---
title: "习题 P082：Stirling归一化阶乘比值的正有限极限"
topic: "probability-theory"
topic_label: "概率论"
difficulty: "advanced"
status: "not-started"
tags: ["exercise", "probability-theory"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第1章习题1.28，印刷页33–34／PDF物理页64–65"
source_id: "DS011"
source_chapter: 1
source_exercise: "1.28"
source_stars: 0
source_refs: ["DS011 Exercise 1.28，印刷33–34／PDF物理64–65"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-12"
---

# 习题 P082：Stirling归一化阶乘比值的正有限极限

## 题目

### 英文原题

> [!question] 英文原题
> **1.28** A way of approximating large factorials is through the use of Stirling’s Formula:
> $$
> n!\approx\sqrt{2\pi}n^{n+(1/2)}e^{-n},
> $$
> a complete derivation of which is difficult. Instead, prove the easier fact
> $$
> \lim_{n\to\infty}\frac{n!}{n^{n+(1/2)}e^{-n}}=\text{a constant}.
> $$
> (Hint: Feller (1968) proceeds by using the monotonicity of the logarithm to establish that
> $$
> \int_{k-1}^{k}\log x\,dx<\log k<\int_{k}^{k+1}\log x\,dx,\qquad k=1,\ldots,n,
> $$
> and hence
> $$
> \int_{0}^{n}\log x\,dx<\log n!<\int_{1}^{n+1}\log x\,dx.
> $$
> Now compare $\log n!$ to the average of the two integrals. See Exercise 5.35 for another derivation.)

### 中文转述

> [!question] 中文转述
> **原题1.28。** 大阶乘可用Stirling公式（Stirling’s formula）近似：
> $$
> n!\approx\sqrt{2\pi}n^{n+(1/2)}e^{-n}.
> $$
> 完整推导比较困难，改为证明较弱结论：
> $$
> \lim_{n\to\infty}\frac{n!}{n^{n+(1/2)}e^{-n}}=\text{某个常数}.
> $$
> 原提示：Feller（1968）利用对数的单调性建立
> $$
> \int_{k-1}^{k}\log x\,dx<\log k<\int_{k}^{k+1}\log x\,dx,\quad k=1,\ldots,n,
> $$
> 进而
> $$
> \int_{0}^{n}\log x\,dx<\log n!<\int_{1}^{n+1}\log x\,dx.
> $$
> 再把$\log n!$与两个积分的平均值比较。另一种推导见习题5.35。

## 提示

> [!hint]- 提示
> 令$a_n=\log(n!)-(n+1/2)\log n+n$，证明差分$a_{n+1}-a_n$的绝对值由常数倍$n^{-2}$控制。仅有随$n$增长的上下界，不足以证明极限存在。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 不预先使用完整Stirling公式，而证明比值存在正有限极限，不确定该极限为$\sqrt{2\pi}$。
>
> 令
> $$
> a_n=\log(n!)-(n+1/2)\log n+n.
> $$
> 直接相减得
> $$
> a_{n+1}-a_n=1-(n+1/2)\log(1+1/n).
> $$
> 由恒等式$1/(1+t)=1-t+t^2/(1+t)$在$[0,x]$上积分，得到
> $$
> \log(1+x)=x-\frac{x^2}{2}+R(x),\qquad
> R(x)=\int_0^x\frac{t^2}{1+t}\,dt,
> $$
> 且当$0\le x\le1$时，$0\le R(x)\le x^3/3$。取$x=1/n$，则
> $$
> a_{n+1}-a_n=\frac{1}{4n^2}-(n+1/2)R(1/n),
> $$
> 所以
> $$
> -\frac{1}{4n^2}\le a_{n+1}-a_n\le\frac{1}{4n^2},\qquad n\ge1.
> $$
> 这里下界利用$1/4-1/3-1/(6n)\ge-1/4$。又因$\sum_{n=1}^{\infty}n^{-2}<\infty$（尾和可由$\int x^{-2}dx$控制），差分绝对可求和，故$a_n$是实数Cauchy序列，趋于某个有限$a$。指数函数连续，因此
> $$
> \frac{n!}{n^{n+(1/2)}e^{-n}}=e^{a_n}\longrightarrow e^a\in(0,\infty).
> $$
> 原提示的积分不等式正确，其中$\int_0^1\log x\,dx$是收敛的反常积分；不过单独列出这些夹逼不等式并没有控制到余项收敛。本证明用绝对可求和差分补齐这一点。

## 相关概念

- [[01 - 概率论/概念/概率模型|概率模型]]
- [[01 - 概率论/概念/随机变量|随机变量]]

## 备注

- 原题已对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=64|印刷第33–34页／PDF物理第64–65页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。原题无星号。
- 原提示跨印刷33–34／PDF64–65，已完整保留；没有把本题较弱的极限存在性误称为已证明完整Stirling常数，也未实际查阅题内Feller或第5章习题。
- 来源核对、独立解答与个人学习分别记录；`verified`仅指本题及所列引用位置已核对，学习状态保持`not-started`。未做Obsidian实际渲染检查。
