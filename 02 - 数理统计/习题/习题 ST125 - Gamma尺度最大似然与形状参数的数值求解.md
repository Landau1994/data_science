---
title: "习题 ST125：Gamma尺度最大似然与形状参数的数值求解"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "advanced"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第7章习题7.2，印刷页287／PDF物理页318"
source_id: "DS011"
source_chapter: 7
source_exercise: "7.2"
source_stars: 0
source_refs: ["DS011 Exercise 7.2，印刷287／PDF物理318", "DS011 Gamma尺度密度式(3.3.6)，印刷81／PDF物理112"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST125：Gamma尺度最大似然与形状参数的数值求解

## 题目

### 英文原题

> [!question] 英文原题
> **7.2** Let $X_1,\ldots,X_n$ be a random sample from a gamma$(\alpha,\beta)$ population.
>
> (a) Find the MLE of $\beta$, assuming $\alpha$ is known.
>
> (b) If $\alpha$ and $\beta$ are both unknown, there is no explicit formula for the MLEs of $\alpha$ and $\beta$, but the maximum can be found numerically. The result in part (a) can be used to reduce the problem to the maximization of a univariate function. Find the MLEs for $\alpha$ and $\beta$ for the data in Exercise 7.10(c).

### 中文转述

> [!question] 中文转述
> **原题7.2。** 设$X_1,\ldots,X_n$为来自$\operatorname{gamma}(\alpha,\beta)$总体的随机样本.
>
> (a)  假设$\alpha$已知，求$\beta$的MLE.
>
> (b)  若$\alpha$与$\beta$均未知，其MLE没有显式公式，但可通过数值方法寻找最大值.利用(a)的结果，可以把问题化为一元函数的极大化.对习题7.10(c)的数据，求$\alpha$和$\beta$的MLE.

## 提示

> [!hint]- 提示
> 先对尺度求导，再代回，把二维优化化为一条形状方程。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 本书用尺度参数$\beta$：$f(x)=x^{\alpha-1}e^{-x/\beta}/[\Gamma(\alpha)\beta^\alpha]$，$x>0$。
>
> **(a)** 记$S=\sum_i x_i$、$H=\sum_i\log x_i$。对数似然为
> $$
> \ell=(\alpha-1)H-S/\beta-n\alpha\log\beta-n\log\Gamma(\alpha).
> $$
> $\partial_\beta\ell=(S-n\alpha\beta)/\beta^2$，在$\beta=S/(n\alpha)$前正后负，故唯一全局MLE为$\widehat\beta=\bar X/\alpha$。
>
> **(b)** 代入(a)后得到剖面对数似然（profile log likelihood）
> $$
> \ell_p(\alpha)=(\alpha-1)H-n\alpha-n\alpha\log(\bar x/\alpha)-n\log\Gamma(\alpha).
> $$
> 令$\psi=\Gamma'/\Gamma$，驻点方程为
> $$
> \log\widehat\alpha-\psi(\widehat\alpha)=\log\bar x-H/n=:d.
> $$
> 对非全等的正数据，Jensen不等式给$d>0$。函数$\log a-\psi(a)$严格递减且从$+\infty$降至0：例如$\psi'(a)=\sum_{j\ge0}(a+j)^{-2}>\int_0^\infty(a+t)^{-2}dt=1/a$，端点可由Gamma递推及Stirling渐近得到。这些Gamma函数性质为明确使用的分析输入；它们保证唯一根，且$\ell_p'$在根前正后负。
>
> 原题7.10(c)的14个卵长依次为22.0、23.9、20.9、23.8、25.0、24.0、21.7、23.8、22.8、23.1、23.1、23.5、23.0、23.0。实际计算$\bar x=23.1142857142857$、$H/n=3.13947841231488$，得到
> $$
> \widehat\alpha=514.3354320691,\qquad\widehat\beta=0.0449400999291.
> $$
> 已执行[[工具/StatisticalInference/ch07_numeric_checks.py|确定性数值核验]]，根方程残差约$4.44\times10^{-16}$；环境和数据存于[[工具/StatisticalInference/ch07-numeric-results.json|实际结果]]。这只是该数据的有限精度求解。若全部数据相等，则$d=0$、形状趋无穷，通常没有有限的双参数MLE。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=318|印刷第287页／PDF物理第318页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 英文原文、中文转述与本库独立解答分别保留；实际核对正文位置列于`source_refs`。题内文献引用不表示已查阅其原文。`source_status: verified`只指本题及所列位置的核对范围，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
