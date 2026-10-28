---
title: "习题 DL142：正态变量经Sigmoid后的密度"
topic: deep-learning
topic_label: 深度学习
difficulty: intermediate
status: not-started
tags:
  - exercise
  - deep-learning
source: "Understanding Deep Learning（2026-02-08 修订稿），Problem 16.2，印刷325／PDF物理339"
source_id: DS001
source_chapter: 16
source_exercise: "16.2"
source_refs: ["DS001 Problem 16.2*，印刷325/PDF339"]
source_status: verified
solution_status: independently-derived
created: 2026-10-28
---

# 习题 DL142：正态变量经Sigmoid后的密度

## 题目

### 英文原题

> [!question] 英文原题
> **Problem 16.2\*** Consider transforming a standard normal distribution:
> $$
> Pr(z)=\frac1{\sqrt{2\pi}}\exp\left[\frac{-z^2}{2}\right],\tag{16.27}
> $$
> with the function:
> $$
> x=f[z]=\frac1{1+\exp[-z]}.\tag{16.28}
> $$
> Find an expression for the transformed distribution $Pr(x)$.

### 中文转述

> [!question] 中文转述
> 将式 (16.27) 的标准正态变量经式 (16.28) 的 Sigmoid 函数变换，求变换后的密度。


## 提示

> [!hint]- 提示
> 逆函数是 logit；别遗漏逆导数的绝对值。

## 解答

> [!success]- 解答
> 独立推导。映射严格递增，值域为 $(0,1)$。对该区间，
> $$
> z=\log\frac{x}{1-x},\qquad\frac{dz}{dx}=\frac1{x(1-x)}.
> $$
> 所以
> $$
> p_X(x)=\frac{\exp\{-\tfrac12[\log(x/(1-x))]^2\}}
> {\sqrt{2\pi}\,x(1-x)},\qquad0<x<1,
> $$
> 区间外密度为零。这是 logit-normal 分布；变量替换回 $z\in\mathbb R$ 可见其积分为一，端点没有点质量。

## 相关概念

- [[06 - 深度学习/概念/归一化流|归一化流]]：可逆变换、雅可比与密度变换。

## 备注

- 原题：[[附件/books/UnderstandingDeepLearning_02_09_26_C.pdf#page=339|印刷 325／PDF 339]]；教材记录见 [[00 - 首页/教材归档/DS001 - Understanding Deep Learning|DS001]]。
- 题干、公式及所引原页已核对；解答为独立推导。
