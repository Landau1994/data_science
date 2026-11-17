---
title: "习题 P233：Beta二项与BetaPascal混合的矩条件"
topic: "probability-theory"
topic_label: "概率论"
difficulty: "advanced"
status: "not-started"
tags: ["exercise", "probability-theory"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第4章习题4.34，印刷页161／PDF物理页192"
source_id: "DS011"
source_chapter: 4
source_exercise: "4.34"
source_stars: 0
source_refs: ["DS011 Exercise 4.34，印刷161／PDF物理192", "DS011 所引正文，印刷78／PDF物理109", "DS011 所引正文，印刷79／PDF物理110", "DS011 所引正文，印刷137／PDF物理168", "DS011 所引正文，印刷138／PDF物理169"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 P233：Beta二项与BetaPascal混合的矩条件

## 题目

### 英文原题

> [!question] 英文原题
> **4.34** (a) For the hierarchy in Example 4.4.6, show that the marginal distribution of $X$ is given by the beta–binomial distribution
> $$
> P(X=x)=\binom nx\frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)}\frac{\Gamma(x+\alpha)\Gamma(n-x+\beta)}{\Gamma(\alpha+\beta+n)}.
> $$
> (b) A variation on the hierarchical model in part (a) is
> $$
> X\mid P\sim\operatorname{negative\ binomial}(r,P)\quad\text{and}\quad P\sim\operatorname{beta}(\alpha,\beta).
> $$
> Find the marginal pmf of $X$, and its mean and variance. (This distribution is the beta–Pascal.)

### 中文转述

> [!question] 中文转述
> **原题4.34。**
> (a)  对例4.4.6 的层次结构，证明 $X$ 的边缘分布为 Beta–二项分布：
>
> $$
> P(X=x)=\binom nx\frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)}\frac{\Gamma(x+\alpha)\Gamma(n-x+\beta)}{\Gamma(\alpha+\beta+n)}.
> $$
>
> (b)  (a) 中分层模型的一种变体是
>
> $$
> X\mid P\sim\operatorname{negative\ binomial}(r,P),\qquad P\sim\operatorname{beta}(\alpha,\beta).
> $$
>
> 求 $X$ 的边缘 pmf、均值与方差. 此分布称为 Beta–Pascal 分布.

## 提示

> [!hint]- 提示
> 直接对Beta密度积分；负二项的倒数成功概率矩只在一定形状参数下存在。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 原例模型为$X\mid P\sim\operatorname{Bin}(n,P)$、$P\sim\operatorname{Beta}(\alpha,\beta)$，$n\ge0$整数、$\alpha,\beta>0$。
> (a) $P(X=x)=\binom nxB(\alpha+x,\beta+n-x)/B(\alpha,\beta)$，$x=0,\ldots,n$；这是将条件二项pmf乘以Beta密度后从0到1积分，展开Beta函数即原式，区间外为0。
> (b) 本书明确默认采用式(3.2.10)的“第$r$次成功前失败次数”版本：给定$p$，$P(X=x\mid p)=\binom{x+r-1}x p^r(1-p)^x$，$x\in\mathbb N_0$。先设$r$为正整数；下式也通过Gamma系数推广到实$r>0$。积分给
> $$
> P(X=x)=\frac{\Gamma(x+r)}{\Gamma(r)x!}\frac{B(\alpha+r,\beta+x)}{B(\alpha,\beta)},\qquad x=0,1,\ldots.
> $$
> 各项非负且由条件pmf的归一化及Tonelli定理总和为1。设$s=\alpha+\beta$。条件均值$r(1-p)/p$，条件方差$r(1-p)/p^2$。Beta积分给
> $$
> E(P^{-1})=\frac{s-1}{\alpha-1}\ (\alpha>1),\qquad E(P^{-2})=\frac{(s-1)(s-2)}{(\alpha-1)(\alpha-2)}\ (\alpha>2).
> $$
> 因此
> $$
> EX=r[E(P^{-1})-1]=\frac{r\beta}{\alpha-1},\qquad \alpha>1,
> $$
> $$
> \operatorname{Var}X=r[E(P^{-2})-E(P^{-1})]+r^2[E(P^{-2})-E(P^{-1})^2]
> =\frac{r\beta(s-1)(\alpha+r-1)}{(\alpha-1)^2(\alpha-2)},\qquad\alpha>2.
> $$
> 若$\alpha\le1$，非负均值为$+\infty$，不存在有限方差；$1<\alpha\le2$均值有限而二阶矩和方差无穷。这些条件可由对应Beta积分在$p=0$附近的幂指数直接判定。
> 若改用本书另列的式(3.2.9)总试验次数$T=X+r$（$r$为正整数），则$P(T=t)=\binom{t-1}{r-1}B(\alpha+r,\beta+t-r)/B(\alpha,\beta)$，$t\ge r$，$ET=r(s-1)/(\alpha-1)$，方差相同。两种版本明确区分，主答案遵从书中默认版本。

## 相关概念

- [[01 - 概率论/概念/概率模型|概率模型]]
- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/条件概率|条件概率]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=192|印刷第161页／PDF物理第192页]]；教材信息与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。原题无星号。
- 题内引用正文已核对：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=109|印刷78／PDF109]]；[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=110|印刷79／PDF110]]；[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=168|印刷137／PDF168]]；[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=169|印刷138／PDF169]]。所需条件在解答重述，原文输入与独立补充分开。
- `source_status: verified`仅指本题题干、公式及所列来源定位已核对，不表示全章正文独立复证。解答写成不等于个人已完成练习，学习状态保持`not-started`；未实测Obsidian界面渲染。
