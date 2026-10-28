---
title: "习题 ML007：共线变量下的岭回归与Lasso"
topic: statistical-learning
topic_label: 统计学习
difficulty: intermediate
status: not-started
tags:
  - exercise
  - statistical-learning
source: "[[00 - 首页/教材归档/DS013 - Introduction to Statistical Learning R|ISLR（DS013）]]"
source_id: DS013
source_chapter: 6
source_exercise: "6.5"
source_refs: ["DS013 第6章习题5，印刷285/PDF296"]
source_status: verified
solution_status: independently-derived
created: 2026-10-25
---

# 习题 ML007：共线变量下的岭回归与Lasso

## 题目

### 英文原题

> [!question] 英文原题
> **5.** It is well-known that ridge regression tends to give similar coefficient values to correlated variables, whereas the lasso may give quite different coefficient values to correlated variables. We will now explore this property in a very simple setting.
>
> Suppose that $n=2$, $p=2$, $x_{11}=x_{12}$, $x_{21}=x_{22}$. Furthermore, suppose that $y_1+y_2=0$ and $x_{11}+x_{21}=0$ and $x_{12}+x_{22}=0$, so that the estimate for the intercept in a least squares, ridge regression, or lasso model is zero: $\hat\beta_0=0$.
>
> (a) Write out the ridge regression optimization problem in this setting.
>
> (b) Argue that in this setting, the ridge coefficient estimates satisfy $\hat\beta_1=\hat\beta_2$.
>
> (c) Write out the lasso optimization problem in this setting.
>
> (d) Argue that in this setting, the lasso coefficients $\hat\beta_1$ and $\hat\beta_2$ are not unique—in other words, there are many possible solutions to the optimization problem in (c). Describe these solutions.

### 中文转述

> [!question] 中文转述
> **ISLR 第6章习题5。** 岭回归（ridge regression）往往给相关变量相近的系数，而 Lasso 可能给相关变量差异很大的系数。本题在一个简单情形研究这种性质。
>
> 设 $n=p=2$，两列预测变量完全相同：$x_{11}=x_{12}$、$x_{21}=x_{22}$。再设 $y_1+y_2=0$、$x_{11}+x_{21}=0$、$x_{12}+x_{22}=0$，于是最小二乘、岭回归或 Lasso 的截距估计为 $\hat\beta_0=0$。
>
> (a) 写出此时的岭回归优化问题。
>
> (b) 说明岭回归系数为何满足 $\hat\beta_1=\hat\beta_2$。
>
> (c) 写出此时的 Lasso 优化问题。
>
> (d) 原题要求说明 Lasso 系数不唯一，并描述全部可能解。该断言所需的非退化条件在解答与备注中单独说明。

## 提示

> [!hint]- 提示 1
> 拟合值只取决于 $t=\beta_1+\beta_2$。固定 $t$，分别比较 $\beta_1^2+\beta_2^2$ 与 $|\beta_1|+|\beta_2|$ 的最小值。

> [!hint]- 提示 2
> 使用 $\beta_1^2+\beta_2^2=t^2/2+(\beta_1-\beta_2)^2/2$，以及三角不等式 $|\beta_1|+|\beta_2|\ge|t|$。后一不等式何时取等？

## 解答

