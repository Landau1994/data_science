---
title: "习题 ST219：Cauchy位置族的有界最强域与UMP反例"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "advanced"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第8章习题8.29，印刷页330／PDF物理页361"
source_id: "DS011"
source_chapter: 8
source_exercise: "8.29"
source_stars: 0
source_refs: ["DS011 Exercise 8.29，印刷页330／PDF物理页361"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST219：Cauchy位置族的有界最强域与UMP反例

## 题目

### 英文原题

> [!question] 英文原题
> **8.29** Let $X$ be one observation from a Cauchy$(\theta)$ distribution.
> (a) Show that this family does not have an MLR.
> (b) Show that the test
> $$\phi(x)=\begin{cases}1&\text{if }1<x<3\\0&\text{otherwise}\end{cases}$$
> is most powerful of its size for testing $H_0:\theta=0$ versus $H_1:\theta=1$. Calculate the Type I and Type II Error probabilities.
> (c) Prove or disprove: The test in part (b) is UMP for testing $H_0:\theta\le0$ versus $H_1:\theta>0$. What can be said about UMP tests in general for the Cauchy location family?

### 中文转述

> [!question] 中文转述
> **原题8.29。**
> 设 $X$ 是来自 $\operatorname{Cauchy}(\theta)$ 分布的一次观测.
>
> (a)  证明此族没有单调似然比.
>
> (b)  证明检验
>
> $$
> \phi(x)=\begin{cases}1,&1<x<3,\\0,&\text{其他}\end{cases}
> $$
>
> 是检验 $H_0:\theta=0$ 对 $H_1:\theta=1$ 时、其自身大小下的最强检验. 计算第一类与第二类错误概率.
>
> (c)  证明或否证：(b) 的检验是 $H_0:\theta\le0$ 对 $H_1:\theta>0$ 的一致最强检验. 对 Cauchy 位置族的一致最强检验，一般可以说些什么？

## 提示

> [!hint]- 提示
> 似然比先增后减；有界拒绝域在位置趋无穷时功效趋0。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 采用单位尺度位置密度$f_\theta(x)=1/[\pi(1+(x-\theta)^2)]$。
> (a) 对0与1，比值$r(x)=(1+x^2)/(1+(x-1)^2)$的导数符号为$-x^2+x+1$，在两个根$(1\pm\sqrt5)/2$两侧改变，既不非减也不非增，故没有MLR。
> (b) $r(x)>2$恰为$1<x<3$，因此Neyman–Pearson引理给出所列最强域。其大小$\alpha=(\arctan3-\arctan1)/\pi$，功效在备择1为$\arctan2/\pi$，第二类错误为$1-\arctan2/\pi$。
> (c) 对$\theta\le0$，有界区间概率$[\arctan(3-\theta)-\arctan(1-\theta)]/\pi$随$\theta$增加，所以(b)也是复合原假设大小$\alpha$检验。但它在$\theta\to\infty$时功效趋0。取上尾检验$\psi=I\{X>q\}$，$q=\cot(\pi\alpha)$，其在0处大小$\alpha$，对所有负位置拒绝概率更小，故也满足同一复合水平；其功效随$\theta\to\infty$趋1。于是(b)不可能UMP。
> 对于本题这一大小，还可证明根本不存在UMP：任何UMP在备择1必须达到(b)的功效，因为(b)为合法竞争者，而Neyman–Pearson必要性及边界零概率使(b)是该简单问题唯一最强检验，随后又被$\psi$在大位置击败，矛盾。一般Cauchy位置族缺少MLR，不能从位置随机序自动推出UMP；简单假设仍有Neyman–Pearson最强检验。本证明的不存在范围是题内所求大小，不把它未经论证推广到所有复合问题或所有水平。

## 相关概念

- [[02 - 数理统计/概念/假设检验|假设检验（hypothesis testing）]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[01 - 概率论/概念/条件概率|条件概率]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 完整原题已逐页对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=361|印刷330／PDF物理361]]；原题无星号。教材信息及归档进度见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 来源已核对与独立解答写成不等于个人已完成练习；学习状态保留`not-started`。未实测Obsidian界面渲染。
