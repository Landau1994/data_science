---
title: "习题 PM044：共享协方差高斯混合的EM更新"
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
source_exercise: "15.7"
source_stars: 2
source_refs:
  - "DS003 Exercise 15.7，印刷491/PDF506"
  - "DS003 §15.2，式15.16–15.18、15.21，印刷471–472/PDF486–487"
  - "DS003 §15.3.1，式15.26、15.29–15.30，印刷478–479/PDF493–494"
source_status: verified
solution_status: independently-derived
created: 2026-11-02
---

# 习题 PM044：共享协方差高斯混合的EM更新

## 题目

### 英文原题

> [!question] 英文原题
> **15.7 (★★)** Consider a special case of a Gaussian mixture model in which the covariance matrices $\boldsymbol\Sigma_k$ of the components are all constrained to have a common value $\boldsymbol\Sigma$. Derive the EM equations for maximizing the likelihood function under such a model.

### 中文转述

> [!question] 中文转述
> 高斯混合模型中，所有分量协方差$\boldsymbol\Sigma_k$被约束为同一个$\boldsymbol\Sigma$。推导该模型的极大似然EM更新。

## 提示

> [!hint]- 提示 1
> 责任度仍用当前共享协方差计算；M步把所有分量的残差二阶矩汇总成一个矩阵。

## 解答

> [!success]- 解答
> **独立推导。**
>
> 设$N>0$，当前$\Sigma^{\mathrm{old}}\succ0$。E步由Bayes公式得
> $$
> \gamma_{nk}=\frac{\pi_k^{\mathrm{old}}\mathcal N(x_n\mid\mu_k^{\mathrm{old}},\Sigma^{\mathrm{old}})}{\sum_j\pi_j^{\mathrm{old}}\mathcal N(x_n\mid\mu_j^{\mathrm{old}},\Sigma^{\mathrm{old}})}.
> $$
> M步将$\gamma$固定，令$N_k=\sum_n\gamma_{nk}$，则忽略与参数无关项后
> $$
> Q=\sum_kN_k\log\pi_k-\frac N2\log\det\Sigma
> -\frac12\sum_{n,k}\gamma_{nk}(x_n-\mu_k)^T\Sigma^{-1}(x_n-\mu_k).
> $$
> 对各均值求导，$\nabla_{\mu_k}Q=\Sigma^{-1}\sum_n\gamma_{nk}(x_n-\mu_k)$，故$N_k>0$时
> $$
> \mu_k^{\mathrm{new}}=\frac{\sum_n\gamma_{nk}x_n}{N_k}.
> $$
> 在$\sum_k\pi_k=1$下乘子优化给出$\pi_k^{\mathrm{new}}=N_k/N$。以这些新均值定义汇总残差矩阵
> $$
> S=\sum_{n,k}\gamma_{nk}(x_n-\mu_k^{\mathrm{new}})(x_n-\mu_k^{\mathrm{new}})^T.
> $$
> 使用精度$\Lambda=\Sigma^{-1}$，协方差部分为$\tfrac N2\log\det\Lambda-\tfrac12\operatorname{tr}(\Lambda S)$，求导得$N\Lambda^{-1}-S=0$，所以
> $$
> \Sigma^{\mathrm{new}}=\frac SN.
> $$
> 若$S\succ0$，精度域中严格凹，因而这是唯一协方差M步最大值。加权均值还对任意正定精度最小化各残差二次型，所以先均值、再共享协方差确实联合最大化该固定责任度的$Q$。
>
> 若$N_k=0$，该分量均值不由本M步确定、闭单纯形最优权重为零。若$S$奇异，普通正定协方差参数域内没有有限最大值：沿其零特征方向令协方差特征值趋零，残差惩罚不变而$-\log\det\Sigma$趋于正无穷。需正则化或明确退化分布的另一模型，不能把奇异更新当成普通非退化高斯MLE。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[01 - 概率论/概念/条件概率|条件概率]]
- [[05 - 概率模型与推断/概念/潜变量|潜变量]]
- [[05 - 概率模型与推断/概念/概率推断|概率推断]]

## 备注

- 原题已核对 DS003 印刷491页／PDF物理506页；正文引用的实际核对范围见 `source_refs`。
- 解答为独立推导；归档与个人学习状态分开，学习状态保持 `not-started`。
