---
title: "习题 ST223：均匀位置参数的支持越界UMP与功效设计"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "advanced"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第8章习题8.33，印刷页330／PDF物理页361"
source_id: "DS011"
source_chapter: 8
source_exercise: "8.33"
source_stars: 0
source_refs: ["DS011 Exercise 8.33，印刷页330／PDF物理页361"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST223：均匀位置参数的支持越界UMP与功效设计

## 题目

### 英文原题

> [!question] 英文原题
> **8.33** Let $X_1,\ldots,X_n$ be a random sample from the uniform$(\theta,\theta+1)$ distribution. To test $H_0:\theta=0$ versus $H_1:\theta>0$, we use the test
> $$\text{reject }H_0\text{ if }Y_n\ge1\text{ or }Y_1\ge k,$$
> where $k$ is a constant, $Y_1=\min\{X_1,\ldots,X_n\}$, $Y_n=\max\{X_1,\ldots,X_n\}$.
> (a) Determine $k$ so that the test will have size $\alpha$.
> (b) Find an expression for the power function of the test in part (a).
> (c) Prove that the test is UMP size $\alpha$.
> (d) Find values of $n$ and $k$ so that the UMP .10 level test will have power at least .8 if $\theta>.1$.

### 中文转述

> [!question] 中文转述
> **原题8.33。**
> 设 $X_1,\ldots,X_n$ 是来自 $\operatorname{uniform}(\theta,\theta+1)$ 的随机样本. 检验 $H_0:\theta=0$ 对 $H_1:\theta>0$，采用规则
>
> $$
> \text{若 }Y_n\ge1\text{ 或 }Y_1\ge k,\quad\text{则拒绝 }H_0,
> $$
>
> 其中 $k$ 为常数，$Y_1=\min\{X_1,\ldots,X_n\}$，$Y_n=\max\{X_1,\ldots,X_n\}$.
>
> (a)  确定 $k$，使检验的大小为 $\alpha$.
>
> (b)  求(a) 中检验的功效函数表达式.
>
> (c)  证明该检验是大小 $\alpha$ 的一致最强检验.
>
> (d)  求 $n,k$，使水平 $.10$ 的一致最强检验在 $\theta>1$ 时功效至少为 $.8$.

## 提示

> [!hint]- 提示
> 原假设支持外的样本可不占大小预算地拒绝；支持交集内似然比恒定。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 设$0<\alpha<1$，$n\ge1$。
> (a) 在0下$P(Y_n\ge1)=0$，$P(Y_1\ge k)=(1-k)^n$，所以$k=1-\alpha^{1/n}$。
> (b) 当$0\le\theta<k$时，备择支持与原假设支持交集是$[\theta,1]^n$，概率$(1-\theta)^n$。其中拒绝子立方体$[k,1]^n$的概率为$(1-k)^n=\alpha$；支持外全拒绝。因此$\beta(\theta)=1-(1-\theta)^n+\alpha$。当$\theta\ge k$时所有样本最小值都至少$k$，功效为1。
> (c) 固定$0<\theta<k$，支持外功效至多$1-(1-\theta)^n$，交集上$f_\theta=f_0=1$，任意大小不超过$\alpha$的竞争检验在交集的拒绝积分至多$\alpha$。本检验达到这两部分上界。对于$\theta\ge k$功效已为1。故对每一正备择都最强，即UMP。
> (d) $\alpha=.10$时，要求最小边界功效$\beta(.1)\ge.8$，即$.9^n\le.3$（若$.1\ge k$则功效本已1）。取$n=12$，$k=1-.1^{1/12}\approx.174596$，$\beta(.1)=1.1-.9^{12}\approx.8175705$，因此所有$\theta>.1$均达到要求；$n=11$时边界功效约$.78619$而不足。

## 相关概念

- [[02 - 数理统计/概念/假设检验|假设检验（hypothesis testing）]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[01 - 概率论/概念/条件概率|条件概率]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 完整原题已逐页对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=361|印刷330／PDF物理361]]；原题无星号。教材信息及归档进度见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 来源已核对与独立解答写成不等于个人已完成练习；学习状态保留`not-started`。未实测Obsidian界面渲染。
