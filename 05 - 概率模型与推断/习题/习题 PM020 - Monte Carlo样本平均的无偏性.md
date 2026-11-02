---
title: 习题 PM020：Monte Carlo样本平均的无偏性
topic: probabilistic-models
topic_label: 概率模型与推断
difficulty: beginner
status: not-started
tags:
- exercise
- probabilistic-models
source: '[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Bishop《深度学习：基础与概念》（DS003）]]'
source_id: DS003
source_chapter: 14
source_exercise: '14.1'
source_stars: 1
source_refs:
- DS003 Exercise 14.1，印刷456/PDF471
- DS003 §14.1.1，式(14.1)–(14.4)，印刷430–431/PDF445–446
source_status: verified
solution_status: independently-derived
created: '2026-11-02'
---

# 习题 PM020：Monte Carlo样本平均的无偏性

## 题目

### 英文原题

> [!question] 英文原题
> **14.1 (★)** Show that $\bar f$ defined by (14.2) is an unbiased estimator, in other words that the expectation of the right-hand side is equal to $\mathrm E[f(\mathbf z)]$.

### 中文转述

> [!question] 中文转述
> **原题14.1。** 证明式(14.2)的Monte Carlo估计量（Monte Carlo estimator） $\bar f=L^{-1}\sum_{l=1}^Lf(\mathbf z^{(l)})$ 无偏。

## 提示

> [!hint]- 提示
> 对有限和使用期望线性性；无偏本身不要求样本间独立。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 假设每个 $\mathbf z^{(l)}$ 的边缘分布均为目标 $p$，且 $\mathrm E_p|f(\mathbf z)|<\infty$，$L\ge1$。则
> $$
> \mathrm E\bar f=\frac1L\sum_{l=1}^L\mathrm E[f(\mathbf z^{(l)})]=\frac1L\sum_{l=1}^L\mathrm E_p f(\mathbf z)=\mathrm E_pf(\mathbf z).
> $$
> 因此无偏。正文还假设样本独立，这用于下一题的方差缩减；本题线性性只需各边缘正确。未达到平稳分布的有限长MCMC样本并不自动具有这些目标边缘，不能因估计式形式相同便声称无偏。

## 相关概念

- [[05 - 概率模型与推断/概念/概率推断|概率推断]]
- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已实际对照[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=471|印刷456／PDF471]]；正文引用范围见 `source_refs`。
- 英文原题与中文转述分列，原文疑误另注；未使用配套答案册。`source_status: verified` 仅表示本题及所列公式的实际核对范围；解答写成不表示个人学习完成，状态保持 `not-started`。
