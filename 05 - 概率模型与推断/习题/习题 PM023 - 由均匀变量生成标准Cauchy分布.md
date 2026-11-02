---
title: 习题 PM023：由均匀变量生成标准Cauchy分布
topic: probabilistic-models
topic_label: 概率模型与推断
difficulty: intermediate
status: not-started
tags:
- exercise
- probabilistic-models
source: '[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Bishop《深度学习：基础与概念》（DS003）]]'
source_id: DS003
source_chapter: 14
source_exercise: '14.4'
source_stars: 2
source_refs:
- DS003 Exercise 14.4，印刷456/PDF471
- DS003 §14.1.2，式(14.5)–(14.12)，印刷431–432/PDF446–447；图14.3，印刷433/PDF448
source_status: verified
solution_status: independently-derived
created: '2026-11-02'
---

# 习题 PM023：由均匀变量生成标准Cauchy分布

## 题目

### 英文原题

> [!question] 英文原题
> **14.4 (★★)** Given a random variable $z$ that is uniformly distributed over $(0,1)$, find a transformation $y=f(z)$ such that $y$ has a Cauchy distribution given by (14.8).

### 中文转述

> [!question] 中文转述
> **原题14.4。** 求将 $Z\sim U(0,1)$ 变成标准Cauchy分布（Cauchy distribution）的变换，其密度为 $1/[\pi(1+y^2)]$。

## 提示

> [!hint]- 提示
> 先积分密度得到CDF，再解出反函数。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 标准Cauchy的CDF为
> $$
> F(y)=\frac12+\frac1\pi\arctan y,
> $$
> 因为其导数为 $1/[\pi(1+y^2)]$，且在负无穷趋0。求逆得到
> $$
> Y=\tan\{\pi(Z-1/2)\}.
> $$
> 对 $0<Z<1$，角位于 $(-\pi/2,\pi/2)$，正切严格递增且覆盖全实轴，由前题的逆CDF论证得目标分布。变换的端点奇异只发生在概率为0的端点；实现中仍应避免使用恰为0或1的伪随机值。

## 相关概念

- [[05 - 概率模型与推断/概念/概率推断|概率推断]]
- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已实际对照[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=471|印刷456／PDF471]]；正文引用范围见 `source_refs`。
- 英文原题与中文转述分列，原文疑误另注；未使用配套答案册。`source_status: verified` 仅表示本题及所列公式的实际核对范围；解答写成不表示个人学习完成，状态保持 `not-started`。
