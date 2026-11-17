---
title: "习题 ST189：Bernoulli平方MLE的jackknife精确校偏与UMVU"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第7章习题7.66，印刷页297／PDF物理页328"
source_id: "DS011"
source_chapter: 7
source_exercise: "7.66"
source_stars: 0
source_refs: ["DS011 Exercise 7.66，印刷297／PDF物理328"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST189：Bernoulli平方MLE的jackknife精确校偏与UMVU

## 题目

### 英文原题

> [!question] 英文原题
> **7.66** The jackknife is a general technique for reducing bias in an estimator (Quenouille 1956). A one-step jackknife estimator is defined as follows. Let $X_1,\ldots,X_n$ be a random sample, and let $T_n=T_n(X_1,\ldots,X_n)$ be some estimator of a parameter $\theta$. In order to “jackknife” $T_n$ we calculate the $n$ statistics $T_n^{(i)}$, $i=1,\ldots,n$, where $T_n^{(i)}$ is calculated just as $T_n$ but using the $n-1$ observations with $X_i$ removed from the sample. The jackknife estimator of $\theta$, denoted by $\operatorname{JK}(T_n)$, is given by
> $$
> \operatorname{JK}(T_n)=nT_n-\frac{n-1}{n}\sum_{i=1}^nT_n^{(i)}.
> $$
> (In general, $\operatorname{JK}(T_n)$ will have a smaller bias than $T_n$. See Miller (1974) for a good review of the properties of the jackknife.)
>
> Now, to be specific, let $X_1,\ldots,X_n$ be iid Bernoulli$(\theta)$. The object is to estimate $\theta^2$.
>
> (a) Show that the MLE of $\theta^2$, $(\sum_{i=1}^nX_i/n)^2$, is a biased estimator of $\theta^2$.
>
> (b) Derive the one-step jackknife estimator based on the MLE.
>
> (c) Show that the one-step jackknife estimator is an unbiased estimator of $\theta^2$. (In general, jackknifing only reduces bias. In this special case, however, it removes it entirely.)
>
> (d) Is this jackknife estimator the best unbiased estimator of $\theta^2$? If so, prove it. If not, find the best unbiased estimator.

### 中文转述

> [!question] 中文转述
> **原题7.66。** 刀切法（jackknife）是减少估计量偏差的一种一般方法（Quenouille 1956）.一步刀切估计量定义如下.设$X_1,\ldots,X_n$为随机样本，$T_n=T_n(X_1,\ldots,X_n)$为参数$\theta$的某个估计量.为对$T_n$实施“刀切”，我们计算$n$个统计量$T_n^{(i)}$，$i=1,\ldots,n$；$T_n^{(i)}$的计算方法与$T_n$相同，但使用从样本中去掉$X_i$后剩下的$n-1$个观测.$\theta$的刀切估计量记为$\operatorname{JK}(T_n)$，定义为
>
> $$
> \operatorname{JK}(T_n)=nT_n-\frac{n-1}{n}\sum_{i=1}^nT_n^{(i)}.
> $$
>
> （一般说来，$\operatorname{JK}(T_n)$的偏差比$T_n$小.Miller（1974）对刀切法的性质作了很好的综述.）
>
> 具体地，现设$X_1,\ldots,X_n$独立同分布于$\operatorname{Bernoulli}(\theta)$.目标是估计$\theta^2$.
>
> (a)  说明$\theta^2$的MLE，$(\sum_{i=1}^nX_i/n)^2$，是$\theta^2$的有偏估计量.
>
> (b)  推导基于MLE的一步刀切估计量.
>
> (c)  说明一步刀切估计量是$\theta^2$的无偏估计量.（一般说来，刀切仅能减小偏差，但在这一特殊情形中，它完全消除了偏差.）
>
> (d)  这个刀切估计量是$\theta^2$的最佳无偏估计量吗？若是，请证明；若不是，请求出最佳无偏估计量.

## 提示

> [!hint]- 提示
> 删一项后的平方和可用$X_i^2=X_i$整体化简。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 取$n\ge2$、$S=\sum_iX_i\sim\operatorname{binomial}(n,\theta)$。
>
> **(a)** $E(S/n)^2=\theta^2+\theta(1-\theta)/n$，故内部参数$0<\theta<1$时正偏，端点偏差为0。MLE不变性给目标$\theta^2$的MLE为$(S/n)^2$。
>
> **(b)** 删去第$i$项后的规则为$T_n^{(i)}=(S-X_i)^2/(n-1)^2$。利用$X_i^2=X_i$，
> $$
> \sum_i(S-X_i)^2=(n-2)S^2+S.
> $$
> 因此
> $$
> \operatorname{JK}(T_n)=\frac{S^2}{n}-\frac{(n-2)S^2+S}{n(n-1)}
> =\frac{S(S-1)}{n(n-1)}.
> $$
> **(c)** $S(S-1)=\sum_{i\ne j}X_iX_j$，每一异序乘积期望$\theta^2$，共$n(n-1)$项，所以该规则处处无偏。
>
> **(d)** $S$是充分二项总数，完备性由零期望产生的多项式逐系数为零直接证明；所给jackknife是其函数且有界、无偏，故为唯一最佳无偏估计。也可以先用$X_1X_2$无偏，再在$S$条件下得到同一规则，直接展示Rao–Blackwell化。此例完全消偏是二次目标与Bernoulli结构的特殊结果，不能推广成所有jackknife均精确无偏。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=328|印刷第297页／PDF物理第328页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 英文原文、中文转述与本库独立解答分别保留；实际核对正文位置列于`source_refs`。题内文献引用不表示已查阅其原文。`source_status: verified`只指本题及所列位置的核对范围，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
