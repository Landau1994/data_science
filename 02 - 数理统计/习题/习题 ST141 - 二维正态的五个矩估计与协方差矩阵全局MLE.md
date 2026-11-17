---
title: "习题 ST141：二维正态的五个矩估计与协方差矩阵全局MLE"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "advanced"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第7章习题7.18，印刷页290／PDF物理页321"
source_id: "DS011"
source_chapter: 7
source_exercise: "7.18"
source_stars: 0
source_refs: ["DS011 Exercise 7.18，印刷290／PDF物理321"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST141：二维正态的五个矩估计与协方差矩阵全局MLE

## 题目

### 英文原题

> [!question] 英文原题
> **7.18** Let $(X_1,Y_1),\ldots,(X_n,Y_n)$ be iid bivariate normal random variables (pairs) where all five parameters are unknown.
>
> (a) Show that the method of moments estimators for $\mu_X,\mu_Y,\sigma_X^2,\sigma_Y^2,\rho$ are $\widetilde\mu_X=\bar x$, $\widetilde\mu_Y=\bar y$, $\widetilde\sigma_X^2=\frac1n\sum(x_i-\bar x)^2$, $\widetilde\sigma_Y^2=\frac1n\sum(y_i-\bar y)^2$, $\widetilde\rho=\frac1n\sum(x_i-\bar x)(y_i-\bar y)/(\widehat\sigma_X\widehat\sigma_Y)$.
>
> (b) Derive the MLEs of the unknown parameters and show that they are the same as the method of moments estimators. (One attack is to write the joint pdf as the product of a conditional and a marginal, that is, write
> $$
> f(x,y\mid\mu_X,\mu_Y,\sigma_X^2,\sigma_Y^2,\rho)=f(y\mid x,\mu_X,\mu_Y,\sigma_X^2,\sigma_Y^2,\rho)\times f(x\mid\mu_X,\sigma_X^2),
> $$
> and argue that the MLEs for $\mu_X$ and $\sigma_X^2$ are given by $\bar x$ and $\frac1n\sum(x_i-\bar x)^2$. Then, turn things around to get the MLEs for $\mu_Y$ and $\sigma_Y^2$. Finally, work with the “partially maximized” likelihood function $L(\bar x,\bar y,\widehat\sigma_X^2,\widehat\sigma_Y^2,\rho\mid\mathbf x,\mathbf y)$ to get the MLE for $\rho$. As might be guessed, this is a difficult problem.)

### 中文转述

> [!question] 中文转述
> **原题7.18。** 设$(X_1,Y_1),\ldots,(X_n,Y_n)$为独立同分布的二元正态随机变量对，全部五个参数均未知.
>
> (a)  说明$\mu_X,\mu_Y,\sigma_X^2,\sigma_Y^2,\rho$的矩估计量为
>
> $$
> \begin{aligned}
> \widetilde\mu_X=\bar x,\quad\widetilde\mu_Y=\bar y,\quad\widetilde\sigma_X^2=\frac1n\sum(x_i-\bar x)^2,\quad\widetilde\sigma_Y^2=\frac1n\sum(y_i-\bar y)^2,\\
> \widetilde\rho=\frac{(1/n)\sum(x_i-\bar x)(y_i-\bar y)}{\widehat\sigma_X\widehat\sigma_Y}.
> \end{aligned}
> $$
>
> (b)  推导未知参数的MLE，并说明它们与矩估计量相同.（一种办法是把联合pdf写成条件密度与边缘密度的乘积，即
>
> $$
> \begin{aligned}
> f(x,y\mid\mu_X,\mu_Y,\sigma_X^2,\sigma_Y^2,\rho)
> &=f(y\mid x,\mu_X,\mu_Y,\sigma_X^2,\sigma_Y^2,\rho)\\
> &\quad\times f(x\mid\mu_X,\sigma_X^2),
> \end{aligned}
> $$
>
> 并论证$\mu_X$和$\sigma_X^2$的MLE为$\bar x$与$(1/n)\sum(x_i-\bar x)^2$.然后调换角色，求$\mu_Y$和$\sigma_Y^2$的MLE.最后，处理“部分极大化”的似然函数$L(\bar x,\bar y,\widehat\sigma_X^2,\widehat\sigma_Y^2,\rho\mid\boldsymbol x,\boldsymbol y)$，求出$\rho$的MLE.可以猜到，这是一道难题.）

## 提示

> [!hint]- 提示
> 矩阵平方分解先解决均值，再用$a-\log a\ge1$解决协方差。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 采用非退化二维正态模型，即$\sigma_X^2,\sigma_Y^2>0$、$|\rho|<1$。
>
> **(a)** 五个总体原始矩为$EX=\mu_X,EY=\mu_Y,EX^2=\sigma_X^2+\mu_X^2,EY^2=\sigma_Y^2+\mu_Y^2,EXY=\mu_X\mu_Y+\rho\sigma_X\sigma_Y$。逐一令其等于五个样本矩，先解出$\bar X,\bar Y$，再解出分母$n$的两个样本中心二阶矩$S_{xx},S_{yy}$与协方差$S_{xy}$，最后$\widetilde\rho=S_{xy}/\sqrt{S_{xx}S_{yy}}$。原题最后一式的hat/tilde不一致只是记号问题。
>
> **(b)** 以下给出矩阵法的全局证明。令$z_i=(x_i,y_i)^\mathsf T$、$\bar z=n^{-1}\sum z_i$、$S=n^{-1}\sum(z_i-\bar z)(z_i-\bar z)^\mathsf T$，协方差矩阵为$\Sigma>0$。忽略常数，负二倍对数似然除以$n$是
> $$
> \log\det\Sigma+\operatorname{tr}(\Sigma^{-1}S)+(\bar z-\mu)^\mathsf T\Sigma^{-1}(\bar z-\mu).
> $$
> 对每个$\Sigma>0$，最后一项非负且只在$\mu=\bar z$为零。若$S>0$，令$A=S^{1/2}\Sigma^{-1}S^{1/2}$，余下表达式等于
> $$
> \log\det S+\operatorname{tr}A-\log\det A
> =\log\det S+\sum_{j=1}^2(a_j-\log a_j),
> $$
> $a_j>0$为$A$特征值。$a-\log a\ge1$，等号只在$a=1$，所以唯一最小点$A=I$，即$\widehat\Sigma=S$。于是$\widehat\mu_X=\bar X,\widehat\mu_Y=\bar Y,\widehat\sigma_X^2=S_{xx},\widehat\sigma_Y^2=S_{yy},\widehat\rho=S_{xy}/\sqrt{S_{xx}S_{yy}}$，与(a)相同。
>
> 若样本中心协方差奇异，可令$\Sigma$在其零特征方向的特征值趋0，使负对数似然趋$-\infty$，所以非退化模型中没有有限MLE；$n\le2$必奇异，$n\ge3$的真实非退化连续样本则几乎必然满秩。零样本方差时相关系数公式亦未定义。原题一般陈述须带此条件。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=321|印刷第290页／PDF物理第321页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 保留原题hat/tilde混用；MLE结论明确要求中心样本协方差正定，奇异样本只有无界似然。
- 英文原文、中文转述与本库独立解答分别保留；实际核对正文位置列于`source_refs`。题内文献引用不表示已查阅其原文。`source_status: verified`只指本题及所列位置的核对范围，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
