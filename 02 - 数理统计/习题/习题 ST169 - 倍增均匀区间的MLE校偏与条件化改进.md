---
title: "习题 ST169：倍增均匀区间的MLE校偏与条件化改进"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第7章习题7.46，印刷页295／PDF物理页326"
source_id: "DS011"
source_chapter: 7
source_exercise: "7.46"
source_stars: 0
source_refs: ["DS011 Exercise 7.46，印刷295／PDF物理326"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST169：倍增均匀区间的MLE校偏与条件化改进

## 题目

### 英文原题

> [!question] 英文原题
> **7.46** Let $X_1,X_2$, and $X_3$ be a random sample of size three from a uniform$(\theta,2\theta)$ distribution, where $\theta>0$.
>
> (a) Find the method of moments estimator of $\theta$.
>
> (b) Find the MLE, $\widehat\theta$, and find a constant $k$ such that $E_\theta(k\widehat\theta)=\theta$.
>
> (c) Which of the two estimators can be improved by using sufficiency? How?
>
> (d) Find the method of moments estimate and the MLE of $\theta$ based on the data
> $$
> 1.29,\ .86,\ 1.33,
> $$
> three observations of average berry sizes (in centimeters) of wine grapes.

### 中文转述

> [!question] 中文转述
> **原题7.46。** 设$X_1,X_2,X_3$为来自$\operatorname{uniform}(\theta,2\theta)$分布的大小为3的随机样本，其中$\theta>0$.
>
> (a)  求$\theta$的矩估计量.
>
> (b)  求MLE $\widehat\theta$，并求常数$k$，使$E_\theta(k\widehat\theta)=\theta$.
>
> (c)  这两个估计量中，哪个可利用充分性改进？如何改进？
>
> (d)  根据数据$1.29,.86,1.33$求$\theta$的矩估计值和MLE.这些是酿酒葡萄平均果粒大小（厘米）的三次观测.

## 提示

> [!hint]- 提示
> 支持给出参数可行区间；给定极值后，中间观测仍有均匀随机性。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 记$m=X_{(1)},M=X_{(3)}$。采用包含支持端点的密度版本。
>
> **(a)** $EX=3\theta/2$，矩估计为$\widetilde\theta=2\bar X/3$，且无偏。
>
> **(b)** 联合密度$\theta^{-3}\mathbf1\{M/2\le\theta\le m\}$在可行区间递减，故$\widehat\theta=M/2$。把$X_i=\theta(1+U_i)$、$U_i\sim U(0,1)$，$EU_{(3)}=3/4$，故$EM=7\theta/4$、$E\widehat\theta=7\theta/8$，取$k=8/7$，校偏MLE为$4M/7$。若严格支持端点被排除，此MLE按通常的闭包极限解释。
>
> **(c)** $(m,M)$充分。给定两端点，中间次序统计量$X_{(2)}$在$(m,M)$均匀（其条件密度由三维均匀次序密度直接归一化为$1/(M-m)$），所以
> $$
> E(\widetilde\theta\mid m,M)=\frac29[m+M+(m+M)/2]=\frac{m+M}{3}.
> $$
> 这保持无偏并严格降低方差：原矩估计的条件方差为$(M-m)^2/243>0$几乎必然，使用全方差即得。MLE及其校偏版本已是充分统计量的函数，单凭对该充分量条件化不会再改变。
>
> **(d)** $\bar x=1.16,m=.86,M=1.33$，所以矩估计$0.773333333333$厘米，MLE$0.665$厘米；校偏MLE$0.76$厘米，条件化矩估计$0.73$厘米。原可行区间$[.665,.86]$非空，数据与模型相容。这些数值已在[[工具/StatisticalInference/ch07_numeric_checks.py|核验程序]]实际计算。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=326|印刷第295页／PDF物理第326页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 英文原文、中文转述与本库独立解答分别保留；实际核对正文位置列于`source_refs`。题内文献引用不表示已查阅其原文。`source_status: verified`只指本题及所列位置的核对范围，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
