---
title: "习题 ST226：Beta区间原假设的双尾改进及局部无偏约束"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "advanced"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第8章习题8.36，印刷页331／PDF物理页362"
source_id: "DS011"
source_chapter: 8
source_exercise: "8.36"
source_stars: 0
source_refs: ["DS011 Exercise 8.36，印刷页331／PDF物理页362"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST226：Beta区间原假设的双尾改进及局部无偏约束

## 题目

### 英文原题

> [!question] 英文原题
> **8.36** We have one observation from a beta$(1,\theta)$ population.
> (a) To test $H_0:\theta_1\le\theta\le\theta_2$ versus $H_1:\theta<\theta_1$ or $\theta>\theta_2$, where $\theta_1=1$ and $\theta_2=2$, a test satisfies $E_{\theta_1}\phi=.5$ and $E_{\theta_2}\phi=.3$. Find a test that is as good, and explain why it is as good.
> (b) For testing $H_0:\theta=\theta_1$ versus $H_1:\theta\ne\theta_1$, with $\theta_1=1$, find a two-sided test (other than $\phi\equiv.1$) that satisfies $E_{\theta_1}\phi=.1$ and $\left.\frac d{d\theta}E_\theta(\phi)\right|_{\theta=\theta_1}=0$.

### 中文转述

> [!question] 中文转述
> **原题8.36。**
> 我们有来自 $\operatorname{beta}(1,\theta)$ 总体的一次观测.
>
> (a)  检验 $H_0:\theta_1\le\theta\le\theta_2$ 对 $H_1:\theta<\theta_1\text{ 或 }\theta>\theta_2$，其中 $\theta_1=1$、$\theta_2=2$. 某检验满足 $\mathrm E_{\theta_1}\phi=.5$ 与 $\mathrm E_{\theta_2}\phi=.3$. 求一个同样好的检验，并说明它为何同样好.
>
> (b)  对检验 $H_0:\theta=\theta_1$ 对 $H_1:\theta\ne\theta_1$，其中 $\theta_1=1$，求一个双侧检验（不同于 $\phi\equiv.1$），满足
>
> $$
> \mathrm E_{\theta_1}\phi=.1,\qquad\left.\frac d{d\theta}\mathrm E_\theta(\phi)\right|_{\theta=\theta_1}=0.
> $$

## 提示

> [!hint]- 提示
> 令$Z=1-X$，密度为$\theta z^{\theta-1}$；用幂函数相对割线的凸凹性。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** (a) 取拒绝域$X<.05$或$X>.55$，即$Z>.95$或$Z<.45$。其功效$\beta_*(\theta)=1-.95^\theta+.45^\theta$，在1为$.5$、在2为$.3$。
> 为证明对任何题设竞争检验都“至少同样好”，设$D(z)=\phi_*(1-z)-\phi(1-z)$。两端点功效相同意味着$\int_0^1D(z)dz=\int_0^1zD(z)dz=0$。固定$\theta<1$或$\theta>2$，函数$q(z)=\theta z^{\theta-1}$严格凸；通过$.45,.95$两点的割线$\ell(z)=a+bz$在区间内高于$q$，在区间外低于$q$。$D$在区间外非负、区间内非正，故$\int D(q-\ell)\ge0$，而割线积分为0，得到$\beta_*(\theta)\ge\beta(\theta)$。对于$1<\theta<2$，$q$凹，符号反转，得到$\beta_*\le\beta$。所以它在原假设内部不增加第一类错误，并在两侧备择不增加第二类错误，严格表达了至少同样好。
> (b) 取拒绝$X<a$或$X>b$，$b=a+.9$、$0<a<.1$，大小在$\theta=1$为$a+1-b=.1$。功效为$1-(1-a)^\theta+(1-b)^\theta$，导数在1为$-(1-a)\log(1-a)+(1-b)\log(1-b)$。令$u=1-a\in(.9,1)$，解
> $$u\log u=(u-.9)\log(u-.9).$$
> 左减右在$.9$为负、在1为正，导数$\log[u/(u-.9)]>0$，故唯一根存在。这给出明确唯一的非平凡双尾检验，满足两项等式；其数值临界值见本章计算核验记录。无需声称未要求的全局UMP性。 实际求根得到$a\approx.08039843657,b\approx.98039843657$；用这两个数代入两项约束，仅有数值舍入误差。

## 相关概念

- [[02 - 数理统计/概念/假设检验|假设检验（hypothesis testing）]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[01 - 概率论/概念/条件概率|条件概率]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 完整原题已逐页对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=362|印刷331／PDF物理362]]；原题无星号。教材信息及归档进度见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 来源已核对与独立解答写成不等于个人已完成练习；学习状态保留`not-started`。未实测Obsidian界面渲染。
