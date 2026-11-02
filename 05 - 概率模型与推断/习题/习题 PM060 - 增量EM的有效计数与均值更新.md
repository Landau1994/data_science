---
title: "习题 PM060：增量EM的有效计数与均值更新"
topic: probabilistic-models
topic_label: 概率模型与推断
difficulty: intermediate
status: not-started
tags:
  - exercise
  - probabilistic-models
source: "[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Bishop 深度学习（DS003）]]"
source_id: DS003
source_chapter: 15
source_exercise: "15.23"
source_stars: 2
source_refs:
  - "DS003 Exercise 15.23，印刷493/PDF508"
  - "DS003 §15.4.5，式15.60–15.61，印刷490/PDF505"
  - "DS003 §15.2，式15.16–15.18、15.21，印刷471–472/PDF486–487"
  - "DS003 §15.3.1，式15.26、15.29–15.30，印刷478–479/PDF493–494"
source_status: verified
solution_status: independently-derived
created: 2026-11-02
---

# 习题 PM060：增量EM的有效计数与均值更新

## 题目

### 英文原题

> [!question] 英文原题
> **15.23 (★★)** Consider the incremental form of the EM algorithm for a mixture of Gaussians, in which the responsibilities are recomputed only for a specific data point $\mathbf x_m$. Starting from the M-step formulae (15.16) and (15.17), derive the results (15.60) and (15.61) for updating the component means.

### 中文转述

> [!question] 中文转述
> 考虑高斯混合的增量EM，每次仅重新计算一个指定样本$\mathbf x_m$的责任度。从M步公式(15.16)、(15.17)出发，推导有效计数和均值的增量更新(15.60)、(15.61)。

## 提示

> [!hint]- 提示 1
> 维护$N_k$与加权和$S_k=N_k\mu_k$，二者的变化只来自第$m$个样本。

## 解答

> [!success]- 解答
> **独立推导。**
>
> 对分量$k$，记$\delta_k=\gamma^{\mathrm{new}}(z_{mk})-\gamma^{\mathrm{old}}(z_{mk})$；所有$n\ne m$的责任度不变。因此
> $$
> N_k^{\mathrm{new}}=\sum_n\gamma^{\mathrm{new}}_{nk}
> =N_k^{\mathrm{old}}+\delta_k,\tag{15.61}
> $$
> $$
> S_k^{\mathrm{new}}=\sum_n\gamma^{\mathrm{new}}_{nk}x_n
> =S_k^{\mathrm{old}}+\delta_kx_m.
> $$
> 旧参数由旧责任度M步得到时，$S_k^{\mathrm{old}}=N_k^{\mathrm{old}}\mu_k^{\mathrm{old}}$。若$N_k^{\mathrm{new}}>0$，新均值为
> $$
> \mu_k^{\mathrm{new}}=\frac{N_k^{\mathrm{old}}\mu_k^{\mathrm{old}}+\delta_kx_m}{N_k^{\mathrm{old}}+\delta_k}
> =\mu_k^{\mathrm{old}}+\frac{\delta_k}{N_k^{\mathrm{new}}}(x_m-\mu_k^{\mathrm{old}}),\tag{15.60}
> $$
> 恰为所求。只维护计数与加权和，即可避免重扫全部$N$个样本。
>
> $\delta_k$可以为负，这是修改已有样本的软分配，不是必然新增一个样本。若$N_k^{\mathrm{new}}=0$，该分量没有有效样本，均值不定义；此时应保留充分统计量并按空分量约定处理。若旧计数也为零，最稳妥直接从$S_k^{\mathrm{new}}/N_k^{\mathrm{new}}$计算，避免引用未定义的旧均值。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[01 - 概率论/概念/条件概率|条件概率]]
- [[05 - 概率模型与推断/概念/潜变量|潜变量]]
- [[05 - 概率模型与推断/概念/概率推断|概率推断]]

## 备注

- 原题已核对 DS003 印刷493页／PDF物理508页；正文引用的实际核对范围见 `source_refs`。
- 解答为独立推导；归档与个人学习状态分开，学习状态保持 `not-started`。
