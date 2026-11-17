---
title: 习题 ST309：均值方差同参正态的MLE及渐近方差
topic: mathematical-statistics
topic_label: 数理统计
difficulty: intermediate
status: not-started
tags:
- exercise
- mathematical-statistics
source: George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第10章习题10.3，印刷页408／PDF物理页439
source_id: DS011
source_chapter: 10
source_exercise: '10.3'
source_stars: 0
source_refs:
- DS011 Exercise 10.3，印刷408／PDF物理439
- DS011题内依赖核对：印刷382／PDF物理413；印刷383／PDF物理414
source_status: verified
solution_status: independently-derived
created: '2026-11-13'
---

# 习题 ST309：均值方差同参正态的MLE及渐近方差

## 题目

### 英文原题

> [!question] 英文原题
> **10.3** A random sample $X_1,\ldots,X_n$ is drawn from a population that is $\operatorname n(\theta,\theta)$, where $\theta>0$.
>
> (a) Show that the MLE of $\theta$, $\hat\theta$, is a root of the quadratic equation $\theta^2+\theta-W=0$, where $W=(1/n)\sum_{i=1}^nX_i^2$, and determine which root equals the MLE.
>
> (b) Find the approximate variance of $\hat\theta$ using the techniques of Section 10.1.3.

### 中文转述

> [!question] 中文转述
> **原题10.3。** 从$\mathrm n(\theta,\theta)$总体中抽取随机样本$X_1,\ldots,X_n$，其中$\theta>0$.
>
> (a)  证明$\theta$的MLE $\hat\theta$是二次方程$\theta^2+\theta-W=0$的根，其中$W=(1/n)\sum_{i=1}^nX_i^2$，并确定哪个根等于MLE.
>
> (b)  用第10.1.3节的技术求$\hat\theta$的近似方差.

## 提示

> [!hint]- 提示
> 先展开(X_i−θ)²/θ；近似方差可由W的中心极限定理与Delta方法得到。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** **(a)** 略去与$\theta$无关项，$l(\theta)=-n\log\theta/2-nW/(2\theta)-n\theta/2+\sum_iX_i$，故$l'(\theta)=n(W-\theta-\theta^2)/(2\theta^2)$。当$W>0$时，正根
> $$
> \hat\theta=\frac{\sqrt{1+4W}-1}2
> $$
> 使导数由正变负；$\theta\downarrow0$或$\theta\uparrow\infty$时$l\to-\infty$，因此为唯一全局MLE。另一根为负，参数空间不容许。连续正态抽样使$W=0$概率0；在全零样本上似然在$\theta\downarrow0$无界，开参数空间没有有限MLE，须另注明此零概率例外。
>
> **(b)** $EX^2=\theta+\theta^2$，正态四阶矩给$\operatorname{Var}(X^2)=2\theta^2+4\theta^3$。对$g(w)=(\sqrt{1+4w}-1)/2$，$g'(\theta+\theta^2)=1/(1+2\theta)$。Delta方法给
> $$
> \sqrt n(\hat\theta-\theta)\Rightarrow N\left(0,\frac{2\theta^2}{1+2\theta}\right),\quad \operatorname{Var}(\hat\theta)\approx\frac{2\theta^2}{n(1+2\theta)}.
> $$
> 等价地每观测Fisher信息$I(\theta)=1/\theta+1/(2\theta^2)$，倒数与上式一致；实际标准误可把$\theta$换成$\hat\theta$。

## 相关概念

- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/期望|期望]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[02 - 数理统计/概念/参数估计|参数估计]]

## 备注

- 来源：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=439|印刷第408页／PDF物理第439页]]；版本与归档见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 已实读本题所用正文：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=413|印刷382／PDF物理413]]；[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=414|印刷383／PDF物理414]]；其余题内外部文献仅保留原引用，未声称查阅。
- 英文原题逐题对照PDF原始页面，保留原分题、提示、引用及可见疑误；原题无星号。题内引用补充与独立解答不混入原文；未查阅答案册或题内外部文献。
- 来源核对不表示个人学习完成，学习状态保持not-started。公式、链接与元数据检查不等于Obsidian实际渲染检查。
