---
title: "习题 DL248：线性Dropout期望损失及闭式权重解"
topic: deep-learning
topic_label: 深度学习
difficulty: advanced
status: not-started
tags: [exercise, deep-learning]
source: "[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Bishop《深度学习：基础与概念》（DS003）]]"
source_id: DS003
source_chapter: 9
source_exercise: "9.18"
source_stars: 3
source_refs: ["DS003 Exercise 9.18，印刷284–285／PDF物理301–302"]
source_status: verified
solution_status: independently-derived
created: 2026-11-02
---

# 习题 DL248：线性Dropout期望损失及闭式权重解

## 题目

### 英文原题

> [!question] 英文原题
> **9.18 (★★★)** Here we explore the effect of dropout regularization on a simple linear regression model trained using least squares. Consider a model of the form
> $$
> y_k=\sum_{i=1}^Dw_{ki}x_i\tag{9.68}
> $$
> along with a sum-of-squares error function given by
> $$
> E(\mathbf W)=\sum_{n=1}^N\sum_{k=1}^K\left\{t_{nk}-\sum_{i=1}^Dw_{ki}R_{ni}x_{ni}\right\}^2\tag{9.69}
> $$
> where the elements $R_{ni}\in\{0,1\}$ of the dropout matrix are chosen randomly from a Bernoulli distribution with parameter $\rho$. We now take an expectation over the distribution of random dropout parameters. Show that
> $$
> \mathbb E[R_{ni}]=\rho\tag{9.70}
> $$
> $$
> \mathbb E[R_{ni}R_{nj}]=\delta_{ij}\rho+(1-\delta_{ij})\rho^2.\tag{9.71}
> $$
> Hence, show that the expected error function for this dropout model is given by
> $$
> \mathbb E[E(\mathbf W)]=\sum_{n=1}^N\sum_{k=1}^K\left\{y_{nk}-\rho\sum_{i=1}^Dw_{ki}x_{ni}\right\}^2\tag{9.72}
> $$
> $$
> \hspace{2em}+\rho(1-\rho)\sum_{n=1}^N\sum_{k=1}^K\sum_{i=1}^Dw_{ki}^2x_{ni}^2.\tag{9.73}
> $$
> Thus, we see that the expected error function corresponds to a sum-of-squares error with a quadratic regularizer in which the regularization coefficient is scaled separately for each input variable according to the data values seen by that input. Finally, write down a closed-form solution for the weight matrix that minimizes this regularized error function.

### 中文转述

> [!question] 中文转述
> 考察最小二乘线性回归中的Dropout正则化。模型和误差分别由(9.68)、(9.69)给出，掩码 $R_{ni}\in\{0,1\}$ 从参数为 $\rho$ 的Bernoulli分布随机抽取。对掩码分布取期望，证明一、二阶矩公式(9.70)、(9.71)，再推导期望误差(9.72)–(9.73)。这一误差等于平方和误差加二次正则项，各输入的正则系数按对应数据值分别缩放。最后写出使该正则化误差最小的权重矩阵闭式解。

## 提示

> [!hint]- 提示
> 掩码须独立。用“平方误差期望=均值误差平方+预测方差”，再写出正则化正规方程。

## 解答

> [!success]- 解答
> **证明范围：独立推导。**
> 固定数据，补充掩码坐标相互独立，$R_{ni}\sim\mathrm{Bernoulli}(\rho)$、$0\le\rho\le1$。因为 $R^2=R$，有 $\mathbb ER_{ni}=\rho$；$i=j$ 时 $\mathbb E R_{ni}^2=\rho$，$i\ne j$ 时独立性给 $\rho^2$，即(9.70)–(9.71)。仅规定伯努利边缘并不足以推出异坐标乘积矩。
>
> 令噪声预测 $S_{nk}=\sum_iw_{ki}R_{ni}x_{ni}$，则 $\mathbb E S_{nk}=\rho\sum_iw_{ki}x_{ni}$、$\operatorname{var}S_{nk}=\rho(1-\rho)\sum_iw_{ki}^2x_{ni}^2$。由 $\mathbb E(t-S)^2=(t-\mathbb ES)^2+\operatorname{var}S$，正确期望为
> $$
> \mathbb EE(W)=\sum_{n,k}(t_{nk}-\rho\sum_iw_{ki}x_{ni})^2
> +\rho(1-\rho)\sum_{n,k,i}w_{ki}^2x_{ni}^2.
> $$
> 原(9.72)首项印作 $y_{nk}$，而(9.69)是目标 $t_{nk}$；若把 $y$ 理解为(9.68)的干净模型预测，原等式不成立。因此英文保留 $y$，独立解答改回目标 $t$。
>
> 令 $X\in\mathbb R^{N\times D}$、$T\in\mathbb R^{N\times K}$、$W\in\mathbb R^{K\times D}$，$D_X=\operatorname{diag}(\sum_nx_{n1}^2,\ldots,\sum_nx_{nD}^2)$。目标写成
> $$
> \|T-\rho XW^{\mathsf T}\|_F^2+\rho(1-\rho)\operatorname{tr}(WD_XW^{\mathsf T}).
> $$
> 直接对 $W$ 求导得到正规方程
> $$
> WA=\rho T^{\mathsf T}X,\qquad A=\rho^2X^{\mathsf T}X+\rho(1-\rho)D_X.
> $$
> 若 $A$ 可逆，唯一解为 $W^\star=\rho T^{\mathsf T}XA^{-1}$。特别 $0<\rho<1$ 且每个输入列不全为零时，$D_X\succ0$，所以 $A\succ0$，闭式解成立。
>
> 一般退化情形用Moore–Penrose伪逆：
> $$
> W^\star=\rho T^{\mathsf T}XA^\dagger+B(I-AA^\dagger),\quad B\in\mathbb R^{K\times D}.
> $$
> 当 $\rho>0$，$Av=0$ 蕴含 $Xv=0$，故右侧 $\rho T^{\mathsf T}X$ 消灭 $\ker A$，正规方程有解。对任意扰动 $\Delta$，在驻点处目标差为 $\operatorname{tr}(\Delta A\Delta^{\mathsf T})\ge0$，因此以上均为全局最小，$B=0$ 给最小Frobenius范数解。$\rho=1$ 退化为普通最小二乘；$\rho=0$ 时预测恒为0、目标 $\|T\|_F^2$ 与 $W$ 无关，任何权重都最优，通式亦给任意 $B$。

## 相关概念

- [[04 - 统计学习/概念/正则化|正则化]]
- [[03 - 线性代数与优化/概念/正规方程|正规方程]]
- [[01 - 概率论/概念/期望|期望]]
- [[06 - 深度学习/概念/神经网络|神经网络]]

## 备注

- 原题已实际查看 [[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=301|印刷284–285／PDF物理301–302]]；所列依赖正文亦逐页核对，精确位置见 `source_refs`。
- 原题跨印刷284–285/PDF301–302；(9.72)的目标记号错误忠实照录，并在解答修正，未把y的错误记号静默替换进英文原题。
- 解答未使用配套答案册。`source_status: verified` 指本题原文与所列依赖的核对范围；独立推导不代表个人学习完成，状态保持 `not-started`。
