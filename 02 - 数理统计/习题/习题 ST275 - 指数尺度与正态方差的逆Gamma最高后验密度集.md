---
title: "习题 ST275：指数尺度与正态方差的逆Gamma最高后验密度集"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第9章习题9.27，印刷页368、369／PDF物理页399、400"
source_id: "DS011"
source_chapter: 9
source_exercise: "9.27"
source_stars: 0
source_refs: ["DS011 Exercise 9.27，印刷368／PDF物理399"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST275：指数尺度与正态方差的逆Gamma最高后验密度集

## 题目

### 英文原题

> [!question] 英文原题
> **9.27** (a) Let $X_1,\ldots,X_n$ be iid observations from an $\operatorname{exponential}(\lambda)$ pdf where $\lambda$ has the conjugate $\mathrm{IG}(a,b)$ prior, an inverted gamma with pdf
> $$
> \pi(\lambda|a,b)=\frac1{\Gamma(a)b^a}\left(\frac1\lambda\right)^{a+1}e^{-1/(b\lambda)},\quad0<\lambda<\infty.
> $$
> Show how to find a $1-\alpha$ Bayes HPD credible set for $\lambda$.
> (b) Find a $1-\alpha$ Bayes HPD credible set for $\sigma^2$, the variance of a normal distribution, based on the sample variance $s^2$ and using a conjugate $\mathrm{IG}(a,b)$ prior for $\sigma^2$.
> (c) Starting with the interval from part (b), find the limiting $1-\alpha$ Bayes HPD credible set for $\sigma^2$ obtained as $a\to0$ and $b\to\infty$.

### 中文转述

> [!question] 中文转述
> **原题9.27。**
> (a)  设$X_1,\ldots,X_n$为来自$\operatorname{exponential}(\lambda)$密度的独立同分布观测，其中$\lambda$具有共轭$\operatorname{IG}(a,b)$先验，即逆伽马分布，其pdf为
>
> $$
> \pi(\lambda\mid a,b)=\frac1{\Gamma(a)b^a}\left(\frac1\lambda\right)^{a+1}e^{-1/(b\lambda)},\qquad0<\lambda<\infty.
> $$
>
> 说明如何寻找$\lambda$的$1-\alpha$贝叶斯HPD可信集.
>
> (b) 基于样本方差$s^2$，并对正态分布方差$\sigma^2$采用共轭$\operatorname{IG}(a,b)$先验，求$\sigma^2$的$1-\alpha$贝叶斯HPD可信集.
>
> (c)  从(b)的区间出发，求$a\to0$且$b\to\infty$时所得的$\sigma^2$的极限$1-\alpha$贝叶斯HPD可信集.

## 提示

> [!hint]- 提示
> 用$1/\lambda$或$1/\sigma^2$的Gamma后验确定分布，再用原参数空间中“端点后验密度相同、区间质量$1-\alpha$”定义HPD集。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 教材输入与补充假设另行标明。
>
> 统一写逆Gamma核$p(v)=D^A\Gamma(A)^{-1}v^{-A-1}e^{-D/v}$，$v>0$。它在$v_0=D/(A+1)$单峰，两端趋零，任意非零非一质量的HPD集是唯一跨众数的$[l,u]$，由
> $$
> F(u)-F(l)=1-\alpha,\qquad(A+1)\log(u/l)=D(1/l-1/u)
> $$
> 确定。可对密度阈值一维二分，每次在众数两侧求根，并由$2D/v\sim\chi^2_{2A}$计算质量；这是完整数值构造，不把倒数变换后Gamma的HPD直接倒回来（HPD不保持一般重参数化）。
> (a) 指数分布尺度似然$\lambda^{-n}e^{-\sum x_i/\lambda}$，取$A=a+n,D=1/b+\sum x_i$。
> (b) 以$S^2$的边缘似然为基础，令$\nu=n-1$，$(\nu S^2)/\sigma^2\sim\chi^2_\nu$，取$A=a+\nu/2,D=1/b+\nu s^2/2$，再用上述两方程。这里明确是“based on sample variance”的后验；若另指定均值先验、用全样本联合似然，需要重新积分干扰均值。
> (c) $A\to\nu/2,D\to\nu s^2/2$，在$n\ge2,s^2>0$时极限后验正规。区间由上述方程取这两个极限值决定，或换成枢轴端点$A_0=\nu s^2/u,B_0=\nu s^2/l$，满足卡方质量$1-\alpha$及$A_0^{\nu/2+1}e^{-A_0/2}=B_0^{\nu/2+1}e^{-B_0/2}$。它对应固定枢轴类的最短方差区间。先验极限是$1/v$非正规先验，但后验正规性已单独检查。

## 相关概念

- [[02 - 数理统计/概念/区间估计|区间估计]]
- [[02 - 数理统计/概念/假设检验|假设检验]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[01 - 概率论/概念/概率模型|概率模型]]

## 备注

- 统一来源见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011教材台账]]；原题位于[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=399|印刷368／PDF物理399]]；[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=400|印刷369／PDF物理400]]。已对照原始页面核对完整英文、分题与定位，原题无星号。
- 解答为独立推导；引用的教材结论按source_refs核对，不使用答案册代替证明。
- 来源核对、归档与个人学习分别记录；verified只指所列来源核对范围，学习状态保持not-started。未实测Obsidian渲染。
