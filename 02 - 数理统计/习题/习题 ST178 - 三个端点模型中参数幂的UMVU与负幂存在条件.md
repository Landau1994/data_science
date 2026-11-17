---
title: "习题 ST178：三个端点模型中参数幂的UMVU与负幂存在条件"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "advanced"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第7章习题7.55，印刷页296／PDF物理页327"
source_id: "DS011"
source_chapter: 7
source_exercise: "7.55"
source_stars: 0
source_refs: ["DS011 Exercise 7.55，印刷296／PDF物理327"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST178：三个端点模型中参数幂的UMVU与负幂存在条件

## 题目

### 英文原题

> [!question] 英文原题
> **7.55** For each of the following pdfs, let $X_1,\ldots,X_n$ be a sample from that distribution. In each case, find the best unbiased estimator of $\theta^r$. (See Guenther (1978) for a complete discussion of this problem.)
>
> (a) $f(x\mid\theta)=1/\theta$, $0<x<\theta$, $r<n$.
>
> (b) $f(x\mid\theta)=e^{-(x-\theta)}$, $x>\theta$.
>
> (c) $f(x\mid\theta)=e^{-x}/(e^{-\theta}-e^{-b})$, $\theta<x<b$, $b$ known.

### 中文转述

> [!question] 中文转述
> **原题7.55。** 对下列每个pdf，设$X_1,\ldots,X_n$是来自该分布的样本.分别求$\theta^r$的最佳无偏估计量.（Guenther（1978）对这一问题有完整讨论.）
>
> (a)  $f(x\mid\theta)=1/\theta$，$0<x<\theta$，$r<n$.
>
> (b)  $f(x\mid\theta)=e^{-(x-\theta)}$，$x>\theta$.
>
> (c)  $f(x\mid\theta)=e^{-x}/(e^{-\theta}-e^{-b})$，$\theta<x<b$，$b$已知.

## 提示

> [!hint]- 提示
> 端点充分统计量的无偏方程是一条变上限积分方程，求导即可反解。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 先按通常的非负整数幂$r$给出答案；这样(b)(c)即使$\theta$为负也有实值目标。更一般地以下公式对可定义且满足积分条件的可微$g(\theta)$成立，最后专门说明(a)负幂边界。
>
> **(a)** $M=X_{(n)}$充分，其密度$nt^{n-1}/\theta^n$。无偏方程等价于$\int_0^\theta u(t)nt^{n-1}dt=\theta^n g(\theta)$；求导得$u(t)=g(t)+tg'(t)/n$，前提是$t^ng(t)\to0$于$t\downarrow0$。对$g(t)=t^r$，
> $$
> \widehat{\theta^r}=\frac{n+r}{n}M^r.
> $$
> 直接积分$EM^r=n\theta^r/(n+r)$核对无偏。$M$完备，因为上述积分对所有$\theta$为零时求导给$u=0$几乎处处，故其有限方差无偏函数是UMVU。正幂其实无需$r<n$的上界。若原题字面允许负$r$，必须$r>-n$才有可积无偏函数，且需$r>-n/2$才有有限方差；$r\le-n$无可积无偏估计，$-n<r\le-n/2$虽有上述可积无偏函数却无有限方差无偏估计。由充分性条件化与完备性可知不能换一个估计绕过这些界限。
>
> **(b)** $T=X_{(1)}$充分，$T=\theta+E$、$E\sim\operatorname{exponential}(1/n)$。无偏方程为$g(\theta)e^{-n\theta}=\int_\theta^\infty u(t)n e^{-nt}dt$，求导给$u(t)=g(t)-g'(t)/n$；只要$g(t)e^{-nt}\to0$于无穷即可由积分回代验证。因此
> $$
> \widehat{\theta^r}=T^r-\frac r nT^{r-1}.
> $$
> $r=0$时把导数项直接视为0。若$E_\theta h(T)=0$对所有$\theta$成立，相同变上限积分求导给$h=0$，所以$T$完备；多项式目标所有矩有限，答案为UMVU。
>
> **(c)** 仍令$T=X_{(1)}$，$C_t=e^{-t}-e^{-b}$。其密度为$ne^{-t}C_t^{n-1}/C_\theta^n$，$\theta<t<b$，且充分。无偏方程$g(\theta)C_\theta^n=\int_\theta^b u(t)ne^{-t}C_t^{n-1}dt$求导，得到
> $$
> u(t)=g(t)-\frac{1-e^{t-b}}n g'(t),\qquad
> \widehat{\theta^r}=T^r-\frac r n(1-e^{T-b})T^{r-1}.
> $$
> 对多项式$g$，$g(t)C_t^n\to0$于$b$且支撑有界，故回代积分成立、二阶矩有限。同一积分求导证明$T$完备，从而UMVU。对非整数$r$须另限定使$\theta^r,T^r$为实值的参数支持，例如$0<\theta<b$；不能在任意负端点上默用实数幂。若使用一般$g$，还需相应端点消失与可积条件。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=327|印刷第296页／PDF物理第327页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 原题只写r<n不足以允许任意负幂；非整数幂在负参数上也可能未定义，解答给明确定义域与矩阈值。
- 英文原文、中文转述与本库独立解答分别保留；实际核对正文位置列于`source_refs`。题内文献引用不表示已查阅其原文。`source_status: verified`只指本题及所列位置的核对范围，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
