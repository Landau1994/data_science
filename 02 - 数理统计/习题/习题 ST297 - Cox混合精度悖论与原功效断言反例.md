---
title: "习题 ST297：Cox混合精度悖论与原功效断言反例"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第9章习题9.49，印刷页372／PDF物理页403"
source_id: "DS011"
source_chapter: 9
source_exercise: "9.49"
source_stars: 0
source_refs: ["DS011 Exercise 9.49，印刷372／PDF物理403"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST297：Cox混合精度悖论与原功效断言反例

## 题目

### 英文原题

> [!question] 英文原题
> **9.49** (Cox’s Paradox) We are to test
> $$
> H_0:\theta=\theta_0\quad\text{versus}\quad H_1:\theta>\theta_0,
> $$
> where $\theta$ is the mean of one of two normal distributions and $\theta_0$ is a fixed but arbitrary value of $\theta$. We observe the random variable $X$ with distribution
> $$
> X\sim\begin{cases}n(\theta,100)&\text{with probability }p,\\n(\theta,1)&\text{with probability }1-p.\end{cases}
> $$
> (a) Show that the test given by reject $H_0$ if $X>\theta_0+z_\alpha\sigma$, where $\sigma=1$ or 10, depending on which population is sampled, is a level $\alpha$ test. Derive a $1-\alpha$ confidence set by inverting the acceptance region of this test.
> (b) Show that a more powerful level $\alpha$ test (for $\alpha>p$) is given by reject $H_0$ if $X>\theta_0+z_{(\alpha-p)/(1-p)}$ and $\sigma=1$, otherwise always reject $H_0$.
> Derive a $1-\alpha$ confidence set by inverting the acceptance region of this test, and show that it is the empty set with positive probability. (Cox’s Paradox states that classic optimal procedures sometimes ignore the information about conditional distributions, and provide us with a procedure that, while optimal, is somehow unreasonable; see Cox 1958 or Cornfield 1969.)

### 中文转述

> [!question] 中文转述
> **原题9.49。**
> **Cox悖论。**
> 我们要检验
>
> $$
> H_0:\theta=\theta_0\qquad\text{对}\qquad H_1:\theta>\theta_0,
> $$
>
> 其中$\theta$为两个正态分布之一的均值，$\theta_0$是$\theta$的一个固定但任意的值. 观测到随机变量$X$，其分布为
>
> $$
> X\sim\begin{cases}\mathrm n(\theta,100),&\text{概率为 }p,\\\mathrm n(\theta,1),&\text{概率为 }1-p.\end{cases}
> $$
>
> (a)  证明以下检验是水平$\alpha$检验：
>
> $$
> \text{若 }X>\theta_0+z_\alpha\sigma,\text{ 则拒绝 }H_0,
> $$
>
> 其中$\sigma=1$或$10$取决于从哪个总体抽样. 反演这个检验的接受域，导出$1-\alpha$置信集.
>
> (b)  证明一个功效更高的水平$\alpha$检验（对$\alpha>p$）为
>
> $$
> \begin{gathered}
> \text{若 }X>\theta_0+z_{(\alpha-p)/(1-p)}\text{ 且 }\sigma=1,\text{ 则拒绝 }H_0,\\
> \text{否则总是拒绝 }H_0.
> \end{gathered}
> $$
>
> 反演该检验的接受域导出$1-\alpha$置信集，并证明它以正概率为空集.（Cox悖论指出，经典最优程序有时忽略条件分布的信息，给出一个虽最优、却在某种意义上不合理的程序；参见Cox 1958或Cornfield 1969.）

## 提示

> [!hint]- 提示
> 把已观察的$\sigma=1$或10作为混合实验标签，分别计算条件拒绝概率再加权；核查(b)的“otherwise”解释及其是否真在所有备择更强。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 教材输入与补充假设另行标明。
>
> 设$0<p<\alpha<1$，抽样总体标识可观察且不含$\theta$信息。
> (a) 条件于每个$\sigma$的拒绝概率都为$\alpha$，故混合后也是$\alpha$。接受$X\le\theta_0+z_\alpha\sigma$，反演下置信集$[X-z_\alpha\sigma,\infty)$。
> (b) 取$\beta=(\alpha-p)/(1-p)$。按题意“otherwise always reject”理解为$\sigma=10$时总拒绝、$\sigma=1$时使用所列阈值；若把otherwise理解为包括阈值不满足也拒绝，则会变为处处拒绝，显然不是水平检验。正确分支下零假设拒绝概率$p+(1-p)\beta=\alpha$。反演为：$\sigma=1$时$[X-z_\beta,\infty)$，$\sigma=10$时空集，故空集概率$p>0$；无条件覆盖$1-\alpha$，大方差分支条件覆盖0。
> 但“more powerful”并非对所有备择成立。令$\delta=\theta-\theta_0>0$，两检验功效分别为
> $$
> \pi_A(\delta)=p\,\overline\Phi(z_\alpha-\delta/10)+(1-p)\overline\Phi(z_\alpha-\delta),
> \quad\pi_B(\delta)=p+(1-p)\overline\Phi(z_\beta-\delta).
> $$
> 实际取$p=.04,\alpha=.05,\delta=.01$，得$\pi_A=.05100240196$、$\pi_B=.05026821793$，原建议反而较弱。其在足够远备择可改善，也能展示无条件规则产生空集的现象，但不能冒称统一更有力或无条件最优。此反例由确定性正态积分计算，结果已保留。

## 相关概念

- [[02 - 数理统计/概念/区间估计|区间估计]]
- [[02 - 数理统计/概念/假设检验|假设检验]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[01 - 概率论/概念/概率模型|概率模型]]

## 备注

- 统一来源见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011教材台账]]；原题位于[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=403|印刷372／PDF物理403]]。已对照原始页面核对完整英文、分题与定位，原题无星号。
- 解答为独立推导；引用的教材结论按source_refs核对，不使用答案册代替证明。
- 来源核对、归档与个人学习分别记录；verified只指所列来源核对范围，学习状态保持not-started。未实测Obsidian渲染。
