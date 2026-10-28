---
title: "习题 DL175：Bellman最优算子的压缩性质"
topic: deep-learning
topic_label: 深度学习
difficulty: advanced
status: not-started
tags:
  - exercise
  - deep-learning
source: "Understanding Deep Learning（2026-02-08 修订稿），Problem 19.5，印刷400／PDF物理414"
source_id: DS001
source_chapter: 19
source_exercise: "19.5"
source_refs: ["DS001 Problem 19.5*，印刷400/PDF414"]
source_status: verified
solution_status: independently-derived
created: 2026-10-28
---

# 习题 DL175：Bellman最优算子的压缩性质

## 题目

### 英文原题

> [!question] 英文原题
> **Problem 19.5\*** When the learning rate $\alpha$ is one, the Q-Learning update is given by:
> $$
> \mathrm f[q[s,a]]=r[s,a]+\gamma\cdot\max_a[q[s',a]].\tag{19.46}
> $$
> where $s$ is a state and $s'$ is the subsequent state. Show that this is a contraction mapping (equation 16.20) so that:
> $$
> \|\mathrm f[q_1[s,a]]-\mathrm f[q_2[s,a]]\|_\infty<\|q_1[s,a]-q_2[s,a]\|_\infty\qquad\forall\ q_1,q_2.\tag{19.47}
> $$
> where $\|\bullet\|_\infty$ represents the $\ell_\infty$ norm. It follows that a fixed point will exist by Banach’s theorem and that the updates will eventually converge.

### 中文转述

> [!question] 中文转述
> 证明折扣Bellman最优更新关于最大范数为压缩映射，解释原式严格不等号与Q-learning收敛断言的适用范围。


## 提示

> [!hint]- 提示
> 对任意有限向量有 $|\max u-\max v|\le\max|u-v|$。需要 $\gamma<1$；不能对相同函数声称严格小于。

## 解答

> [!success]- 解答
> 先证最大值不等式。设 $\delta=\max_b|u_b-v_b|$，则每个 $u_b\le v_b+\delta\le\max_cv_c+\delta$，故 $\max u-\max v\le\delta$；交换二者得到
> $$
> |\max u-\max v|\le\delta.
> $$
> 令 $\Delta=\|q_1-q_2\|_\infty$，奖励与模型在两次更新中相同。若每个 $(s,a)$ 的后继 $s'$ 固定，按题式
> $$
> |f(q_1)(s,a)-f(q_2)(s,a)|\le\gamma\max_b|q_1(s',b)-q_2(s',b)|\le\gamma\Delta.
> $$
> 对全部状态动作取最大，得到正确的压缩界
> $$
> \|f(q_1)-f(q_2)\|_\infty\le\gamma\|q_1-q_2\|_\infty.
> $$
> 当 $0\le\gamma<1$ 且 $q_1\ne q_2$ 时，才进一步严格小于 $\|q_1-q_2\|_\infty$。原题19.47写对所有 $q_1,q_2$ 都严格小于；取 $q_1=q_2$ 即变成 $0<0$，必须排除此情形。
>
> 随机转移下，标准Bellman最优算子是
> $$
> (Tq)(s,a)=r(s,a)+\gamma\sum_{s'}P(s'|s,a)\max_bq(s',b).
> $$
> 同样用三角不等式、$\sum P=1$ 可得 $\|Tq_1-Tq_2\|_\infty\le\gamma\Delta$。有限表格空间配最大范数是完备空间，所以Banach定理保证该固定算子有唯一不动点 $q_*$，且全表同步迭代 $q_{k+1}=Tq_k$ 满足 $\|q_k-q_*\|_\infty\le\gamma^k\|q_0-q_*\|_\infty$。
>
> 这个结论不能直接推广到每次抽取不同后继、学习率恒为1的随机Q-learning：其更新算子随样本变化，噪声可能持续。一般随机表格Q-learning还需访问和步长等条件；这里没有证明那种算法的收敛。$\gamma=1$ 也只给非扩张界，不能由本证明调用压缩不动点定理。

## 相关概念

- [[08 - 随机过程与时间序列/概念/马尔可夫链|马尔可夫链]]：状态转移与条件期望。

- [[08 - 随机过程与时间序列/概念/马尔可夫决策过程|马尔可夫决策过程]]：状态、动作、策略及环境转移。
- [[08 - 随机过程与时间序列/概念/价值函数与贝尔曼方程|价值函数与贝尔曼方程]]：回报、策略价值及贝尔曼递推。

## 备注

- 原题：[[附件/books/UnderstandingDeepLearning_02_09_26_C.pdf#page=414|印刷 400／PDF 414]]；教材记录见 [[00 - 首页/教材归档/DS001 - Understanding Deep Learning|DS001]]。
- 题干、公式及所引原页已核对；解答为独立推导。保留原式19.47并明确修正严格不等号的量词；收敛结论限于已证明的固定折扣算子。
