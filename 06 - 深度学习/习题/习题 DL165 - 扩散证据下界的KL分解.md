---
title: "习题 DL165：扩散证据下界的KL分解"
topic: deep-learning
topic_label: 深度学习
difficulty: advanced
status: not-started
tags:
  - exercise
  - deep-learning
source: "Understanding Deep Learning（2026-02-08 修订稿），Problem 18.7，印刷373／PDF物理387"
source_id: DS001
source_chapter: 18
source_exercise: "18.7"
source_refs: ["DS001 Problem 18.7*，印刷373/PDF387", "DS001 式18.25，印刷359/PDF373"]
source_status: verified
solution_status: independently-derived
created: 2026-10-28
---

# 习题 DL165：扩散证据下界的KL分解

## 题目

### 英文原题

> [!question] 英文原题
> **Problem 18.7\*** Derive the third line of equation 18.25 from the second line.

### 中文转述

> [!question] 中文转述
> 从式18.25第二行的路径期望，推导第三行的重构期望减去条件KL项，说明积分中如何消去无关潜变量。


## 提示

> [!hint]- 提示
> 每个对数比值只依赖 $(z_{t-1},z_t)$。先保留该二元边缘，再用其条件分解。

## 解答

> [!success]- 解答
> 对固定 $x$，第二行的近似式为
> $$
> E_{q(z_{1:T}|x)}\left[\log p_\phi(x|z_1)+\sum_{t=2}^T\log\frac{p_{\phi_t}(z_{t-1}|z_t)}{q(z_{t-1}|z_t,x)}\right].
> $$
> 假定各项可积，将有限和与积分交换。重构项只含 $z_1$，积分掉其他变量，得到 $E_{q(z_1|x)}\log p_\phi(x|z_1)$。第 $t$ 项只含 $(z_{t-1},z_t)$，故
> $$
> \begin{aligned}
> &E_{q(z_{t-1},z_t|x)}\log\frac{p_{\phi_t}(z_{t-1}|z_t)}{q(z_{t-1}|z_t,x)}\\
> &=\int q(z_t|x)\left[\int q(z_{t-1}|z_t,x)\log\frac{p_{\phi_t}(z_{t-1}|z_t)}{q(z_{t-1}|z_t,x)}\,dz_{t-1}\right]dz_t\\
> &=-E_{q(z_t|x)}D_{KL}\big(q(z_{t-1}|z_t,x)\Vert p_{\phi_t}(z_{t-1}|z_t)\big).
> \end{aligned}
> $$
> 代回即得第三行。原式将外层期望写为 $q(z_{t,t-1}|x)$；由于KL已经对 $z_{t-1}$ 积分、其值只依赖 $z_t,x$，对二元边缘取期望与上面仅对 $q(z_t|x)$ 取期望数值相同，但后者更清晰。
>
> 本题第二行到第三行是精确的积分恒等变形。第一行到第二行已忽略终点项 $-D_{KL}(q(z_T|x)\Vert p(z_T))$；有限步扩散一般仅近似达到标准高斯，所以此处不能把整个简化式无条件称作精确原始ELBO。

## 相关概念

- [[06 - 深度学习/概念/扩散模型|扩散模型]]：前向加噪、反向条件分布与训练目标。
- [[01 - 概率论/概念/相对熵|相对熵]]：高斯KL散度与证据下界。

## 备注

- 原题：[[附件/books/UnderstandingDeepLearning_02_09_26_C.pdf#page=387|印刷 373／PDF 387]]；教材记录见 [[00 - 首页/教材归档/DS001 - Understanding Deep Learning|DS001]]。
- 题干、公式及所引原页已核对；解答为独立推导。
