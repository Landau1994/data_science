---
title: 习题 DL316：扩散ELBO的一致性KL项分解
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
source_exercise: '20.9'
source_stars: 2
source_refs:
- DS003 Exercise 20.9，印刷604/PDF614
- DS003 §20.2.2–20.2.3，式(20.21)–(20.32)，印刷588–590/PDF598–600
source_status: verified
solution_status: independently-derived
created: '2026-11-02'
---

# 习题 DL316：扩散ELBO的一致性KL项分解

## 题目

### 英文原题

> [!question] 英文原题
> **20.9 (★★)** Verify that the ELBO for the diffusion model given by (20.31) can be written in the form (20.32) where the Kullback–Leibler divergence is defined by (20.23).

### 中文转述

> [!question] 中文转述
> **原题20.9。** 利用KL散度的定义(20.23)，验证式(20.31)给出的扩散模型ELBO可以写成(20.32)的形式。

## 提示

> [!hint]- 提示
> 对只涉及相邻时刻的函数，其余轨道变量积分为1；再把两时联合写成条件分布乘边缘。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 正文省略参数无关项后的目标为
> $$
> \mathcal L_{\rm red}=\mathrm E_q\left[\ln p(\mathbf x\mid\mathbf z_1,\mathbf w)+\sum_{t=2}^T\ln\frac{p(\mathbf z_{t-1}\mid\mathbf z_t,\mathbf w)}{q(\mathbf z_{t-1}\mid\mathbf z_t,\mathbf x)}\right].
> $$
> 重建项仅依赖 $\mathbf z_1$，其余变量积分掉，得 $\int q(\mathbf z_1\mid\mathbf x)\ln p(\mathbf x\mid\mathbf z_1,\mathbf w)\,\mathrm d\mathbf z_1$。第 $t$ 项只需两时联合
> $$
> q(\mathbf z_{t-1},\mathbf z_t\mid\mathbf x)=q(\mathbf z_t\mid\mathbf x)q(\mathbf z_{t-1}\mid\mathbf z_t,\mathbf x).
> $$
> 固定 $\mathbf z_t$ 后，内积分恰为负KL。因此
> $$
> \mathcal L_{\rm red}=\mathrm E_{q(\mathbf z_1\mid\mathbf x)}\ln p(\mathbf x\mid\mathbf z_1,\mathbf w)
> -\sum_{t=2}^T\mathrm E_{q(\mathbf z_t\mid\mathbf x)}\operatorname{KL}(q(\mathbf z_{t-1}\mid\mathbf z_t,\mathbf x)\Vert p(\mathbf z_{t-1}\mid\mathbf z_t,\mathbf w)).
> $$
> 这就是(20.32)。该目标与完整ELBO相差一个固定终端项，优化 $\mathbf w$ 等价，但数值不能无条件称为同一个精确下界；完整恢复见下一题。

## 相关概念

- [[05 - 概率模型与推断/概念/变分推断|变分推断]]
- [[01 - 概率论/概念/相对熵|相对熵]]
- [[06 - 深度学习/概念/扩散模型|扩散模型]]

## 备注

- 原题已实际对照[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=614|印刷604／PDF614]]；正文引用范围见 `source_refs`。
- 英文原题与中文转述分列，原文疑误另注；未使用配套答案册。`source_status: verified` 仅表示本题及所列公式的实际核对范围；解答写成不表示个人学习完成，状态保持 `not-started`。
