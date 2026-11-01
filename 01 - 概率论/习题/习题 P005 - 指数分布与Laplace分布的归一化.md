---
title: "习题 P005：指数分布与Laplace分布的归一化"
topic: "probability-theory"
topic_label: "概率论"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "probability-theory"]
source: "[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Bishop《深度学习：基础与概念》（DS003）]]"
source_id: "DS003"
source_chapter: 2
source_exercise: "2.5"
source_stars: 2
source_refs: ["DS003 Exercise 2.5，印刷58/PDF78", "DS003 §2.2.1，式(2.34)–(2.35)，印刷34/PDF54"]
source_status: "verified"
solution_status: "independently-derived"
created: 2026-11-01
---

# 习题 P005：指数分布与Laplace分布的归一化

## 题目

### 英文原题

> [!question] 英文原题
> **2.5 (★★)** Verify that the exponential distribution (2.34) and the Laplace distribution (2.35) are correctly normalized.

### 中文转述

> [!question] 中文转述
> **Bishop 原题 2.5。** 验证式(2.34)的指数分布（exponential distribution）及式(2.35)的 Laplace 分布（Laplace distribution）都已正确归一化。原书密度分别为
> $$
> p(x|\lambda)=\lambda e^{-\lambda x},\quad x\ge0,
> $$
> 以及
> $$
> p(x|\mu,\gamma)=\frac1{2\gamma}\exp\!\left(-\frac{|x-\mu|}{\gamma}\right).
> $$
> 指数分布在 $x<0$ 时密度为0。

## 提示

> [!hint]- 提示 1
> 指数分布直接积分。Laplace 密度的绝对值要求在 $x=\mu$ 处分成两个积分，或利用关于 $\mu$ 的对称性。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 指数分布要求 $\lambda>0$；Laplace 分布要求 $\gamma>0$、$\mu\in\mathbb R$。在这些参数条件下两密度均非负。
>
> 指数分布满足
> $$
> \int_{\mathbb R}p(x|\lambda)\,\mathrm dx
> =\int_0^\infty\lambda e^{-\lambda x}\,\mathrm dx
> =\left[-e^{-\lambda x}\right]_0^\infty=1.
> $$
> Laplace 分布以 $z=x-\mu$ 换元，并对正负半轴利用对称性，得到
> $$
> \begin{aligned}
> \int_{\mathbb R}p(x|\mu,\gamma)\,\mathrm dx
> &=\frac1{2\gamma}\int_{-\infty}^{\infty}e^{-|z|/\gamma}\,\mathrm dz\\
> &=\frac1\gamma\int_0^\infty e^{-z/\gamma}\,\mathrm dz=1.
> \end{aligned}
> $$
> 这也解释了常数 $1/(2\gamma)$ 中的2：中心两侧各贡献一半概率质量。$\lambda=0$ 或 $\gamma=0$ 不在上述密度参数范围内。

## 相关概念

- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/概率模型|概率模型]]

## 备注

- 原题定位：[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=78|印刷第58页／PDF物理第78页]]；题干引用正文的位置见 `source_refs`。
- 原书星号表示习题难度，本笔记保留其星数；解答为本库独立推导，未使用配套答案册作核验。
- `source_status: verified` 只指本题题干、所用公式和定位已对照原始页面；不表示整章或整书理论全部核验。学习状态保留 `not-started`。
