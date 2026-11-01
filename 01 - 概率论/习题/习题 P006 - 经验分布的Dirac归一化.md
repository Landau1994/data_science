---
title: "习题 P006：经验分布的Dirac归一化"
topic: "probability-theory"
topic_label: "概率论"
difficulty: "beginner"
status: "not-started"
tags: ["exercise", "probability-theory"]
source: "[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Bishop《深度学习：基础与概念》（DS003）]]"
source_id: "DS003"
source_chapter: 2
source_exercise: "2.6"
source_stars: 1
source_refs: ["DS003 Exercise 2.6，印刷59/PDF79", "DS003 §2.2.1，式(2.36)–(2.37)，印刷34/PDF54"]
source_status: "verified"
solution_status: "independently-derived"
created: 2026-11-01
---

# 习题 P006：经验分布的Dirac归一化

## 题目

### 英文原题

> [!question] 英文原题
> **2.6 (★)** Using the properties of the Dirac delta function, show that the empirical density (2.37) is correctly normalized.

### 中文转述

> [!question] 中文转述
> **Bishop 原题 2.6。** 利用 Dirac delta 函数（Dirac delta function）的性质，证明式(2.37)的经验密度（empirical density）已正确归一化：
> $$
> p(x|\mathcal D)=\frac1N\sum_{n=1}^N\delta(x-x_n).
> $$

## 提示

> [!hint]- 提示 1
> 对每一项使用 $\int_{\mathbb R}\delta(x-x_n)\,\mathrm dx=1$，然后交换有限求和与积分。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 设 $N\ge1$ 且所有样本 $x_n\in\mathbb R$。Dirac 点质量在其中心具有总质量1，所以
> $$
> \int_{\mathbb R}p(x|\mathcal D)\,\mathrm dx
> =\frac1N\sum_{n=1}^N\int_{\mathbb R}\delta(x-x_n)\,\mathrm dx
> =\frac1N\sum_{n=1}^N1=1.
> $$
> 更严格地，经验分布是概率测度
> $$
> P_N(A)=\frac1N\sum_{n=1}^N\mathbf1_{\{x_n\in A\}},
> $$
> 故 $P_N(\mathbb R)=1$，且各项均非负。即使样本值重复，总质量也仍为1：重复点所带的权重相加即可。
>
> 这里的“密度”是教材用 Dirac 符号书写离散点质量的简记，并非关于 Lebesgue 测度的普通函数密度。

## 相关概念

- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/概率模型|概率模型]]

## 备注

- 原题定位：[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=79|印刷第59页／PDF物理第79页]]；题干引用正文的位置见 `source_refs`。
- 原书星号表示习题难度，本笔记保留其星数；解答为本库独立推导，未使用配套答案册作核验。
- `source_status: verified` 只指本题题干、所用公式和定位已对照原始页面；不表示整章或整书理论全部核验。学习状态保留 `not-started`。
