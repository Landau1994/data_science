---
title: "习题 ST243：点零假设Bayes后验与Lindley悖论"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "advanced"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第8章习题8.53，印刷页334、335／PDF物理页365、366"
source_id: "DS011"
source_chapter: 8
source_exercise: "8.53"
source_stars: 0
source_refs: ["DS011 Exercise 8.53，印刷页334、335／PDF物理页365、366"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST243：点零假设Bayes后验与Lindley悖论

## 题目

### 英文原题

> [!question] 英文原题
> **8.53** In Example 8.2.7, we saw an example of a one-sided Bayesian hypothesis test. Now we will consider a similar situation, but with a two-sided test. We want to test
> $$H_0:\theta=0\quad\text{versus}\quad H_1:\theta\ne0,$$
> and we observe $X_1,\ldots,X_n$, a random sample from a n$(\theta,\sigma^2)$ population, $\sigma^2$ known. A type of prior distribution that is often used in this situation is a mixture of a point mass on $\theta=0$ and a pdf spread out over $H_1$. A typical choice is to take $P(\theta=0)=1/2$, and if $\theta\ne0$, take the prior distribution to be $\tfrac12\mathrm n(0,\tau^2)$, where $\tau^2$ is known.
> (a) Show that the prior defined above is proper, that is, $P(-\infty<\theta<\infty)=1$.
> (b) Calculate the posterior probability that $H_0$ is true, $P(\theta=0\mid x_1,\ldots,x_n)$.
> (c) Find an expression for the p-value corresponding to a given value of $\bar x$.
> (d) For the special case $\sigma^2=\tau^2=1$, compare $P(\theta=0\mid x_1,\ldots,x_n)$ and the p-value for a range of values of $\bar x$. In particular,
> (i) For $n=9$, plot the p-value and posterior probability as a function of $\bar x$, and show that the Bayes probability is bigger than the p-value for moderately large values of $\bar x$.
> (ii) Now, for $\alpha=.05$, set $\bar x=z_{\alpha/2}/\sqrt n$, fixing the p-value at $\alpha$ for all $n$. Show that the posterior probability at $\bar x=z_{\alpha/2}/\sqrt n$ goes to 1 as $n\to\infty$. This is Lindley’s Paradox.
> Note that small values of $P(\theta=0\mid x_1,\ldots,x_n)$ are evidence against $H_0$, and thus this quantity is similar in spirit to a p-value. The fact that these two quantities can have very different values was noted by Lindley (1957), and is also examined by Berger and Sellke (1987). (See the Miscellanea section.)

### 中文转述

> [!question] 中文转述
> **原题8.53。**
> 例8.2.7给出了单侧贝叶斯假设检验的例子. 现在考虑类似情形，但使用双侧检验. 希望检验
>
> $$
> H_0:\theta=0\quad\text{对}\quad H_1:\theta\ne0,
> $$
>
> 观察来自 $\mathrm n(\theta,\sigma^2)$ 总体的随机样本 $X_1,\ldots,X_n$，$\sigma^2$ 已知. 此时常用的一类先验是 $\theta=0$ 处的点质量与分散在 $H_1$ 上的密度的混合. 典型选择为 $P(\theta=0)=1/2$，当 $\theta\ne0$ 时，取先验分布为 $\frac12\mathrm n(0,\tau^2)$，$\tau^2$ 已知.
>
> (a)  证明上述先验正常，即 $P(-\infty<\theta<\infty)=1$.
>
> (b)  计算 $H_0$ 为真的后验概率 $P(\theta=0\mid x_1,\ldots,x_n)$.
>
> (c)  求对应于给定 $\bar x$ 值的 $p$ 值表达式.
>
> (d)  当 $\sigma^2=\tau^2=1$ 时，在一段 $\bar x$ 取值范围上比较 $P(\theta=0\mid x_1,\ldots,x_n)$ 与 $p$ 值. 特别地，
>
> (i)  对 $n=9$，把 $p$ 值和后验概率作为 $\bar x$ 的函数作图，证明在 $\bar x$ 适度偏大时，贝叶斯概率大于 $p$ 值.
>
> (ii)  取 $\alpha=.05$，令 $\bar x=Z_{\alpha/2}/\sqrt n$，使所有 $n$ 下的 $p$ 值都固定为 $\alpha$. 证明当 $n\to\infty$ 时，在 $\bar x=Z_{\alpha/2}/\sqrt n$ 处的后验概率趋于 $1$. 这就是 Lindley 悖论（Lindley's Paradox）.
>
> 注意，$P(\theta=0\mid x_1,\ldots,x_n)$ 的小值是反对 $H_0$ 的证据，因此这个量在意义上类似于 $p$ 值. Lindley (1957) 指出了这两个量可能差别很大，Berger and Sellke (1987) 也考察了这一事实（见节8.5的杂录）.

## 提示

> [!hint]- 提示
> 点质量与连续密度通过各自边缘似然更新，不能把点零假设当连续先验下的普通事件。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** (a) 精确先验测度为$\pi=\frac12\delta_0+\frac12N(0,\tau^2)$，总质量$1/2+(1/2)\int\phi_{\tau^2}=1$。原文“if”后的$\frac12N$表示连续部分的未归一化质量，不是一个条件分布自身只有半质量。
> (b) 令$v=\sigma^2/n,m=\bar x$。在点零假设下$m\sim N(0,v)$，连续成分积分正态均值得$m\sim N(0,v+\tau^2)$；样本残差因子两边相同相消。等先验赔率给
> $$P(H_0\mid x)=\left[1+\sqrt{\frac v{v+\tau^2}}\exp\left\{\frac{m^2\tau^2}{2v(v+\tau^2)}\right\}\right]^{-1}.$$
> (c) 经典双侧$p$值为$2\Phi(-|m|/\sqrt v)$。
> (d)(i) 当两方差为1，后验为$[1+(n+1)^{-1/2}e^{n^2m^2/[2(n+1)]}]^{-1}$，$p=2\Phi(-\sqrt n|m|)$。$n=9$图见下：例如$m=.5$时后验约$.535$而$p\approx.1336$，$m=1$时后验约$.0522$而$p\approx.00270$，展示中等偏离时的差距；$m=0$后验小于$p=1$，不声称所有$m$都较大。
>
> ![[附件/习题图/DS011/习题8.53-Lindley比较.png]]
>
> (ii) 令$z=z_{.025}$、$m=z/\sqrt n$，则$p=.05$恒定，而后验为$[1+(n+1)^{-1/2}e^{nz^2/[2(n+1)]}]^{-1}\to1$。因为指数项趋有限正数$e^{z^2/2}$，前因子趋0。这里数据序列随$n$变化，不能误解为固定非零效应下后验仍趋向原假设。

## 相关概念

- [[02 - 数理统计/概念/假设检验|假设检验（hypothesis testing）]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[01 - 概率论/概念/条件概率|条件概率]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 完整原题已逐页对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=365|印刷334／PDF物理365]]、[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=366|印刷335／PDF物理366]]；原题无星号。教材信息及归档进度见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 本题图件按解答公式独立绘制并保留[[附件/习题图/DS011/习题8.53-Lindley比较.pdf|矢量PDF]]及[[附件/习题图/DS011/源码/第8章/ch08_53.tex|可编辑绘图源文件]]；数据为公式数值采样，不是随机模拟。
- 来源已核对与独立解答写成不等于个人已完成练习；学习状态保留`not-started`。未实测Obsidian界面渲染。