> [!success]- 解答
> **证明范围：独立推导，显式补充原题未写出的惩罚与非退化条件。** 先假设惩罚系数 $\lambda>0$。截距不受惩罚；由样本中心化，任意斜率下最优截距均为零。记公共设计列、其平方范数及与响应的内积为
> $$
> u=(x_{11},x_{21})^\top,\qquad a=u^\top u\ge0,\qquad c=u^\top y,
> \qquad t=\beta_1+\beta_2.
> $$
> **(a) 岭回归目标。**
> $$
> \min_{\beta_1,\beta_2\in\mathbb R}
> \left\{\sum_{i=1}^{2}\bigl(y_i-x_{i1}(\beta_1+\beta_2)\bigr)^2
> +\lambda(\beta_1^2+\beta_2^2)\right\}.
> $$
> **(b) 相同列得到相同岭系数。** 因为
> $$
> \beta_1^2+\beta_2^2=\frac{t^2}{2}+\frac{(\beta_1-\beta_2)^2}{2},
> $$
> 固定 $t$ 时，唯一的最优分配是 $\beta_1=\beta_2=t/2$。降为一维后，目标为
> $$
> \|y-ut\|_2^2+\frac\lambda2t^2
> =\|y\|_2^2-2ct+(a+\lambda/2)t^2.
> $$
> 由于 $a+\lambda/2>0$，最小点唯一，故
> $$
> \hat t_R=\frac{c}{a+\lambda/2},\qquad
> \hat\beta_1^R=\hat\beta_2^R=\frac{c}{2a+\lambda}.
> $$
> **(c) Lasso 目标。**
> $$
> \min_{\beta_1,\beta_2\in\mathbb R}
> \left\{\sum_{i=1}^{2}\bigl(y_i-x_{i1}(\beta_1+\beta_2)\bigr)^2
> +\lambda(|\beta_1|+|\beta_2|)\right\}.
> $$
> **(d) 描述 Lasso 全部解及唯一性例外。** 固定 $t$，三角不等式给出 $|\beta_1|+|\beta_2|\ge|t|$，且当两个系数同号或其中一个为零时取等。因此需先最小化
> $$
> q_L(t)=\|y-ut\|_2^2+\lambda|t|.
> $$
> 当 $a>0$ 时，此函数严格凸。分别在 $t>0$、$t<0$ 求导，并在零点检查左右导数，得到
> $$
> \hat t_L=\frac{S(c,\lambda/2)}{a},\qquad
> S(z,h)=\operatorname{sign}(z)\max(|z|-h,0).
> $$
> 若 $\hat t_L>0$，全部解恰为
> $$
> (\hat\beta_1,\hat\beta_2)=(r,\hat t_L-r),\qquad 0\le r\le\hat t_L.
> $$
> 若 $\hat t_L<0$，全部解恰为同一表达式，其中 $\hat t_L\le r\le0$。两种情形都有无穷多解，包括把全部系数放在第一列或第二列的两个端点；但所有解给出相同拟合值 $u\hat t_L$。
>
> 若 $|c|\le\lambda/2$，则 $\hat t_L=0$。达到最低惩罚还要求 $|\beta_1|+|\beta_2|=0$，因此唯一解反而是 $(0,0)$。若 $a=0$，公共设计列为零，$c=0$，正惩罚同样使唯一解为 $(0,0)$。
>
> **无惩罚边界。** 若 $\lambda=0$，岭与 Lasso 都退化成最小二乘。当 $a>0$ 时只确定 $t=c/a$，任意实数 $r$ 都可给出 $(r,t-r)$，这时不能断言所有岭解的两系数相等；若 $a=0$，任意系数都最优。
>
> **独立延伸：为什么弹性网络能解除这里的系数不唯一。** 在 Lasso 目标另加 $\lambda_2(\beta_1^2+\beta_2^2)$，其中 Lasso 权重记为 $\lambda_1\ge0$、$\lambda_2>0$。固定 $t$ 时两种惩罚同时在 $\beta_1=\beta_2=t/2$ 取到最小值，且平方惩罚使该分配唯一。于是
> $$
> \hat t_{EN}=\frac{S(c,\lambda_1/2)}{a+\lambda_2/2},\qquad
> \hat\beta_1^{EN}=\hat\beta_2^{EN}=\frac{\hat t_{EN}}2.
> $$
> 这是对本题的独立推导，使用的是残差平方和加两项惩罚的约定，不属于 ISLR 原题。

## 相关概念

- [[04 - 统计学习/概念/Lasso回归|Lasso回归]]：绝对值惩罚、稀疏性与系数不唯一。
- [[04 - 统计学习/概念/岭回归|岭回归]]：正平方惩罚带来的唯一性。
- [[04 - 统计学习/概念/弹性网络|弹性网络]]：同时加入两类惩罚的独立延伸。
- [[04 - 统计学习/概念/正则化|正则化]]：惩罚权重与截距约定。
- [[03 - 线性代数与优化/概念/凸函数|凸函数]]：严格凸性与最小点唯一性的区别。

## 备注

- 原题全文已对照 [[附件/books/ISLR.pdf#page=296|ISLR 印刷285／PDF物理296]] 的原始页面图像核对；6.5 无星号，页边有黄色难题图标。
- **原题断言的边界：** (b) 对所有最优解成立需要 $\lambda>0$；(d) 在正惩罚下需要 $a>0$ 且 $|c|>\lambda/2$ 才有系数不唯一。原文“不唯一”未写这些条件，英文原文原样保留，中文备注和解答说明例外。
- `source_status: verified` 仅覆盖该题原文、分题和定位；解析解答及弹性网络延伸为独立推导，没有核对答案册或进行数据实验。学习状态保持 `not-started`。
