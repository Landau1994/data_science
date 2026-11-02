---
title: 习题 LA013：Mahalanobis球对应椭球的体积
topic: linear-algebra-optimization
topic_label: 线性代数与优化
difficulty: intermediate
status: not-started
tags:
- exercise
- linear-algebra-optimization
source: '[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Bishop《深度学习：基础与概念》（DS003）]]'
source_id: DS003
source_chapter: 3
source_exercise: '3.17'
source_stars: 2
source_refs:
- DS003 Exercise 3.17，印刷108/PDF127
- DS003 §3.2.1，式(3.27)–(3.32)，印刷71–72/PDF90–91
source_status: verified
solution_status: independently-derived
created: '2026-11-02'
---

# 习题 LA013：Mahalanobis球对应椭球的体积

## 题目

### 英文原题

> [!question] 英文原题
> **3.17 (★★)** By diagonalizing the coordinate system using the eigenvector expansion (3.31), show that the volume contained within the hyperellipsoid corresponding to a constant Mahalanobis distance $\Delta$ is given by
> $$
> V_D|\Sigma|^{1/2}\Delta^D\tag{3.207}
> $$
> where $V_D$ is the volume of the unit sphere in $D$ dimensions, and the Mahalanobis distance is defined by (3.27).

### 中文转述

> [!question] 中文转述
> **原题3.17。** 用谱分解证明Mahalanobis距离（Mahalanobis distance）不超过 $\Delta$ 的椭球体积为式(3.207)，其中 $V_D$ 是单位球体积。

## 提示

> [!hint]- 提示
> 在特征方向先旋转，再按 $\sqrt{\lambda_i}$ 缩放。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 设 $\Sigma\succ0$，$\Delta\ge0$。取列为单位特征向量的正交矩阵 $U$，写 $\Sigma=U\operatorname{diag}(\lambda_i)U^{\mathsf T}$。变换
> $$
> \mathbf x=\boldsymbol\mu+U\operatorname{diag}(\sqrt{\lambda_i})\mathbf z
> $$
> 使 $(\mathbf x-\boldsymbol\mu)^{\mathsf T}\Sigma^{-1}(\mathbf x-\boldsymbol\mu)=\|\mathbf z\|^2$。Jacobian绝对值为 $|\det U|\prod_i\sqrt{\lambda_i}=|\Sigma|^{1/2}$。因此积分区域变成半径 $\Delta$ 的球，体积为
> $$
> \int_{\|\mathbf z\|\le\Delta}|\Sigma|^{1/2}\,\mathrm d\mathbf z
> =|\Sigma|^{1/2}V_D\Delta^D.
> $$
> 其中 $V_D=\pi^{D/2}/\Gamma(D/2+1)$ 已在第6章6.1独立求出。原题的“constant distance”指等距面围住的实体；等距面本身的 $D$ 维体积为0。

## 相关概念

- [[01 - 概率论/概念/概率模型|概率模型]]
- [[03 - 线性代数与优化/概念/链式法则|链式法则]]

## 备注

- 原题已实际对照[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=127|印刷108／PDF127]]；正文引用范围见 `source_refs`。
- 英文原题与中文转述分列，原文疑误另注；未使用配套答案册。`source_status: verified` 仅表示本题及所列公式的实际核对范围；解答写成不表示个人学习完成，状态保持 `not-started`。
