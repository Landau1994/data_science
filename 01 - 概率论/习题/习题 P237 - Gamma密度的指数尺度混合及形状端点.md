---
title: "习题 P237：Gamma密度的指数尺度混合及形状端点"
topic: "probability-theory"
topic_label: "概率论"
difficulty: "advanced"
status: "not-started"
tags: ["exercise", "probability-theory"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第4章习题4.38，印刷页162／PDF物理页193"
source_id: "DS011"
source_chapter: 4
source_exercise: "4.38"
source_stars: 0
source_refs: ["DS011 Exercise 4.38，印刷162／PDF物理193"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 P237：Gamma密度的指数尺度混合及形状端点

## 题目

### 英文原题

> [!question] 英文原题
> **4.38** (The gamma as a mixture of exponentials) Gleser (1989) shows that, in certain cases, the gamma distribution can be written as a scale mixture of exponentials, an identity suggested by different analyses of the same data. Let $f(x)$ be a gamma$(r,\lambda)$ pdf.
> (a) Show that if $r\le1$ then $f(x)$ can be written
> $$
> f(x)=\int_0^\lambda\frac1\nu e^{-x/\nu}p_\lambda(\nu)d\nu,
> $$
> where
> $$
> p_\lambda(\nu)=\frac1{\Gamma(r)\Gamma(1-r)}\frac{\nu^{r-1}}{(\lambda-\nu)^r},\quad0<\nu<\lambda.
> $$
> (Hint: Make a change of variable from $\nu$ to $u$, where $u=x/\nu-x/\lambda$.)
> (b) Show that $p_\lambda(\nu)$ is a pdf, for $r\le1$, by showing
> $$\int_0^\lambda p_\lambda(\nu)d\nu=1.$$
> (c) Show that the restriction $r\le1$ is necessary for the representation in part (a) to be valid, that is, there is no such representation if $r>1$. (Hint: Suppose $f(x)$ can be written $f(x)=\int_0^\infty(e^{-x/\nu}/\nu)q_\lambda(\nu)d\nu$ for some pdf $q_\lambda(\nu)$. Show that $\frac\partial{\partial x}\log(f(x))>0$ but $\frac\partial{\partial x}\log(\int_0^\infty(e^{-x/\nu}/\nu)q_\lambda(\nu)d\nu)<0$, a contradiction.)

### 中文转述

> [!question] 中文转述
> **原题4.38。**
> Gleser (1989) 证明，在某些情形下 Gamma 分布可以写为指数分布的尺度混合；对同一数据的不同分析启发了这一恒等式. 设 $f(x)$ 为 $\operatorname{gamma}(r,\lambda)$ 的 pdf.
>
> (a)  证明若 $r\le1$，则
>
> $$
> f(x)=\int_0^\lambda\frac1\nu e^{-x/\nu}p_\lambda(\nu)\,d\nu,
> $$
>
> 其中
>
> $$
> p_\lambda(\nu)=\frac1{\Gamma(r)\Gamma(1-r)}\frac{\nu^{r-1}}{(\lambda-\nu)^r},\qquad0<\nu<\lambda.
> $$
>
> 提示：作变量替换 $u=x/\nu-x/\lambda$.
>
> (b)  通过证明 $\int_0^\lambda p_\lambda(\nu)\,d\nu=1$，说明当 $r\le1$ 时 $p_\lambda(\nu)$ 是 pdf.
>
> (c)  证明限制 $r\le1$ 是 (a) 的表示成立的必要条件，即 $r>1$ 时不存在这种表示. 提示：假设对某个 pdf $q_\lambda(\nu)$，可写成
>
> $$
> f(x)=\int_0^\infty\frac{e^{-x/\nu}}\nu q_\lambda(\nu)\,d\nu.
> $$
>
> 证明 $\frac\partial{\partial x}\log f(x)>0$，而 $\frac\partial{\partial x}\log\left(\int_0^\infty\frac{e^{-x/\nu}}\nu q_\lambda(\nu)\,d\nu\right)<0$，产生矛盾.

## 提示

> [!hint]- 提示
> 先在$0<r<1$验证；$r=1$只能以点质量混合解释。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 尺度$\lambda>0$，Gamma要求$r>0$。
> (a) 对$0<r<1,x>0$，用$u=x/\nu-x/\lambda$，得$\nu=\lambda x/(x+\lambda u)$，$\lambda-\nu=\lambda^2u/(x+\lambda u)$。代换并化简，原混合积分为
> $$
> \frac{x^{r-1}e^{-x/\lambda}}{\lambda^r\Gamma(r)\Gamma(1-r)}\int_0^\infty e^{-u}u^{-r}du
> =\frac{x^{r-1}e^{-x/\lambda}}{\lambda^r\Gamma(r)}=f(x).
> $$
> (b) 置$t=\nu/\lambda$，积分为$B(r,1-r)/[\Gamma(r)\Gamma(1-r)]=1$。被积函数非负，故为普通密度。原文包含$r=1$，但这时$\Gamma(1-r)$无定义，公式不能作普通密度；边界对应混合测度$\delta_\lambda$，即单个尺度$\lambda$的指数分布。
> (c) 任意非负指数尺度混合在$x$上非增，因为对每个$\nu>0$，$e^{-x/\nu}/\nu$严格递减，积分保持单调。$r>1$的Gamma密度对数导数为$(r-1)/x-1/\lambda$，在$0<x<\lambda(r-1)$上为正，故在该区间递增，矛盾。此论证不需不合法的积分下求导，也适用于任意概率混合测度。原Hint称导数正未指明区间，正确矛盾只需上述非空区间。

## 相关概念

- [[01 - 概率论/概念/概率模型|概率模型]]
- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/条件概率|条件概率]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=193|印刷第162页／PDF物理第193页]]；教材信息与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。原题无星号。
- `source_status: verified`仅指本题题干、公式及所列来源定位已核对，不表示全章正文独立复证。解答写成不等于个人已完成练习，学习状态保持`not-started`；未实测Obsidian界面渲染。
