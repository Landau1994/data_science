---
title: 习题 ML069：独立样本ELBO的可加分解
topic: statistical-learning
topic_label: 统计学习
difficulty: beginner
status: not-started
tags:
- exercise
- statistical-learning
source: '[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Deep Learning: Foundations and Concepts（DS003）]]'
source_id: DS003
source_chapter: 16
source_exercise: '16.19'
source_stars: 1
source_refs:
- DS003 Exercise 16.19，印刷530/PDF544
- DS003 i.i.d.证据与ELBO式(16.62)–(16.63)，印刷517/PDF531
source_status: verified
solution_status: independently-derived
created: '2026-11-02'
---

# 习题 ML069：独立样本ELBO的可加分解

## 题目

### 英文原题

> [!question] 英文原题
> **Exercise 16.19（★）** Show that, for a set of i.i.d. data, the evidence lower bound (ELBO) takes the form (16.63).

### 中文转述

> [!question] 中文转述
> **原题16.19。** 证明对于独立同分布数据集，证据下界可写成式(16.63)的逐样本求和形式。

## 提示

> [!hint]- 提示 1
> 写联合模型 $p(X,Z|w)=\prod_np(x_n,z_n|w)$ 以及逐样本变分分布 $q(Z)=\prod_nq_n(z_n)$。

## 解答

> [!success]- 解答
> **独立推导。** 给每个独立观测 $x_n$ 配一个局部潜变量 $z_n$，各样本共享参数 $w$。模型满足 $p(X,Z|w)=\prod_{n=1}^Np(x_n,z_n|w)$。按正文选择 $q(Z)=\prod_nq_n(z_n)$，则
> $$\begin{aligned}
> \mathcal L(q,w)&=\int\prod_mq_m(z_m)\ln\frac{\prod_np(x_n,z_n|w)}{\prod_nq_n(z_n)}\,\mathrm dZ\\
> &=\sum_n\int q_n(z_n)\ln\frac{p(x_n,z_n|w)}{q_n(z_n)}\,\mathrm dz_n,
> \end{aligned}$$
> 因为其余 $q_m$ 均积分为1。这就是(16.63)，相应证据和后验KL也分别逐样本相加。
>
> 数据独立性给模型的样本分解；ELBO这个具体形式还使用了逐样本的变分分布选择。若允许任意相关 $q(Z)$、记其边缘为 $q_n$，则在有限熵条件下有
> $$\mathcal L(q,w)=\sum_n\mathcal L(q_n,w)-\operatorname{KL}\left(q(Z)\middle\|\prod_nq_n(z_n)\right),$$
> 最后一项为总相关，通常不能省略。本题所用因子化不损失最优下界，因为该独立局部潜变量模型的真实后验本身也按样本因子化。

## 相关概念

- [[04 - 统计学习/概念/无监督学习|无监督学习]]
- [[05 - 概率模型与推断/概念/潜变量|潜变量]]
- [[05 - 概率模型与推断/概念/变分推断|变分推断]]
- [[01 - 概率论/概念/相对熵|相对熵]]

## 备注

- 原题及星数：[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=544|印刷530／PDF544]]；题页及引用正文已实际查看原PDF图像，精确定位见 `source_refs`。
- `source_status: verified` 仅指本题及所列实际核对范围；解答独立推导，不构成用户已完成学习，状态保持 `not-started`。
