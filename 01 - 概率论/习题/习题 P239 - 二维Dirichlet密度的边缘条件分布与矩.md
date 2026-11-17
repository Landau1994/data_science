---
title: "习题 P239：二维Dirichlet密度的边缘条件分布与矩"
topic: "probability-theory"
topic_label: "概率论"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "probability-theory"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第4章习题4.40，印刷页162–163／PDF物理页193–194"
source_id: "DS011"
source_chapter: 4
source_exercise: "4.40"
source_stars: 0
source_refs: ["DS011 Exercise 4.40，印刷162–163／PDF物理193–194"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 P239：二维Dirichlet密度的边缘条件分布与矩

## 题目

### 英文原题

> [!question] 英文原题
> **4.40** A generalization of the beta distribution is the Dirichlet distribution. In its bivariate version, $(X,Y)$ have pdf
> $$
> f(x,y)=Cx^{a-1}y^{b-1}(1-x-y)^{c-1},\quad0<x<1,\quad0<y<1,\quad0<y<1-x<1,
> $$
> where $a>0,b>0,$ and $c>0$ are constants.
> (a) Show that $C=\Gamma(a+b+c)/(\Gamma(a)\Gamma(b)\Gamma(c))$.
> (b) Show that, marginally, both $X$ and $Y$ are beta.
> (c) Find the conditional distribution of $Y\mid X=x$, and show that $Y/(1-x)$ is beta$(b,c)$.
> (d) Show that $E(XY)=ab/((a+b+c+1)(a+b+c))$, and find their covariance.

### 中文转述

> [!question] 中文转述
> **原题4.40。**
> Beta 分布的一个推广是 Dirichlet 分布. 在二元版本中，$(X,Y)$ 的 pdf 为
>
> $$
> f(x,y)=Cx^{a-1}y^{b-1}(1-x-y)^{c-1},\quad0<x<1,\quad0<y<1,\quad0<y<1-x<1,
> $$
>
> 其中 $a,b,c$ 为正的常数.
>
> (a)  证明 $C=\Gamma(a+b+c)/(\Gamma(a)\Gamma(b)\Gamma(c))$.
>
> (b)  证明 $X,Y$ 的边缘分布都是 Beta 分布.
>
> (c)  求 $Y\mid X=x$ 的条件分布，并证明 $Y/(1-x)$ 服从 $\operatorname{beta}(b,c)$.
>
> (d)  证明 $E(XY)=ab/((a+b+c+1)(a+b+c))$，并求协方差.

## 提示

> [!hint]- 提示
> 内层积分置$y=(1-x)t$，所有归一化与矩都变为Beta积分。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 记$s=a+b+c$，支持为$x>0,y>0,x+y<1$。
> (a) 未归一化积分为$\int_0^1x^{a-1}(1-x)^{b+c-1}B(b,c)dx=B(a,b+c)B(b,c)=\Gamma(a)\Gamma(b)\Gamma(c)/\Gamma(s)$，故$C$为其倒数。
> (b) 对$y$积分得$f_X(x)=x^{a-1}(1-x)^{b+c-1}/B(a,b+c)$，故$X\sim\operatorname{Beta}(a,b+c)$；对称得$Y\sim\operatorname{Beta}(b,a+c)$。
> (c) 比值$f(x,y)/f_X(x)$给
> $$
> f_{Y\mid X}(y\mid x)=\frac1{(1-x)B(b,c)}\left(\frac y{1-x}\right)^{b-1}\left(1-\frac y{1-x}\right)^{c-1},\quad0<y<1-x.
> $$
> 因此给定$x$，$Y/(1-x)$为Beta$(b,c)$，条件分布不依赖$x$；积分条件分布后，无条件$Y/(1-X)$也同为Beta$(b,c)$，并与$X$独立。
> (d) 在归一化积分中把$a,b$各加1，得$E(XY)=ab/[s(s+1)]$；$EX=a/s,EY=b/s$，所以$\operatorname{Cov}(X,Y)=-ab/[s^2(s+1)]$。

## 相关概念

- [[01 - 概率论/概念/概率模型|概率模型]]
- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/条件概率|条件概率]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=193|印刷第162页／PDF物理第193页]]及续页194；教材信息与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。原题无星号。
- `source_status: verified`仅指本题题干、公式及所列来源定位已核对，不表示全章正文独立复证。解答写成不等于个人已完成练习，学习状态保持`not-started`；未实测Obsidian界面渲染。
