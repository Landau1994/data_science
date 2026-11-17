---
title: "习题 ST197：移位指数与Weibull形状的干扰参数似然比"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "advanced"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第8章习题8.7，印刷页327／PDF物理页358"
source_id: "DS011"
source_chapter: 8
source_exercise: "8.7"
source_stars: 0
source_refs: ["DS011 Exercise 8.7，印刷页327／PDF物理页358", "DS011 所引正文，印刷108／PDF物理139"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST197：移位指数与Weibull形状的干扰参数似然比

## 题目

### 英文原题

> [!question] 英文原题
> **8.7** We have already seen the usefulness of the LRT in dealing with problems with nuisance parameters. We now look at some other nuisance parameter problems.
> (a) Find the LRT of
> $$H_0:\theta\le0\quad\text{versus}\quad H_1:\theta>0,$$
> based on a sample $X_1,\ldots,X_n$ from a population with probability density function $f(x\mid\theta,\lambda)=\lambda^{-1}e^{-(x-\theta)/\lambda}I_{(\theta,\infty)}(x)$, where both $\theta$ and $\lambda$ are unknown.
> (b) We have previously seen that the exponential pdf is a special case of a gamma pdf. Generalizing in another way, the exponential pdf can be considered as a special case of the Weibull$(\gamma,\beta)$. The Weibull pdf, which reduces to the exponential if $\gamma=1$, is very important in modeling reliability of systems. Suppose that $X_1,\ldots,X_n$ is a random sample from a Weibull population with both $\gamma$ and $\beta$ unknown. Find the LRT of $H_0:\gamma=1$ versus $H_1:\gamma\ne1$.

### 中文转述

> [!question] 中文转述
> **原题8.7。**
> 我们已经看到似然比检验在处理干扰参数问题时的用处. 现在考察另外一些干扰参数问题.
>
> (a)  基于来自密度为 $f(x\mid\theta,\lambda)=\lambda^{-1}e^{-(x-\theta)/\lambda}I_{(\theta,\infty)}(x)$ 的总体的样本 $X_1,\ldots,X_n$，求
>
> $$
> H_0:\theta\le0\quad\text{对}\quad H_1:\theta>0
> $$
>
> 的似然比检验，其中 $\theta,\lambda$ 都未知.
>
> (b)  前面已看到指数密度是伽马密度的特例. 沿另一方向推广，指数密度也是 $\operatorname{Weibull}(\gamma,\beta)$ 的特例：当 $\gamma=1$ 时，Weibull 密度退化为指数密度. Weibull 密度在系统可靠性建模中非常重要. 设 $X_1,\ldots,X_n$ 是来自 Weibull 总体的随机样本，$\gamma,\beta$ 均未知. 求 $H_0:\gamma=1$ 对 $H_1:\gamma\ne1$ 的似然比检验.

## 提示

> [!hint]- 提示
> 移位指数的端点取上确界；Weibull先剖面消去尺度。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** (a) 设$n\ge2$、$S=\sum X_i$、$M=\min X_i$、$D=S-nM>0$。固定$\theta<M$时尺度MLE为$(S-n\theta)/n$，剖面似然随$\theta$增加，故全参数sup在$\theta\uparrow M$，值为$(n/D)^ne^{-n}$；开支持意味着端点可能没有取得最大值。若$M\le0$，原假设也能逼近该sup，故$\lambda=1$；若$M>0$，原假设最大在$\theta=0$，$\lambda=(D/S)^n$。因此拒绝域为$M>0$且$R=nM/S>r$。在$\theta=0$下，$nM\sim\operatorname{Gamma}(1,\lambda)$与$D\sim\operatorname{Gamma}(n-1,\lambda)$独立，故$R\sim\operatorname{Beta}(1,n-1)$。对固定底层标准指数样本，$R$在其正支持上随$\theta$增加，原假设最大拒绝概率在0，取$r=1-\alpha^{1/(n-1)}$得精确大小$\alpha$。$n=1$时全似然无界，不属于此非退化推导。
> (b) 按本书习题3.24(a)约定，Weibull密度为$(\gamma/\beta)x^{\gamma-1}e^{-x^\gamma/\beta}$，$x,\gamma,\beta>0$。固定$\gamma$时$\hat\beta_\gamma=n^{-1}\sum x_i^\gamma$，剖面对数似然为
> $$\ell_p(\gamma)=n\log\gamma-n\log\left(n^{-1}\sum x_i^\gamma\right)+(\gamma-1)\sum\log x_i-n.$$
> 全形状MLE为方程$1/\gamma+\overline{\log x}-\sum x_i^\gamma\log x_i/\sum x_i^\gamma=0$的唯一正根：左端导数为$-1/\gamma^2$减加权$\log x_i$方差，严格负；非恒等样本时两端极限分别正无穷和负数。原假设下$\hat\beta_0=\bar x$。因此明确LRT为
> $$\lambda=\exp\{\ell_p(1)-\ell_p(\hat\gamma)\},\qquad\text{拒绝当 }\lambda\le c_\alpha.$$
> 这是可用一维严格单调方程实施的统计量。所有$x_i$乘同一正常数不改变比值，故原假设分布与未知尺度无关，$c_\alpha$由独立Exp$(1)$样本所诱导的该比值分布的下侧$\alpha$分位数确定；必要时在分位点随机化。不存在题面给定的$n$数值，故这里给出可精确标定的分布定义，不虚构数表。样本全等的零概率情形及$n=1$可使形状似然无界，另行排除。

## 相关概念

- [[02 - 数理统计/概念/假设检验|假设检验（hypothesis testing）]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[01 - 概率论/概念/条件概率|条件概率]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 完整原题已逐页对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=358|印刷327／PDF物理358]]；原题无星号。教材信息及归档进度见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 引用输入实际核对页：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=139|印刷108／PDF物理139]]；解答已重述所需假设及结果。
- 来源已核对与独立解答写成不等于个人已完成练习；学习状态保留`not-started`。未实测Obsidian界面渲染。
