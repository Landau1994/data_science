---
title: "习题 ST224：位置族及MLR族的尾概率单调性"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第8章习题8.34，印刷页330／PDF物理页361"
source_id: "DS011"
source_chapter: 8
source_exercise: "8.34"
source_stars: 0
source_refs: ["DS011 Exercise 8.34，印刷页330／PDF物理页361", "DS011 所引正文，印刷317／PDF物理348"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST224：位置族及MLR族的尾概率单调性

## 题目

### 英文原题

> [!question] 英文原题
> **8.34** In each of the following two situations, show that for any number $c$, if $\theta_1\le\theta_2$ then
> $$P_{\theta_1}(T>c)\le P_{\theta_2}(T>c).$$
> (a) $\theta$ is a location parameter in the distribution of the random variable $T$.
> (b) The family of pdfs of $T$, $\{g(t\mid\theta):\theta\in\Theta\}$, has an MLR.

### 中文转述

> [!question] 中文转述
> **原题8.34。**
> 在以下两种情形中，证明对任意数 $c$，若 $\theta_1\le\theta_2$，则
>
> $$
> P_{\theta_1}(T>c)\le P_{\theta_2}(T>c).
> $$
>
> (a)  $\theta$ 是随机变量 $T$ 分布中的位置参数.
>
> (b)  $T$ 的密度族 $\{g(t\mid\theta):\theta\in\Theta\}$ 具有单调似然比.

## 提示

> [!hint]- 提示
> 位置用平移耦合，MLR用左右半轴交叉密度积。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** (a) 位置族可写$T_\theta=\theta+Z$且$Z$的分布不含$\theta$。固定同一个$Z$时$T_{\theta_1}\le T_{\theta_2}$，所以尾事件指示量逐点有序，取期望即得。
> (b) 需要MLR方向为$g_2/g_1$关于$t$非减。此时$x>c\ge y$有$g_2(x)g_1(y)\ge g_1(x)g_2(y)$，两边在左右半轴积分，差恰为$P_2(T>c)-P_1(T>c)$，故非负。若定义中的MLR容许反向非增，则相应尾概率方向也要反转；本题原断言不能在未指方向时无条件使用，$T\sim N(-\theta,1)$就是反向例。等参数或非严格比值不影响非严格不等式。

## 相关概念

- [[02 - 数理统计/概念/假设检验|假设检验（hypothesis testing）]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[01 - 概率论/概念/条件概率|条件概率]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 完整原题已逐页对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=361|印刷330／PDF物理361]]；原题无星号。教材信息及归档进度见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 引用输入实际核对页：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=348|印刷317／PDF物理348]]；解答已重述所需假设及结果。
- 来源已核对与独立解答写成不等于个人已完成练习；学习状态保留`not-started`。未实测Obsidian界面渲染。
