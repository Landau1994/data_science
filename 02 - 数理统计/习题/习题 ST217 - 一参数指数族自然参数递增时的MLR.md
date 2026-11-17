---
title: "习题 ST217：一参数指数族自然参数递增时的MLR"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第8章习题8.27，印刷页329／PDF物理页360"
source_id: "DS011"
source_chapter: 8
source_exercise: "8.27"
source_stars: 0
source_refs: ["DS011 Exercise 8.27，印刷页329／PDF物理页360"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST217：一参数指数族自然参数递增时的MLR

## 题目

### 英文原题

> [!question] 英文原题
> **8.27** Suppose $g(t\mid\theta)=h(t)c(\theta)e^{w(\theta)t}$ is a one-parameter exponential family for the random variable $T$. Show that this family has an MLR if $w(\theta)$ is an increasing function of $\theta$. Give three examples of such a family.

### 中文转述

> [!question] 中文转述
> **原题8.27。**
> 设 $g(t\mid\theta)=h(t)c(\theta)e^{w(\theta)t}$ 是随机变量 $T$ 的单参数指数族. 证明，若 $w(\theta)$ 是 $\theta$ 的增函数，则此族具有单调似然比. 给出三个这类分布族的例子.

## 提示

> [!hint]- 提示
> 指数族的参数无关因子在两似然相除时消去。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 在共同支持上$g(t\mid\theta_2)/g(t\mid\theta_1)=[c(\theta_2)/c(\theta_1)]e^{[w(\theta_2)-w(\theta_1)]t}$。当$\theta_2>\theta_1$且$w$递增时，指数中$t$系数非负，故比值非减，得到MLR。若严格增加且支持非单点则严格单调。
> 例1：已知方差正态均值族，$w(\theta)=\theta/\sigma^2$、$h(t)=e^{-t^2/(2\sigma^2)}$（归一化项放入$c$）。例2：Poisson，$h(t)=1/t!$、$c(\theta)=e^{-\theta}$、$w(\theta)=\log\theta$，整数$t\ge0$。例3：已知$n$二项，$h(t)=\binom nt$、$c(\theta)=(1-\theta)^n$、$w(\theta)=\log[\theta/(1-\theta)]$。三例各在相应内部参数空间满足条件，边界退化值另取极限。

## 相关概念

- [[02 - 数理统计/概念/假设检验|假设检验（hypothesis testing）]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[01 - 概率论/概念/条件概率|条件概率]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 完整原题已逐页对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=360|印刷329／PDF物理360]]；原题无星号。教材信息及归档进度见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 来源已核对与独立解答写成不等于个人已完成练习；学习状态保留`not-started`。未实测Obsidian界面渲染。
