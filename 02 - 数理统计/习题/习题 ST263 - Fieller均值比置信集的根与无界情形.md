---
title: "习题 ST263：Fieller均值比置信集的根与无界情形"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第9章习题9.15，印刷页367／PDF物理页398"
source_id: "DS011"
source_chapter: 9
source_exercise: "9.15"
source_stars: 0
source_refs: ["DS011 Exercise 9.15，印刷367／PDF物理398", "DS011 Miscellanea 9.5.3，印刷375–376／PDF物理406–407"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST263：Fieller均值比置信集的根与无界情形

## 题目

### 英文原题

> [!question] 英文原题
> **9.15** Solve for the roots of the quadratic equation that defines Fieller’s confidence set for the ratio of normal means (see Miscellanea 9.5.3). Find conditions on the random variables for which
> (a) The parabola opens upward (the confidence set is an interval).
> (b) The parabola opens downward (the confidence set is the complement of an interval).
> (c) The parabola has no real roots.
> In each case, give an interpretation of the meaning of the confidence set. For example, what would you tell an experimenter if, for his data, the parabola had no real roots?

### 中文转述

> [!question] 中文转述
> **原题9.15。**
> 求解定义正态均值比的Fieller置信集的二次方程之根（见节9.5.3）. 求出随机变量满足何种条件时，
>
> (a)  抛物线开口向上（置信集为一个区间）.
>
> (b)  抛物线开口向下（置信集为一个区间的补集）.
>
> (c)  抛物线没有实根.
>
> 在每种情形下解释置信集的含义. 例如，若某位实验者的数据导致抛物线没有实根，你会如何向他解释？

## 提示

> [!hint]- 提示
> 把Fieller接受不等式整理为候选比值$r$的$Ar^2+Br+C\le0$；分别检查$A$的符号、判别式及$A=0$的边界。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 教材输入与补充假设另行标明。
>
> 按原书定义$S_X^2=n^{-1}\sum(X_i-\bar X)^2$，$S_Y^2,S_{YX}$同理。设$c=t_{n-1,\alpha/2}^2/(n-1)$，$A=\bar x^2-cS_X^2$，$B=\bar x\bar y-cS_{YX}$，$C=\bar y^2-cS_Y^2$。置信集为$A\theta^2-2B\theta+C\le0$。令$D=B^2-AC$，当$A\ne0,D\ge0$时两根为$(B\pm\sqrt D)/A$，排序成$r_1\le r_2$。
> (a) $A>0,D>0$时集合$[r_1,r_2]$，分母均值显著远离零，可给有限比值范围。对正定样本协方差，$A>0$已保证$D>0$：代入$\theta=\bar y/\bar x$二次式为负。
> (b) $A<0,D>0$时集合$(-\infty,r_1]\cup[r_2,\infty)$；不能排除分母近零及很大正负比值，却可排除中段。仅“向下”不足以保证两个分离区间，还需$D>0$。
> (c) 无实根即$D<0$。当$A<0$二次式处处负，集合为整个实线，数据不足以排除任何有限均值比。纯代数上$A>0,D<0$会给空集，但正定样本协方差下不可能出现，不能将常规Fieller无根解释为证实某个比值。$A<0,D=0$同样为全实线；$A>0,D=0$退化单点。$A=0$时为线性不等式：$B>0$得$[C/(2B),\infty)$，$B<0$得$(-\infty,C/(2B)]$，$B=0$按$C\le0$取全实线否则空集。总体均值比本身要求$\mu_X\ne0$，无界置信集反映对该分母的统计不确定性。

## 相关概念

- [[02 - 数理统计/概念/区间估计|区间估计]]
- [[02 - 数理统计/概念/假设检验|假设检验]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[01 - 概率论/概念/概率模型|概率模型]]

## 备注

- 统一来源见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011教材台账]]；原题位于[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=398|印刷367／PDF物理398]]。已对照原始页面核对完整英文、分题与定位，原题无星号。
- 解答为独立推导；引用的教材结论按source_refs核对，不使用答案册代替证明。
- 来源核对、归档与个人学习分别记录；verified只指所列来源核对范围，学习状态保持not-started。未实测Obsidian渲染。
