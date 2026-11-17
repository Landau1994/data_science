---
title: "习题 ST200：PoissonGamma后验概率与卡方表的Bayes检验"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第8章习题8.10，印刷页327／PDF物理页358"
source_id: "DS011"
source_chapter: 8
source_exercise: "8.10"
source_stars: 0
source_refs: ["DS011 Exercise 8.10，印刷页327／PDF物理页358", "DS011 所引正文，印刷290／PDF物理321"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST200：PoissonGamma后验概率与卡方表的Bayes检验

## 题目

### 英文原题

> [!question] 英文原题
> **8.10** Let $X_1,\ldots,X_n$ be iid Poisson$(\lambda)$, and let $\lambda$ have a gamma$(\alpha,\beta)$ distribution, the conjugate family for the Poisson. In Exercise 7.24 the posterior distribution of $\lambda$ was found, including the posterior mean and variance. Now consider a Bayesian test of $H_0:\lambda\le\lambda_0$ versus $H_1:\lambda>\lambda_0$.
> (a) Calculate expressions for the posterior probabilities of $H_0$ and $H_1$.
> (b) If $\alpha=5/2$ and $\beta=2$, the prior distribution is a chi squared distribution with 5 degrees of freedom. Explain how a chi squared table could be used to perform a Bayesian test.

### 中文转述

> [!question] 中文转述
> **原题8.10。**
> 设 $X_1,\ldots,X_n$ 独立同分布于 $\operatorname{Poisson}(\lambda)$，$\lambda$ 服从泊松分布的共轭族 $\operatorname{gamma}(\alpha,\beta)$. 习题7.24已求出 $\lambda$ 的后验分布，包括后验均值和方差. 现考虑 $H_0:\lambda\le\lambda_0$ 对 $H_1:\lambda>\lambda_0$ 的贝叶斯检验.
>
> (a)  求 $H_0,H_1$ 的后验概率表达式.
>
> (b)  若 $\alpha=5/2$、$\beta=2$，先验分布为自由度 $5$ 的卡方分布. 说明如何利用卡方表进行贝叶斯检验.

## 提示

> [!hint]- 提示
> Gamma先验第二参数为尺度，后验的率会相加。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 设$\alpha,\beta,\lambda_0>0$、$s=\sum_i x_i$。似然核为$\lambda^s e^{-n\lambda}$，先验核$\lambda^{\alpha-1}e^{-\lambda/\beta}$，故后验为形状$A=\alpha+s$、率$B=n+1/\beta$的Gamma。
> (a) $P(H_0\mid x)=\Gamma(A)^{-1}\int_0^{B\lambda_0}u^{A-1}e^{-u}du$，$P(H_1\mid x)=1-P(H_0\mid x)$；连续先验下边界概率0。等误判损失的Bayes检验在后验$H_1$概率大于$1/2$时拒绝$H_0$，平局可任选。
> (b) $2B\lambda\mid x\sim\chi^2_{2A}$，此时$2A=5+2s$、$2B=2n+1$。所以$P(H_0\mid x)=F_{\chi^2_{5+2s}}((2n+1)\lambda_0)$，可查卡方表比较该CDF与$1/2$。若两类错误损失不同，则改相应后验赔率阈值；题目未给损失时不能声称存在唯一Bayes决策阈值。

## 相关概念

- [[02 - 数理统计/概念/假设检验|假设检验（hypothesis testing）]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[01 - 概率论/概念/条件概率|条件概率]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 完整原题已逐页对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=358|印刷327／PDF物理358]]；原题无星号。教材信息及归档进度见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 引用输入实际核对页：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=321|印刷290／PDF物理321]]；解答已重述所需假设及结果。
- 来源已核对与独立解答写成不等于个人已完成练习；学习状态保留`not-started`。未实测Obsidian界面渲染。
