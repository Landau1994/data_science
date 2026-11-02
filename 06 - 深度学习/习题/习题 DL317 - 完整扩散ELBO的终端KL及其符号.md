---
title: 习题 DL317：完整扩散ELBO的终端KL及其符号
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
source_exercise: '20.10'
source_stars: 2
source_refs:
- DS003 Exercise 20.10，印刷604–605/PDF614–615
- DS003 §20.2.2–20.2.3，式(20.21)–(20.32)，印刷588–590/PDF598–600
- DS003 §20.1–20.1.1，式(20.1)–(20.10)，印刷582–584/PDF592–594
source_status: verified
solution_status: independently-derived
created: '2026-11-02'
---

# 习题 DL317：完整扩散ELBO的终端KL及其符号

## 题目

### 英文原题

> [!question] 英文原题
> **20.10 (★★)** When we derived the ELBO for the diffusion model given by (20.32), we omitted the first and third terms in (20.26) because they are independent of $\mathbf w$. Similarly we omitted the second term in the right-hand side of (20.30) because this is also independent of $\mathbf w$. Show that if all of these omitted terms are retained they lead to an additional term in the ELBO $\mathcal L(\mathbf x)$ given by
> $$
> \operatorname{KL}(q(\mathbf z_T\mid\mathbf x)\Vert p(\mathbf z_T)).\tag{20.63}
> $$
> Note that the noise process is constructed in such a way that the distribution $q(\mathbf z_T\mid\mathbf x)$ is equal to the Gaussian $\mathcal N(\mathbf x\mid\mathbf0,I)$. Similarly, the distribution $p(\mathbf z_T)$ is defined to be equal to $\mathcal N(\mathbf x\mid\mathbf0,I)$, and hence the two distributions in (20.63) are equal and so the Kullback–Leibler divergence vanishes.

### 中文转述

> [!question] 中文转述
> **原题20.10。** 推导扩散模型ELBO(20.32)时，因与 $\mathbf w$ 无关，省略了(20.26)中的第一、第三项和(20.30)右侧的第二项。证明保留这些项后，在 $\mathcal L(\mathbf x)$ 中得到由(20.63)给出的额外项
> $$
> \operatorname{KL}(q(\mathbf z_T\mid\mathbf x)\Vert p(\mathbf z_T)).
> $$
> 噪声过程被构造为使 $q(\mathbf z_T\mid\mathbf x)$ 等于 $\mathcal N(\mathbf x\mid\mathbf0,I)$，而 $p(\mathbf z_T)$ 也被定义为同一高斯；因此两分布相同，(20.63)的KL散度为零。

## 提示

> [!hint]- 提示
> 利用相邻 $\ln q(\mathbf z_{t-1}\mid\mathbf x)-\ln q(\mathbf z_t\mid\mathbf x)$ 的望远镜相消。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 在(20.26)中保留 $\ln p(\mathbf z_T)-\ln q(\mathbf z_1\mid\mathbf x)$，再代入(20.30)的全部项。省略项之和为
> $$
> \mathrm E_q\left[\ln p(\mathbf z_T)-\ln q(\mathbf z_1\mid\mathbf x)+\sum_{t=2}^T\{\ln q(\mathbf z_{t-1}\mid\mathbf x)-\ln q(\mathbf z_t\mid\mathbf x)\}\right].
> $$
> 逐项相消后只剩
> $$
> \mathrm E_{q(\mathbf z_T\mid\mathbf x)}\ln\frac{p(\mathbf z_T)}{q(\mathbf z_T\mid\mathbf x)}
> =-\operatorname{KL}(q(\mathbf z_T\mid\mathbf x)\Vert p(\mathbf z_T)).
> $$
> 所以完整ELBO为前题重建减一致性目标再**减去**终端KL；原题(20.63)列的是其正的大小，若按“额外加上该项”理解则缺少负号。
>
> 有限 $T$ 下 $q(\mathbf z_T\mid\mathbf x)=\mathcal N(\sqrt{\alpha_T}\mathbf x,(1-\alpha_T)I)$，而 $p(\mathbf z_T)=\mathcal N(0,I)$，其KL精确为
> $$
> \frac12\{\alpha_T\|\mathbf x\|^2-D\alpha_T-D\ln(1-\alpha_T)\}.
> $$
> 通常非零；当满足 $\alpha_T\to0$ 的理想终端极限才趋0。它独立于可训练参数 $\mathbf w$，因此可在训练优化中省略，但不是对所有有限噪声日程精确为零。原题以 $\mathbf x$ 作为终端高斯的密度自变量也属记号混用，应为 $\mathbf z_T$。

## 相关概念

- [[05 - 概率模型与推断/概念/变分推断|变分推断]]
- [[01 - 概率论/概念/相对熵|相对熵]]
- [[06 - 深度学习/概念/扩散模型|扩散模型]]

## 备注

- 原题已实际对照[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=614|印刷604–605／PDF614–615]]；正文引用范围见 `source_refs`。
- 原题跨PDF614–615；正KL符号、有限步等号及N(x|0,I)均照录，修正另述。
- 英文原题与中文转述分列，原文疑误另注；未使用配套答案册。`source_status: verified` 仅表示本题及所列公式的实际核对范围；解答写成不表示个人学习完成，状态保持 `not-started`。
