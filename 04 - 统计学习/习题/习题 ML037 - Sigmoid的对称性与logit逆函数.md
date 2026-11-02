---
title: "习题 ML037：Sigmoid的对称性与logit逆函数"
topic: statistical-learning
topic_label: 统计学习
difficulty: beginner
status: not-started
tags:
  - exercise
  - statistical-learning
source: "[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Bishop 深度学习（DS003）]]"
source_id: DS003
source_chapter: 5
source_exercise: "5.11"
source_stars: 1
source_refs: ["DS003 Exercise 5.11，印刷167/PDF186", "DS003 §5.3，式(5.42)–(5.44)，印刷151/PDF170"]
source_status: verified
solution_status: independently-derived
created: 2026-11-02
---

# 习题 ML037：Sigmoid的对称性与logit逆函数

## 题目

### 英文原题

> [!question] 英文原题
> **5.11 (★)** Show that the logistic sigmoid function (5.42) satisfies the property $\sigma(-a)=1-\sigma(a)$ and that its inverse is given by $\sigma^{-1}(y)=\ln\{y/(1-y)\}$.

### 中文转述

> [!question] 中文转述
> **原题5.11。** 证明式(5.42)的逻辑Sigmoid函数（logistic sigmoid）满足 $\sigma(-a)=1-\sigma(a)$，并证明其逆函数为 $\sigma^{-1}(y)=\ln\{y/(1-y)\}$。

## 提示

> [!hint]- 提示 1
> 把 $1-1/(1+e^{-a})$ 通分；求逆时先从 $y=1/(1+e^{-a})$ 解出 $e^{-a}$。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 对任意 $a\in\mathbb R$，式(5.42)为 $\sigma(a)=1/(1+e^{-a})$。直接计算，
> $$
> 1-\sigma(a)=\frac{e^{-a}}{1+e^{-a}}=\frac1{1+e^a}=\sigma(-a).
> $$
> 其次，指数为正，所以有限 $a$ 总有 $0<\sigma(a)<1$。当 $a$ 增加时，$e^{-a}$ 严格减小，故 $\sigma$ 严格增加；并且在 $a\to-\infty$、$a\to+\infty$ 时分别趋于0、1。因而它是从 $\mathbb R$ 到 $(0,1)$ 的双射。
>
> 设 $0<y<1$，由 $y=1/(1+e^{-a})$ 得
> $$
> e^{-a}=\frac{1-y}{y},\qquad
> a=-\ln\frac{1-y}{y}=\ln\frac{y}{1-y}.
> $$
> 因此
> $$
> \sigma^{-1}(y)=\ln\frac{y}{1-y},\qquad0<y<1.
> $$
> 这就是logit函数。端点 $y=0,1$ 没有有限实数逆像，只能按扩展极限分别记为 $-\infty,+\infty$；不可在普通实数逆函数中直接代入端点。

## 相关概念

- [[06 - 深度学习/概念/激活函数|激活函数]]
- [[04 - 统计学习/概念/判别式模型|判别式模型]]

## 备注

- 原题已核对 [[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=186|印刷167／PDF物理186]]；所引正文公式的实际位置见 `source_refs`。
- 逆函数的定义域是开区间 $(0,1)$。其边界极限在解答中说明，未添加进英文原题。
- `source_status: verified` 仅指本题原文、引用公式与定位核对，不表示整章或整书理论全部核验。解答未使用配套答案册；个人学习状态保留 `not-started`。
