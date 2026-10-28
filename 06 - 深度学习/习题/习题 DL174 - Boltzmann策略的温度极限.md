---
title: "习题 DL174：Boltzmann策略的温度极限"
topic: deep-learning
topic_label: 深度学习
difficulty: intermediate
status: not-started
tags:
  - exercise
  - deep-learning
source: "Understanding Deep Learning（2026-02-08 修订稿），Problem 19.4，印刷400／PDF物理414"
source_id: DS001
source_chapter: 19
source_exercise: "19.4"
source_refs: ["DS001 Problem 19.4，印刷400/PDF414"]
source_status: verified
solution_status: independently-derived
created: 2026-10-28
---

# 习题 DL174：Boltzmann策略的温度极限

## 题目

### 英文原题

> [!question] 英文原题
> **Problem 19.4** The Boltzmann policy strikes a balance between exploration and exploitation by basing the action probabilities $\pi[a|s]$ on the current state-action reward function $q[s,a]$:
> $$
> \pi[a|s]=\frac{\exp[q[s,a]/\tau]}{\sum_{a'}\exp[q[s,a']/\tau]}.\tag{19.45}
> $$
> Explain how the temperature parameter $\tau$ can be varied to prioritize exploration or exploitation.

### 中文转述

> [!question] 中文转述
> 解释正温度参数如何控制Boltzmann策略的探索与利用，说明趋于0和趋于无穷时的极限。


## 提示

> [!hint]- 提示
> 比较两个动作的概率比 $e^{(q_a-q_b)/\tau}$；先减最大Q值可同时看清低温极限并避免数值溢出。

## 解答

> [!success]- 解答
> 设同一状态有有限个动作，$\tau>0$，令 $M=\max_aq(s,a)$。数值上可等价写为
> $$
> \pi(a|s)=\frac{\exp[(q(s,a)-M)/\tau]}{\sum_b\exp[(q(s,b)-M)/\tau]}.
> $$
> 减小温度会放大价值差异，因为 $\pi(a|s)/\pi(b|s)=\exp[(q(s,a)-q(s,b))/\tau]$。当 $\tau\downarrow0$ 时，非最大动作概率趋于0；若有 $m$ 个并列最大动作，它们各趋于 $1/m$，更侧重利用。
>
> 增大温度使概率变平；当 $\tau\to\infty$ 时各指数趋于1，所有 $|A_s|$ 个动作概率趋于 $1/|A_s|$，更侧重探索。中间温度保留所有有限Q值动作的正概率，可随训练调整。温度不能直接设为0代入原分式，而要取极限；单靠某个温度日程也不能自动保证足够探索或最优学习。

## 相关概念

- [[01 - 概率论/概念/期望|期望]]：随机回报与梯度估计。

- [[08 - 随机过程与时间序列/概念/马尔可夫决策过程|马尔可夫决策过程]]：状态、动作、策略及环境转移。
- [[06 - 深度学习/概念/强化学习|强化学习]]：策略及期望累计回报目标。

## 备注

- 原题：[[附件/books/UnderstandingDeepLearning_02_09_26_C.pdf#page=414|印刷 400／PDF 414]]；教材记录见 [[00 - 首页/教材归档/DS001 - Understanding Deep Learning|DS001]]。
- 题干、公式及所引原页已核对；解答为独立推导。
