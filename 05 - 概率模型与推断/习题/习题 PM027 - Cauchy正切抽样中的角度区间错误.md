---
title: 习题 PM027：Cauchy正切抽样中的角度区间错误
topic: probabilistic-models
topic_label: 概率模型与推断
difficulty: beginner
status: not-started
tags:
- exercise
- probabilistic-models
source: '[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Bishop《深度学习：基础与概念》（DS003）]]'
source_id: DS003
source_chapter: 14
source_exercise: '14.8'
source_stars: 1
source_refs:
- DS003 Exercise 14.8，印刷457/PDF472
- DS003 §14.1.3–14.1.4，式(14.13)–(14.17)，印刷433–435/PDF448–450
source_status: verified
solution_status: independently-derived
created: '2026-11-02'
---

# 习题 PM027：Cauchy正切抽样中的角度区间错误

## 题目

### 英文原题

> [!question] 英文原题
> **14.8 (★)** Suppose that $z$ has a uniform distribution over the interval $[0,1]$. Show that the variable $y=b\tan z+c$ has a Cauchy distribution given by (14.16).

### 中文转述

> [!question] 中文转述
> **原题14.8。** 设 $Z$ 在区间 $[0,1]$ 上均匀分布。证明变量 $Y=b\tan Z+c$ 服从式(14.16)给出的Cauchy分布（Cauchy distribution）。

## 提示

> [!hint]- 提示
> 当 $b>0$ 时，该变换只能生成 $[c,c+b\tan1]$ 内的值。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 按字面令尺度 $b>0$。正切在 $[0,1]$ 上单调且无极点，故 $Y$ 的支撑为 $[c,c+b\tan1]$。逆变换 $z=\arctan((y-c)/b)$ 给出
> $$
> p_Y(y)=\frac{1}{b\{1+((y-c)/b)^2\}}\mathbf1_{[c,c+b\tan1]}(y).
> $$
> 该密度积分为 $[\arctan((y-c)/b)]_c^{c+b\tan1}=1$，是截断的正切变换分布，并非支撑全实轴的Cauchy。$b=0$ 时更是退化点质量。
>
> 正确的均匀变换应为
> $$
> Y=c+b\tan\{\pi(Z-1/2)\},\qquad Z\sim U(0,1),
> $$
> 其全轴密度为 $1/[\pi b\{1+((y-c)/b)^2\}]$。等价地，可令正切的直接输入均匀分布于 $(-\pi/2,\pi/2)$。原书(14.16)形式 $q(y)=k/[1+(y-c)^2/b^2]$ 归一化时须取 $k=1/(\pi b)$；若把 $k$ 用作包络放大常数，则不再是归一化概率密度。

## 相关概念

- [[05 - 概率模型与推断/概念/概率推断|概率推断]]
- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已实际对照[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=472|印刷457／PDF472]]；正文引用范围见 `source_refs`。
- 主书正文印刷434／PDF449也有相同的均匀区间与正切输入问题；未静默更改英文。
- 英文原题与中文转述分列，原文疑误另注；未使用配套答案册。`source_status: verified` 仅表示本题及所列公式的实际核对范围；解答写成不表示个人学习完成，状态保持 `not-started`。
