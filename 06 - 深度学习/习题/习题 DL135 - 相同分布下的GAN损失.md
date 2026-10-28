---
title: "习题 DL135：相同分布下的GAN损失"
topic: "deep-learning"
topic_label: "深度学习"
difficulty: "intermediate"
status: "not-started"
tags:
  - exercise
  - deep-learning
source: "Understanding Deep Learning（2026-02-08修订稿），Problem 15.1，印刷303/PDF物理317"
source_id: "DS001"
source_chapter: 15
source_exercise: "15.1"
source_refs: ["DS001 Problem 15.1，印刷303/PDF317", "DS001 式(15.8)–(15.9)，印刷282/PDF296"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-10-28"
---

# 习题 DL135：相同分布下的GAN损失

## 题目

### 英文原题

> [!question] 英文原题
> **Problem 15.1** What will the loss be in equation 15.9 when $Pr(x^*)=Pr(x)$?

### 中文转述

> [!question] 中文转述
> 当生成分布与真实分布相同，式(15.9)的“损失”是多少？

## 提示

> [!hint]- 提示
> 区分式(15.9)的JS散度和式(15.8)的判别器负对数损失。

## 解答

> [!success]- 解答
> **独立推导。** 记两密度均为 $p$，混合密度也为 $p$。式(15.9)为
> $$
> D_{\rm JS}(p\|p)=\tfrac12D_{\rm KL}(p\|p)+\tfrac12D_{\rm KL}(p\|p)=0,
> $$
> 因为非零密度处 $\log(p/p)=0$，零密度处按 $0\log0=0$ 约定。
> 若“损失”实际指式(15.8)，则最优判别器输出 $1/2$，所以
> $$
> L=-\int p\log(1/2)-\int p\log(1/2)=2\log2.
> $$
> 不能把去掉常数与缩放后的JS值0当成未改写的判别器损失。

## 相关概念

- [[06 - 深度学习/概念/神经网络|神经网络]]
- [[01 - 概率论/概念/相对熵|相对熵]]

- [[06 - 深度学习/概念/生成对抗网络|生成对抗网络]]：生成器、判别器与对抗目标。

## 备注

- 原题：[[附件/books/UnderstandingDeepLearning_02_09_26_C.pdf#page=317|主书印刷303／PDF317]]；来源记录见 [[00 - 首页/教材归档/DS001 - Understanding Deep Learning|DS001]]。
- verified只覆盖本题实际核对的来源；解答独立撰写，学习状态不因归档改变。
