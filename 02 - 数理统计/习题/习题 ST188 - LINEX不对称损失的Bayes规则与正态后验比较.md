---
title: "习题 ST188：LINEX不对称损失的Bayes规则与正态后验比较"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "advanced"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第7章习题7.65，印刷页297／PDF物理页328"
source_id: "DS011"
source_chapter: 7
source_exercise: "7.65"
source_stars: 0
source_refs: ["DS011 Exercise 7.65，印刷297／PDF物理328"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST188：LINEX不对称损失的Bayes规则与正态后验比较

## 题目

### 英文原题

> [!question] 英文原题
> **7.65** A loss function investigated by Zellner (1986) is the LINEX (LINear–EXponential) loss, a loss function that can handle asymmetries in a smooth way. The LINEX loss is given by
> $$
> L(\theta,a)=e^{c(a-\theta)}-c(a-\theta)-1,
> $$
> where $c$ is a positive constant. As the constant $c$ varies, the loss function varies from very asymmetric to almost symmetric.
>
> (a) For $c=.2,.5,1$, plot $L(\theta,a)$ as a function of $a-\theta$.
>
> (b) If $X\sim F(x\mid\theta)$, show that the Bayes estimator of $\theta$, using a prior $\pi$, is given by $\delta^\pi(X)=-\frac1c\log E(e^{-c\theta}\mid X)$.
>
> (c) Let $X_1,\ldots,X_n$ be iid $n(\theta,\sigma^2)$, where $\sigma^2$ is known, and suppose that $\theta$ has the noninformative prior $\pi(\theta)=1$. Show that the Bayes estimator versus LINEX loss is given by $\delta^B(\bar X)=\bar X-(c\sigma^2/(2n))$.
>
> (d) Calculate the posterior expected loss for $\delta^B(\bar X)$ and $\bar X$ using LINEX loss.
>
> (e) Calculate the posterior expected loss for $\delta^B(\bar X)$ and $\bar X$ using squared error loss.

### 中文转述

> [!question] 中文转述
> **原题7.65。** Zellner（1986）研究的一种损失函数是LINEX（LINear--EXponential，线性—指数）损失，它能以光滑方式处理非对称性.LINEX损失为
>
> $$
> L(\theta,a)=e^{c(a-\theta)}-c(a-\theta)-1,
> $$
>
> 其中$c$是正常数.随着$c$变化，损失函数可以从极不对称变为近乎对称.
>
> (a)  对$c=.2,.5,1$，将$L(\theta,a)$作为$a-\theta$的函数作图.
>
> (b)  若$X\sim F(x\mid\theta)$，证明采用先验$\pi$时，$\theta$的贝叶斯估计量为$\delta^\pi(X)=-(1/c)\log E(e^{-c\theta}\mid X)$.
>
> (c)  设$X_1,\ldots,X_n$独立同分布于$n(\theta,\sigma^2)$，其中$\sigma^2$已知，并设$\theta$具有无信息先验$\pi(\theta)=1$.证明LINEX损失下的贝叶斯估计量为$\delta^B(\boldsymbol X)=\bar X-c\sigma^2/(2n)$.
>
> (d)  在LINEX损失下，计算$\delta^B(\boldsymbol X)$与$\bar X$的后验期望损失.
>
> (e)  在平方误差损失下，计算$\delta^B(\boldsymbol X)$与$\bar X$的后验期望损失.

## 提示

> [!hint]- 提示
> 先对后验期望损失求导；正态指数矩会产生一个明确的向下平移。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 令误差$d=a-\theta$、$c>0$。
>
> **(a)** $L(d)=e^{cd}-cd-1\ge0$，$L'(d)=c(e^{cd}-1)$，$L''(d)=c^2e^{cd}>0$，唯一最小点$d=0$。正误差有指数增长，负误差远端为近似线性增长；小$cd$时$L(d)=c^2d^2/2+c^3d^3/6+\cdots$，所以较小$c$在同一误差区间内更接近对称二次形。三条精确公式的图及最小点附近放大如下。
>
> ![[附件/习题图/DS011/习题7.65-LINEX损失曲线.png]]
>
> **(b)** 设给定数据后$0<C=E(e^{-c\theta}\mid X)<\infty$且$E(|\theta|\mid X)<\infty$，以保证后验期望损失有限。它等于$\rho(a)=e^{ca}C-ca+cE(\theta\mid X)-1$。导数$\rho'(a)=c(e^{ca}C-1)$、二阶导数$c^2e^{ca}C>0$，所以唯一最小点为$a_*=-c^{-1}\log C$。后验指数矩发散时原有限公式不适用。
>
> **(c)** $\pi(\theta)=1$是非正常先验，严格说得到的是广义Bayes（generalized Bayes）规则；正态似然仍给正常后验$\theta\mid\mathbf X\sim n(z,v)$，$z=\bar X,v=\sigma^2/n$。其指数矩$C=e^{-cz+c^2v/2}$，所以$\delta^B=z-cv/2=\bar X-c\sigma^2/(2n)$。
>
> **(d)** 对任意行动$a$，正态后验期望LINEX损失为$e^{c(a-z)+c^2v/2}-c(a-z)-1$。因此
> $$
> \rho_{LINEX}(\delta^B)=c^2v/2,\qquad
> \rho_{LINEX}(z)=e^{c^2v/2}-1.
> $$
> 因为$e^u-1>u$对$u>0$成立，前者严格小；这里$c,v>0$。
>
> **(e)** 平方损失后验风险为$v+(a-z)^2$，所以
> $$
> \rho_{SE}(\delta^B)=v+c^2v^2/4,\qquad\rho_{SE}(z)=v.
> $$
> 平方损失下后验均值严格更好；两个不同损失的最优行动不同，不能把(d)的优劣直接沿用到(e)。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=328|印刷第297页／PDF物理第328页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 非正常平坦先验明确按广义Bayes处理。图为独立构造，保留[[工具/StatisticalInference/ch07-figures/exercise-7-65.tex|可编辑TeX]]与[[附件/习题图/DS011/习题7.65-LINEX损失曲线.pdf|矢量PDF]]，已核对参数、最小点与实际渲染。
- 英文原文、中文转述与本库独立解答分别保留；实际核对正文位置列于`source_refs`。题内文献引用不表示已查阅其原文。`source_status: verified`只指本题及所列位置的核对范围，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
