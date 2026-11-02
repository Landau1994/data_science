---
title: 习题 P054：指数族对数归一化因子的Hessian与协方差
topic: probability-theory
topic_label: 概率论
difficulty: beginner
status: not-started
tags:
- exercise
- probability-theory
source: '[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Bishop《深度学习：基础与概念》（DS003）]]'
source_id: DS003
source_chapter: 3
source_exercise: '3.36'
source_stars: 1
source_refs:
- DS003 Exercise 3.36，印刷110/PDF129
- DS003 §3.4，式(3.138)–(3.139)，印刷94/PDF113；式(3.164)–(3.172)，印刷97/PDF116
source_status: verified
solution_status: independently-derived
created: '2026-11-02'
---

# 习题 P054：指数族对数归一化因子的Hessian与协方差

## 题目

### 英文原题

> [!question] 英文原题
> **3.36 (★)** The result (3.172) showed that the negative gradient of $\ln g(\boldsymbol\eta)$ for the exponential family is given by the expectation of $\mathbf u(\mathbf x)$. By taking the second derivatives of (3.139), show that
> $$
> -\nabla\nabla\ln g(\boldsymbol\eta)=\mathrm E[\mathbf u(\mathbf x)\mathbf u(\mathbf x)^{\mathsf T}]-\mathrm E[\mathbf u(\mathbf x)]\mathrm E[\mathbf u(\mathbf x)^{\mathsf T}]=\operatorname{cov}[\mathbf u(\mathbf x)].\tag{3.218}
> $$

### 中文转述

> [!question] 中文转述
> **原题3.36。** 对指数族归一化条件二次求导，证明负对数归一化因子的Hessian等于充分统计量的协方差矩阵。

## 提示

> [!hint]- 提示
> 令 $Z=1/g$；归一化积分的一阶与二阶导数分别产生一阶和二阶矩。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 设支撑不依赖参数，自然参数在归一化积分有限的开域内，且可将两次求导移入积分（如邻域内存在可积控制函数）。记
> $$
> Z(\boldsymbol\eta)=\int h(\mathbf x)e^{\boldsymbol\eta^{\mathsf T}\mathbf u(\mathbf x)}\,\mathrm d\mathbf x=1/g(\boldsymbol\eta).
> $$
> 逐项求导得到 $\partial_iZ=Z\mathrm E[u_i]$ 与 $\partial_{ij}Z=Z\mathrm E[u_iu_j]$，故
> $$
> \partial_{ij}\ln Z=\frac{\partial_{ij}Z}{Z}-\frac{\partial_iZ\partial_jZ}{Z^2}
> =\mathrm E[u_iu_j]-\mathrm E[u_i]\mathrm E[u_j].
> $$
> 由 $\ln Z=-\ln g$ 即得(3.218)。对任意向量 $\mathbf a$，$\mathbf a^{\mathsf T}\nabla^2\ln Z\mathbf a=\operatorname{var}(\mathbf a^{\mathsf T}\mathbf u)\ge0$，所以对数配分函数凸；若表示冗余，Hessian可以奇异，不能无条件说严格正定。

## 相关概念

- [[01 - 概率论/概念/期望|期望]]
- [[03 - 线性代数与优化/概念/凸函数|凸函数]]

## 备注

- 原题已实际对照[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=129|印刷110／PDF129]]；正文引用范围见 `source_refs`。
- 英文原题与中文转述分列，原文疑误另注；未使用配套答案册。`source_status: verified` 仅表示本题及所列公式的实际核对范围；解答写成不表示个人学习完成，状态保持 `not-started`。
