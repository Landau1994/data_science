---
title: "习题 ST187：乘积先验与可加损失下逐坐标Bayes规则"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第7章习题7.64，印刷页297／PDF物理页328"
source_id: "DS011"
source_chapter: 7
source_exercise: "7.64"
source_stars: 0
source_refs: ["DS011 Exercise 7.64，印刷297／PDF物理328"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST187：乘积先验与可加损失下逐坐标Bayes规则

## 题目

### 英文原题

> [!question] 英文原题
> **7.64** Let $X_1,\ldots,X_n$ be independent random variables, where $X_i$ has cdf $F(x\mid\theta_i)$. Show that, for $i=1,\ldots,n$, if $\delta_i^{\pi_i}(X_i)$ is a Bayes rule for estimating $\theta_i$ using loss $L(\theta_i,a_i)$ and prior $\pi_i(\theta_i)$, then $\delta^\pi(\mathbf X)=(\delta_1^{\pi_1}(X_1),\ldots,\delta_n^{\pi_n}(X_n))$ is a Bayes rule for estimating $\boldsymbol\theta=(\theta_1,\ldots,\theta_n)$ using the loss $\sum_{i=1}^nL(\theta_i,a_i)$ and prior $\pi(\boldsymbol\theta)=\prod_{i=1}^n\pi_i(\theta_i)$.

### 中文转述

> [!question] 中文转述
> **原题7.64。** 设$X_1,\ldots,X_n$是独立随机变量，$X_i$的cdf为$F(x\mid\theta_i)$.证明：若对$i=1,\ldots,n$，$\delta_i^{\pi_i}(X_i)$是在损失$L(\theta_i,a_i)$和先验$\pi_i(\theta_i)$下估计$\theta_i$的贝叶斯法则，则$\delta^\pi(\boldsymbol X)=(\delta_1^{\pi_1}(X_1),\ldots,\delta_n^{\pi_n}(X_n))$是在损失$\sum_{i=1}^nL(\theta_i,a_i)$和先验$\pi(\boldsymbol\theta)=\prod_{i=1}^n\pi_i(\theta_i)$下估计$\boldsymbol\theta=(\theta_1,\ldots,\theta_n)$的贝叶斯法则.

## 提示

> [!hint]- 提示
> 后验乘积分解后，可加损失的每项只依赖自己的行动坐标。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 假定各先验为正常分布、后验存在，各坐标行动空间的乘积就是联合行动空间，损失非负或满足可交换积分条件。独立抽样及乘积先验使联合后验分解为$\pi(\boldsymbol\theta\mid\mathbf x)=\prod_i\pi_i(\theta_i\mid x_i)$。
>
> 固定数据$\mathbf x$，联合行动$\mathbf a$的后验期望损失为
> $$
> \rho(\mathbf a\mid\mathbf x)=\int\sum_iL(\theta_i,a_i)\prod_j\pi_j(\theta_j\mid x_j)d\boldsymbol\theta
> =\sum_i\int L(\theta_i,a_i)\pi_i(\theta_i\mid x_i)d\theta_i.
> $$
> 第$i$项只含$a_i$，由坐标Bayes规则的假设，它在$a_i=\delta_i^{\pi_i}(x_i)$时最小。因此把这些坐标最小点组合起来，后验损失对任意其他联合行动逐点不大；再对数据边际分布积分，得到总Bayes风险最小。
>
> 如果“Bayes规则”仅按整体积分最优定义，则每个坐标在其边际数据几乎处处可选成后验最小版本，零概率集合任意延拓即可。若联合行动受到例如$\sum_i a_i=1$的额外耦合约束，坐标最小点可能不可行；原结论使用原题没有这类限制的乘积行动空间。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=328|印刷第297页／PDF物理第328页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 英文原文、中文转述与本库独立解答分别保留；实际核对正文位置列于`source_refs`。题内文献引用不表示已查阅其原文。`source_status: verified`只指本题及所列位置的核对范围，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
