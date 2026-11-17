---
title: "习题 ST292：Poisson下限与logistic上限的UMA性质"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第9章习题9.44，印刷页371／PDF物理页402"
source_id: "DS011"
source_chapter: 9
source_exercise: "9.44"
source_stars: 0
source_refs: ["DS011 Exercise 9.44，印刷371／PDF物理402"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST292：Poisson下限与logistic上限的UMA性质

## 题目

### 英文原题

> [!question] 英文原题
> **9.44** (a) Let $X_1,\ldots,X_n$ be iid Poisson($\lambda$). Find a UMA $1-\alpha$ confidence interval based on inverting the UMP level $\alpha$ test of $H_0:\lambda=\lambda_0$ versus $H_1:\lambda>\lambda_0$.
> (b) Let $f(x|\theta)$ be the logistic($\theta,1$) location pdf. Based on one observation, $x$, find the UMA one-sided $1-\alpha$ confidence interval of the form $\{\theta:\theta\le U(x)\}$.

### 中文转述

> [!question] 中文转述
> **原题9.44。**
> (a)  设$X_1,\ldots,X_n$独立同分布于$\operatorname{Poisson}(\lambda)$. 反演$H_0:\lambda=\lambda_0$对$H_1:\lambda>\lambda_0$的水平$\alpha$ UMP检验，求一个UMA $1-\alpha$置信区间.
>
> (b)  设$f(x\mid\theta)$为$\operatorname{logistic}(\theta,1)$位置pdf. 基于一个观测$x$，求形式为$\{\theta:\theta\le U(x)\}$的UMA单侧$1-\alpha$置信区间.

## 提示

> [!hint]- 提示
> 逐候选参数反演适当方向的单侧UMP接受域；Poisson用总数，Logistic用位置标准化，并检查得到的是上限还是下限。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 教材输入与补充假设另行标明。
>
> (a) $Y=\sum X_i\sim\mathrm{Pois}(n\lambda)$，对$\lambda$有单调似然比，向大备择拒绝大$Y$。非随机尾检验反演下端$L(y)$由$P_{L(y)}(Y\ge y)=\alpha$确定，即$L(y)=q_{2y,\alpha}/(2n)$，$y>0$，$L(0)=0$，区间$[L(y),\infty)$。离散不随机化时覆盖至少$1-\alpha$，在相应非随机单调检验类中取紧尾界；严格跨所有检验的精确UMA结论需允许在临界计数随机化，使每个零假设检验大小恰为$\alpha$。随机化检验用额外独立均匀量反演即可得到对应随机化置信程序。原题的level不能自动当size，二者边界已区分。
> (b) $Z=X-\theta$的cdf$G(z)=(1+e^{-z})^{-1}$，密度对数严格凹，位置族有单调似然比。$H_0:\theta=\theta_0$对$\theta<\theta_0$的UMP检验拒绝$X<\theta_0+G^{-1}(\alpha)$。反演得$\theta\le X-G^{-1}(\alpha)=X+\log[(1-\alpha)/\alpha]$，覆盖恰$1-\alpha$。因每个检验对指定方向一致最强，反演后对大于真值的错误参数覆盖概率一致最小，即上侧UMA。

## 相关概念

- [[02 - 数理统计/概念/区间估计|区间估计]]
- [[02 - 数理统计/概念/假设检验|假设检验]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[01 - 概率论/概念/概率模型|概率模型]]

## 备注

- 统一来源见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011教材台账]]；原题位于[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=402|印刷371／PDF物理402]]。已对照原始页面核对完整英文、分题与定位，原题无星号。
- 解答为独立推导；引用的教材结论按source_refs核对，不使用答案册代替证明。
- 来源核对、归档与个人学习分别记录；verified只指所列来源核对范围，学习状态保持not-started。未实测Obsidian渲染。
