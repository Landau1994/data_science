---
title: "习题 ST296：未知方差正态t区间的LRT反演与无偏性"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第9章习题9.48，印刷页372／PDF物理页403"
source_id: "DS011"
source_chapter: 9
source_exercise: "9.48"
source_stars: 0
source_refs: ["DS011 Exercise 9.48，印刷372／PDF物理403", "DS011 (9.2.14)，印刷347／PDF物理378"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST296：未知方差正态t区间的LRT反演与无偏性

## 题目

### 英文原题

> [!question] 英文原题
> **9.48** Let $X_1,\ldots,X_n$ be a random sample from a $n(\theta,\sigma^2)$ population, where $\sigma^2$ is unknown.
> (a) Show that the interval $\theta\le\bar x+t_{n-1,\alpha}s/\sqrt n$ can be derived by inverting the acceptance region of an LRT.
> (b) Show that the corresponding two-sided interval in (9.2.14) can also derived by inverting the acceptance region of an LRT.
> (c) Show that the intervals in parts (a) and (b) are unbiased intervals.

### 中文转述

> [!question] 中文转述
> **原题9.48。**
> 设$X_1,\ldots,X_n$为来自$\mathrm n(\theta,\sigma^2)$总体的随机样本，其中$\sigma^2$未知.
>
> (a) 证明区间$\theta\le\bar x+t_{n-1,\alpha}s/\sqrt n$可由反演LRT接受域导出.
>
> (b) 证明式9.2.14中相应的双侧区间也可由反演LRT接受域导出.
>
> (c)  证明(a)和(b)中的区间无偏.

## 提示

> [!hint]- 提示
> 剖面消去未知方差后，似然比是$t$统计量绝对值或单侧正部的单调函数；反演前先写清接受域方向。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 教材输入与补充假设另行标明。
>
> 设$\nu=n-1\ge1$、$Q=\nu S^2$、$T_0=\sqrt n(\bar X-\theta_0)/S$。无约束MLE为$\bar X,Q/n$；固定均值$\theta_0$时方差MLE为$[Q+n(\bar X-\theta_0)^2]/n$。
> (a) 针对$\theta\ge\theta_0$对$\theta<\theta_0$，当$\bar X\ge\theta_0$时似然比为1；当$\bar X<\theta_0$时为$(1+T_0^2/\nu)^{-n/2}$。通常$0<\alpha<1/2$时拒绝$T_0<-t_{\nu,\alpha}$，反演上限$\theta_0\le\bar X+t_{\nu,\alpha}S/\sqrt n$。如考虑大于一半的非通常显著性水平，需在似然比平顶作相应选择，不能直接以严格阈值越过平顶。
> (b) 双侧LRT比为$(1+T_0^2/\nu)^{-n/2}$，拒绝$|T_0|>t_{\nu,\alpha/2}$，反演$\bar X\pm t_{\nu,\alpha/2}S/\sqrt n$，即(9.2.14)。
> (c) 写$T_0=(Z+\delta)/\sqrt{V/\nu}$，$Z\sim N(0,1)$、$V\sim\chi^2_\nu$独立，$\delta=\sqrt n(\theta-\theta_0)/\sigma$。单侧接受概率随$\delta$单调，错误大候选值对应$\delta<0$，其接受概率小于零假设时$1-\alpha$。双侧对固定$V=v$，$P(|Z+\delta|\le c\sqrt{v/\nu})$由正态对称单峰性在$\delta=0$最大；积分$v$得所有$\delta\ne0$的接受概率至多$1-\alpha$。所以双侧区间满足定义9.3.7，单侧区间在相应错误方向上满足修复后的无偏性。若严格要求定义9.3.7对所有错误值成立，原(a)的单侧区间并不无偏，较小候选均值的覆盖概率会超过$1-\alpha$。

## 相关概念

- [[02 - 数理统计/概念/区间估计|区间估计]]
- [[02 - 数理统计/概念/假设检验|假设检验]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[01 - 概率论/概念/概率模型|概率模型]]

## 备注

- 统一来源见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011教材台账]]；原题位于[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=403|印刷372／PDF物理403]]。已对照原始页面核对完整英文、分题与定位，原题无星号。
- 解答为独立推导；引用的教材结论按source_refs核对，不使用答案册代替证明。
- 来源核对、归档与个人学习分别记录；verified只指所列来源核对范围，学习状态保持not-started。未实测Obsidian渲染。
