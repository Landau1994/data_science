---
title: "习题 ST155：先验重要性重抽样的两层收敛与RaoBlackwell化"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "advanced"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第7章习题7.32，印刷页292–293／PDF物理页323,324"
source_id: "DS011"
source_chapter: 7
source_exercise: "7.32"
source_stars: 0
source_refs: ["DS011 Exercise 7.32，印刷292–293／PDF物理323,324"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST155：先验重要性重抽样的两层收敛与RaoBlackwell化

## 题目

### 英文原题

> [!question] 英文原题
> **7.32** The algorithm of Exercise 5.65 can be adapted to simulate (approximately) a sample from the posterior distribution using only a sample from the prior distribution. Let $X_1,X_2,\ldots,X_n\sim f(x\mid\theta)$, where $\theta$ has prior distribution $\pi$. Generate $\theta_1,\theta_2,\ldots,\theta_m$ from $\pi$, and calculate $q_i=L(\theta_i/\mid\mathbf x)\sum_j L(\theta_j/\mid\mathbf x)$, where $L(\theta/\mid\mathbf x)=\prod_i f(x_i\mid\theta)$ is the likelihood function.
>
> (a) Generate $\theta_1^*,\theta_2^*,\ldots,\theta_r^*$, where $P(\theta^*=\theta_i)=q_i$. Show that this is an (approximate) sample from the posterior in the sense that $P(\theta^*\le t)$ converges to $\int_{-\infty}^t\pi(\theta\mid\mathbf x)d\theta$.
>
> (b) Show that the estimator $\sum_{j=1}^r h(\theta_j^*)/r$ converges to $E[h(\theta)\mid\mathbf x]$, where the expectation is with respect to the posterior distribution.
>
> (c) Ross (1996) suggests that Rao-Blackwellization can improve the estimate in part (b). Show that for any $j$
> $$
> E[h(\theta_j^*)\mid\theta_1,\theta_2,\ldots,\theta_m]=\frac1{\sum_{i=1}^mL(\theta_i\mid\mathbf x)}\sum_{i=1}^mh(\theta_i)L(\theta_i\mid\mathbf x)
> $$
> has the same mean and smaller variance than the estimator in part (b).

### 中文转述

> [!question] 中文转述
> **原题7.32。** 习题5.65的算法可以调整，使其仅用一个先验分布样本，就能近似模拟后验分布的样本.设$X_1,X_2,\ldots,X_n\sim f(x\mid\theta)$，其中$\theta$的先验分布为$\pi$.从$\pi$生成$\theta_1,\theta_2,\ldots,\theta_m$，并计算$ q_i=L(\theta_i/\mid\boldsymbol x)\sum_jL(\theta_j/\mid\boldsymbol x)$，其中$L(\theta/\mid\boldsymbol x)=\prod_i f(x_i\mid\theta)$是似然函数.
>
> (a)  生成$\theta_1^*,\theta_2^*,\ldots,\theta_r^*$，其中$P(\theta^*=\theta_i)=q_i$.说明这是一个近似的后验样本，其意义是$P(\theta^*\le t)$收敛到$\int_{-\infty}^t\pi(\theta\mid\boldsymbol x)\,d\theta$.
>
> (b)  说明估计量$\sum_{j=1}^rh(\theta_j^*)/r$收敛到$E[h(\theta)\mid\boldsymbol x]$，其中期望针对后验分布.
>
> (c)  Ross（1996）建议用Rao--Blackwell化改进(b)中的估计.说明对于任意$j$，
>
> $$
> E[h(\theta_j^*)\mid\theta_1,\theta_2,\ldots,\theta_m]=\frac1{\sum_{i=1}^mL(\theta_i\mid\boldsymbol x)}\sum_{i=1}^mh(\theta_i)L(\theta_i\mid\boldsymbol x)
> $$
>
> 与(b)的估计量均值相同，方差较小.

## 提示

> [!hint]- 提示
> 把误差分成先验重要性样本近似与条件重抽样两层。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 固定数据$\mathbf x$，令$w(\theta)=L(\theta\mid\mathbf x)\ge0$。原题把归一化印成乘法且多出斜线；正确权重是$q_i=w_i/\sum_jw_j$。假设$\theta_i$独立同分布于正常先验$\pi$，$0<Z=E_\pi w<\infty$。若有限样本全部$w_i=0$，该次重抽样未定义；随$m\to\infty$分母除以$m$几乎必然趋$Z>0$，故最终几乎必然可定义。
>
> **(a)** 条件于先验样本，重抽分布函数为
> $$
> F_m(t)=\frac{m^{-1}\sum_iw_i\mathbf1\{\theta_i\le t\}}{m^{-1}\sum_iw_i}
> \longrightarrow\frac{E_\pi[w\mathbf1\{\theta\le t\}]}Z
> =\int_{-\infty}^t\pi(\theta\mid\mathbf x)d\theta
> $$
> 几乎必然成立，来自分子、分母的强大数定律。对每个固定$t$均成立；对分布弱收敛只需后验CDF连续点。条件于该样本的独立有放回重抽产生iid的$F_m$样本，无条件下这些重抽值共享随机经验分布，不可直接说彼此独立。
>
> **(b)** 若$E_\pi(|h|w)<\infty$，先验加权均值$H_m=\sum_iq_i h(\theta_i)$由同一比值定律几乎必然趋后验均值。固定$m$时，条件强大数定律给$\bar h_{m,r}=r^{-1}\sum_jh(\theta_j^*)\to H_m$（$r\to\infty$），故先$r\to\infty$再$m\to\infty$得到目标。固定$m$而只增加$r$通常不会消除先验样本的离散近似误差。
>
> 若进一步$E_\pi(h^2w)<\infty$，加权经验二阶矩几乎必然有有限极限。于是任意$r=r(m)\to\infty$均有$\operatorname{Var}(\bar h_{m,r}\mid\theta_{1:m})\le\sum_iq_i h(\theta_i)^2/r\to0$，条件Chebyshev再结合有界概率的支配收敛，得到联合极限下依概率收敛。
>
> **(c)** 条件期望直接等于$H_m$，而且$E(\bar h_{m,r}\mid\theta_{1:m})=H_m$。在联合二阶矩存在时，迭代期望与全方差给
> $$
> EH_m=E\bar h_{m,r},\quad
> \operatorname{Var}\bar h_{m,r}=\operatorname{Var}H_m+
> E\left[\frac1r\sum_iq_i(h(\theta_i)-H_m)^2\right]\ge\operatorname{Var}H_m.
> $$
> 严格改进需要条件加权方差以正概率大于0；$h$恒定时为等号。两估计量有限$m$时虽有相同均值，但这个均值不必恰等于真实后验均值，不能把Rao–Blackwell化等同于消除重要性比值的有限样本偏差。本题要求的是收敛与方差证明，没有另行声称执行随机模拟。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=323|印刷第292页／PDF物理第323页]]及[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=324|续页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 原归一化乘法、条件竖线前斜线照录；“smaller”说明为不增并列出严格改进条件。
- 英文原文、中文转述与本库独立解答分别保留；实际核对正文位置列于`source_refs`。题内文献引用不表示已查阅其原文。`source_status: verified`只指本题及所列位置的核对范围，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
