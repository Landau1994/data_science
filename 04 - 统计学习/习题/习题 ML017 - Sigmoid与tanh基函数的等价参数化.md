---
title: "习题 ML017：Sigmoid与tanh基函数的等价参数化"
topic: "statistical-learning"
topic_label: "统计学习"
difficulty: "beginner"
status: "not-started"
tags: ["exercise", "statistical-learning"]
source: "[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Bishop《深度学习：基础与概念》（DS003）]]"
source_id: "DS003"
source_chapter: 4
source_exercise: "4.3"
source_stars: 1
source_refs: ["DS003 Exercise 4.3，式(4.55)–(4.58)，印刷128–129/PDF147–148", "DS003 §4.1.1，式(4.5)–(4.6)，印刷113/PDF132"]
source_status: "verified"
solution_status: "independently-derived"
created: 2026-11-02
---

# 习题 ML017：Sigmoid与tanh基函数的等价参数化

## 题目

### 英文原题

> [!question] 英文原题
> **4.3 (★)** Show that the tanh function defined by
> $$
> \tanh(a)=\frac{e^a-e^{-a}}{e^a+e^{-a}}\tag{4.55}
> $$
> and the logistic sigmoid function defined by (4.6) are related by
> $$
> \tanh(a)=2\sigma(2a)-1.\tag{4.56}
> $$
> Hence, show that a general linear combination of logistic sigmoid functions of the form
> $$
> y(x,\mathbf w)=w_0+\sum_{j=1}^Mw_j\sigma\!\left(\frac{x-\mu_j}{s}\right)\tag{4.57}
> $$
> is equivalent to a linear combination of tanh functions of the form
> $$
> y(x,\mathbf u)=u_0+\sum_{j=1}^Mu_j\tanh\!\left(\frac{x-\mu_j}{2s}\right)\tag{4.58}
> $$
> and find expressions to relate the new parameters $\{u_1,\ldots,u_M\}$ to the original parameters $\{w_1,\ldots,w_M\}$.

### 中文转述

> [!question] 中文转述
> **Bishop 原题 4.3。** 证明式(4.55)定义的双曲正切函数（hyperbolic tangent，tanh）和式(4.6)定义的逻辑 Sigmoid 函数（logistic sigmoid）满足 $\tanh(a)=2\sigma(2a)-1$。继而证明式(4.57)的 Sigmoid 基函数线性组合与式(4.58)的 tanh 基函数线性组合等价，并给出新参数 $\{u_1,\ldots,u_M\}$ 与原参数 $\{w_1,\ldots,w_M\}$ 之间的关系。这里两式的中心相同，tanh 自变量中的尺度为 $2s$。
>
> 所引式(4.6)是 $\sigma(a)=1/(1+e^{-a})$。

## 提示

> [!hint]- 提示 1
> 把 $2\sigma(2a)-1$ 通分，再用 $e^a$ 同乘分子分母。

> [!hint]- 提示 2
> 从 $\sigma(z)=\{1+\tanh(z/2)\}/2$ 出发，别遗漏每个基函数贡献的常数项。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 对任意 $a\in\mathbb R$，
> $$
> 2\sigma(2a)-1=\frac2{1+e^{-2a}}-1
> =\frac{1-e^{-2a}}{1+e^{-2a}}
> =\frac{e^a-e^{-a}}{e^a+e^{-a}}
> =\tanh(a).
> $$
> 令 $z=2a$，得到 $\sigma(z)=\frac12\{1+\tanh(z/2)\}$。设 $s>0$，将 $z=(x-\mu_j)/s$ 代入式(4.57)，
> $$
> \begin{aligned}
> y(x,\mathbf w)
> &=w_0+\frac12\sum_{j=1}^Mw_j
> +\frac12\sum_{j=1}^Mw_j\tanh\!\left(\frac{x-\mu_j}{2s}\right).
> \end{aligned}
> $$
> 因此完整的参数对应为
> $$
> u_j=\frac{w_j}{2}\quad(j=1,\ldots,M),\qquad
> u_0=w_0+\frac12\sum_{j=1}^Mw_j.
> $$
> 原题最后只点名 $u_1,\ldots,u_M$；要让两个函数对所有 $x$ 完全相同，偏置 $u_0$ 也必须随之调整。反向关系为
> $$
> w_j=2u_j\quad(j=1,\ldots,M),\qquad
> w_0=u_0-\sum_{j=1}^Mu_j.
> $$
> 代回即可恢复原式，因此这是一一对应的参数重写，表示的是同一类输入输出函数，不只是训练样本上的数值相等。这里 $s>0$ 沿用尺度参数的含义；代数恒等式对任意 $s\ne0$ 也成立，但 $s=0$ 的式子没有定义。
>
> 这种函数表示的等价不自动保证对两组系数分别施加同样的平方惩罚后，两个优化问题仍然等价；惩罚必须也按上述参数映射变换。

## 相关概念

- [[06 - 深度学习/概念/激活函数|激活函数]]
- [[06 - 深度学习/概念/神经网络|神经网络]]
- [[04 - 统计学习/概念/统计学习|统计学习]]

## 备注

- 原题定位：[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=147|印刷第128–129页／PDF物理第147–148页]]；所用正文公式的印刷页与PDF物理页见 `source_refs`。
- 本题原文跨印刷128–129／PDF147–148，两个模型及末尾参数任务均已保留。
- 偏置对应和反向参数式是为完整说明等价性而独立补出的内容，没有加入英文原题。
- 原题及依赖公式已实际对照原页；`source_status: verified` 仅限本题的来源核对。解答为独立推导，未使用答案册；学习状态保留 `not-started`。
