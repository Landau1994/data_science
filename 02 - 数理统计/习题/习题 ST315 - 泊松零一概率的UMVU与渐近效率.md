---
title: 习题 ST315：泊松零一概率的UMVU与渐近效率
topic: mathematical-statistics
topic_label: 数理统计
difficulty: advanced
status: not-started
tags:
- exercise
- mathematical-statistics
source: George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第10章习题10.9，印刷页409／PDF物理页440
source_id: DS011
source_chapter: 10
source_exercise: '10.9'
source_stars: 0
source_refs:
- DS011 Exercise 10.9，印刷409／PDF物理440
- DS011题内依赖核对：印刷384／PDF物理415
source_status: verified
solution_status: independently-derived
created: '2026-11-13'
---

# 习题 ST315：泊松零一概率的UMVU与渐近效率

## 题目

### 英文原题

> [!question] 英文原题
> **10.9** Suppose that $X_1,\ldots,X_n$ are iid Poisson$(\lambda)$. Find the best unbiased estimator of
>
> (a) $e^{-\lambda}$, the probability that $X=0$.
>
> (b) $\lambda e^{-\lambda}$, the probability that $X=1$.
>
> (c) For the best unbiased estimators of parts (a) and (b), calculate the asymptotic relative efficiency with respect to the MLE. Which estimators do you prefer? Why?
>
> (d) A preliminary test of a possible carcinogenic compound can be performed by measuring the mutation rate of microorganisms exposed to the compound. An experimenter places the compound in 15 petri dishes and records the following number of mutant colonies:
> $$
> 10,7,8,13,8,9,5,7,6,8,3,6,6,3,5.
> $$
> Estimate $e^{-\lambda}$, the probability that no mutant colonies emerge, and $\lambda e^{-\lambda}$, the probability that one mutant colony will emerge. Calculate both the best unbiased estimator and the MLE.

### 中文转述

> [!question] 中文转述
> **原题10.9。** 假设$X_1,\ldots,X_n$独立同分布于Poisson$(\lambda)$. 求以下各量的最佳无偏估计量：
>
> (a)  $e^{-\lambda}$，即$X=0$的概率.
>
> (b)  $\lambda e^{-\lambda}$，即$X=1$的概率.
>
> (c)  对(a)和(b)的最佳无偏估计量，计算相对于MLE的渐近相对效率. 你更倾向于哪些估计量？为什么？
>
> (d)  测量暴露于某种化合物的微生物突变率，可以对该化合物可能的致癌性进行初步检验. 实验者将化合物放入15个培养皿，记录到以下突变菌落数：
>
> $$
> 10,7,8,13,8,9,5,7,6,8,3,6,6,3,5.
> $$
>
> 估计没有突变菌落出现的概率$e^{-\lambda}$，以及出现一个突变菌落的概率$\lambda e^{-\lambda}$. 分别计算最佳无偏估计与MLE.

## 提示

> [!hint]- 提示
> 条件于完全充分的总计数T，单个计数服从Bin(T,1/n)。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 设$T=\sum_iX_i\sim\operatorname{Poi}(n\lambda)$。联合PMF因子分解给$T$充分。若$E_\lambda h(T)=0$对所有$\lambda>0$成立，则幂级数$\sum_{t\ge0}h(t)(n\lambda)^t/t!$在正区间为0，各系数为0，故$T$完全。这里期望存在保证相应幂级数的局部绝对收敛。由条件多项分配，$X_1\mid T\sim\operatorname{Bin}(T,1/n)$。
>
> **(a)** 对无偏指标$I(X_1=0)$作Rao–Blackwell，得到$U_0=(1-1/n)^T$，完全性保证其为唯一UMVU。
>
> **(b)** 同理$U_1=(T/n)(1-1/n)^{T-1}$，$T=0$时定义0。$n=1$时应直接取$U_0=I(T=0),U_1=I(T=1)$，避免$0\cdot0^{-1}$。
>
> **(c)** MLE为$M_0=e^{-T/n},M_1=(T/n)e^{-T/n}$。当$n\to\infty$，在固定$\lambda>0$处，$\log(1-1/n)=-1/n-1/(2n^2)+O(n^{-3})$且$T=O_p(n)$，可得$U_j-M_j=O_p(1/n)$。所以二者同一一阶正态极限：$\sqrt n(U_0-e^{-\lambda})\Rightarrow N(0,\lambda e^{-2\lambda})$；对$\lambda\ne1$，$\sqrt n(U_1-\lambda e^{-\lambda})\Rightarrow N(0,\lambda(1-\lambda)^2e^{-2\lambda})$。相对MLE的ARE均1。在$\lambda=1$第二项一阶退化，须二阶比较：$n(M_1-e^{-1})\Rightarrow-e^{-1}Z^2/2$，$n(U_1-e^{-1})\Rightarrow-e^{-1}(Z^2-1)/2$，两者二阶方差相同但偏差不同，不能把一阶0/0当作通常ARE。若重视无偏且计算同样简单，倾向UMVU；MLE仍有同一常规一阶效率，不能仅凭UMVU声称对所有有偏估计都有最小MSE。
>
> **(d)** 数据总和$T=104$、$n=15$，所以$\hat\lambda=104/15$。四个估计为
> $$
> U_0=(14/15)^{104},\quad M_0=e^{-104/15},\quad U_1=\frac{104}{15}(14/15)^{103},\quad M_1=\frac{104}{15}e^{-104/15}.
> $$
> 实际计算$U_0=0.000765287763$、$M_0=0.000974746293$、$U_1=0.005684994808$、$M_1=0.006758240963$。
> 这些只是指定泊松模型下的菌落概率估计，本题并未提供对照组以推断化合物的因果致癌效应。

## 相关概念

- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/期望|期望]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[02 - 数理统计/概念/参数估计|参数估计]]

## 备注

- 来源：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=440|印刷第409页／PDF物理第440页]]；版本与归档见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 已实读本题所用正文：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=415|印刷384／PDF物理415]]；其余题内外部文献仅保留原引用，未声称查阅。
- 英文原题逐题对照PDF原始页面，保留原分题、提示、引用及可见疑误；原题无星号。题内引用补充与独立解答不混入原文；未查阅答案册或题内外部文献。
- 来源核对不表示个人学习完成，学习状态保持not-started。公式、链接与元数据检查不等于Obsidian实际渲染检查。
