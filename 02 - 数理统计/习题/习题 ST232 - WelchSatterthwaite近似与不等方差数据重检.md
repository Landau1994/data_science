---
title: "习题 ST232：WelchSatterthwaite近似与不等方差数据重检"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第8章习题8.42，印刷页332、333／PDF物理页363、364"
source_id: "DS011"
source_chapter: 8
source_exercise: "8.42"
source_stars: 0
source_refs: ["DS011 Exercise 8.42，印刷页332、333／PDF物理页363、364"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST232：WelchSatterthwaite近似与不等方差数据重检

## 题目

### 英文原题

> [!question] 英文原题
> **8.42** The assumption of equal variances, which was made in Exercise 8.41, is not always tenable. In such a case, the distribution of the statistic is no longer a $t$. Indeed, there is doubt as to the wisdom of calculating a pooled variance estimate. (This problem, of making inference on means when variances are unequal, is, in general, quite a difficult one. It is known as the Behrens–Fisher Problem.) A natural test to try is the following modification of the two-sample $t$ test: Test
> $$H_0:\mu_X=\mu_Y\quad\text{versus}\quad H_1:\mu_X\ne\mu_Y,$$
> where we do not assume that $\sigma_X^2=\sigma_Y^2$, using the statistic
> $$T'=\frac{\bar X-\bar Y}{\sqrt{S_X^2/n+S_Y^2/m}},$$
> where $S_X^2=(n-1)^{-1}\sum_{i=1}^n(X_i-\bar X)^2$ and $S_Y^2=(m-1)^{-1}\sum_{i=1}^m(Y_i-\bar Y)^2$. The distribution of $T'$ is not pleasant, but we can approximate the distribution using Satterthwaite’s approximation (Example 7.2.3).
> (a) Show that
> $$\frac{S_X^2/n+S_Y^2/m}{\sigma_X^2/n+\sigma_Y^2/m}\sim\frac{\chi_\nu^2}{\nu},\quad\text{(approximately)}$$
> where $\nu$ can be estimated with
> $$\hat\nu=\frac{(S_X^2/n+S_Y^2/m)^2}{S_X^4/[n^2(n-1)]+S_Y^4/[m^2(m-1)]}.$$
> (b) Argue that the distribution of $T'$ can be approximated by a $t$ distribution with $\hat\nu$ degrees of freedom.
> (c) Re-examine the data from Exercise 8.41 using the approximate $t$ test of this exercise, that is, test if the mean age of the core is the same as the mean age of the periphery using the $T'$ statistic.
> (d) Is there any statistical evidence that the variance of the data from the core may be different from the variance of the data from the periphery? (Recall Example 5.4.1.)

### 中文转述

> [!question] 中文转述
> **原题8.42。**
> 习题8.41的方差相等假设并非总能成立. 若不成立，统计量不再服从 $t$ 分布，计算合并方差估计是否明智也值得怀疑. （方差不等时对均值作推断，一般相当困难，称为 Behrens–Fisher 问题.）自然可尝试如下双样本 $t$ 检验的修正：不假定 $\sigma_X^2=\sigma_Y^2$，使用统计量
>
> $$
> T'=\frac{\bar X-\bar Y}{\sqrt{S_X^2/n+S_Y^2/m}}
> $$
>
> 检验 $H_0:\mu_X=\mu_Y$ 对 $H_1:\mu_X\ne\mu_Y$，其中
>
> $$
> S_X^2=\frac1{n-1}\sum_{i=1}^n(X_i-\bar X)^2,\qquad
> S_Y^2=\frac1{m-1}\sum_{i=1}^m(Y_i-\bar Y)^2.
> $$
>
> $T'$ 的精确分布不好处理，但可以用 Satterthwaite 近似（例7.2.3）来近似其分布.
>
> (a)  证明近似地有
>
> $$
> \frac{S_X^2/n+S_Y^2/m}{\sigma_X^2/n+\sigma_Y^2/m}\sim\frac{\chi_\nu^2}{\nu},
> $$
>
> 其中 $\nu$ 可由下式估计：
>
> $$
> \hat\nu=\frac{(S_X^2/n+S_Y^2/m)^2}{S_X^4/[n^2(n-1)]+S_Y^4/[m^2(m-1)]}.
> $$
>
> (b)  说明 $T'$ 的分布可用自由度为 $\hat\nu$ 的 $t$ 分布近似.
>
> (c)  用本题的近似 $t$ 检验重新考察习题8.41的数据，即用 $T'$ 检验核心的平均年代是否与外围相同.
>
> (d)  是否有统计证据表明核心数据的方差可能不同于外围数据的方差？（回顾例 5.4.1.）

## 提示

> [!hint]- 提示
> 匹配加权卡方和的前两矩，不把近似分布写成精确分布。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** (a) 令$V=S_X^2/n+S_Y^2/m$、$a=\sigma_X^2/n,b=\sigma_Y^2/m$。正态样本下$EV=a+b$，$\operatorname{Var}V=2a^2/(n-1)+2b^2/(m-1)$。用$(a+b)\chi_\nu^2/\nu$匹配均值与方差，得到$\nu=(a+b)^2/[a^2/(n-1)+b^2/(m-1)]$；将未知方差用样本方差代替即题列$\hat\nu$。这只匹配前两矩，一般不证明精确卡方分布。
> (b) 在原假设下$Z=(\bar X-\bar Y)/\sqrt{a+b}\sim N(0,1)$，且独立于两样本方差，故$T'=Z/\sqrt{V/(a+b)}$可近似$t_\nu$；以$\hat\nu$替换又加入估计误差，称Welch–Satterthwaite近似，不能宣称有限样本精确大小。
> (c) 以原表全部23项，$T'\approx-1.459884392,\hat\nu\approx20.63598587$，双侧近似$p\approx.1593789710$，$.05$水平不拒绝均值相等。
> (d) 方差相等下$F=S_X^2/S_Y^2\sim F_{13,8}$，观察$F\approx3.360014985$；按两倍较小尾概率的双侧检验，$p\approx.0920088110$。在$.05$水平证据不足，在$.10$水平会拒绝，表明结论对水平有一定敏感性；不拒绝不能证明方差相等，更不能据此保证合并$t$模型。

## 相关概念

- [[02 - 数理统计/概念/假设检验|假设检验（hypothesis testing）]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[01 - 概率论/概念/条件概率|条件概率]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 完整原题已逐页对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=363|印刷332／PDF物理363]]、[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=364|印刷333／PDF物理364]]；原题无星号。教材信息及归档进度见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 来源已核对与独立解答写成不等于个人已完成练习；学习状态保留`not-started`。未实测Obsidian界面渲染。
