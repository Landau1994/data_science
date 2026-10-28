---
title: "习题 DL136：GAN损失与JS散度的精确关系"
topic: "deep-learning"
topic_label: "深度学习"
difficulty: "intermediate"
status: "not-started"
tags:
  - exercise
  - deep-learning
source: "Understanding Deep Learning（2026-02-08修订稿），Problem 15.2，印刷303/PDF物理317"
source_id: "DS001"
source_chapter: 15
source_exercise: "15.2"
source_refs: ["DS001 Problem 15.2*，印刷303/PDF317", "DS001 式(15.8)–(15.9)，印刷282/PDF296"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-10-28"
---

# 习题 DL136：GAN损失与JS散度的精确关系

## 题目

### 英文原题

> [!question] 英文原题
> **Problem 15.2\*** Write an equation relating the loss $L$ in equation 15.8 to the Jensen-Shannon distance $D_{JS}[Pr(x)^*\|Pr(x)]$ in equation 15.9.

### 中文转述

> [!question] 中文转述
> 写出式(15.8)损失与式(15.9)的Jensen–Shannon散度之间的精确关系。

## 提示

> [!hint]- 提示
> 把对数中的常数2分离，并利用两个密度的积分均为1。

## 解答

> [!success]- 解答
> **独立推导。** 记真实密度 $p$、生成密度 $q$，均归一化，采用自然对数。最优判别器的式(15.8)为
> $$
> L=-\int q\log\frac q{p+q}-\int p\log\frac p{p+q}.
> $$
> 因而
> $$
> D_{\rm JS}(q\|p)=\tfrac12\int q\log\frac{2q}{p+q}
> +\tfrac12\int p\log\frac{2p}{p+q}=\log2-\frac L2.
> $$
> 即 $L=2\log2-2D_{\rm JS}(q\|p)$。此处是带负号的判别器损失；改用其相反数作GAN极小极大价值时，符号也要反转。

## 相关概念

- [[06 - 深度学习/概念/神经网络|神经网络]]
- [[01 - 概率论/概念/相对熵|相对熵]]

- [[06 - 深度学习/概念/生成对抗网络|生成对抗网络]]：生成器、判别器与对抗目标。

## 备注

- 原题：[[附件/books/UnderstandingDeepLearning_02_09_26_C.pdf#page=317|主书印刷303／PDF317]]；来源记录见 [[00 - 首页/教材归档/DS001 - Understanding Deep Learning|DS001]]。
- verified只覆盖本题实际核对的来源；解答独立撰写，学习状态不因归档改变。
