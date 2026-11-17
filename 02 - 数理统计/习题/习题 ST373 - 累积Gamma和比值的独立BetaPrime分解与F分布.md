---
title: "习题 ST373：累积Gamma和比值的独立BetaPrime分解与F分布"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "advanced"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第11章习题11.19，印刷页459／PDF物理页490"
source_id: "DS011"
source_chapter: 11
source_exercise: "11.19"
source_stars: 0
source_refs: ["DS011 Exercise 11.19，印刷459／PDF物理490"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST373：累积Gamma和比值的独立BetaPrime分解与F分布

## 题目

### 英文原题

> [!question] 英文原题
> **11.19** Let $X_i\sim\operatorname{gamma}(\lambda_i,1)$ independently for $i=1,\ldots,n$. Define $Y_i=X_{i+1}/(\sum_{j=1}^iX_j)$, $i=1,\ldots,n-1$, and $Y_n=\sum_{i=1}^nX_i$.
>
> (a) Find the joint and marginal distributions of $Y_i$, $i=1,\ldots,n$.
>
> (b) Connect your results to any distributions that are commonly employed in the ANOVA.

### 中文转述

> [!question] 中文转述
> **原题11.19。** 设$X_i\sim\operatorname{gamma}(\lambda_i,1)$相互独立，$i=1,\ldots,n$. 定义$Y_i=X_{i+1}/(\sum_{j=1}^iX_j)$，$i=1,\ldots,n-1$，以及$Y_n=\sum_{i=1}^nX_i$.
>
> (a)  求$Y_i$，$i=1,\ldots,n$，的联合分布和边缘分布.
>
> (b)  将结果与ANOVA中常用的分布联系起来.

## 提示

> [!hint]- 提示
> 每次合并两个独立Gamma块，总和与一个比例分离，再递推。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 设所有$\lambda_i>0$，记$\Lambda_i=\sum_{j=1}^i\lambda_j$，Gamma第二参数1按尺度记。
>
> **(a)** 先证明两块变换：若$A\sim\Gamma(a,1),B\sim\Gamma(b,1)$独立，令$S=A+B,R=B/A$，则$A=S/(1+R),B=SR/(1+R)$、Jacobian为$S/(1+R)^2$。代入完整密度后分解为
> $$
> \frac{S^{a+b-1}e^{-S}}{\Gamma(a+b)}\cdot
> \frac{\Gamma(a+b)}{\Gamma(a)\Gamma(b)}R^{b-1}(1+R)^{-(a+b)},\quad S,R>0.
> $$
> 因此$S$与$R$独立，$S\sim\Gamma(a+b,1)$，$R\sim\operatorname{BetaPrime}(b,a)$。从$A=X_1,B=X_2$开始，每次把新的独立$X_{i+1}$与旧总和$S_i$合并；旧总和与已构造比值独立，新的两块变换使新总和与新增比值独立，同时保持与旧比值的独立。归纳得全部$Y_1,\ldots,Y_n$相互独立，且
> $$
> Y_i\sim\operatorname{BetaPrime}(\lambda_{i+1},\Lambda_i)\ (i<n),\qquad
> Y_n\sim\Gamma(\Lambda_n,1).
> $$
> 完整联合密度为这些边际的乘积：
> $$
> \frac{y_n^{\Lambda_n-1}e^{-y_n}}{\Gamma(\Lambda_n)}
> \prod_{i=1}^{n-1}\frac{\Gamma(\Lambda_{i+1})}{\Gamma(\lambda_{i+1})\Gamma(\Lambda_i)}
> y_i^{\lambda_{i+1}-1}(1+y_i)^{-\Lambda_{i+1}},\quad y_i>0.
> $$
> **(b)** 比例$1/(1+Y_i)=S_i/S_{i+1}\sim\operatorname{Beta}(\Lambda_i,\lambda_{i+1})$。Gamma形状为半自由度时等价于缩放卡方，故
> $$
> \frac{\Lambda_i}{\lambda_{i+1}}Y_i\sim F_{2\lambda_{i+1},2\Lambda_i}.
> $$
> 这与ANOVA中独立组间、组内卡方平方和除以各自自由度再取比的F分布同源；最终总和也是Gamma/卡方可加性。形状不必为半整数，F分布也允许正实数自由度。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=490|印刷第459页／PDF物理第490页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 英文原文、中文转述与本库独立解答分别保留；实际核对正文位置列于`source_refs`。题内文献引用不表示已查阅其原文。`source_status: verified`只指本题及所列位置的核对范围，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
