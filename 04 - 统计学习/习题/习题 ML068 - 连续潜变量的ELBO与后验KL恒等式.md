---
title: 习题 ML068：连续潜变量的ELBO与后验KL恒等式
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
source_exercise: '16.18'
source_stars: 1
source_refs:
- DS003 Exercise 16.18，印刷530/PDF544
- DS003 ELBO与KL定义(16.57)–(16.59)，印刷516/PDF530；下界(16.60)，印刷517/PDF531
source_status: verified
solution_status: independently-derived
created: '2026-11-02'
---

# 习题 ML068：连续潜变量的ELBO与后验KL恒等式

## 题目

### 英文原题

> [!question] 英文原题
> **Exercise 16.18（★）** Verify that the log likelihood function for a model with continuous latent variables can be written as the sum of two terms in the form (16.57) in which the terms are defined by (16.58) and (16.59). This can be done by using the product rule of probability in the form
> $$p(\mathbf x,\mathbf z|\mathbf w)=p(\mathbf z|\mathbf x,\mathbf w)p(\mathbf x|\mathbf w)\tag{16.89}$$
> and then substituting for $p(\mathbf x,\mathbf z|\mathbf w)$ in (16.58).

### 中文转述

> [!question] 中文转述
> **原题16.18。** 对连续潜变量模型，将概率乘法公式(16.89)代入(16.58)，验证对数证据等于ELBO与后验KL之和，即(16.57)，两项分别由(16.58)–(16.59)定义。

## 提示

> [!hint]- 提示 1
> 对数证据与积分变量 $z$ 无关，且 $q$ 积分为1。

## 解答

> [!success]- 解答
> **独立推导。** 设 $0<p(x|w)<\infty$，$q(z)$ 是归一化密度，并保证下述期望可定义。将(16.89)代入下界定义：
> $$\begin{aligned}
> \mathcal L(q,w)&=\int q(z)\ln\frac{p(x,z|w)}{q(z)}\,\mathrm dz\\
> &=\int q(z)\left[\ln p(x|w)+\ln\frac{p(z|x,w)}{q(z)}\right]\,\mathrm dz\\
> &=\ln p(x|w)-\operatorname{KL}(q(z)\|p(z|x,w)).
> \end{aligned}$$
> 移项即 $\ln p(x|w)=\mathcal L(q,w)+\operatorname{KL}(q\|p(z|x,w))$。散度非负给ELBO下界，且在 $q$ 与真实后验几乎处处相等时取等号。
>
> 若 $q$ 在后验零密度集上有正质量，则KL为 $+\infty$、ELBO为 $-\infty$，仍可表述“下界”，但不能在实数代数中写成无穷项相加等于有限证据。实际使用恒等式应先验证绝对连续性与可积性，或直接使用未拆分的扩展值形式。

## 相关概念

- [[04 - 统计学习/概念/无监督学习|无监督学习]]
- [[05 - 概率模型与推断/概念/潜变量|潜变量]]
- [[05 - 概率模型与推断/概念/变分推断|变分推断]]
- [[01 - 概率论/概念/相对熵|相对熵]]

## 备注

- 原题及星数：[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=544|印刷530／PDF544]]；题页及引用正文已实际查看原PDF图像，精确定位见 `source_refs`。
- `source_status: verified` 仅指本题及所列实际核对范围；解答独立推导，不构成用户已完成学习，状态保持 `not-started`。
