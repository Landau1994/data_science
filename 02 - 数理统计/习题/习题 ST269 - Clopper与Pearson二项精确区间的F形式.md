---
title: "习题 ST269：Clopper与Pearson二项精确区间的F形式"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第9章习题9.21，印刷页368／PDF物理页399"
source_id: "DS011"
source_chapter: 9
source_exercise: "9.21"
source_stars: 0
source_refs: ["DS011 Exercise 9.21，印刷368／PDF物理399", "DS011 Exercise 2.40，印刷67／PDF物理98；Exercise 5.17，印刷210／PDF物理241；Example 9.2.15，印刷351／PDF物理382"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST269：Clopper与Pearson二项精确区间的F形式

## 题目

### 英文原题

> [!question] 英文原题
> **9.21** In Example 9.2.15, it was shown that a confidence interval for a Poisson parameter can be expressed in terms of chi squared cutoff points. Use a similar technique to show that if $X\sim\operatorname{binomial}(n,p)$, then a $1-\alpha$ confidence interval for $p$ is
> $$
> \frac1{1+\frac{n-x+1}{x}F_{2(n-x+1),2x,\alpha/2}}
> \le p\le
> \frac{\frac{x+1}{n-x}F_{2(x+1),2(n-x),\alpha/2}}{1+\frac{x+1}{n-x}F_{2(x+1),2(n-x),\alpha/2}},
> $$
> where $F_{\nu_1,\nu_2,\alpha}$ is the upper $\alpha$ cutoff from an $F$ distribution with $\nu_1$ and $\nu_2$ degrees of freedom, and we make the endpoint adjustment that the lower endpoint is 0 if $x=0$ and the upper endpoint is 1 if $x=n$. These are the Clopper and Pearson (1934) intervals.
> (Hint: Recall the following identity from Exercise 2.40, which can be interpreted in the following way. If $X\sim\operatorname{binomial}(n,\theta)$, then $P_\theta(X\ge x)=P(Y\le\theta)$, where $Y\sim\operatorname{beta}(x,n-x+1)$. Use the properties of the $F$ and beta distributions from Chapter 5.)

### 中文转述

> [!question] 中文转述
> **原题9.21。**
> 例9.2.15表明，泊松参数的置信区间可用卡方临界点表示. 用类似技术证明，若$X\sim\operatorname{binomial}(n,p)$，则$p$的一个$1-\alpha$置信区间为
>
> $$
> \frac1{1+\frac{n-x+1}xF_{2(n-x+1),2x,\alpha/2}}\le p\le\frac{\frac{x+1}{n-x}F_{2(x+1),2(n-x),\alpha/2}}{1+\frac{x+1}{n-x}F_{2(x+1),2(n-x),\alpha/2}},
> $$
>
> 其中$F_{\nu_1,\nu_2,\alpha}$为自由度$\nu_1,\nu_2$的$F$分布的上侧$\alpha$临界点，并作如下端点调整：若$x=0$，下端点为$0$；若$x=n$，上端点为$1$. 这些就是Clopper和Pearson（1934）区间.
>
> （提示：回顾习题2.40中的恒等式，它可解释为：若$X\sim\operatorname{binomial}(n,\theta)$，则$P_\theta(X\ge x)=P(Y\le\theta)$，其中$Y\sim\operatorname{beta}(x,n-x+1)$. 使用节5中$F$分布与贝塔分布的性质.）

## 提示

> [!hint]- 提示
> 按原Hint把二项尾和写成Beta分布概率，再用两个独立卡方之比把Beta分位数改写成$F$分位数；$x=0,n$单独处理。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 教材输入与补充假设另行标明。
>
> 设$B_{a,b;u}$为$\mathrm{Beta}(a,b)$下侧$u$分位数。小尾检验反演给
> $$
> L=B_{x,n-x+1;\alpha/2},\qquad U=B_{x+1,n-x;1-\alpha/2}.
> $$
> 因为$P_p(X\ge x)=P(\mathrm{Beta}(x,n-x+1)\le p)$，$P_p(X\le x)=P(\mathrm{Beta}(x+1,n-x)\ge p)$，排除真值的两尾概率各至多$\alpha/2$，覆盖至少$1-\alpha$。
> 若$B\sim\mathrm{Beta}(a,b)$，独立$G_a,G_b$分别为形状$a,b$、同尺度Gamma，则$B=G_a/(G_a+G_b)$，$\frac ba\frac B{1-B}\sim F_{2a,2b}$。利用$F_{v,w;u}^{-1}=F_{w,v;1-u}$（此处分位用上尾记法），下端写成$[1+(b/a)F_{2b,2a,\alpha/2}]^{-1}$，上端写成$[(a/b)F_{2a,2b,\alpha/2}]/[1+(a/b)F_{2a,2b,\alpha/2}]$，代入即原式。$x=0$定义$L=0,U=1-(\alpha/2)^{1/n}$；$x=n$定义$L=(\alpha/2)^{1/n},U=1$。离散性通常使覆盖严格大于标称值。

## 相关概念

- [[02 - 数理统计/概念/区间估计|区间估计]]
- [[02 - 数理统计/概念/假设检验|假设检验]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[01 - 概率论/概念/概率模型|概率模型]]

## 备注

- 统一来源见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011教材台账]]；原题位于[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=399|印刷368／PDF物理399]]。已对照原始页面核对完整英文、分题与定位，原题无星号。
- 解答为独立推导；引用的教材结论按source_refs核对，不使用答案册代替证明。
- 来源核对、归档与个人学习分别记录；verified只指所列来源核对范围，学习状态保持not-started。未实测Obsidian渲染。
