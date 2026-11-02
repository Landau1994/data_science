---
title: "习题 DL198：Softplus的恒等式导数与逆函数"
topic: "deep-learning"
topic_label: "深度学习"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "deep-learning"]
source: "[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Bishop《深度学习：基础与概念》（DS003）]]"
source_id: "DS003"
source_chapter: 6
source_exercise: "6.7"
source_stars: 2
source_refs: ["DS003 Exercise 6.7，式(6.62)–(6.65)，印刷206/PDF224", "DS003 §6.2.3，Sigmoid式(6.13)，印刷183/PDF201；Softplus式(6.16)，印刷185/PDF203"]
source_status: "verified"
solution_status: "independently-derived"
created: 2026-11-02
---

# 习题 DL198：Softplus的恒等式导数与逆函数

## 题目

### 英文原题

> [!question] 英文原题
> **6.7 (★★)** Show that the softplus activation function $\zeta(a)$ given by (6.16) satisfies the properties:
> $$
> \zeta(a)-\zeta(-a)=a\tag{6.62}
> $$
> $$
> \ln\sigma(a)=-\zeta(-a)\tag{6.63}
> $$
> $$
> \frac{\mathrm d\zeta(a)}{\mathrm da}=\sigma(a)\tag{6.64}
> $$
> $$
> \zeta^{-1}(a)=\ln(\exp(a)-1)\tag{6.65}
> $$
> where $\sigma(a)$ is the logistic-sigmoid activation function given by (6.13).

### 中文转述

> [!question] 中文转述
> **Bishop 原题 6.7。** 证明式(6.16)的 Softplus 激活函数（softplus activation function）满足四条性质：$\zeta(a)-\zeta(-a)=a$；$\ln\sigma(a)=-\zeta(-a)$；$\zeta'(a)=\sigma(a)$；逆函数为 $\zeta^{-1}(a)=\ln(e^a-1)$。这里 $\sigma$ 是式(6.13)的逻辑 Sigmoid，所引定义为 $\zeta(a)=\ln(1+e^a)$。

## 提示

> [!hint]- 提示 1
> 前三条分别用对数差、Sigmoid定义和链式求导。求逆前先确定Softplus的值域，避免在 $e^a-1\le0$ 时取实对数。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 对所有实数输入 $a$，$1+e^a>0$，所以Softplus和下列对数有定义。
>
> 首先，
> $$
> \zeta(a)-\zeta(-a)
> =\ln\frac{1+e^a}{1+e^{-a}}
> =\ln(e^a)=a.
> $$
> 其次，由 $\sigma(a)=1/(1+e^{-a})$，
> $$
> \ln\sigma(a)=-\ln(1+e^{-a})=-\zeta(-a).
> $$
> 再次，直接求导得到
> $$
> \zeta'(a)=\frac{e^a}{1+e^a}=\frac1{1+e^{-a}}=\sigma(a).
> $$
> 最后，$\zeta'(a)>0$，并且 $\zeta(a)\to0$ 当 $a\to-\infty$、$\zeta(a)\to+\infty$ 当 $a\to+\infty$。所以 $\zeta:\mathbb R\to(0,\infty)$ 连续且严格递增，是一个双射。对输出值 $y>0$，
> $$
> y=\ln(1+e^a)\iff e^y=1+e^a
> \iff a=\ln(e^y-1).
> $$
> 故 $\zeta^{-1}(y)=\ln(e^y-1)$，定义域为 $y\in(0,\infty)$。原题式(6.65)复用字母 $a$ 表示逆函数输入，因此该式只有在其 $a>0$ 时成立。$y\downarrow0$ 时逆像趋于 $-\infty$，$y=0$ 没有有限实数逆像。

## 相关概念

- [[06 - 深度学习/概念/激活函数|激活函数]]
- [[03 - 线性代数与优化/概念/链式法则|链式法则]]
- [[06 - 深度学习/概念/神经网络|神经网络]]

## 备注

- 原题定位：[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=224|印刷206／PDF物理224]]；所用正文公式的实际位置见 `source_refs`。
- 原题的四式和编号全部保留，逆函数定义域另在解答中明确；没有把附加条件混入英文原题。
- 题干、星号、引用公式与定位已实际对照原页；`source_status: verified` 仅限本题实际核对范围。解答为独立推导，未使用配套答案册；个人学习状态保持 `not-started`。
