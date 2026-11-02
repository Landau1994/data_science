---
title: 习题 DL306：ELBO的期望联合对数密度与熵分解
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
source_exercise: '19.5'
source_stars: 1
source_refs:
- DS003 Exercise 19.5，印刷579/PDF590
- DS003 式(19.11)，印刷571/PDF582；式(19.14)，印刷574/PDF585
source_status: verified
solution_status: independently-derived
created: '2026-11-02'
---

# 习题 DL306：ELBO的期望联合对数密度与熵分解

## 题目

### 英文原题

> [!question] 英文原题
> **Exercise 19.5（★）** We have seen that the ELBO given by (19.11) can be written in the form (19.14). Show that it can also be written as
> $$
> \begin{aligned}
> \mathcal L_n(\mathbf w,\boldsymbol\phi)&=\int q(\mathbf z_n|\mathbf x_n,\boldsymbol\phi)\ln\{p(\mathbf x_n|\mathbf z_n,\mathbf w)p(\mathbf z_n)\}\,\mathrm d\mathbf z_n\\
> &\quad-\int q(\mathbf z_n|\mathbf x_n,\boldsymbol\phi)\ln q(\mathbf z_n|\mathbf x_n,\boldsymbol\phi)\,\mathrm d\mathbf z_n.\tag{19.24}
> \end{aligned}
> $$

### 中文转述

> [!question] 中文转述
> **原题19.5。** 由(19.11)的证据下界（evidence lower bound，ELBO）证明(19.24)：ELBO等于编码分布下的联合对数密度期望，加上编码分布的熵。完整积分式见英文原题。

## 提示

> [!hint]- 提示 1
> 将对数中的分子与分母拆开，辨认第二个积分的负号。

## 解答

> [!success]- 解答
> **独立推导。** 固定数据 $x_n$，记 $q_n(z)=q(z|x_n,\phi)$，联合模型 $p_w(x_n,z)=p(x_n|z,w)p(z)$。在相关期望存在且不形成 $\infty-\infty$ 时，式(19.11)给出
> $$
> \mathcal L_n=\int q_n\ln\frac{p_w(x_n,z)}{q_n(z)}\,\mathrm dz=\int q_n\ln p_w(x_n,z)\,\mathrm dz-\int q_n\ln q_n(z)\,\mathrm dz.
> $$
> 把联合分解代回即为(19.24)。第二项为微分熵 $H(q_n)$（连续变量的熵不一定非负），所以 $\mathcal L_n=\mathrm E_q\ln p_w(x_n,Z)+H(q_n)$。再拆开联合密度，得到 $\mathrm E_q\ln p(x_n|Z,w)-\mathrm E_q\ln(q_n/p)$，恢复(19.14)。若 $q_n$ 在 $p_w(x_n,z)=0$ 的区域有正质量，下界可为 $-\infty$，这时应直接使用扩展值积分而非无条件拆分无穷项。

## 相关概念

- [[06 - 深度学习/概念/VAE（变分自编码器）|VAE（变分自编码器）]]
- [[05 - 概率模型与推断/概念/变分推断|变分推断]]
- [[01 - 概率论/概念/期望|期望]]
- [[01 - 概率论/概念/信息熵|信息熵]]

## 备注

- 原题及星数：[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=590|印刷579／PDF590]]；题页及引用正文已实际查看原PDF图像，精确定位见 `source_refs`。
- `source_status: verified` 仅指本题及所列实际核对范围；解答独立推导，不构成用户已完成学习，状态保持 `not-started`。
