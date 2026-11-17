---
title: "习题 ST276：正态逆Gamma共轭与经典均值区间的极限障碍"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第9章习题9.28，印刷页369／PDF物理页400"
source_id: "DS011"
source_chapter: 9
source_exercise: "9.28"
source_stars: 0
source_refs: ["DS011 Exercise 9.28，印刷369／PDF物理400"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST276：正态逆Gamma共轭与经典均值区间的极限障碍

## 题目

### 英文原题

> [!question] 英文原题
> **9.28** Let $X_1,\ldots,X_n$ be iid $n(\theta,\sigma^2)$, where both $\theta$ and $\sigma^2$ are unknown, but there is only interest on inference about $\theta$. Consider the prior pdf
> $$
> \pi(\theta,\sigma^2|\mu,\tau^2,a,b)=\frac1{\sqrt{2\pi\tau^2\sigma^2}}e^{-(\theta-\mu)^2/(2\tau^2\sigma^2)}\frac1{\Gamma(a)b^a}\left(\frac1{\sigma^2}\right)^{a+1}e^{-1/(b\sigma^2)},
> $$
> a $n(\mu,\tau^2\sigma^2)$ multiplied by an $\mathrm{IG}(a,b)$.
> (a) Show that this prior is a conjugate prior for this problem.
> (b) Find the posterior distribution of $\theta$ and use it to construct a $1-\alpha$ credible set for $\theta$.
> (c) The classical $1-\alpha$ confidence set for $\theta$ can be expressed as
> $$
> \left\{\theta:|\theta-\bar x|^2\le F_{1,n-1,\alpha/2}\frac{s^2}{n}\right\}.
> $$
> Is there any (limiting) sequence of $\tau^2,a,$ and $b$ that would allow this set to be approached by a Bayes set from part (b)?

### 中文转述

> [!question] 中文转述
> **原题9.28。**
> 设$X_1,\ldots,X_n$独立同分布于$\mathrm n(\theta,\sigma^2)$，其中$\theta,\sigma^2$均未知，但只关心关于$\theta$的推断. 考虑先验pdf
>
> $$
> \pi(\theta,\sigma^2\mid\mu,\tau^2,a,b)=\frac1{\sqrt{2\pi\tau^2\sigma^2}}e^{-(\theta-\mu)^2/(2\tau^2\sigma^2)}\frac1{\Gamma(a)b^a}\left(\frac1{\sigma^2}\right)^{a+1}e^{-1/(b\sigma^2)},
> $$
>
> 即$\mathrm n(\mu,\tau^2\sigma^2)$乘以$\operatorname{IG}(a,b)$.
>
> (a)  证明这个先验是该问题的共轭先验.
>
> (b) 求$\theta$的后验分布，并用它构造$\theta$的$1-\alpha$可信集.
>
> (c)  $\theta$的经典$1-\alpha$置信集可以表示为
>
> $$
> \left\{\theta:|\theta-\bar x|^2\le F_{1,n-1,\alpha/2}\frac{s^2}n\right\}.
> $$
>
> 是否存在$\tau^2,a,b$的某个（极限）序列，使(b)中的贝叶斯集合逼近这个集合？

## 提示

> [!hint]- 提示
> 先对$\sum(x_i-\theta)^2+\tau^{-2}(\theta-\mu)^2$配方；积分方差得到Student分布后，再比较自由度及半宽关于残差平方和的系数。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 教材输入与补充假设另行标明。
>
> 取$n\ge2$、$Q=\sum(x_i-\bar x)^2>0$（非退化正态模型下几乎处处），设$\kappa_0=1/\tau^2$，$\kappa_n=\kappa_0+n$，$m_n=(\kappa_0\mu+n\bar x)/\kappa_n$。平方配方为
> $$
> \sum(x_i-\theta)^2+\kappa_0(\theta-\mu)^2
> =Q+\frac{n\kappa_0}{\kappa_n}(\bar x-\mu)^2+\kappa_n(\theta-m_n)^2.
> $$
> (a) 因而$\theta\mid v,x\sim N(m_n,v/\kappa_n)$，$v\mid x\sim\mathrm{InvGamma}(A,D)$，其中$A=a+n/2$，$D=1/b+\{Q+n\kappa_0(\bar x-\mu)^2/\kappa_n\}/2$，逆Gamma采用$D^Av^{-A-1}e^{-D/v}/\Gamma(A)$。仍属相同共轭族。
> (b) 积分$v$得$(\theta-m_n)/\sqrt{D/(A\kappa_n)}\mid x\sim t_{2A}$。故等尾且HPD区间为$m_n\pm t_{2A,\alpha/2}\sqrt{D/(A\kappa_n)}$。
> (c) 先记录排印问题：本书$F_{v,w,u}$为上尾$u$分位，$t_{\nu,\alpha/2}^2=F_{1,\nu,\alpha}$，不是$F_{1,\nu,\alpha/2}$。原式按字面覆盖$1-\alpha/2$，正确经典$1-\alpha$区间应改用$F_{1,n-1,\alpha}$。
> 在正规先验$a,b,\tau^2>0$下，若希望以不依赖观测数据的先验序列、对所有数据逼近经典中心$\bar x$，必须$\kappa_0\to0$。下面给出半宽不能逼近的严格论证，而不只比较自由度名称。记$\nu=2A=n+2a\ge n$，后验半宽平方为$t_{\nu,\alpha/2}^2D/(A\kappa_n)$。固定$\bar x$、取两个不同的正$Q$，其关于$Q$的斜率恰为
> $$
> K=\frac{t_{\nu,\alpha/2}^2}{\nu\kappa_n}.
> $$
> 对$\nu_2>\nu_1>0$，可耦合$V_{\nu_2}=V_{\nu_1}+W$，其中$V_{\nu_1}\sim\chi^2_{\nu_1}$、$W\sim\chi^2_{\nu_2-\nu_1}$独立且$W>0$。取同一独立$|Z|$，则$|Z|/\sqrt{V_{\nu_2}}<|Z|/\sqrt{V_{\nu_1}}$几乎处处；因此$t_{\nu,\alpha/2}/\sqrt\nu$的相应正分位数随$\nu$严格下降。于是$K\le t_{n,\alpha/2}^2/(n\kappa_n)\to t_{n,\alpha/2}^2/n^2$，严格小于经典半宽平方关于$Q$的斜率$t_{n-1,\alpha/2}^2/[n(n-1)]$。任意数据无关的加性先验项都无法同时修复两个不同$Q$的这个差距，所以正规序列不能作为整个区间规则逼近经典$t_{n-1}$区间。
> 例如再令$a\to0,b\to\infty$只得到自由度$n$的更窄区间。形式上$a\to-1/2$才使后验自由度为$n-1$并给出经典尺度，但这不是正$a$正规先验族的序列；它对应另行选择联合非正规先验$\pi(\theta,v)\propto1/v$。原文误标的$F_{1,n-1,\alpha/2}$区间更宽，同样受上述斜率界阻碍。这里排除的是一组先验序列对所有数据的统一规则逼近，不排除针对某一个已观察样本事后调参数凑出相同端点。

## 相关概念

- [[02 - 数理统计/概念/区间估计|区间估计]]
- [[02 - 数理统计/概念/假设检验|假设检验]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[01 - 概率论/概念/概率模型|概率模型]]

## 备注

- 统一来源见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011教材台账]]；原题位于[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=400|印刷369／PDF物理400]]。已对照原始页面核对完整英文、分题与定位，原题无星号。
- 解答为独立推导；引用的教材结论按source_refs核对，不使用答案册代替证明。
- 来源核对、归档与个人学习分别记录；verified只指所列来源核对范围，学习状态保持not-started。未实测Obsidian渲染。
