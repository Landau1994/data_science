---
title: "习题 P161：二项计数与负二项等待的CDF互补关系"
topic: "probability-theory"
topic_label: "概率论"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "probability-theory"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第3章习题3.12，印刷页106／PDF物理页137"
source_id: "DS011"
source_chapter: 3
source_exercise: "3.12"
source_stars: 0
source_refs: ["DS011 Exercise 3.12，印刷106／PDF物理137", "DS011 式(3.2.10)失败次数参数化，印刷78／PDF物理109"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 P161：二项计数与负二项等待的CDF互补关系

## 题目

### 英文原题

> [!question] 英文原题
> **3.12** Suppose $X$ has a binomial$(n,p)$ distribution and let $Y$ have a negative binomial$(r,p)$ distribution. Show that $F_X(r-1)=1-F_Y(n-r)$.

### 中文转述

> [!question] 中文转述
> **原题3.12。** 设$X$具有二项$(n,p)$分布，$Y$具有负二项$(r,p)$分布. 证明$F_X(r-1)=1-F_Y(n-r)$.

## 提示

> [!hint]- 提示
> 成功次数不足r，等价于第r次成功晚于第n次试验。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 沿用式(3.2.10)，$Y$是第$r$次成功前的失败数，取$r\ge1$整数、$0<p<1$。在同一无限独立Bernoulli序列上，令$X$为前$n$次的成功数，第$r$次成功时刻为$T_r=Y+r$。则
> $$
> \{X\ge r\}=\{T_r\le n\}=\{Y\le n-r\}.
> $$
> 取补即$P(X\le r-1)=1-P(Y\le n-r)$。当$r>n$时两边都为1，因为$Y\ge0$；无需假定两个边缘变量在原叙述中独立，这里为证明关系选择共同构造。

## 相关概念

- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/期望|期望]]
- [[01 - 概率论/概念/概率模型|概率模型]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=137|印刷第106页／PDF物理第137页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 英文原文、中文转述与本库独立解答分别保留；所用正文实际核对位置列于`source_refs`。题内文献只保留原题引用，不表示已查阅原文献。`source_status: verified`只指本题及所列位置核对，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
