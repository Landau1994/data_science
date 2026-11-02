---
title: 习题 DL307：ELBO的先验期望与似然熵比值分解
topic: deep-learning
topic_label: 深度学习
difficulty: beginner
status: not-started
tags:
- exercise
- deep-learning
source: '[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Deep Learning: Foundations and Concepts（DS003）]]'
source_id: DS003
source_chapter: 19
source_exercise: '19.6'
source_stars: 1
source_refs:
- DS003 Exercise 19.6，印刷579/PDF590
- DS003 式(19.11)，印刷571/PDF582；式(19.14)，印刷574/PDF585
source_status: verified
solution_status: independently-derived
created: '2026-11-02'
---

# 习题 DL307：ELBO的先验期望与似然熵比值分解

## 题目

### 英文原题

> [!question] 英文原题
> **Exercise 19.6（★）** Show that the ELBO given by (19.11) can be written in the form
> $$
> \begin{aligned}
> \mathcal L_n(\mathbf w,\boldsymbol\phi)&=\int q(\mathbf z_n|\mathbf x_n,\boldsymbol\phi)\ln p(\mathbf z_n)\,\mathrm d\mathbf z_n\\
> &\quad+\int q(\mathbf z_n|\mathbf x_n,\boldsymbol\phi)\ln\left\{\frac{p(\mathbf x_n|\mathbf z_n,\mathbf w)}{q(\mathbf z_n|\mathbf x_n,\boldsymbol\phi)}\right\}\,\mathrm d\mathbf z_n.\tag{19.25}
> \end{aligned}
> $$

### 中文转述

> [!question] 中文转述
> **原题19.6。** 证明式(19.11)的ELBO可写为(19.25)：第一项为编码分布下的先验对数密度期望，第二项为同一分布下“解码似然除以编码密度”的对数期望。完整两个积分见英文原题。

## 提示

> [!hint]- 提示 1
> 在对数内将先验 $p(z)$ 单独提出；积分分布始终是 $q(z|x,\phi)$。

## 解答

> [!success]- 解答
> **独立推导。** 令 $q_n(z)=q(z|x_n,\phi)$。在期望可拆分时，对 $q_n$ 几乎处处有
> $$
> \ln\frac{p(x_n|z,w)p(z)}{q_n(z)}=\ln p(z)+\ln\frac{p(x_n|z,w)}{q_n(z)}.
> $$
> 乘以 $q_n(z)$ 并积分，立即得到(19.25)。展开第二项也可写成
> $$
> \mathcal L_n=\mathrm E_{q_n}\ln p(Z)+\mathrm E_{q_n}\ln p(x_n|Z,w)+H(q_n).
> $$
> 因此它与前一题的联合对数密度加熵完全一致。这里 $p(x_n|z,w)/q_n(z)$ 是关于固定 $x_n$ 的函数，通常不是归一化密度；第二项本身不应被误称为一个KL散度。若涉及无限值，需从原始对数比定义下界并先验证可积性，不能无条件把 $+\infty$ 与 $-\infty$ 相消。

## 相关概念

- [[06 - 深度学习/概念/VAE（变分自编码器）|VAE（变分自编码器）]]
- [[05 - 概率模型与推断/概念/变分推断|变分推断]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题及星数：[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=590|印刷579／PDF590]]；题页及引用正文已实际查看原PDF图像，精确定位见 `source_refs`。
- `source_status: verified` 仅指本题及所列实际核对范围；解答独立推导，不构成用户已完成学习，状态保持 `not-started`。
