---
title: "习题 ST168：样本方差缩放的最优MSE及峰度符号勘误"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "advanced"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第7章习题7.45，印刷页294／PDF物理页325"
source_id: "DS011"
source_chapter: 7
source_exercise: "7.45"
source_stars: 0
source_refs: ["DS011 Exercise 7.45，印刷294／PDF物理325", "DS011 例7.3.4正态方差的MSE比较，印刷268／PDF物理299", "DS011 Stein引理3.6.5，印刷102／PDF物理133"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST168：样本方差缩放的最优MSE及峰度符号勘误

## 题目

### 英文原题

> [!question] 英文原题
> **7.45** Let $X_1,X_2,\ldots,X_n$ be iid from a distribution with mean $\mu$ and variance $\sigma^2$, and let $S^2$ be the usual unbiased estimator of $\sigma^2$. In Example 7.3.4 we saw that, under normality, the MLE has smaller MSE than $S^2$. In this exercise, we will explore variance estimates some more.
>
> (a) Show that, for any estimator of the form $aS^2$, where $a$ is a constant,
> $$
> \operatorname{MSE}(aS^2)=E[aS^2-\sigma^2]^2=a^2\operatorname{Var}(S^2)+(a-1)^2\sigma^4.
> $$
> (b) Show that
> $$
> \operatorname{Var}(S^2)=\frac1n\left(\kappa-\frac{n-3}{n-1}\sigma^4\right),
> $$
> where $\kappa=E[X-\mu]^4$ is the kurtosis. (You may have already done this in Exercise 5.8b.)
>
> (c) Show that, under normality the kurtosis is $3\sigma^4$ and establish that, in this case, the estimator of the form $aS^2$ with the minimum MSE is $\frac{n-1}{n+1}S^2$. (Lemma 3.6.5 may be helpful.)
>
> (d) If normality is not assumed, show that $\operatorname{MSE}(aS^2)$ is minimized at $a=\frac{n-1}{(n+1)+\frac{(\kappa-1)(n-1)}n}$, which is useless as it depends on a parameter.
>
> (e) Show that
>
> i. for distributions with $\kappa>3$, the optimal $a$ will satisfy $a<\frac{n-1}{n+1}$;
>
> ii. for distributions with $\kappa<3$, the optimal $a$ will satisfy $\frac{n-1}{n+1}<a<1$.
>
> See Searls and Intarapanich (1990) for more details.

### 中文转述

> [!question] 中文转述
> **原题7.45。** 设$X_1,X_2,\ldots,X_n$独立同分布于均值为$\mu$、方差为$\sigma^2$的分布，$S^2$为通常的$\sigma^2$无偏估计量.在例7.3.4中，看到在正态假设下，MLE的MSE小于$S^2$.本题进一步考察方差估计.
>
> (a)  说明对任意形如$aS^2$（$a$为常数）的估计量，有
>
> $$
> \operatorname{MSE}(aS^2)=E[aS^2-\sigma^2]^2=a^2\operatorname{Var}(S^2)+(a-1)^2\sigma^4.
> $$
>
> (b)  说明
>
> $$
> \operatorname{Var}(S^2)=\frac1n\left(\kappa-\frac{n-3}{n-1}\sigma^4\right),
> $$
>
> 其中$\kappa=E[X-\mu]^4$为峰度（kurtosis）.（你可能已在习题5.8(b)中完成此题.）
>
> (c)  说明正态假设下峰度为$3\sigma^4$，并确立此时$aS^2$形式中MSE最小的估计量是$\frac{n-1}{n+1}S^2$.（引理3.6.5可能有帮助.）
>
> (d)  若不假设正态性，说明$\operatorname{MSE}(aS^2)$在
>
> $$
> a=\frac{n-1}{(n+1)+\frac{(\kappa-1)(n-1)}n}
> $$
>
> 处最小；由于依赖参数，这个结果没有实际用处.
>
> (e)  说明
>
> i.  对于$\kappa>3$的分布，最优$a$满足$a<(n-1)/(n+1)$；
>
> ii.  对于$\kappa<3$的分布，最优$a$满足$(n-1)/(n+1)<a<1$.
>
> 更多细节参见Searls和Intarapanich（1990）.

## 提示

> [!hint]- 提示
> 先区分四阶中心矩与标准化峰度，二次式求导便能检验原(d)。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 明确$n\ge2$、$0<\sigma^2<\infty$、四阶中心矩$\mu_4=E(X-\mu)^4<\infty$。原题混用$\kappa=\mu_4$与标准化峰度，以下另记$K=\mu_4/\sigma^4$以免静默改符号。
>
> **(a)** 将$aS^2-\sigma^2=a(S^2-\sigma^2)+(a-1)\sigma^2$展开，交叉项因$ES^2=\sigma^2$期望为零，即得原式。
>
> **(b)** 令$Y_i=X_i-\mu$、$A=\sum_iY_i^2$、$B=\sum_iY_i$，则$(n-1)S^2=A-B^2/n$。独立零均值使
> $$
> EA^2=n\mu_4+n(n-1)\sigma^4,\quad EAB^2=EA^2,\quad
> EB^4=n\mu_4+3n(n-1)\sigma^4.
> $$
> 将这些代入$E(A-B^2/n)^2=EA^2-2EAB^2/n+EB^4/n^2$，除以$(n-1)^2$再减去$\sigma^4$，得
> $$
> \operatorname{Var}S^2=\frac1n\left(\mu_4-\frac{n-3}{n-1}\sigma^4\right).
> $$
> 因此原(b)若将$\kappa$理解为四阶中心矩则公式正确，只是它不是无量纲的通常峰度。
>
> **(c)** 正态中心矩为$\mu_4=3\sigma^4$：对标准正态Stein恒等式取$g(z)=z^3$得到$EZ^4=3EZ^2=3$。所以$\operatorname{Var}S^2=2\sigma^4/(n-1)$。对(a)二次式求导给$a_*=\sigma^4/(\operatorname{Var}S^2+\sigma^4)=(n-1)/(n+1)$。
>
> **(d)** 一般正确最优系数是
> $$
> a_* =\frac1{1+\frac1n(K-\frac{n-3}{n-1})}
> =\frac{n-1}{n+1+\frac{(K-3)(n-1)}n}.
> $$
> 原(d)即便把$\kappa$解释成标准化峰度，其“$\kappa-1$”仍错误，应为$K-3$；若沿(b)的四阶矩定义则还要除以$\sigma^4$。例如正态$\sigma^2=1$时原(d)与(c)已互相矛盾。最优$a$依赖未知分布峰度，故在不知道峰度时不是直接可用的常数。
>
> **(e)** 以$K$作正确比较量，分母严格随$K$增加，故$K>3$时$a_*<(n-1)/(n+1)$，$K<3$时$a_*>(n-1)/(n+1)$。又Cauchy–Schwarz给$K\ge1$，因此$\operatorname{Var}S^2\ge2\sigma^4/[n(n-1)]>0$，从而$a_*<1$。若按原符号$\kappa=\mu_4$直接与常数3比较，则命题有量纲错误且缩放数据即可反驳。四阶矩无穷时这些有限MSE优化也不适用。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=325|印刷第294页／PDF物理第325页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 原(b)κ定义、(d)系数及(e)比较量照录，解答以μ4和K明确分离并给正确范围。
- 英文原文、中文转述与本库独立解答分别保留；实际核对正文位置列于`source_refs`。题内文献引用不表示已查阅其原文。`source_status: verified`只指本题及所列位置的核对范围，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
