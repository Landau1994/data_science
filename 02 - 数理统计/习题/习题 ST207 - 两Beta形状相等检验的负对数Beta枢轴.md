---
title: "习题 ST207：两Beta形状相等检验的负对数Beta枢轴"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第8章习题8.17，印刷页328／PDF物理页359"
source_id: "DS011"
source_chapter: 8
source_exercise: "8.17"
source_stars: 0
source_refs: ["DS011 Exercise 8.17，印刷页328／PDF物理页359"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST207：两Beta形状相等检验的负对数Beta枢轴

## 题目

### 英文原题

> [!question] 英文原题
> **8.17** Suppose that $X_1,\ldots,X_n$ are iid with a beta$(\mu,1)$ pdf and $Y_1,\ldots,Y_m$ are iid with a beta$(\theta,1)$ pdf. Also assume that the $X$s are independent of the $Y$s.
> (a) Find an LRT of $H_0:\theta=\mu$ versus $H_1:\theta\ne\mu$.
> (b) Show that the test in part (a) can be based on the statistic
> $$T=\frac{\Sigma\log X_i}{\Sigma\log X_i+\Sigma\log Y_i}.$$
> (c) Find the distribution of $T$ when $H_0$ is true, and then show how to get a test of size $\alpha=.10$.

### 中文转述

> [!question] 中文转述
> **原题8.17。**
> 设 $X_1,\ldots,X_n$ 独立同分布于 $\operatorname{beta}(\mu,1)$，$Y_1,\ldots,Y_m$ 独立同分布于 $\operatorname{beta}(\theta,1)$，且 $X$ 样本与 $Y$ 样本独立.
>
> (a)  求 $H_0:\theta=\mu$ 对 $H_1:\theta\ne\mu$ 的一个似然比检验.
>
> (b)  证明，(a) 中的检验可以基于统计量
>
> $$
> T=\frac{\sum\log X_i}{\sum\log X_i+\sum\log Y_i}.
> $$
>
> (c)  求 $H_0$ 为真时 $T$ 的分布，再说明如何得到大小 $\alpha=.10$ 的检验.

## 提示

> [!hint]- 提示
> 负对数把Beta$(a,1)$化为率为$a$的指数变量。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 令$A=-\sum\log X_i>0,B=-\sum\log Y_i>0,N=n+m$。联合似然关于参数的核为$\mu^n\theta^m e^{-\mu A-\theta B}$。
> (a) 自由MLE为$n/A,m/B$，原假设共同MLE为$N/(A+B)$，故$\lambda=N^N A^nB^m/[n^nm^m(A+B)^N]$，拒绝小比值。
> (b) 题内两个和均负，相除仍为$T=A/(A+B)$，故$\lambda=K T^n(1-T)^m$，$K=N^N/(n^nm^m)$。两尾拒绝域$T<a$或$T>b$，$a<n/N<b$，满足$K a^n(1-a)^m=K b^n(1-b)^m$。
> (c) $-\log X_i$为率$\mu$的指数变量，另一组为率$\theta$；在原假设下独立总和具有共同尺度，比例$T\sim\operatorname{Beta}(n,m)$（换元总和与比例的Jacobian为总和）。因此再令$F_{\operatorname{Beta}(n,m)}(a)+1-F_{\operatorname{Beta}(n,m)}(b)=.10$便给出大小$.10$的LRT。也可用Beta等尾分位数$.05,.95$得到大小$.10$检验，但除对称情形不必是同一个LRT。

## 相关概念

- [[02 - 数理统计/概念/假设检验|假设检验（hypothesis testing）]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[01 - 概率论/概念/条件概率|条件概率]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 完整原题已逐页对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=359|印刷328／PDF物理359]]；原题无星号。教材信息及归档进度见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 来源已核对与独立解答写成不等于个人已完成练习；学习状态保留`not-started`。未实测Obsidian界面渲染。
