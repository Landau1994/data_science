---
title: "习题 DL197：tanh导数的函数值表达"
topic: "deep-learning"
topic_label: "深度学习"
difficulty: "beginner"
status: "not-started"
tags: ["exercise", "deep-learning"]
source: "[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Bishop《深度学习：基础与概念》（DS003）]]"
source_id: "DS003"
source_chapter: 6
source_exercise: "6.6"
source_stars: 1
source_refs: ["DS003 Exercise 6.6，印刷206/PDF224", "DS003 §6.2.3，tanh式(6.14)，印刷184/PDF202", "DS003 §5.4.3，Sigmoid导数式(5.72)，印刷160/PDF179"]
source_status: "verified"
solution_status: "independently-derived"
created: 2026-11-02
---

# 习题 DL197：tanh导数的函数值表达

## 题目

### 英文原题

> [!question] 英文原题
> **6.6 (★)** We saw in (5.72) that the derivative of the logistic-sigmoid activation function can be expressed in terms of the function value itself. Derive the corresponding result for the tanh activation function defined by (6.14).

### 中文转述

> [!question] 中文转述
> **Bishop 原题 6.6。** 式(5.72)表明逻辑 Sigmoid 的导数可用函数值本身表示。对式(6.14)定义的 tanh 激活函数，推导相应结果。这里 $\tanh(a)=(e^a-e^{-a})/(e^a+e^{-a})$。

## 提示

> [!hint]- 提示 1
> 对指数分式求导；把分子整理成分母的平方减去原分子的平方。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 令 $u=e^a-e^{-a}$、$v=e^a+e^{-a}>0$，则 $u'=v$、$v'=u$。由商法则，
> $$
> \frac{\mathrm d}{\mathrm da}\tanh(a)
> =\frac{u'v-uv'}{v^2}
> =\frac{v^2-u^2}{v^2}
> =1-\left(\frac uv\right)^2
> =1-\tanh^2(a).
> $$
> 因此若隐藏单元输出为 $z=\tanh(a)$，其局部导数可直接写为 $1-z^2$，无需重新计算指数。
>
> 对任何有限 $a$，$-1<z<1$，故导数严格为正且不超过1，在 $a=0$ 时取1。当 $a\to\pm\infty$，$z\to\pm1$，导数趋零，说明激活两端会饱和。
>
> 作为比较，原书式(5.72)是 $\sigma'(a)=\sigma(a)\{1-\sigma(a)\}$。也可将 $\tanh(a)=2\sigma(2a)-1$ 求导得到 $4\sigma(2a)(1-\sigma(2a))=1-\tanh^2(a)$，与直接推导一致。

## 相关概念

- [[06 - 深度学习/概念/激活函数|激活函数]]
- [[03 - 线性代数与优化/概念/链式法则|链式法则]]
- [[06 - 深度学习/概念/反向传播|反向传播]]

## 备注

- 原题定位：[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=224|印刷206／PDF物理224]]；所用正文公式的实际位置见 `source_refs`。
- 题干、星号、引用公式与定位已实际对照原页；`source_status: verified` 仅限本题实际核对范围。解答为独立推导，未使用配套答案册；个人学习状态保持 `not-started`。
