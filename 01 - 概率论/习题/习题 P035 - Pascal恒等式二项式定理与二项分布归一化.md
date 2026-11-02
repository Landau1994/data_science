---
title: 习题 P035：Pascal恒等式二项式定理与二项分布归一化
topic: probability-theory
topic_label: 概率论
difficulty: intermediate
status: not-started
tags:
- exercise
- probability-theory
source: '[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Bishop《深度学习：基础与概念》（DS003）]]'
source_id: DS003
source_chapter: 3
source_exercise: '3.3'
source_stars: 2
source_refs:
- DS003 Exercise 3.3，印刷105–106/PDF124–125
- DS003 §3.1.1–3.1.2，式(3.2)、(3.9)，印刷66–67/PDF85–86
source_status: verified
solution_status: independently-derived
created: '2026-11-02'
---

# 习题 P035：Pascal恒等式二项式定理与二项分布归一化

## 题目

### 英文原题

> [!question] 英文原题
> **3.3 (★★)** In this exercise, we prove that the binomial distribution (3.9) is normalized. First, use the definition (3.10) of the number of combinations of $m$ identical objects chosen from a total of $N$ to show that
> $$
> \binom Nm+\binom N{m-1}=\binom{N+1}m.\tag{3.196}
> $$
> Use this result to prove by induction the following result:
> $$
> (1+x)^N=\sum_{m=0}^N\binom Nm x^m,\tag{3.197}
> $$
> which is known as the binomial theorem and which is valid for all real values of $x$. Finally, show that the binomial distribution is normalized, so that
> $$
> \sum_{m=0}^N\binom Nm\mu^m(1-\mu)^{N-m}=1,\tag{3.198}
> $$
> which can be done by first pulling a factor $(1-\mu)^N$ out of the summation and then making use of the binomial theorem.

### 中文转述

> [!question] 中文转述
> **原题3.3。** 先由组合数定义证明Pascal恒等式，再归纳证明对任意实数 $x$ 成立的二项式定理，最后证明二项分布（binomial distribution）归一化。

## 提示

> [!hint]- 提示
> 将两项通分；归纳时乘上 $1+x$ 并合并同次幂。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 约定 $\binom Nm=0$ 当 $m<0$ 或 $m>N$。对 $1\le m\le N$，
> $$
> \frac{N!}{m!(N-m)!}+\frac{N!}{(m-1)!(N-m+1)!}
> =\frac{N![(N-m+1)+m]}{m!(N-m+1)!}=\binom{N+1}m.
> $$
> 两端 $m=0,N+1$ 也满足该式。$N=0$ 时二项式定理为 $1=1$。若对 $N$ 成立，乘以 $1+x$，$x^m$ 的系数变为 $\binom Nm+\binom N{m-1}=\binom{N+1}m$，即得到 $N+1$ 情形，归纳完成。
>
> 当 $0\le\mu<1$，令 $x=\mu/(1-\mu)$，则
> $$
> \sum_{m=0}^N\binom Nm\mu^m(1-\mu)^{N-m}
> =(1-\mu)^N\left(1+\frac{\mu}{1-\mu}\right)^N=1.
> $$
> $\mu=1$ 时仅 $m=N$ 的概率为1；$N=0$ 时仅 $m=0$，同样归一化。

## 相关概念

- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/期望|期望]]
- [[01 - 概率论/概念/概率模型|概率模型]]

## 备注

- 原题已实际对照[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=124|印刷105–106／PDF124–125]]；正文引用范围见 `source_refs`。
- 原题跨印刷105–106／PDF124–125，末页归一化任务完整保留。
- 英文原题与中文转述分列，原文疑误另注；未使用配套答案册。`source_status: verified` 仅表示本题及所列公式的实际核对范围；解答写成不表示个人学习完成，状态保持 `not-started`。
