---
title: "习题 ST177：尼罗河模型MLE校偏与两种无偏估计的风险比较"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "advanced"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第7章习题7.54，印刷页296／PDF物理页327"
source_id: "DS011"
source_chapter: 7
source_exercise: "7.54"
source_stars: 0
source_refs: ["DS011 Exercise 7.54，印刷296／PDF物理327", "DS011 习题6.37的尼罗河联合模型与T、U定义，印刷248／PDF物理279"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST177：尼罗河模型MLE校偏与两种无偏估计的风险比较

## 题目

### 英文原题

> [!question] 英文原题
> **7.54** For the “Problem of the Nile” (see Exercise 6.37),
>
> (a) Show that $T$ is the MLE of $\theta$ and $U$ is ancillary, and
> $$
> E(T)=\frac{\Gamma(n+1/2)\Gamma(n-1/2)}{[\Gamma(n)]^2}\theta\quad\text{and}\quad
> E(T^2)=\frac{\Gamma(n+1)\Gamma(n-1)}{[\Gamma(n)]^2}\theta^2.
> $$
> (b) Let $Z_1=(n-1)/\sum X_i$ and $Z_2=\sum Y_i/n$. Show that are both unbiased with variances $\theta^2/(n-2)$ and $\theta^2/n$, respectively.
>
> (c) Find the best unbiased estimator of the form $aZ_1+(1-a)Z_2$, calculate its variance, and compare it to the bias-corrected MLE.

### 中文转述

> [!question] 中文转述
> **原题7.54。** 对于“尼罗河问题”（见习题6.37），
>
> (a)  说明$T$是$\theta$的MLE，$U$是辅助统计量，并且
>
> $$
> E(T)=\frac{\Gamma(n+1/2)\Gamma(n-1/2)}{[\Gamma(n)]^2}\theta,\qquad E(T^2)=\frac{\Gamma(n+1)\Gamma(n-1)}{[\Gamma(n)]^2}\theta^2.
> $$
>
> (b)  令$Z_1=(n-1)/\sum X_i$，$Z_2=\sum Y_i/n$.说明两者均为无偏估计量，方差分别为$\theta^2/(n-2)$和$\theta^2/n$.
>
> (c)  求形如$aZ_1+(1-a)Z_2$的最佳无偏估计量，计算其方差，并将它与经偏差校正的MLE比较.

## 提示

> [!hint]- 提示
> 两个独立Gamma和的正负矩可分开算；比较时别预设线性组合优于MLE。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 6.37的联合密度为$f(x,y\mid\theta)=e^{-\theta x-y/\theta}$、$x,y>0,\theta>0$。因此$X_i$为尺度$1/\theta$的指数，$Y_i$为尺度$\theta$的指数，所有变量独立。记$A=\sum_iX_i,B=\sum_iY_i,T=\sqrt{B/A},U=\sqrt{AB}$。
>
> **(a)** $\ell=-\theta A-B/\theta$，导数$-A+B/\theta^2$在$\sqrt{B/A}$前正后负，故$T$为唯一MLE。$\theta A$与$B/\theta$独立且均为Gamma$(n,1)$，于是$U=\sqrt{(\theta A)(B/\theta)}$分布不含$\theta$，辅助性成立。
>
> 用独立Gamma矩积分，对$|s|<2n$有
> $$
> ET^s=EB^{s/2}EA^{-s/2}
> =\theta^s\frac{\Gamma(n+s/2)\Gamma(n-s/2)}{\Gamma(n)^2}.
> $$
> 取$s=1$得题中均值；取$s=2$需$n>1$，得$ET^2=n\theta^2/(n-1)$。
>
> **(b)** $n>1$时$EA^{-1}=\theta/(n-1)$，故$EZ_1=\theta$；$n>2$时$EA^{-2}=\theta^2/[(n-1)(n-2)]$，所以$\operatorname{Var}Z_1=\theta^2/(n-2)$。$EB=n\theta,\operatorname{Var}B=n\theta^2$给$EZ_2=\theta,\operatorname{Var}Z_2=\theta^2/n$。二者独立。
>
> **(c)** 以下$n>2$。方差$\theta^2[a^2/(n-2)+(1-a)^2/n]$在$a_*=(n-2)/[2(n-1)]$最小，得到
> $$
> Z_* =\frac{n-2}{2(n-1)}Z_1+\frac n{2(n-1)}Z_2,
> \qquad\operatorname{Var}Z_* =\frac{\theta^2}{2(n-1)}.
> $$
> 令$c_n=\Gamma(n+1/2)\Gamma(n-1/2)/\Gamma(n)^2$，校偏MLE为$T/c_n$，其方差
> $$
> \operatorname{Var}(T/c_n)=\left[\frac{n}{(n-1)c_n^2}-1\right]\theta^2.
> $$
> 它实际上**小于**上述最佳线性组合的方差。给出所需Gamma比不等式证明：令$q_n=c_n^2(2n-1)/(2n)$，Gamma递推给
> $$
> \frac{q_{n+1}}{q_n}=\frac{(2n-1)(2n+1)^3}{16n^3(n+1)}
> =1-\frac{4n+1}{16n^3(n+1)}<1.
> $$
> 经典Gamma版Stirling渐近给$c_n\to1$，所以$q_n\downarrow1$而$q_n>1$。因此$c_n^2>2n/(2n-1)$，代入上式即得$\operatorname{Var}(T/c_n)<\theta^2/[2(n-1)]$。这里Gamma Stirling渐近作为明确的已知分析输入；递推及比较独立完成。线性类最优不排除非线性估计改进。$n\le2$时不能使用原(b)(c)的有限方差比较。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=327|印刷第296页／PDF物理第327页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 原(b)缺少they的措辞照录；均值、二阶矩和方差各自所需n范围分别列明。
- 英文原文、中文转述与本库独立解答分别保留；实际核对正文位置列于`source_refs`。题内文献引用不表示已查阅其原文。`source_status: verified`只指本题及所列位置的核对范围，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
