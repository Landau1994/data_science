---
title: 习题 PM021：独立Monte Carlo平均的方差
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
source_exercise: '14.2'
source_stars: 1
source_refs:
- DS003 Exercise 14.2，印刷456/PDF471
- DS003 §14.1.1，式(14.1)–(14.4)，印刷430–431/PDF445–446
source_status: verified
solution_status: independently-derived
created: '2026-11-02'
---

# 习题 PM021：独立Monte Carlo平均的方差

## 题目

### 英文原题

> [!question] 英文原题
> **14.2 (★)** Show that $\bar f$ defined by (14.2) has variance given by (14.4).

### 中文转述

> [!question] 中文转述
> **原题14.2。** 证明独立同分布样本平均的方差为 $\operatorname{var}(\bar f)=L^{-1}\mathrm E[(f-\mathrm Ef)^2]$，即式(14.4)。

## 提示

> [!hint]- 提示
> 展开中心化平方，非对角交叉项由独立性消失。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 设 $Y_l=f(\mathbf z^{(l)})$ 独立同分布，二阶矩有限，均值 $\mu_f$、方差 $\sigma_f^2$。则
> $$
> \operatorname{var}(\bar f)=\frac1{L^2}\sum_{l,m}\mathrm E[(Y_l-\mu_f)(Y_m-\mu_f)]
> =\frac{L\sigma_f^2}{L^2}=\frac1L\mathrm E_p[(f-\mathrm E_pf)^2].
> $$
> 这就是(14.4)。若样本相关，真实方差还含 $L^{-2}\sum_{l\ne m}\operatorname{cov}(Y_l,Y_m)$，不能直接套用 $1/L$。若二阶矩不存在，该有限方差公式也无从适用。

## 相关概念

- [[05 - 概率模型与推断/概念/概率推断|概率推断]]
- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已实际对照[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=471|印刷456／PDF471]]；正文引用范围见 `source_refs`。
- 英文原题与中文转述分列，原文疑误另注；未使用配套答案册。`source_status: verified` 仅表示本题及所列公式的实际核对范围；解答写成不表示个人学习完成，状态保持 `not-started`。
