---
title: 习题 ST031：t与F分布的条件混合积分
topic: mathematical-statistics
topic_label: 数理统计
difficulty: intermediate
status: not-started
tags:
- exercise
- mathematical-statistics
source: George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第5章习题5.20，印刷页210/211／PDF物理页241/242
source_id: DS011
source_chapter: 5
source_exercise: '5.20'
source_stars: 0
source_refs:
- DS011 Exercise 5.20，印刷210/211／PDF物理241/242
source_status: verified
solution_status: independently-derived
created: '2026-11-13'
---

# 习题 ST031：t与F分布的条件混合积分

## 题目

### 英文原题

> [!question] 英文原题
> **5.20** (a) We can see that the $t$ distribution is a mixture of normals using the following argument:
> $$
> P(T_\nu\le t)=P\left(\frac Z{\sqrt{\chi_\nu^2/\nu}}\le t\right)=\int_0^\infty P(Z\le t\sqrt x/\sqrt\nu)P(\chi_\nu^2=x)dx,
> $$
> where $T_\nu$ is a $t$ random variable with $\nu$ degrees of freedom. Using the Fundamental Theorem of Calculus, and interpreting $P(\chi_\nu^2=\nu x)$ as a pdf, we obtain
> $$
> f_{T_\nu}(t)=\int_0^\infty\frac1{\sqrt{2\pi}}e^{-t^2x/2\nu}\frac{\sqrt x}{\sqrt\nu}\frac1{\Gamma(\nu/2)2^{\nu/2}}x^{(\nu/2)-1}e^{-x/2}dx,
> $$
> a scale mixture of normals. Verify this formula by direct integration.
>
> (b) A similar formula holds for the $F$ distribution; that is, it can be written as a mixture of chi squareds. If $F_{1,\nu}$ is an $F$ random variable with 1 and $\nu$ degrees of freedom, then we can write
> $$
> P(F_{1,\nu}\le\nu t)=\int_0^\infty P(\chi_1^2\le ty)f_\nu(y)dy,
> $$
> where $f_\nu(y)$ is a $\chi_\nu^2$ pdf. Use the Fundamental Theorem of Calculus to obtain an integral expression for the pdf of $F_{1,\nu}$, and show that the integral equals the pdf.
>
> (c) Verify that the generalization of part (b),
> $$
> P\left(F_{m,\nu}\le t\frac\nu m\right)=\int_0^\infty P(\chi_m^2\le ty)f_\nu(y)dy,
> $$
> is valid for all integers $m>1$.

### 中文转述

> [!question] 中文转述
> **原题5.20。** (a)  以下论证说明$t$分布是正态分布的混合：
>
> $$
> P(T_\nu\le t)=P\left(\frac Z{\sqrt{\chi_\nu^2/\nu}}\le t\right)=\int_0^\infty P(Z\le t\sqrt x/\sqrt\nu)P(\chi_\nu^2=x)\,dx,
> $$
>
> 其中$T_\nu$为自由度为$\nu$的$t$随机变量.利用微积分基本定理，并将$P(\chi_\nu^2=\nu x)$解释为pdf，得到
>
> $$
> f_{T_\nu}(t)=\int_0^\infty\frac1{\sqrt{2\pi}}e^{-t^2x/(2\nu)}\frac{\sqrt x}{\sqrt\nu}\frac1{\Gamma(\nu/2)2^{\nu/2}}x^{(\nu/2)-1}e^{-x/2}\,dx,
> $$
>
> 它是正态分布的尺度混合.用直接积分验证此公式.
>
> (b)  $F$分布也有类似公式，即可写成卡方分布的混合.若$F_{1,\nu}$为自由度为1和$\nu$的$F$随机变量，则
>
> $$
> P(F_{1,\nu}\le\nu t)=\int_0^\infty P(\chi_1^2\le ty)f_\nu(y)\,dy,
> $$
>
> 其中$f_\nu(y)$为$\chi_\nu^2$的pdf.用微积分基本定理得到$F_{1,\nu}$的pdf的积分表达式，并证明积分等于该pdf.
>
> (c)  验证(b)的推广
>
> $$
> P\left(F_{m,\nu}\le\frac\nu m t\right)=\int_0^\infty P(\chi_m^2\le ty)f_\nu(y)\,dy
> $$
>
> 对所有整数$m>1$成立.

## 提示

> [!hint]- 提示
> 条件于分母卡方变量，注意左边自变量的缩放导数。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 设所有比值表示式的分子、分母独立，$\nu>0$。**(a)** 被积幂为$x^{(\nu+1)/2-1}$、指数率为$(1+t^2/\nu)/2$。用$\int_0^\infty x^{a-1}e^{-bx}dx=\Gamma(a)b^{-a}$得
> $$
> f_{T_\nu}(t)=\frac{\Gamma((\nu+1)/2)}{\sqrt{\nu\pi}\Gamma(\nu/2)}(1+t^2/\nu)^{-(\nu+1)/2}.
> $$
> 严格的混合写法是$\Phi(t\sqrt{x/\nu})f_\nu(x)dx$，连续卡方的点概率并非密度；原文在解释句另写$\nu x$与该积分也不一致。
>
> **(b)** 对左边以$t$求导得到$\nu f_F(\nu t)=\int_0^\infty y f_1(ty)f_\nu(y)dy$。令$x=\nu t$，于是
> $$
> f_F(x)=\frac1\nu\int_0^\infty y f_1(xy/\nu)f_\nu(y)dy=\frac{\Gamma((\nu+1)/2)}{\sqrt\nu\,\Gamma(1/2)\Gamma(\nu/2)}x^{-1/2}(1+x/\nu)^{-(\nu+1)/2},\ x>0.
> $$
> 最后一步仍为形状$(\nu+1)/2$的Gamma积分，即$F_{1,\nu}$密度。各混合密度非负，可由Tonelli先对区间积分证明CDF公式，避免未说明的换导数。
>
> **(c)** 写$F_{m,\nu}=(A/m)/(B/\nu)$，$A\sim\chi_m^2,B\sim\chi_\nu^2$独立。则$F_{m,\nu}\le t\nu/m$当且仅当$A\le tB$，条件于$B=y$即原式。$t<0$两边均0；$t\ge0$由全概率公式成立，实际上任意实数自由度$m>0$均可。

## 相关概念

- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/期望|期望]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[02 - 数理统计/概念/参数估计|参数估计]]

## 备注

- 来源：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=241|印刷第210/211页／PDF物理第241/242页]]；版本与归档见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 原题P(χ²=x)与解释句P(χ²=νx)均原样保留；解答明确区分密度、点概率和尺度。
- 英文原题逐题对照PDF原始页面，保留原分题、提示、引用及可见疑误；原题无星号。题内引用补充与独立解答不混入原文；未查阅答案册或题内外部文献。
- 来源核对不表示个人学习完成，学习状态保持not-started。公式、链接与元数据检查不等于Obsidian实际渲染检查。
