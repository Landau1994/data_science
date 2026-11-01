---
title: "习题 P018：用Jensen不等式证明离散熵上界"
topic: probability-theory
topic_label: 概率论
difficulty: beginner
status: not-started
tags:
  - exercise
  - probability-theory
source: "[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Bishop 深度学习（DS003）]]"
source_id: DS003
source_chapter: 2
source_exercise: "2.23"
source_stars: 1
source_refs: ["DS003 Exercise 2.23，印刷61/PDF81", "DS003 §2.5.2，式(2.86)，印刷48/PDF68", "DS003 §2.5.5，式(2.102)，印刷52/PDF72"]
source_status: verified
solution_status: independently-derived
created: 2026-11-01
---

# 习题 P018：用Jensen不等式证明离散熵上界

## 题目

### 英文原题

> [!question] 英文原题
> **2.23 (★)** Consider an $M$-state discrete random variable $x$, and use Jensen’s inequality in the form (2.102) to show that the entropy of its distribution $p(x)$ satisfies $\mathrm H[x]\le\ln M$.

### 中文转述

> [!question] 中文转述
> **原题 2.23。** 考虑一个有 $M$ 个状态的离散随机变量 $x$。利用式(2.102)形式的Jensen不等式，证明其熵满足 $H[x]\le\ln M$。

## 提示

> [!hint]- 提示
> 在正概率的状态上，以 $p_i$ 为权重，对凹函数 $\ln t$ 使用Jensen不等式。零概率状态不应代入 $1/p_i$。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 设正概率支持集为 $S=\{i:p_i>0\}$，其大小为 $K$，则 $1\le K\le M$。书中式(2.102)针对凸函数；将它应用于凸函数 $-\ln t$，等价于对凹函数 $\ln t$ 使用反向不等号。以权重 $p_i$ 和取值 $1/p_i$ 得到
> $$
> H[x]=\sum_{i\in S}p_i\ln\frac1{p_i}
> \le\ln\left(\sum_{i\in S}p_i\frac1{p_i}\right)
> =\ln K\le\ln M.
> $$
> 这也处理了含零概率的分布，因为熵中那些项按 $0\ln0=0$ 计入。
>
> 当 $M>1$ 时，第一步取等号要求所有 $1/p_i$ 在正权重支持上相同；第二步取等号要求 $K=M$。因此总等号当且仅当 $p_i=1/M$ 对所有状态成立。$M=1$ 时结论同样成立。

## 相关概念

- [[01 - 概率论/概念/信息熵|信息熵]]
- [[01 - 概率论/概念/期望|期望]]
- [[03 - 线性代数与优化/概念/凸函数|凸函数]]

## 备注

- 原题已核对 [[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=81|印刷第61页／PDF物理第81页]]；所引公式按 `source_refs` 记录的原页核对。

- `source_status: verified` 仅指本题原文、引用公式和定位的核对；解答为本库独立推导，未使用配套答案册。个人学习状态保留 `not-started`。
