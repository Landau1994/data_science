---
title: "习题 ST185：正态线性估计的频率风险与正态先验Bayes风险"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第7章习题7.62，印刷页297／PDF物理页328"
source_id: "DS011"
source_chapter: 7
source_exercise: "7.62"
source_stars: 0
source_refs: ["DS011 Exercise 7.62，印刷297／PDF物理328", "DS011 例7.2.16正态后验式(7.2.10)，印刷263／PDF物理294"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST185：正态线性估计的频率风险与正态先验Bayes风险

## 题目

### 英文原题

> [!question] 英文原题
> **7.62** Let $X_1,\ldots,X_n$ be a random sample from a $n(\theta,\sigma^2)$ population, $\sigma^2$ known. Consider estimating $\theta$ using squared error loss. Let $\pi(\theta)$ be a $n(\mu,\tau^2)$ prior distribution on $\theta$ and let $\delta^\pi$ be the Bayes estimator of $\theta$. Verify the following formulas for the risk function and Bayes risk.
>
> (a) For any constants $a$ and $b$, the estimator $\delta(\mathbf x)=a\bar X+b$ has risk function
> $$
> R(\theta,\delta)=a^2\frac{\sigma^2}{n}+[b-(1-a)\theta]^2.
> $$
> (b) Let $\eta=\sigma^2/(n\tau^2+\sigma^2)$. The risk function for the Bayes estimator is
> $$
> R(\theta,\delta^\pi)=(1-\eta)^2\frac{\sigma^2}{n}+\eta^2(\theta-\mu)^2.
> $$
> (c) The Bayes risk for the Bayes estimator is
> $$
> B(\pi,\delta^\pi)=\tau^2\eta.
> $$

### 中文转述

> [!question] 中文转述
> **原题7.62。** 设$X_1,\ldots,X_n$是来自$n(\theta,\sigma^2)$总体的随机样本，$\sigma^2$已知.考虑在平方误差损失下估计$\theta$.令$\pi(\theta)$为$\theta$的$n(\mu,\tau^2)$先验分布，$\delta^\pi$为$\theta$的贝叶斯估计量.验证下列风险函数与贝叶斯风险公式.
>
> (a)  对任意常数$a,b$，估计量$\delta(\boldsymbol x)=a\bar X+b$的风险函数为
>
> $$
> R(\theta,\delta)=a^2\frac{\sigma^2}{n}+(b-(1-a)\theta)^2.
> $$
>
> (b)  令$\eta=\sigma^2/(n\tau^2+\sigma^2)$.贝叶斯估计量的风险函数为
>
> $$
> R(\theta,\delta^\pi)=(1-\eta)^2\frac{\sigma^2}{n}+\eta^2(\theta-\mu)^2.
> $$
>
> (c)  贝叶斯估计量的贝叶斯风险为$B(\pi,\delta^\pi)=\tau^2\eta$.

## 提示

> [!hint]- 提示
> 区分固定参数的风险与再对先验平均的Bayes风险。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 令$v=\sigma^2/n>0$、$\tau^2>0$。
>
> **(a)** 在固定真实参数$\theta$下，$E_\theta\delta-\theta=(a-1)\theta+b$、$\operatorname{Var}_\theta\delta=a^2v$。均方误差分解为方差加偏差平方，恰得$R=a^2v+[b-(1-a)\theta]^2$。
>
> **(b)** 正态后验配方给$E(\theta\mid\mathbf X)=[\tau^2\bar X+v\mu]/(\tau^2+v)$。平方损失的后验均值最优，因为$E[(a-\theta)^2\mid X]=\operatorname{Var}(\theta\mid X)+(a-E(\theta\mid X))^2$。令$\eta=v/(\tau^2+v)$，则$\delta^\pi=(1-\eta)\bar X+\eta\mu$，代入(a)即得$R=(1-\eta)^2v+\eta^2(\theta-\mu)^2$。
>
> **(c)** Bayes风险是频率风险对先验的平均，$E_\pi(\theta-\mu)^2=\tau^2$，所以
> $$
> B=(1-\eta)^2v+\eta^2\tau^2
> =\frac{\tau^4v+v^2\tau^2}{(\tau^2+v)^2}
> =\frac{v\tau^2}{v+\tau^2}=\tau^2\eta.
> $$
> 它也等于这里不随数据变化的后验方差，所有期望均有限。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=328|印刷第297页／PDF物理第328页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 英文原文、中文转述与本库独立解答分别保留；实际核对正文位置列于`source_refs`。题内文献引用不表示已查阅其原文。`source_status: verified`只指本题及所列位置的核对范围，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
