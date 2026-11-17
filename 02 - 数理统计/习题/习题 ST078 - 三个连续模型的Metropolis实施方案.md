---
title: 习题 ST078：三个连续模型的Metropolis实施方案
topic: mathematical-statistics
topic_label: 数理统计
difficulty: advanced
status: not-started
tags:
- exercise
- mathematical-statistics
source: George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第5章习题5.67，印刷页217／PDF物理页248
source_id: DS011
source_chapter: 5
source_exercise: '5.67'
source_stars: 0
source_refs:
- DS011 Exercise 5.67，印刷217／PDF物理248
- DS011题内依赖核对：印刷83／PDF物理114；印刷207／PDF物理238
source_status: verified
solution_status: independently-derived
created: '2026-11-13'
---

# 习题 ST078：三个连续模型的Metropolis实施方案

## 题目

### 英文原题

> [!question] 英文原题
> **5.67** In many instances the Metropolis algorithm is the algorithm of choice because either (i) there are no obvious candidate densities that satisfy the Accept/Reject supremum condition, or (ii) the supremum condition is difficult to verify, or (iii) laziness leads us to substitute computing power for brain power.
>
> For each of the following situations show how to implement a Metropolis algorithm to generate a sample of size 100 from the specified distribution.
>
> (a) $X\sim\frac1\sigma f[(x-\mu)/\sigma]$, $f=$ Student's $t$ with $\nu$ degrees of freedom, $\nu,\mu$, and $\sigma$ known.
>
> (b) $X\sim\operatorname{lognormal}(\mu,\sigma^2)$, $\mu,\sigma^2$ known.
>
> (c) $X\sim\operatorname{Weibull}(\alpha,\beta)$, $\alpha,\beta$ known.

### 中文转述

> [!question] 中文转述
> **原题5.67。** 很多情况下Metropolis算法是首选，因为：(i)没有明显满足接受／拒绝上确界条件的候选密度；或(ii)难以验证上确界条件；或(iii)懒惰促使我们用计算力代替脑力.
>
> 对以下各情形，说明如何实施Metropolis算法，从指定分布生成容量为100的样本.
>
> (a)  $X\sim\sigma^{-1}f[(x-\mu)/\sigma]$，$f$为自由度$\nu$的Student $t$分布，$\nu,\mu,\sigma$已知.
>
> (b)  $X\sim\operatorname{lognormal}(\mu,\sigma^2)$，$\mu,\sigma^2$已知.
>
> (c)  $X\sim\operatorname{Weibull}(\alpha,\beta)$，$\alpha,\beta$已知.

## 提示

> [!hint]- 提示
> 按本书独立提议的Metropolis算法操作，正变量可在log坐标实施并保留Jacobian。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 下面给出可直接实施的100个保留值流程。参数须$\nu,\sigma,\alpha,\beta>0$。使用本书独立提议形式：给定目标对数密度$\ell$与正支持候选对数密度$\ell_g$，每步独立抽$v\sim g,U\sim U(0,1)$，计算
> $$
> \log A=\min\{0,\ell(v)-\ell(z)+\ell_g(z)-\ell_g(v)\},
> $$
> 若$\log U\le\log A$接受$v$，否则保持$z$。可设预热$B=5000$、保留随后100次连续状态作为具体初始实施；这个固定预热长度不保证任何参数下都已平稳，实际应检查多起点轨迹、相关与目标分位数，并按诊断增加长度。
>
> **(a)** 在标准化坐标$Z=(X-\mu)/\sigma$运行，目标$\ell(z)=-(\nu+1)\log(1+z^2/\nu)/2$，常数相消。候选$g=N(0,1)$，$\ell_g(z)=-z^2/2$，初值$z_0=0$。执行$B+100$步，把最后100个值变成$x_i=\mu+\sigma z_i$。正常数无需求出；轻尾候选对重尾t可能混合慢，尤其小$\nu$，可改独立柯西候选并在接受率中使用其密度。
>
> **(b)** 在$Z=\log X$坐标运行。目标变换密度$f_X(e^z)e^z$恰为$N(\mu,\sigma^2)$，故$\ell(z)=-(z-\mu)^2/(2\sigma^2)$。取独立候选$g=N(\mu,4\sigma^2)$，初值$z_0=\mu$，使用其$\ell_g(z)=-(z-\mu)^2/(8\sigma^2)$，最后输出$e^{z_i}$。这是合法MH；已知该模型也可直接抽正态取指数，题目这里要求说明MH实施，不称其必要。
>
> **(c)** 原书式(3.3.12)把Weibull第一参数作为形状、第二参数作为幂变换尺度：$f_X(x)=(\alpha/\beta)x^{\alpha-1}e^{-x^\alpha/\beta}$。在$Z=\log X$坐标，目标对数密度（略常数）为$\ell(z)=\alpha z-e^{\alpha z}/\beta$，Jacobian$e^z$已包含。取独立$g=N(\log\beta/\alpha,4/\alpha^2)$，初值$z_0=\log\beta/\alpha$，用$\ell_g(z)=-\alpha^2(z-\log\beta/\alpha)^2/8$计算接受率，保留后输出$e^{z_i}$。在数值上用对数接受率，极大$z$使$e^{\alpha z}$溢出时按$\ell=-\infty$拒绝即可。
>
> 上述输出有序列依赖，不能声称100个精确iid样本；目标分布是平稳分布，有限预热后只是近似。本题未给具体参数数值，因此给出对所有合法参数完整的实施公式，而不是虚构特定100个运行值。

## 相关概念

- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/期望|期望]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/重采样|重采样]]

## 备注

- 来源：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=248|印刷第217页／PDF物理第248页]]；版本与归档见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 实读本书Metropolis步骤：印刷207／PDF238；Weibull参数化实读印刷83／PDF114式(3.3.12)。正变量的log坐标Jacobian未省略。
- 已实读本题所用正文：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=114|印刷83／PDF物理114]]；[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=238|印刷207／PDF物理238]]；其余题内外部文献仅保留原引用，未声称查阅。
- 英文原题逐题对照PDF原始页面，保留原分题、提示、引用及可见疑误；原题无星号。题内引用补充与独立解答不混入原文；未查阅答案册或题内外部文献。
- 来源核对不表示个人学习完成，学习状态保持not-started。公式、链接与元数据检查不等于Obsidian实际渲染检查。
