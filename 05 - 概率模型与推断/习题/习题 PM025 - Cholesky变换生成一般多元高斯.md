---
title: 习题 PM025：Cholesky变换生成一般多元高斯
topic: probabilistic-models
topic_label: 概率模型与推断
difficulty: intermediate
status: not-started
tags:
- exercise
- probabilistic-models
source: '[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Bishop《深度学习：基础与概念》（DS003）]]'
source_id: DS003
source_chapter: 14
source_exercise: '14.6'
source_stars: 2
source_refs:
- DS003 Exercise 14.6，印刷456/PDF471
- DS003 §14.1.2，式(14.5)–(14.12)，印刷431–432/PDF446–447；图14.3，印刷433/PDF448
source_status: verified
solution_status: independently-derived
created: '2026-11-02'
---

# 习题 PM025：Cholesky变换生成一般多元高斯

## 题目

### 英文原题

> [!question] 英文原题
> **14.6 (★★)** Let $\mathbf z$ be a $D$-dimensional random variable having a Gaussian distribution with zero mean and unit covariance matrix, and suppose that the positive definite symmetric matrix $\Sigma$ has the Cholesky decomposition $\Sigma=LL^{\mathsf T}$, where $L$ is a lower-triangular matrix (i.e., one with zeros above the leading diagonal). Show that the variable $\mathbf y=\boldsymbol\mu+L\mathbf z$ has a Gaussian distribution with mean $\boldsymbol\mu$ and covariance $\Sigma$. This provides a technique for generating samples from a general multivariate Gaussian using samples from a univariate Gaussian having zero mean and unit variance.

### 中文转述

> [!question] 中文转述
> **原题14.6。** 利用Cholesky分解（Cholesky decomposition）将独立标准高斯向量变成给定均值和正定协方差的高斯向量。

## 提示

> [!hint]- 提示
> $L$ 可逆，直接使用密度变换并识别二次型和归一化常数。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 取 $\mathbf z\sim\mathcal N_D(0,I)$，$\Sigma=LL^{\mathsf T}\succ0$。由于 $L$ 可逆，$\mathbf z=L^{-1}(\mathbf y-\boldsymbol\mu)$。密度变换给
> $$
> p(\mathbf y)=(2\pi)^{-D/2}|\det L|^{-1}
> \exp\{-\tfrac12(\mathbf y-\boldsymbol\mu)^{\mathsf T}L^{-\mathsf T}L^{-1}(\mathbf y-\boldsymbol\mu)\}.
> $$
> 而 $L^{-\mathsf T}L^{-1}=\Sigma^{-1}$、$|\det L|=|\Sigma|^{1/2}$，所以这正是 $\mathcal N_D(\boldsymbol\mu,\Sigma)$。矩也直接满足 $\mathrm E\mathbf y=\boldsymbol\mu$、$\operatorname{Cov}\mathbf y=LIL^{\mathsf T}=\Sigma$。
>
> 为了从一元发生器生成所需 $\mathbf z$，必须独立生成各个标准高斯坐标；仅有各坐标边缘标准高斯而联合未知，不能保证该向量服从 $\mathcal N_D(0,I)$。

## 相关概念

- [[05 - 概率模型与推断/概念/概率推断|概率推断]]
- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已实际对照[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=471|印刷456／PDF471]]；正文引用范围见 `source_refs`。
- 英文原题与中文转述分列，原文疑误另注；未使用配套答案册。`source_status: verified` 仅表示本题及所列公式的实际核对范围；解答写成不表示个人学习完成，状态保持 `not-started`。
