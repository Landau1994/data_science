---
title: 习题 P033：Bernoulli分布的归一化矩与熵
topic: probability-theory
topic_label: 概率论
difficulty: beginner
status: not-started
tags:
- exercise
- probability-theory
source: '[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Bishop《深度学习：基础与概念》（DS003）]]'
source_id: DS003
source_chapter: 3
source_exercise: '3.1'
source_stars: 1
source_refs:
- DS003 Exercise 3.1，印刷105/PDF124
- DS003 §3.1.1–3.1.2，式(3.2)、(3.9)，印刷66–67/PDF85–86
source_status: verified
solution_status: independently-derived
created: '2026-11-02'
---

# 习题 P033：Bernoulli分布的归一化矩与熵

## 题目

### 英文原题

> [!question] 英文原题
> **3.1 (★)** Verify that the Bernoulli distribution (3.2) satisfies the following properties:
> $$
> \sum_{x=0}^1p(x\mid\mu)=1\tag{3.191}
> $$
> $$
> \mathrm E[x]=\mu\tag{3.192}
> $$
> $$
> \operatorname{var}[x]=\mu(1-\mu).\tag{3.193}
> $$
> Show that the entropy $\mathrm H[x]$ of a Bernoulli-distributed random binary variable $x$ is given by
> $$
> \mathrm H[x]=-\mu\ln\mu-(1-\mu)\ln(1-\mu).\tag{3.194}
> $$

### 中文转述

> [!question] 中文转述
> **原题3.1。** 对式(3.2)的Bernoulli分布（Bernoulli distribution），验证归一化、均值、方差及上述熵（entropy）公式。

## 提示

> [!hint]- 提示
> 直接列出0、1两点的概率，并用 $x^2=x$。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 设 $P(X=1)=\mu$、$P(X=0)=1-\mu$，$0\le\mu\le1$。两点概率之和为1，且
> $$
> \mathrm EX=0(1-\mu)+1\mu=\mu,\qquad \mathrm EX^2=\mu.
> $$
> 所以 $\operatorname{var}X=\mathrm EX^2-(\mathrm EX)^2=\mu(1-\mu)$。由离散熵的定义，
> $$
> \mathrm H(X)=-\sum_{x=0}^1P(X=x)\ln P(X=x)
> =-(1-\mu)\ln(1-\mu)-\mu\ln\mu.
> $$
> 在端点采用 $0\ln0=0$ 的连续延拓，分布退化、方差和熵均为0。

## 相关概念

- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/期望|期望]]
- [[01 - 概率论/概念/信息熵|信息熵]]

## 备注

- 原题已实际对照[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=124|印刷105／PDF124]]；正文引用范围见 `source_refs`。
- 英文原题与中文转述分列，原文疑误另注；未使用配套答案册。`source_status: verified` 仅表示本题及所列公式的实际核对范围；解答写成不表示个人学习完成，状态保持 `not-started`。
