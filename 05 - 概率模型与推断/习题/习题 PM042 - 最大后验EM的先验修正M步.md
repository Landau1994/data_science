---
title: "习题 PM042：最大后验EM的先验修正M步"
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
source_exercise: "15.5"
source_stars: 2
source_refs:
  - "DS003 Exercise 15.5，印刷491/PDF506"
  - "DS003 §15.3，式15.23，印刷476/PDF491"
  - "DS003 §15.4，式15.51–15.54，印刷485/PDF500"
source_status: verified
solution_status: independently-derived
created: 2026-11-02
---

# 习题 PM042：最大后验EM的先验修正M步

## 题目

### 英文原题

> [!question] 英文原题
> **15.5 (★★)** Suppose we wish to use the EM algorithm to maximize the posterior distribution over parameters $p(\boldsymbol\theta\mid\mathbf X)$ for a model containing latent variables, where $\mathbf X$ is the observed data set. Show that the E step remains the same as in the maximum likelihood case, whereas in the M step the quantity to be maximized is given by $\mathcal Q(\boldsymbol\theta,\boldsymbol\theta^{\mathrm{old}})+\ln p(\boldsymbol\theta)$ where $\mathcal Q(\boldsymbol\theta,\boldsymbol\theta^{\mathrm{old}})$ is defined by (15.23).

### 中文转述

> [!question] 中文转述
> 对含潜变量、观测数据为$\mathbf X$的模型，用EM最大化参数后验$p(\boldsymbol\theta\mid\mathbf X)$。证明E步与极大似然时相同，而M步最大化由(15.23)定义的$\mathcal Q(\boldsymbol\theta,\boldsymbol\theta^{\mathrm{old}})$加上$\ln p(\boldsymbol\theta)$。

## 提示

> [!hint]- 提示 1
> 将参数对数先验加到EM下界；它不依赖潜变量分布$q$。

## 解答

> [!success]- 解答
> **独立推导。**
>
> 由Bayes公式，最大化后验等价于最大化$\log p(X\mid\theta)+\log p(\theta)$。对任意潜变量分布$q$，有
> $$
> \log p(X\mid\theta)+\log p(\theta)
> =\mathcal L(q,\theta)+\log p(\theta)+D_{\mathrm{KL}}(q\|p(Z\mid X,\theta)).
> $$
> 固定当前$\theta^{\mathrm{old}}$，先验项不依赖$q$，因此最大化下界仍在
> $$
> q^{\mathrm{new}}(Z)=p(Z\mid X,\theta^{\mathrm{old}})
> $$
> 取得，E步不变。固定此$q$后，
> $$
> \mathcal L(q,\theta)+\log p(\theta)
> =\sum_Zq(Z)\log p(X,Z\mid\theta)+\log p(\theta)-\sum_Zq(Z)\log q(Z).
> $$
> 最后一项不依赖待优化$\theta$，第一项是(15.23)的$\mathcal Q(\theta,\theta^{\mathrm{old}})$，故M步为
> $$
> \theta^{\mathrm{new}}\in\arg\max_\theta\{\mathcal Q(\theta,\theta^{\mathrm{old}})+\log p(\theta)\}.
> $$
> 这就是最大后验（MAP）EM。假设当前后验有定义，优化限制在先验的支持内，且各期望有意义；先验取零处可把对数先验记为$-\infty$以表达硬约束。先验加入后可改善某些退化问题，但并不普遍保证全局最优或唯一解。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[01 - 概率论/概念/条件概率|条件概率]]
- [[05 - 概率模型与推断/概念/潜变量|潜变量]]
- [[05 - 概率模型与推断/概念/概率推断|概率推断]]
- [[05 - 概率模型与推断/概念/变分推断|变分推断]]

## 备注

- 原题已核对 DS003 印刷491页／PDF物理506页；正文引用的实际核对范围见 `source_refs`。
- 解答为独立推导；归档与个人学习状态分开，学习状态保持 `not-started`。
