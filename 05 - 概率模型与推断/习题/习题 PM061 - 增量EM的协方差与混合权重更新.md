---
title: "习题 PM061：增量EM的协方差与混合权重更新"
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
source_exercise: "15.24"
source_stars: 2
source_refs:
  - "DS003 Exercise 15.24，印刷493/PDF508"
  - "DS003 §15.4.5，增量EM与式15.60–15.61，印刷490/PDF505"
  - "DS003 §15.2，式15.16–15.18、15.21，印刷471–472/PDF486–487"
  - "DS003 §15.3.1，式15.26、15.29–15.30，印刷478–479/PDF493–494"
source_status: verified
solution_status: independently-derived
created: 2026-11-02
---

# 习题 PM061：增量EM的协方差与混合权重更新

## 题目

### 英文原题

> [!question] 英文原题
> **15.24 (★★)** Derive M-step formulae for updating the covariance matrices and mixing coefficients in a Gaussian mixture model when the responsibilities are updated incrementally, analogous to the result (15.60) for updating the means.

### 中文转述

> [!question] 中文转述
> 高斯混合模型每次增量修改责任度时，推导协方差矩阵和混合权重的M步更新，形式类似均值更新(15.60)。

## 提示

> [!hint]- 提示 1
> 协方差由加权二阶原点矩减均值外积得到；先更新二阶充分统计量。

## 解答

> [!success]- 解答
> **独立推导。**
>
> 仅修改样本$m$的责任度，令$\delta_k=\gamma_{mk}^{\mathrm{new}}-\gamma_{mk}^{\mathrm{old}}$，$N'=N_k^{\mathrm{new}}=N_k^{\mathrm{old}}+\delta_k$。定义充分统计量
> $$
> T_k=\sum_n\gamma_{nk}x_nx_n^T
> =N_k(\Sigma_k+\mu_k\mu_k^T).
> $$
> 它的精确增量为$T_k^{\mathrm{new}}=T_k^{\mathrm{old}}+\delta_kx_mx_m^T$。因此当$N'>0$时，先按(15.60)更新均值，再令
> $$
> \Sigma_k^{\mathrm{new}}
> =\frac{N_k^{\mathrm{old}}(\Sigma_k^{\mathrm{old}}+\mu_k^{\mathrm{old}}\mu_k^{\mathrm{old}T})+\delta_kx_mx_m^T}{N'}
> -\mu_k^{\mathrm{new}}\mu_k^{\mathrm{new}T}.
> $$
> 若旧计数也正，记$a=x_m-\mu_k^{\mathrm{old}}$、$\mu_k^{\mathrm{new}}=\mu_k^{\mathrm{old}}+(\delta_k/N')a$，展开并消去均值交叉项，可得等价的中心化更新
> $$
> \Sigma_k^{\mathrm{new}}=\frac{N_k^{\mathrm{old}}}{N'}\Sigma_k^{\mathrm{old}}
> +\frac{\delta_k N_k^{\mathrm{old}}}{(N')^2}aa^T.
> $$
> 对固定责任度，混合权重M步仍是计数比例。样本总数$N$不变，因此
> $$
> \pi_k^{\mathrm{new}}=\frac{N_k^{\mathrm{new}}}{N}
> =\pi_k^{\mathrm{old}}+\frac{\delta_k}{N}.
> $$
> 每个样本责任度和为1，所以$\sum_k\delta_k=0$，保证新权重仍归一化。
>
> 这些式子是对合法新旧非负责任度的精确充分统计量更新，不允许任意选择$\delta_k$而仍声称协方差半正定；$\delta_k<0$时应由实际责任度的修改约束保证合法性。$N'=0$时均值、协方差无定义。新残差协方差若仅半正定而不正定，则不是普通正定高斯族内取得的有限M步最大值，仍需空分量或正则化约定。数值实现可维护$N_k,S_k,T_k$，但直接二阶矩减均值外积可能有消去误差，中心化等价式有助于说明这一点。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[01 - 概率论/概念/条件概率|条件概率]]
- [[05 - 概率模型与推断/概念/潜变量|潜变量]]
- [[05 - 概率模型与推断/概念/概率推断|概率推断]]

## 备注

- 原题已核对 DS003 印刷493页／PDF物理508页；正文引用的实际核对范围见 `source_refs`。
- 解答为独立推导；归档与个人学习状态分开，学习状态保持 `not-started`。
