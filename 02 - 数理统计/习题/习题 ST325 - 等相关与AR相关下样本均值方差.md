---
title: 习题 ST325：等相关与AR相关下样本均值方差
topic: mathematical-statistics
topic_label: 数理统计
difficulty: advanced
status: not-started
tags:
- exercise
- mathematical-statistics
source: George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第10章习题10.19，印刷页411／PDF物理页442
source_id: DS011
source_chapter: 10
source_exercise: '10.19'
source_stars: 0
source_refs:
- DS011 Exercise 10.19，印刷411／PDF物理442
- DS011题内依赖核对：印刷389／PDF物理420
source_status: verified
solution_status: independently-derived
created: '2026-11-13'
---

# 习题 ST325：等相关与AR相关下样本均值方差

## 题目

### 英文原题

> [!question] 英文原题
> **10.19** Another way in which underlying assumptions can be violated is if there is correlation in the sampling, which can seriously effect the properties of the sample mean. Suppose we introduce correlation in the case discussed in Exercise 10.2.1, that is, we observe $X_1,X_2,\ldots,X_n$ where $X_i\sim\operatorname n(\theta,\sigma^2)$, but the $X_i$s are no longer independent.
>
> (a) For the equicorrelated case, that is, $\operatorname{Corr}(X_i,X_j)=\rho$ for $i\ne j$, show that
> $$
> \operatorname{Var}(\bar X)=\frac{\sigma^2}n+\frac{n-1}n\rho\sigma^2,
> $$
> so $\operatorname{Var}(\bar X)\not\to0$ as $n\to\infty$.
>
> (b) If the $X_i$s are observed through time (or distance), it is sometimes assumed that the correlation decreases with time (or distance), with one specific model being $\operatorname{Corr}(X_i,X_j)=\rho^{|i-j|}$. Show that in this case
> $$
> \operatorname{Var}(\bar X)=\frac{\sigma^2}n+\frac{2\sigma^2}{n^2}\frac\rho{1-\rho}\left(n+\frac{1-\rho^n}{1-\rho}\right),
> $$
> so $\operatorname{Var}(\bar X)\to0$ as $n\to\infty$. (See Miscellanea 5.8.2 for another effect of correlation.)
>
> (c) The correlation structure in part (b) arises in an autoregressive AR(1) model, where we assume that $X_{i+1}=\rho X_i+\delta_i$, with $\delta_i$ iid $\operatorname n(0,1)$. If $|\rho|<1$, and we define $\sigma^2=1/(1-\rho^2)$, show that $\operatorname{Corr}(X_1,X_i)=\rho^{i-1}$.

### 中文转述

> [!question] 中文转述
> **原题10.19。** 基础假设还可能因抽样中的相关性而被违反，这会严重影响样本均值的性质. 假设在习题10.2.1所讨论的情形中引入相关性，即观测$X_1,X_2,\ldots,X_n$，各$X_i\sim\mathrm n(\theta,\sigma^2)$，但不再独立.
>
> (a)  对等相关情形，即$i\ne j$时$\operatorname{Corr}(X_i,X_j)=\rho$，证明
>
> $$
> \operatorname{Var}(\bar X)=\frac{\sigma^2}n+\frac{n-1}n\rho\sigma^2,
> $$
>
> 因此$n\to\infty$时$\operatorname{Var}(\bar X)\not\to0$.
>
> (b)  若沿时间（或距离）观测$X_i$，有时假设相关性随时间（或距离）减小，一个具体模型是$\operatorname{Corr}(X_i,X_j)=\rho^{|i-j|}$. 证明在这种情形下
>
> $$
> \operatorname{Var}(\bar X)=\frac{\sigma^2}n+\frac{2\sigma^2}{n^2}\frac\rho{1-\rho}\left(n+\frac{1-\rho^n}{1-\rho}\right),
> $$
>
> 所以$n\to\infty$时$\operatorname{Var}(\bar X)\to0$. （相关性的另一影响见杂录5.8.2.）
>
> (c)  (b)的相关结构出现在自回归AR(1)模型（autoregressive AR(1) model）中，假设$X_{i+1}=\rho X_i+\delta_i$，其中$\delta_i$独立同分布于$\mathrm n(0,1)$. 若$|\rho|<1$，定义$\sigma^2=1/(1-\rho^2)$，证明$\operatorname{Corr}(X_1,X_i)=\rho^{i-1}$.

## 提示

> [!hint]- 提示
> 从所有协方差求和；n=1即可发现原(b)加号产生不应有的协方差项。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** **(a)** $\operatorname{Var}\bar X=n^{-2}[n\sigma^2+n(n-1)\rho\sigma^2]$，即原式。固定$\rho>0$时极限为$\rho\sigma^2$，不趋0；$\rho=0$时则趋0，原笼统结论需排除此情形。等相关矩阵特征值为$1-\rho$和$1+(n-1)\rho$，固定$n$需$-1/(n-1)\le\rho\le1$；要让固定$\rho$对任意$n$均合法，需$0\le\rho\le1$。
>
> **(b)** 协方差按间隔$h$有$n-h$对，故
> $$
> \operatorname{Var}\bar X=\frac{\sigma^2}n+\frac{2\sigma^2}{n^2}\sum_{h=1}^{n-1}(n-h)\rho^h.
> $$
> 对$\rho\ne1$，由几何和及其导数，
> $$
> \sum_{h=1}^{n-1}(n-h)\rho^h=\frac\rho{1-\rho}\left[n-\frac{1-\rho^n}{1-\rho}\right].
> $$
> 原括号中的**加号错误，应为减号**；$n=1$时正确和为0，而原式通常非0。若$|\rho|<1$，和的绝对值至多$n\sum_{h\ge1}|\rho|^h=O(n)$，所以方差$O(1/n)\to0$，更精确首项为$\sigma^2(1+\rho)/[n(1-\rho)]$。$\rho=1$时所有值完全正相关，方差$\sigma^2$不趋0，必须排除。
>
> **(c)** 还需平稳初值$X_1\sim N(0,\sigma^2)$独立于全部后续创新，$\sigma^2=1/(1-\rho^2)$。递推得$X_i=\rho^{i-1}X_1+\sum_{j=1}^{i-1}\rho^{i-1-j}\delta_j$，因此$\operatorname{Cov}(X_1,X_i)=\rho^{i-1}\sigma^2$，且$\operatorname{Var}X_i=\rho^{2(i-1)}\sigma^2+\sum_{j=0}^{i-2}\rho^{2j}=\sigma^2$，除以标准差积得到所求。若初值方差任意，相关系数一般不同；非零平稳均值需在递推中加$(1-\rho)\theta$截距，原无截距递推的平稳均值是0。

## 相关概念

- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/期望|期望]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[02 - 数理统计/概念/参数估计|参数估计]]

## 备注

- 来源：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=442|印刷第411页／PDF物理第442页]]；版本与归档见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 原(b)错误加号及(c)遗漏的初值/独立条件原样保留，修正明确在解答中。
- 已实读本题所用正文：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=420|印刷389／PDF物理420]]；其余题内外部文献仅保留原引用，未声称查阅。
- 英文原题逐题对照PDF原始页面，保留原分题、提示、引用及可见疑误；原题无星号。题内引用补充与独立解答不混入原文；未查阅答案册或题内外部文献。
- 来源核对不表示个人学习完成，学习状态保持not-started。公式、链接与元数据检查不等于Obsidian实际渲染检查。
