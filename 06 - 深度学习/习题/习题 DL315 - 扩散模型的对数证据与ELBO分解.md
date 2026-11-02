---
title: 习题 DL315：扩散模型的对数证据与ELBO分解
topic: deep-learning
topic_label: 深度学习
difficulty: intermediate
status: not-started
tags:
- exercise
- deep-learning
source: '[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Bishop《深度学习：基础与概念》（DS003）]]'
source_id: DS003
source_chapter: 20
source_exercise: '20.8'
source_stars: 2
source_refs:
- DS003 Exercise 20.8，印刷604/PDF614
- DS003 §20.2.2–20.2.3，式(20.21)–(20.32)，印刷588–590/PDF598–600
source_status: verified
solution_status: independently-derived
created: '2026-11-02'
---

# 习题 DL315：扩散模型的对数证据与ELBO分解

## 题目

### 英文原题

> [!question] 英文原题
> **20.8 (★★)** By substituting the product rule of probability in the form (20.24) into the definition (20.22) of the ELBO for the diffusion model and making use of the definition (20.23) of the Kullback–Leibler divergence, verify that the log likelihood function can be written as the sum of a lower bound and a Kullback–Leibler divergence in the form (20.21).

### 中文转述

> [!question] 中文转述
> **原题20.8。** 证明扩散模型中对数证据等于证据下界（evidence lower bound, ELBO）加近似后验对真实后验的KL散度。

## 提示

> [!hint]- 提示
> 将联合密度拆成真实后验乘证据，证据与积分变量无关。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 记所有潜变量为 $\mathbf z$，设 $q$ 为归一化近似分布，相应KL和期望有定义。由 $p(\mathbf x,\mathbf z\mid\mathbf w)=p(\mathbf z\mid\mathbf x,\mathbf w)p(\mathbf x\mid\mathbf w)$，
> $$
> \begin{aligned}
> \mathcal L(\mathbf w)&=\int q(\mathbf z)\ln\frac{p(\mathbf x,\mathbf z\mid\mathbf w)}{q(\mathbf z)}\,\mathrm d\mathbf z\\
> &=\ln p(\mathbf x\mid\mathbf w)-\operatorname{KL}(q(\mathbf z)\Vert p(\mathbf z\mid\mathbf x,\mathbf w)).
> \end{aligned}
> $$
> 移项即(20.21)。KL非负，所以是下界，等号恰在 $q$ 与真实后验几乎处处一致时成立。扩散训练取固定前向过程 $q(\mathbf z\mid\mathbf x)$，但该依赖 $\mathbf x$ 不妨碍对每个固定观测使用此分解。若支撑不匹配导致KL无穷，应按扩展意义处理，不能任意作无穷项相减。

## 相关概念

- [[05 - 概率模型与推断/概念/变分推断|变分推断]]
- [[01 - 概率论/概念/相对熵|相对熵]]
- [[06 - 深度学习/概念/扩散模型|扩散模型]]

## 备注

- 原题已实际对照[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=614|印刷604／PDF614]]；正文引用范围见 `source_refs`。
- 英文原题与中文转述分列，原文疑误另注；未使用配套答案册。`source_status: verified` 仅表示本题及所列公式的实际核对范围；解答写成不表示个人学习完成，状态保持 `not-started`。
