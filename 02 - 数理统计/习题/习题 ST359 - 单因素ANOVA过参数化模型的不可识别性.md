---
title: "习题 ST359：单因素ANOVA过参数化模型的不可识别性"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第11章习题11.5，印刷页456／PDF物理页487"
source_id: "DS011"
source_chapter: 11
source_exercise: "11.5"
source_stars: 0
source_refs: ["DS011 Exercise 11.5，印刷456／PDF物理487", "DS011 过参数化模型式(11.2.2)，印刷422／PDF物理453"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST359：单因素ANOVA过参数化模型的不可识别性

## 题目

### 英文原题

> [!question] 英文原题
> **11.5** Suppose that random variables $Y_{ij}$ are observed according to the overparameterized oneway ANOVA model in (11.2.2). Show that, without some restriction on the parameters, this model is not identifiable by exhibiting two distinct collections of parameters that lead to exactly the same distribution of the $Y_{ij}$s.

### 中文转述

> [!question] 中文转述
> **原题11.5。** 假设按照式11.2.2的过参数化单因素ANOVA模型观测随机变量$Y_{ij}$. 给出两组不同的参数，使$Y_{ij}$具有完全相同的分布，从而说明：若不对参数施加某种限制，该模型不可识别.

## 提示

> [!hint]- 提示
> 给共同截距加常数，同时从每个处理效应减去相同常数。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 原模型是$Y_{ij}=\mu+\tau_i+\varepsilon_{ij}$，误差分布与这些均值参数分离。任取非零常数$c$，将参数变为$\mu'=\mu+c$、$\tau_i'=\tau_i-c$，则每个$\mu'+\tau_i'=\mu+\tau_i$；保持误差方差及联合误差分布相同，全部观测的联合分布就完全相同，参数向量却不同。
>
> 显式例子是$(\mu,\tau_1,\ldots,\tau_k)=(0,0,\ldots,0)$与$(1,-1,\ldots,-1)$，均使所有均值为0。故未加限制的参数化不是可识别模型（identifiable model）。限制如$\sum_i\tau_i=0$、或$\sum_i n_i\tau_i=0$、或固定某个$\tau_i=0$可选定唯一代表，但这些不同约束对应不同的$\mu$解释；可识别的基本量是处理均值$\theta_i=\mu+\tau_i$。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=487|印刷第456页／PDF物理第487页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 英文原文、中文转述与本库独立解答分别保留；实际核对正文位置列于`source_refs`。题内文献引用不表示已查阅其原文。`source_status: verified`只指本题及所列位置的核对范围，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
