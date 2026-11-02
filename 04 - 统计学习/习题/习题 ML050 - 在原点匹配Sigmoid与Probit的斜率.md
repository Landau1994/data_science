---
title: 习题 ML050：在原点匹配Sigmoid与Probit的斜率
topic: statistical-learning
topic_label: 统计学习
difficulty: intermediate
status: not-started
tags:
- exercise
- statistical-learning
source: '[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Deep Learning: Foundations and Concepts（DS003）]]'
source_id: DS003
source_chapter: 5
source_exercise: '5.24'
source_stars: 2
source_refs:
- DS003 Exercise 5.24，印刷169/PDF188
- DS003 §5.3，式(5.42)，印刷151/PDF170
- DS003 §5.4.3，式(5.72)，印刷160/PDF179
- DS003 §5.4.5，式(5.86)，印刷163/PDF182
- DS004 Solution 5.24，式(180)–(181)，印刷59/PDF59
source_status: verified
solution_status: independently-derived
created: '2026-11-02'
---

# 习题 ML050：在原点匹配Sigmoid与Probit的斜率

## 题目

### 英文原题

> [!question] 英文原题
> **Exercise 5.24（★★）** Suppose we wish to approximate the logistic sigmoid $\sigma(a)$ defined by (5.42) by a scaled probit function $\Phi(\lambda a)$, where $\Phi(a)$ is defined by (5.86). Show that if $\lambda$ is chosen so that the derivatives of the two functions are equal at $a=0$, then $\lambda^2=\pi/8$.

### 中文转述

> [!question] 中文转述
> **原题5.24（★★）。** 希望用缩放后的 Probit 函数（scaled probit function）$\Phi(\lambda a)$ 近似式 (5.42) 的 Logistic sigmoid $\sigma(a)$，其中 $\Phi$ 由式 (5.86) 定义。证明：若选择 $\lambda$ 使两函数在 $a=0$ 处导数相同，则 $\lambda^2=\pi/8$。所用定义为
> $$
> \sigma(a)=\frac1{1+e^{-a}},\qquad
> \Phi(a)=\frac1{\sqrt{2\pi}}\int_{-\infty}^a e^{-\theta^2/2}\,\mathrm d\theta.
> $$

## 提示

> [!hint]- 提示 1
> sigmoid 在零点的值为1/2，导数可由 $\sigma(1-\sigma)$ 计算。

> [!hint]- 提示 2
> 分布函数的导数是密度，但复合函数 $\Phi(\lambda a)$ 还要乘上 $\lambda$。匹配正斜率时不能选择负根。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 对有限实数 $a$，sigmoid 可微。由 $\sigma(0)=1/2$ 及其导数公式，
> $$
> \left.\frac{\mathrm d\sigma(a)}{\mathrm da}\right|_{a=0}
> =\frac12\left(1-\frac12\right)=\frac14.
> $$
> 标准高斯密度连续，因此由微积分基本定理和链式法则，
> $$
> \frac{\mathrm d}{\mathrm da}\Phi(\lambda a)
> =\frac\lambda{\sqrt{2\pi}}e^{-(\lambda a)^2/2},\qquad
> \left.\frac{\mathrm d}{\mathrm da}\Phi(\lambda a)\right|_{a=0}
> =\frac\lambda{\sqrt{2\pi}}.
> $$
> 令两者相等，得到唯一的斜率匹配尺度
> $$
> \lambda=\frac{\sqrt{2\pi}}4=\sqrt{\frac\pi8}>0,
> \qquad\lambda^2=\frac\pi8.
> $$
> 负根虽然满足平方等式，却会产生负斜率，不能满足最初的导数相等条件。
>
> 两函数在零点还满足 $\sigma(0)=\Phi(0)=1/2$，因此该尺度匹配了函数值和一阶导数；这是原点附近的局部匹配，不是两函数处处相等，也没有证明任何全局最优逼近性质。此计算直接使用正态分布函数定义，不受上一题两种 erf 约定的影响。

## 相关概念

- [[06 - 深度学习/概念/激活函数|激活函数]]
- [[03 - 线性代数与优化/概念/链式法则|链式法则]]
- [[01 - 概率论/概念/随机变量|随机变量]]

## 备注

- 原题与星号：[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=188|印刷169／PDF物理188]]；原题及实际引用的正文页均已对照原始PDF图像。正文精确定位见 `source_refs`。
- 已查看[[00 - 首页/教材归档/DS004 - Bishop 深度学习答案册|DS004]]印刷59／PDF59的5.24；这里独立保留链式因子及正根条件。
- `source_status: verified` 仅指本题及所列实际核对范围；独立解答不构成个人完成学习，状态保持 `not-started`。
