---
title: "习题 ST293：指数尺度的UMA上限与更短期望长度反例"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第9章习题9.45，印刷页371、372／PDF物理页402、403"
source_id: "DS011"
source_chapter: 9
source_exercise: "9.45"
source_stars: 0
source_refs: ["DS011 Exercise 9.45，印刷371／PDF物理402"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST293：指数尺度的UMA上限与更短期望长度反例

## 题目

### 英文原题

> [!question] 英文原题
> **9.45** Let $X_1,\ldots,X_n$ be iid exponential($\lambda$).
> (a) Find a UMP size $\alpha$ hypothesis test of $H_0:\lambda=\lambda_0$ versus $H_1:\lambda<\lambda_0$.
> (b) Find a UMA $1-\alpha$ confidence interval based on inverting the test in part (a). Show that the interval can be expressed as
> $$
> C^*(x_1,\ldots,x_n)=\left\{\lambda:0\le\lambda\le\frac{2\sum x_i}{\chi^2_{2n,\alpha}}\right\}.
> $$
> (c) Find the expected length of $C^*(x_1,\ldots,x_n)$.
> (d) Madansky (1962) exhibited a $1-\alpha$ interval whose expected length is shorter than that of the UMA interval. In general, Madansky’s interval is difficult to calculate, but in the following situation calculation is relatively simple. Let $1-\alpha=.3$ and $n=120$. Madansky’s interval is
> $$
> C^M(x_1,\ldots,x_n)=\left\{\lambda:0\le\lambda\le-\frac{x_{(1)}}{\log(.99)}\right\},
> $$
> which is a 30% confidence interval. Use the fact that $\chi^2_{240,.7}=251.046$ to show that the 30% UMA interval satisfies
> $$
> E[\operatorname{Length}(C^*(x_1,\ldots,x_n))]=.956\lambda>E[\operatorname{Length}(C^M(x_1,\ldots,x_n))]=.829\lambda.
> $$

### 中文转述

> [!question] 中文转述
> **原题9.45。**
> 设$X_1,\ldots,X_n$独立同分布于$\operatorname{exponential}(\lambda)$.
>
> (a) 求$H_0:\lambda=\lambda_0$对$H_1:\lambda<\lambda_0$的大小为$\alpha$的UMP假设检验.
>
> (b)  反演(a)中的检验，求一个UMA $1-\alpha$置信区间. 证明该区间可表示为
>
> $$
> C^*(x_1,\ldots,x_n)=\left\{\lambda:0\le\lambda\le\frac{2\sum x_i}{\chi^2_{2n,\alpha}}\right\}.
> $$
>
> (c)  求$C^*(x_1,\ldots,x_n)$的期望长度.
>
> (d)  Madansky（1962）展示了一个期望长度比UMA区间更短的$1-\alpha$区间. 一般而言，Madansky区间难以计算，但在以下情形中计算相对简单. 令$1-\alpha=.3$，$n=120$. Madansky区间为
>
> $$
> C^{\mathrm M}(x_1,\ldots,x_n)=\left\{\lambda:0\le\lambda\le-\frac{x_{(1)}}{\log(.99)}\right\},
> $$
>
> 它是$30\%$置信区间. 利用$\chi^2_{240,.7}=251.046$这一事实，证明$30\%$ UMA区间满足
>
> $$
> \begin{aligned}
> E[\operatorname{Length}(C^*(x_1,\ldots,x_n))]&=.956\lambda\\
> &>E[\operatorname{Length}(C^{\mathrm M}(x_1,\ldots,x_n))]=.829\lambda.
> \end{aligned}
> $$

## 提示

> [!hint]- 提示
> 本书指数参数是尺度，故小尺度备择支持小总和；用$2\sum X_i/\lambda$校准后，另用$EX_{(1)}=\lambda/n$比较期望长度，并核查卡方下标约定。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 教材输入与补充假设另行标明。
>
> 设$T=\sum X_i$，$2T/\lambda\sim\chi^2_{2n}$；密度对$T$有单调似然比，向小尺度备择应拒绝小$T$。
> (a) 记$q_{v,u}$为**下侧**$u$分位，拒绝$2T/\lambda_0<q_{2n,\alpha}$，大小恰$\alpha$，由单调似然比得UMP。
> (b) 接受$2T/\lambda_0\ge q_{2n,\alpha}$，反演$(0,2T/q_{2n,\alpha}]$，端点0可形式加入不改变正尺度参数的覆盖。本书其他位置$\chi^2_{v,\alpha}$为**上侧**$\alpha$截值，故原式按该约定下标应为$1-\alpha$，原式不经说明会给错误覆盖。
> (c) 期望长度$2n\lambda/q_{2n,\alpha}$。上侧UMA只比较比真值更大的错误参数覆盖，不惩罚比真值小的候选值；因此并不保证期望长度最小。
> (d) 30%覆盖即$\alpha=.7$，需下侧$.7$分位$q_{240,.7}=250.9880967313$（原给251.046是近似但并非该精确值），期望长度系数$.9562206460$。按原区间$M=X_{(1)}$均值$\lambda/120$，覆盖率为$P(M\ge-\lambda\log.99)=.99^{120}=.2993803913$，期望长度$.8291596873\lambda$；“30%”只近似成立。若要求精确$.3$覆盖，改分母为$-\log(.3)/120$，即上限$-120M/\log(.3)$，期望长度$.8305835451\lambda$，仍严格短于$.9562206460\lambda$。因此原想说明的期望长度反例可修复成立，两个近似与分位约定均保持可见。

## 相关概念

- [[02 - 数理统计/概念/区间估计|区间估计]]
- [[02 - 数理统计/概念/假设检验|假设检验]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[01 - 概率论/概念/概率模型|概率模型]]

## 备注

- 统一来源见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011教材台账]]；原题位于[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=402|印刷371／PDF物理402]]；[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=403|印刷372／PDF物理403]]。已对照原始页面核对完整英文、分题与定位，原题无星号。
- 解答为独立推导；引用的教材结论按source_refs核对，不使用答案册代替证明。
- 来源核对、归档与个人学习分别记录；verified只指所列来源核对范围，学习状态保持not-started。未实测Obsidian渲染。
