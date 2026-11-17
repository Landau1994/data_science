---
title: "习题 ST225：非中心t矩密度与MLR的完整证明"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "advanced"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第8章习题8.35，印刷页330／PDF物理页361"
source_id: "DS011"
source_chapter: 8
source_exercise: "8.35"
source_stars: 0
source_refs: ["DS011 Exercise 8.35，印刷页330／PDF物理页361"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST225：非中心t矩密度与MLR的完整证明

## 题目

### 英文原题

> [!question] 英文原题
> **8.35** The usual $t$ distribution, as derived in Section 5.3.2, is also known as a central $t$ distribution. It can be thought of as the pdf of a random variable of the form $T=\mathrm n(0,1)/\sqrt{\chi_\nu^2/\nu}$, where the normal and the chi squared random variables are independent. A generalization of the $t$ distribution, the noncentral $t$, is of the form $T'=\mathrm n(\mu,1)/\sqrt{\chi_\nu^2/\nu}$, where the normal and the chi squared random variables are independent and we can have $\mu\ne0$. (We have already seen a noncentral pdf, the noncentral chi squared, in (4.4.3).) Formally, if $X\sim\mathrm n(\mu,1)$, and $Y\sim\chi_\nu^2$, independent of $X$, then $T'=X/\sqrt{Y/\nu}$ has a noncentral $t$ distribution with $\nu$ degrees of freedom and noncentrality parameter $\delta=\sqrt{\mu^2}$.
> (a) Calculate the mean and variance of $T'$.
> (b) The pdf of $T'$ is given by
> $$f_{T'}(t\mid\delta)=\frac{e^{-\delta^2/2}}{\Gamma(1/2)\Gamma(\nu/2)\sqrt\nu}\sum_{k=0}^{\infty}\frac{(2/\nu)^{k/2}(\delta t)^k}{k!}\frac{\Gamma[(\nu+k+1)/2]}{(1+t^2/\nu)^{(\nu+k+1)/2}}.$$
> Show that this pdf reduces to that of a central $t$ if $\delta=0$.
> (c) Show that the pdf of $T'$ has MLR in its noncentrality parameter.

### 中文转述

> [!question] 中文转述
> **原题8.35。**
> 节5.3.2推导的通常 $t$ 分布，也称为中心 $t$ 分布（central $t$ distribution）. 它可看成形如 $T=\mathrm n(0,1)/\sqrt{\chi_\nu^2/\nu}$ 的随机变量的密度，其中正态变量与卡方变量独立. 一种推广是非中心 $t$ 分布（noncentral $t$），形式为 $T'=\mathrm n(\mu,1)/\sqrt{\chi_\nu^2/\nu}$，正态与卡方变量独立，且允许 $\mu\ne0$. （我们已在式4.4.3见过非中心卡方密度.）正式地，若 $X\sim\mathrm n(\mu,1)$，$Y\sim\chi_\nu^2$ 且独立于 $X$，则 $T'=X/\sqrt{Y/\nu}$ 服从自由度为 $\nu$、非中心参数为 $\delta=\sqrt{\mu^2}$ 的非中心 $t$ 分布.
>
> (a)  计算 $T'$ 的均值和方差.
>
> (b)  证明 $T'$ 的密度为
>
> $$
> f_{T'}(t\mid\delta)=\frac{e^{-\delta^2/2}}{\Gamma(\frac12)\Gamma(\frac\nu2)\sqrt\nu}
> \sum_{k=0}^\infty\frac{(2/\nu)^{k/2}(\delta t)^k}{k!}
> \frac{\Gamma((\nu+k+1)/2)}{(1+t^2/\nu)^{(\nu+k+1)/2}}.
> $$
>
> 证明，当 $\delta=0$ 时，它退化为中心 $t$ 密度.
>
> (c)  证明 $T'$ 的密度关于其非中心参数具有单调似然比.

## 提示

> [!hint]- 提示
> 非中心参数必须保留正态均值符号；MLR可由辅助指数族的协方差正性证明。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 先指出源疑误：有符号变量$T'$的参数应为$\delta=\mu$；原文$\sqrt{\mu^2}$丢失符号，除非另外限制$\mu\ge0$。例如$P(T'>0)=\Phi(\mu)$，$\mu$与$-\mu$不可能同分布。以下令$\delta=\mu\in\mathbb R$、$\nu>0$。
> (a) 独立性和Gamma积分$E(Y^{-a})=2^{-a}\Gamma(\nu/2-a)/\Gamma(\nu/2)$（$\nu>2a$）给
> $$ET'=\delta\sqrt{\nu/2}\frac{\Gamma((\nu-1)/2)}{\Gamma(\nu/2)},\quad\nu>1,$$
> $$\operatorname{Var}T'=\frac{\nu(1+\delta^2)}{\nu-2}-\frac{\delta^2\nu}{2}\left[\frac{\Gamma((\nu-1)/2)}{\Gamma(\nu/2)}\right]^2,\quad\nu>2.$$
> $\nu\le1$时$E|T'|=\infty$，均值不存在（$\delta=0$的对称主值也不等于有限期望）；$1<\nu\le2$均值有限而方差无穷。
> (b) 令$S=\sqrt{Y/\nu}$，条件于$S=s$有密度$s\phi(ts-\delta)$。乘$S$密度并积分，得到常数乘$e^{-\delta^2/2}\int_0^\infty s^\nu e^{-(\nu+t^2)s^2/2+\delta ts}ds$。展开$e^{\delta ts}$后逐项积分即原级数；绝对项和以$e^{|\delta t|s}$控制，仍由二次负指数可积，故交换合法。$\delta=0$只剩$k=0$，化为$\Gamma((\nu+1)/2)/[\Gamma(\nu/2)\sqrt{\pi\nu}](1+t^2/\nu)^{-(\nu+1)/2}$，正是中心$t_\nu$。
> (c) 置$r(t)=t/\sqrt{\nu+t^2}$，严格递增。定义$A(z)=\int_0^\infty u^\nu e^{-u^2/2+zu}du$及该核归一化后的随机变量$U_z$，记$m(z)=EU_z=A'(z)/A(z)$。换元后$f_\delta(t)=C_\nu(\nu+t^2)^{-(\nu+1)/2}e^{-\delta^2/2}A(\delta r(t))$。因此对$\delta_2>\delta_1$，对数似然比对$r$的导数为$\delta_2m(\delta_2r)-\delta_1m(\delta_1r)$。
> 对核作分部积分，边界因$\nu>0$及高斯衰减为0，得到$EU_z^2=\nu+1+zEU_z$。指数族微分给$m'(z)=\operatorname{Var}U_z$，所以
> $$\frac d{dz}[zm(z)]=m(z)+z\operatorname{Var}U_z=\operatorname{Cov}(U_z^2,U_z)>0.$$
> 最后的严格正性可用独立副本写成$\frac12E[(U_z^2-U_z'^2)(U_z-U_z')]>0$；密度非退化且所有矩有限。固定$r$时$\delta\mapsto\delta m(\delta r)$的导数恰为$m(\delta r)+\delta r\operatorname{Var}U_{\delta r}>0$，包括$r=0$。故所列对数比导数严格正，复合$r'(t)>0$，证明完整有符号非中心$t$族在$t$上具有非减MLR。没有把随机序替代为更强的MLR而漏证。

## 相关概念

- [[02 - 数理统计/概念/假设检验|假设检验（hypothesis testing）]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[01 - 概率论/概念/条件概率|条件概率]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 完整原题已逐页对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=361|印刷330／PDF物理361]]；原题无星号。教材信息及归档进度见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 来源已核对与独立解答写成不等于个人已完成练习；学习状态保留`not-started`。未实测Obsidian界面渲染。
