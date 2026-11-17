---
title: "习题 ST137：竞争指数寿命中最小值与类型观测的MLE"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第7章习题7.14，印刷页288／PDF物理页319"
source_id: "DS011"
source_chapter: 7
source_exercise: "7.14"
source_stars: 0
source_refs: ["DS011 Exercise 7.14，印刷288／PDF物理319"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST137：竞争指数寿命中最小值与类型观测的MLE

## 题目

### 英文原题

> [!question] 英文原题
> **7.14** Let $X$ and $Y$ be independent exponential random variables, with
> $$
> f(x\mid\lambda)=\frac1\lambda e^{-x/\lambda},\ x>0,\qquad f(y\mid\mu)=\frac1\mu e^{-y/\mu},\ y>0.
> $$
> We observe $Z$ and $W$ with
> $$
> Z=\min(X,Y)\quad\text{and}\quad W=\begin{cases}1&\text{if }Z=X\\0&\text{if }Z=Y.\end{cases}
> $$
> In Exercise 4.26 the joint distribution of $Z$ and $W$ was obtained. Now assume that $(Z_i,W_i)$, $i=1,\ldots,n$, are $n$ iid observations. Find the MLEs of $\lambda$ and $\mu$.

### 中文转述

> [!question] 中文转述
> **原题7.14。** 设$X$和$Y$为独立指数随机变量，且
>
> $$
> f(x\mid\lambda)=\frac1\lambda e^{-x/\lambda},\ x>0,\qquad f(y\mid\mu)=\frac1\mu e^{-y/\mu},\ y>0.
> $$
>
> 观测到$Z$和$W$，其中
>
> $$
> Z=\min(X,Y)\qquad\text{及}\qquad W=\begin{cases}1,&\text{若 }Z=X,\\0,&\text{若 }Z=Y.\end{cases}
> $$
>
> 习题4.26已求出$Z$和$W$的联合分布.现假设$(Z_i,W_i)$，$i=1,\ldots,n$，为$n$个独立同分布观测.求$\lambda$和$\mu$的MLE.

## 提示

> [!hint]- 提示
> 用“一个先失效，另一个仍存活”写联合密度，再改用速率参数。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 独立性给$P(Z\in dz,W=1)=f_X(z)P(Y>z)dz$，因此相对于$z$的Lebesgue测度及$w$的计数测度，
> $$
> f(z,w)=\lambda^{-w}\mu^{-(1-w)}e^{-z(1/\lambda+1/\mu)},\qquad z>0,\quad w=0,1.
> $$
> 记$R=\sum_iw_i$、$S=\sum_i z_i>0$，则$\ell=-R\log\lambda-(n-R)\log\mu-S/\lambda-S/\mu$。令速率$a=1/\lambda,b=1/\mu$，它化为$R\log a+(n-R)\log b-S(a+b)$，为两个独立凹优化问题。当$0<R<n$时，唯一MLE为
> $$
> \widehat\lambda=S/R,\qquad\widehat\mu=S/(n-R).
> $$
> 若$R=0$，对$a>0$似然在$a\downarrow0$时增至上确界，所以有限正尺度空间中$\lambda$无MLE，扩展值为$+\infty$；另一个参数$\widehat\mu=S/n$。若$R=n$则角色互换。原始连续寿命相等的事件概率零，$W$在该事件的定义不影响结果。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=319|印刷第288页／PDF物理第319页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 英文原文、中文转述与本库独立解答分别保留；实际核对正文位置列于`source_refs`。题内文献引用不表示已查阅其原文。`source_status: verified`只指本题及所列位置的核对范围，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
