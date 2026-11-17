---
title: "习题 ST139：广义均值最小二乘与指数族MLE的成立条件"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "advanced"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第7章习题7.16，印刷页289／PDF物理页320"
source_id: "DS011"
source_chapter: 7
source_exercise: "7.16"
source_stars: 0
source_refs: ["DS011 Exercise 7.16，印刷289／PDF物理320", "DS011 lognormal定义与密度式(3.3.21)，印刷89／PDF物理120"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST139：广义均值最小二乘与指数族MLE的成立条件

## 题目

### 英文原题

> [!question] 英文原题
> **7.16** Berger and Casella (1992) also investigate power means, which we have seen in Exercise 4.57. Recall that a power mean is defined as $[\frac1n\sum_{i=1}^n x_i^r]^{1/r}$. This definition can be further generalized by noting that the power function $x^r$ can be replaced by any continuous, monotone function $h$, yielding the generalized mean $h^{-1}(\frac1n\sum_{i=1}^nh(x_i))$.
>
> (a) The least squares problem $\min_a\sum_i(x_i-a)^2$ is sometimes solved using transformed variables, that is, solving $\min_a\sum_i[h(x_i)-h(a)]^2$. Show that the solution to this latter problem is $a=h^{-1}((1/n)\sum_i h(x_i))$.
>
> (b) Show that the arithmetic mean is the solution to the untransformed least squares problem, the geometric mean is the solution to the problem transformed by $h(x)=\log x$, and the harmonic mean is the solution to the problem transformed by $h(x)=1/x$.
>
> (c) Show that if the least squares problem is transformed with the Box-Cox Transformation (see Exercise 11.3) then the solution is a generalized mean with $h(x)=x^\lambda$.
>
> (d) Let $X_1,X_2,\ldots,X_n$ be a sample from a lognormal$(\mu,\sigma^2)$ population. Show that the MLE of $\mu$ is the geometric mean.
>
> (e) Suppose that $X_1,X_2,\ldots,X_n$ is a sample from a one-parameter exponential family $f(x\mid\theta)=\exp\{\theta h(x)-H(\theta)\}g(x)$, where $h=H'$ and $h$ is an increasing function.
>
> i. Show that the ML estimator of $\theta$ is $\widehat\theta=h^{-1}((1/n)\sum_i h(x_i))$.
>
> ii. Show that two densities that satisfy $h=H'$ are the normal and the inverted gamma with pdf $f(x\mid\theta)=\theta x^{-2}\exp\{-\theta/x\}$ for $x>0$, and for the normal the MLE is the arithmetic mean and for the inverted gamma it is the harmonic mean.

### 中文转述

> [!question] 中文转述
> **原题7.16。** Berger和Casella（1992）还研究了习题4.57中见过的幂平均.回顾其定义为$[(1/n)\sum_{i=1}^nx_i^r]^{1/r}$.注意幂函数$x^r$可以替换为任意连续单调函数$h$，于是可进一步推广，得到广义平均$h^{-1}((1/n)\sum_{i=1}^nh(x_i))$.
>
> (a)  最小二乘问题$\min_a\sum_i(x_i-a)^2$有时通过变换变量求解，即求解$\min_a\sum_i[h(x_i)-h(a)]^2$.说明后一个问题的解为$a=h^{-1}((1/n)\sum_i h(x_i))$.
>
> (b)  说明算术平均是未变换的最小二乘问题的解；几何平均是经$h(x)=\log x$变换后问题的解；调和平均是经$h(x)=1/x$变换后问题的解.
>
> (c)  说明若用Box--Cox变换（见习题11.3）变换最小二乘问题，则解是$h(x)=x^\lambda$所对应的广义平均.
>
> (d)  设$X_1,X_2,\ldots,X_n$为来自$\operatorname{lognormal}(\mu,\sigma^2)$总体的样本.说明$\mu$的MLE为几何平均.
>
> (e)  假设$X_1,X_2,\ldots,X_n$为来自单参数指数族$f(x\mid\theta)=\exp\{\theta h(x)-H(\theta)\}g(x)$的样本，其中$h=H'$，且$h$递增.
>
> i.  说明$\theta$的极大似然估计量为$\widehat\theta=h^{-1}((1/n)\sum_i h(x_i))$.
>
> ii.  说明满足$h=H'$的两个密度是正态密度，以及pdf为$f(x\mid\theta)=\theta x^{-2}\exp\{-\theta/x\}$（$x>0$）的逆gamma密度；对于正态分布，MLE是算术平均，对于逆gamma分布，MLE是调和平均.

## 提示

> [!hint]- 提示
> 变换后的平方分解仍成立；检查原参数是对数尺度还是原尺度。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** **(a)** 为使$h^{-1}$有意义，应假定$h$在数据及$a$所在区间上连续且**严格**单调。令$\bar h=n^{-1}\sum_i h(x_i)$，平方分解为
> $$
> \sum_i[h(x_i)-h(a)]^2=\sum_i[h(x_i)-\bar h]^2+n[h(a)-\bar h]^2.
> $$
> 区间的连续像为区间，$\bar h$位于其中，所以唯一极小点为$h(a)=\bar h$。仅“单调”允许常函数或平段，原题逆函数可能不存在；那时最小解可不唯一。
>
> **(b)** $h(x)=x$给算术平均；正数据下$h(x)=\log x$给$\exp(n^{-1}\sum_i\log x_i)=(\prod_i x_i)^{1/n}$；$h(x)=1/x$给$n/\sum_i1/x_i$。
>
> **(c)** Box–Cox变换为$B_\lambda(x)=(x^\lambda-1)/\lambda$（$\lambda\ne0$）及$B_0(x)=\log x$。对$\lambda\ne0$，$B_\lambda$是$x^\lambda$的非零仿射变换，不改变变换空间平均的逆像，故解为$(n^{-1}\sum_i x_i^\lambda)^{1/\lambda}$；$\lambda=0$的解为几何平均，是该幂均值的连续极限。
>
> **(d)** 书中lognormal$(\mu,\sigma^2)$指$\log X\sim n(\mu,\sigma^2)$。令$Y_i=\log X_i$，与参数无关的Jacobian$\prod_i1/x_i$不影响似然，正态平方和最小点给$\widehat\mu=\bar Y$。因此原题“$\mu$的MLE为几何平均”按本书参数化**不成立**；几何平均估计的是$e^\mu$（亦为该分布中位数）。若另以原尺度中位数$m=e^\mu$命名参数，则其MLE才是几何平均。对未知方差还需非全等样本以取得有限的正方差MLE。
>
> **(e)i** $\ell(\theta)=\theta\sum_i h(x_i)-nH(\theta)+C$，得分为$n[\bar h-h(\theta)]$。若$h=H'$严格递增、且$\bar h\in h(\Theta)$，则$\widehat\theta=h^{-1}(\bar h)$前得分正、后负，是唯一全局MLE；若不在像内，只能检查参数边界或不存在最大值，不能直接套逆函数。
>
> **(e)ii** 对单位已知方差正态族，$h(x)=x,H(\theta)=\theta^2/2,g(x)=(2\pi)^{-1/2}e^{-x^2/2}$，因此$H'=h$，MLE为$\bar X$。给定的倒Gamma密度取$h(x)=-1/x,H(\theta)=-\log\theta,g(x)=x^{-2}$、$\theta>0$；$h$严格递增且$H'(\theta)=-1/\theta=h(\theta)$，所以MLE为$[-1/\bar h]=n/\sum_i1/X_i$，即调和平均。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=320|印刷第289页／PDF物理第320页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 原题单调函数的逆需严格性与定义域；(d)的lognormal参数化错误原样保留并另作解释。
- 英文原文、中文转述与本库独立解答分别保留；实际核对正文位置列于`source_refs`。题内文献引用不表示已查阅其原文。`source_status: verified`只指本题及所列位置的核对范围，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
