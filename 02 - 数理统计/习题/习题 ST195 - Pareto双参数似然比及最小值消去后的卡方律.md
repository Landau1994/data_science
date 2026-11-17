---
title: "习题 ST195：Pareto双参数似然比及最小值消去后的卡方律"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "advanced"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第8章习题8.5，印刷页326、327／PDF物理页357、358"
source_id: "DS011"
source_chapter: 8
source_exercise: "8.5"
source_stars: 0
source_refs: ["DS011 Exercise 8.5，印刷页326、327／PDF物理页357、358"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST195：Pareto双参数似然比及最小值消去后的卡方律

## 题目

### 英文原题

> [!question] 英文原题
> **8.5** A random sample, $X_1,\ldots,X_n$, is drawn from a Pareto population with pdf
> $$f(x\mid\theta,\nu)=\frac{\theta\nu^\theta}{x^{\theta+1}}I_{[\nu,\infty)}(x),\quad\theta>0,\quad\nu>0.$$
> (a) Find the MLEs of $\theta$ and $\nu$.
> (b) Show that the LRT of
> $$H_0:\theta=1,\ \nu\text{ unknown}\quad\text{versus}\quad H_1:\theta\ne1,\ \nu\text{ unknown},$$
> has critical region of the form $\{\boldsymbol x:T(\boldsymbol x)\le c_1\text{ or }T(\boldsymbol x)\ge c_2\}$, where $0<c_1<c_2$ and
> $$T=\log\left[\frac{\prod_{i=1}^nX_i}{(\min_iX_i)^n}\right].$$
> (c) Show that, under $H_0$, $2T$ has a chi squared distribution, and find the number of degrees of freedom. (Hint: Obtain the joint distribution of the $n-1$ nontrivial terms $X_i/(\min_iX_i)$ conditional on $\min_iX_i$. Put these $n-1$ terms together, and notice that the distribution of $T$ given $\min_iX_i$ does not depend on $\min_iX_i$, so it is the unconditional distribution of $T$.)

### 中文转述

> [!question] 中文转述
> **原题8.5。**
> 随机样本 $X_1,\ldots,X_n$ 来自 Pareto 总体，其密度为
>
> $$
> f(x\mid\theta,\nu)=\frac{\theta\nu^\theta}{x^{\theta+1}}I_{[\nu,\infty)}(x),\qquad\theta>0,\quad\nu>0.
> $$
>
> (a)  求 $\theta$ 与 $\nu$ 的最大似然估计量.
>
> (b)  证明，检验
>
> $$
> H_0:\theta=1,\ \nu\text{ 未知}\quad\text{对}\quad H_1:\theta\ne1,\ \nu\text{ 未知}
> $$
>
> 的似然比检验具有形如 $\{\boldsymbol x:T(\boldsymbol x)\le c_1\text{ 或 }T(\boldsymbol x)\ge c_2\}$ 的临界域，其中 $0<c_1<c_2$，且
>
> $$
> T=\log\left[\frac{\prod_{i=1}^nX_i}{(\min_iX_i)^n}\right].
> $$
>
> (c)  证明，在 $H_0$ 下，$2T$ 服从卡方分布，并求自由度. （提示：给定 $\min_iX_i$，求 $n-1$ 个非平凡项 $X_i/(\min_iX_i)$ 的联合分布. 将这 $n-1$ 项合并，并注意到给定 $\min_iX_i$ 后 $T$ 的分布不依赖 $\min_iX_i$，因而也就是 $T$ 的无条件分布.）

## 提示

> [!hint]- 提示
> 先对支持端点最大化，再将对数样本化为指数变量。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 以下$n\ge2$且样本不全相同（连续模型下概率1）。记$M=\min_iX_i$、$T=\sum_i\log(X_i/M)>0$。
> (a) $L=\theta^n\nu^{n\theta}\prod_iX_i^{-\theta-1}$，$0<\nu\le M$，对$\nu$递增，故$\hat\nu=M$。剖面对数似然除常数为$n\log\theta-\theta T$，严格凹，得到$\hat\theta=n/T$。
> (b) 在$\theta=1$下仍取$\nu=M$，相除得$\lambda(T)=(T/n)^n e^{n-T}$。其对数导数$n/T-1$先正后负，最大值1在$T=n$。故$0<c<1$的小似然比域为$T\le c_1$或$T\ge c_2$，其中$c_1<n<c_2$且$\lambda(c_1)=\lambda(c_2)=c$。给定大小$\alpha$，用(c)的Gamma分布选$c$使两尾总概率为$\alpha$；不能任意等分尾概率并仍称同一个LRT。
> (c) 在$H_0$下，$Z_i=\log(X_i/\nu)$独立尺度1指数变量。给定最小值$Z_{(1)}=z$及唯一最小者的下标，其余$n-1$个残差$Z_i-z$由无记忆性独立为尺度1指数：联合条件密度为$\prod_{i\ne j}e^{-w_i}$，$w_i>0$，不依赖$z$或$j$。因此$T=\sum_i(Z_i-Z_{(1)})\sim\operatorname{Gamma}(n-1,1)$，$2T\sim\chi^2_{2n-2}$。对应比值$X_i/M=e^{w_i}$条件独立Pareto$(1,1)$，满足原Hint。
> 若$n=1$或样本全相等，$T=0$而$\theta^n$可无限增大，有限MLE不存在，不能套$\hat\theta=n/T$或正自由度卡方结论。

## 相关概念

- [[02 - 数理统计/概念/假设检验|假设检验（hypothesis testing）]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[01 - 概率论/概念/条件概率|条件概率]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 完整原题已逐页对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=357|印刷326／PDF物理357]]、[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=358|印刷327／PDF物理358]]；原题无星号。教材信息及归档进度见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 来源已核对与独立解答写成不等于个人已完成练习；学习状态保留`not-started`。未实测Obsidian界面渲染。
