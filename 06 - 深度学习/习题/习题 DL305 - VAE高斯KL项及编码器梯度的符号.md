---
title: 习题 DL305：VAE高斯KL项及编码器梯度的符号
topic: deep-learning
topic_label: 深度学习
difficulty: intermediate
status: not-started
tags:
- exercise
- deep-learning
source: '[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Deep Learning: Foundations and Concepts（DS003）]]'
source_id: DS003
source_chapter: 19
source_exercise: '19.4'
source_stars: 2
source_refs:
- DS003 Exercise 19.4，印刷579/PDF590
- DS003 标准高斯先验(19.5)，印刷570/PDF581；ELBO式(19.11)，印刷571/PDF582；对角编码器(19.13)，印刷573/PDF584；(19.14)–(19.15)，印刷574/PDF585
source_status: verified
solution_status: independently-derived
created: '2026-11-02'
---

# 习题 DL305：VAE高斯KL项及编码器梯度的符号

## 题目

### 英文原题

> [!question] 英文原题
> **Exercise 19.4（★★）** Evaluate the Kullback–Leibler divergence term in (19.14). Hence, show how the gradients of this term with respect to $\mathbf w$ and $\boldsymbol\phi$ can be evaluated for training the encoder and decoder networks.

### 中文转述

> [!question] 中文转述
> **原题19.4。** 计算式(19.14)中对角高斯编码分布与标准高斯先验之间的KL散度，并说明该项对解码器参数 $\mathbf w$、编码器参数 $\boldsymbol\phi$ 的梯度如何计算。

## 提示

> [!hint]- 提示 1
> 令 $q=\mathcal N(\mu,\operatorname{diag}v)$、$p=\mathcal N(0,I)$，先计算 $\mathrm E_q(\ln q-\ln p)$。

> [!hint]- 提示 2
> 网络若输出 $a_j=\ln v_j$，先对 $\mu_j,a_j$ 求导再用链式法则。

## 解答

> [!success]- 解答
> **独立推导。** 对单个数据点，令 $v_j=\sigma_j^2>0$。由 $\mathrm E_q(Z_j-\mu_j)^2=v_j$ 和 $\mathrm E_qZ_j^2=v_j+\mu_j^2$，
> $$
> K=\operatorname{KL}(q\|p)=\mathrm E_q\sum_j\left[-\frac12\ln v_j-\frac{(Z_j-\mu_j)^2}{2v_j}+\frac{Z_j^2}2\right]=\frac12\sum_j(\mu_j^2+v_j-1-\ln v_j).
> $$
> 因此 $K\geq0$，在 $\mu=0,v_j=1$ 时为零。若编码器输出对数方差 $a_j=\ln v_j$，
> $$
> \frac{\partial K}{\partial\mu_j}=\mu_j,\quad\frac{\partial K}{\partial v_j}=\frac12(1-v_j^{-1}),\quad\frac{\partial K}{\partial a_j}=\frac12(e^{a_j}-1),
> $$
> $$
> \nabla_\phi K=\sum_j\left[\mu_j\nabla_\phi\mu_j+\frac12(v_j-1)\nabla_\phi a_j\right].
> $$
> 若输出对数标准差 $b_j=\ln\sigma_j$，则对应导数为 $\partial_{b_j}K=\sigma_j^2-1$；不能把它与对数方差混用。
>
> 本章先验固定，编码器仅依赖 $x,\phi$，所以 $\nabla_w K=0$。KL项不给解码器提供梯度；解码器由重构对数似然项训练。ELBO中实际出现的是 $-K$，最大化ELBO时上面编码器梯度需取负；最小化负ELBO则直接用 $\nabla K$。数据集／小批次损失按样本求和或平均即可。
>
> 正文(19.15)把 $\tfrac12\sum_j[1+\ln v_j-\mu_j^2-v_j]$ 标成 $\operatorname{KL}$，它实际是 **负KL**；该形式用于(19.19)的ELBO时符号才正确。

## 相关概念

- [[06 - 深度学习/概念/VAE（变分自编码器）|VAE（变分自编码器）]]
- [[05 - 概率模型与推断/概念/变分推断|变分推断]]
- [[01 - 概率论/概念/期望|期望]]
- [[01 - 概率论/概念/相对熵|相对熵]]
- [[03 - 线性代数与优化/概念/链式法则|链式法则]]

## 备注

- 原题及星数：[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=590|印刷579／PDF590]]；题页及引用正文已实际查看原PDF图像，精确定位见 `source_refs`。
- 已实际核对(19.15)的KL符号误印并单独指出；未把负KL当成非负散度。
- `source_status: verified` 仅指本题及所列实际核对范围；解答独立推导，不构成用户已完成学习，状态保持 `not-started`。
