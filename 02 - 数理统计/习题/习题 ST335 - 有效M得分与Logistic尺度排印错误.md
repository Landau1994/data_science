---
title: 习题 ST335：有效M得分与Logistic尺度排印错误
topic: mathematical-statistics
topic_label: 数理统计
difficulty: advanced
status: not-started
tags:
- exercise
- mathematical-statistics
source: George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第10章习题10.29，印刷页413／PDF物理页444
source_id: DS011
source_chapter: 10
source_exercise: '10.29'
source_stars: 0
source_refs:
- DS011 Exercise 10.29，印刷413／PDF物理444
- DS011题内依赖核对：印刷394／PDF物理425
source_status: verified
solution_status: independently-derived
created: '2026-11-13'
---

# 习题 ST335：有效M得分与Logistic尺度排印错误

## 题目

### 英文原题

> [!question] 英文原题
> **10.29** From (10.2.9) we know that an M-estimator can never be more efficient than a maximum likelihood estimator. However, we also know when it can be as efficient.
>
> (a) Show that (10.2.9) is an equality if we choose $\psi(x-\theta)=cl'(\theta\mid x)$ where $l$ is the log likelihood and $c$ is a constant.
>
> (b) For each of the following distributions, verify that the corresponding $\psi$ functions give asymptotically efficient M-estimators.
>
> (i) Normal: $f(x)=e^{-x^2/2}/\sqrt{2\pi}$, $\psi(x)=x$
>
> (ii) Logistic: $f(x)=e^{-x}/(1+e^{-x})^2$, $\psi(x)=\tanh(x)$ when $\tanh(x)$ is the hyperbolic tangent
>
> (iii) Cauchy: $f(x)=[\pi(1+x^2)]^{-1}$, $\psi(x)=2x/(1+x^2)$
>
> (iv) Least Informative Distribution:
> $$
> f(x)=\begin{cases}Ce^{-x^2/2}&|x|\le c,\\Ce^{-c|x|+c^2/2}&|x|>c,\end{cases}
> $$
> with $\psi(x)=\max\{-c,\min(c,x)\}$, and $C$ and $c$ are constants.
>
> (See Huber 1981, Section 3.5, for more details.)

### 中文转述

> [!question] 中文转述
> **原题10.29。** 由式(10.2.9)，知道$M$估计量不可能比最大似然估计量更有效. 不过，也知道何时能同样有效.
>
> (a)  证明：若取$\psi(x-\theta)=cl'(\theta\mid x)$，其中$l$为对数似然，$c$为常数，则式(10.2.9)取等号.
>
> (b)  对下列各分布，验证对应的$\psi$函数给出渐近有效的$M$估计量.
>
> (i)  正态：$f(x)=e^{-x^2/2}/\sqrt{2\pi}$，$\psi(x)=x$.
>
> (ii)  逻辑斯蒂：$f(x)=e^{-x}/(1+e^{-x})^2$，$\psi(x)=\tanh(x)$，其中$\tanh(x)$为双曲正切（hyperbolic tangent）.
>
> (iii)  柯西：$f(x)=[\pi(1+x^2)]^{-1}$，$\psi(x)=2x/(1+x^2)$.
>
> (iv)  最少信息分布（least informative distribution）：
>
> $$
> f(x)=\begin{cases}Ce^{-x^2/2},&|x|\leq c,\\Ce^{-c|x|+c^2/2},&|x|>c,\end{cases}
> $$
>
> 对应$\psi(x)=\max\{-c,\min(c,x)\}$，$C$与$c$为常数.
>
> （更多细节见Huber，1981，第3.5节.）

## 提示

> [!hint]- 提示
> 位置得分为−d log f(u)/du。Logistic的得分是tanh(u/2)，不能用常数倍把tanh(u)改成它。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 在正则、相合根及非零有限信息范围内，位置得分$s(u)=-f'(u)/f(u)$，式(10.2.9)为$\operatorname{ARE}=\{E[\psi s]\}^2/[E\psi^2\,Es^2]\le1$。
>
> **(a)** 若$\psi=cs$且$c\ne0$，分子$c^2(Es^2)^2$，分母相同，所以ARE=1。Cauchy–Schwarz等号也说明有效时应有几乎处处比例关系；$c=0$不能识别参数，不能把0/0称为等号。
>
> **(b)(i)** 正态$\log f(u)=-u^2/2+\mathrm{const}$，$s(u)=u=\psi(u)$，有效；信息1。
>
> **(ii) 原配对错误。** 标准Logistic得分$s(u)=1-2/(1+e^u)=\tanh(u/2)$，不是$\tanh u$。这两个函数的比值不恒定，原$\psi$不能达到等号。可进一步精确检验：令$S=\tanh(X/2)$，在Logistic下$S\sim U(-1,1)$，$\tanh X=2S/(1+S^2)$。于是$Es^2=1/3$，$E(\psi s)=2-\pi/2$，$E\psi^2=\pi/2-1$，所以原配对ARE为
> $$
> \frac{3(2-\pi/2)^2}{\pi/2-1}<1.
> $$
> 把$\psi(u)$修正为$\tanh(u/2)$才有效。
>
> **(iii)** Cauchy $s(u)=2u/(1+u^2)$，正是原$\psi$；$Es^2=1/2$有限，正则相合全局MLE或适当相合根具有渐近有效性。仅声明任意得分根并不保证选到相合解。
>
> **(iv)** 要求$c>0$，$C^{-1}=2\int_0^ce^{-u^2/2}du+2e^{-c^2/2}/c$。分段负对数导数分别为$u$和$c\operatorname{sign}u$，拼接一阶导数连续，故$s(u)=\operatorname{clip}(u,-c,c)=\psi(u)$，达到等号。目标损失为凸Huber损失，正常识别条件下其相合极小化点可用上述效率结果。

## 相关概念

- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/期望|期望]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[02 - 数理统计/概念/参数估计|参数估计]]

## 备注

- 来源：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=444|印刷第413页／PDF物理第444页]]；版本与归档见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 式(10.2.9)实读印刷394／PDF425。原Logistic错误原样保留；没有以不同尺度的Logistic偷换题内密度。
- 已实读本题所用正文：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=425|印刷394／PDF物理425]]；其余题内外部文献仅保留原引用，未声称查阅。
- 英文原题逐题对照PDF原始页面，保留原分题、提示、引用及可见疑误；原题无星号。题内引用补充与独立解答不混入原文；未查阅答案册或题内外部文献。
- 来源核对不表示个人学习完成，学习状态保持not-started。公式、链接与元数据检查不等于Obsidian实际渲染检查。
