---
title: 习题 ML049：Probit与两种erf约定的换元关系
topic: statistical-learning
topic_label: 统计学习
difficulty: beginner
status: not-started
tags:
- exercise
- statistical-learning
source: '[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Deep Learning: Foundations and Concepts（DS003）]]'
source_id: DS003
source_chapter: 5
source_exercise: '5.23'
source_stars: 1
source_refs:
- DS003 Exercise 5.23，印刷169/PDF188
- DS003 §5.4.5，式(5.86)–(5.88)，印刷163–164/PDF182–183
- DS004 Solution 5.23，式(178)–(179)及续页，印刷58–59/PDF58–59
source_status: verified
solution_status: independently-derived
created: '2026-11-02'
---

# 习题 ML049：Probit与两种erf约定的换元关系

## 题目

### 英文原题

> [!question] 英文原题
> **Exercise 5.23（★）** Show that the probit function (5.86) and the erf function (5.87) are related by (5.88).

### 中文转述

> [!question] 中文转述
> **原题5.23（★）。** 证明 Probit 函数（probit function）式 (5.86) 与误差函数（erf function）式 (5.87) 满足关系 (5.88)。原书这三式为
> $$
> \Phi(a)=\int_{-\infty}^a\mathcal N(\theta\mid0,1)\,\mathrm d\theta,\tag{5.86}
> $$
> $$
> \operatorname{erf}(a)=\frac2{\sqrt\pi}\int_0^a e^{-\theta^2/2}\,\mathrm d\theta,\tag{5.87}
> $$
> $$
> \Phi(a)=\frac12\left\{1+\frac1{\sqrt2}\operatorname{erf}(a)\right\}.\tag{5.88}
> $$

## 提示

> [!hint]- 提示 1
> 利用标准高斯的对称性把 $\Phi(a)$ 写成 $1/2$ 加上从0到 $a$ 的积分。

> [!hint]- 提示 2
> 先严格按主书式(5.87)的被积函数和系数计算；再用 $\theta=\sqrt2u$ 对照采用 $e^{-u^2}$ 的标准 erf 定义。

## 解答

> [!success]- 解答
> **证明范围：独立推导，并区分主书与答案册的函数约定。** 对任意实数 $a$，以下从0到负数上限的积分均按有向积分理解，所以不必限制 $a\geq0$。记主书式 (5.87) 的函数为
> $$
> E_{\mathrm{book}}(a)=\frac2{\sqrt\pi}\int_0^a e^{-\theta^2/2}\,\mathrm d\theta.
> $$
> 标准高斯的对称性与归一化给出 $\Phi(0)=1/2$。由其密度定义直接得到
> $$
> \begin{aligned}
> \Phi(a)
> &=\frac12+\frac1{\sqrt{2\pi}}\int_0^a e^{-\theta^2/2}\,\mathrm d\theta\\
> &=\frac12+\frac{E_{\mathrm{book}}(a)}{2\sqrt2}\\
> &=\frac12\left(1+\frac1{\sqrt2}E_{\mathrm{book}}(a)\right).
> \end{aligned}
> $$
> 这正是主书实际印出的式 (5.88)，与其式 (5.87) 完全自洽。
>
> 但通常的标准误差函数另定义为
> $$
> \operatorname{erf}_{\mathrm{std}}(z)=\frac2{\sqrt\pi}\int_0^z e^{-u^2}\,\mathrm du.
> $$
> 在主书积分中令 $\theta=\sqrt2u$，上下限相应变为0和 $a/\sqrt2$，故
> $$
> E_{\mathrm{book}}(a)
> =\frac{2\sqrt2}{\sqrt\pi}\int_0^{a/\sqrt2}e^{-u^2}\,\mathrm du
> =\sqrt2\,\operatorname{erf}_{\mathrm{std}}(a/\sqrt2).
> $$
> 代回可得标准约定下的等价式
> $$
> \Phi(a)=\frac12\left(1+\operatorname{erf}_{\mathrm{std}}(a/\sqrt2)\right).
> $$
> 两式数值一致，区别仅在所指的 erf 函数。主书函数在 $a\to\infty$ 时趋于 $\sqrt2$，标准 erf 趋于1；因此不能将同一个字样直接当作同一个函数。两函数也都是奇函数，负 $a$ 情况由上述有向积分换元同时覆盖。

## 相关概念

- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/概率模型|概率模型]]

## 备注

- 原题与星号：[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=188|印刷169／PDF物理188]]；原题及实际引用的正文页均已对照原始PDF图像。正文精确定位见 `source_refs`。
- 已逐式查看主书原页：式(5.87)指数确为 $-\theta^2/2$，式(5.88)确为 $\tfrac12[1+\operatorname{erf}(a)/\sqrt2]$。[[00 - 首页/教材归档/DS004 - Bishop 深度学习答案册|DS004]]印刷58–59／PDF58–59则使用 $e^{-u^2}$ 的标准 erf 并写 $\tfrac12[1+\operatorname{erf}(a/\sqrt2)]$。本笔记保留主书实际公式，显式解释缩放差异，没有把答案册的约定静默替换进题目。
- `source_status: verified` 仅指本题及所列实际核对范围；独立解答不构成个人完成学习，状态保持 `not-started`。
