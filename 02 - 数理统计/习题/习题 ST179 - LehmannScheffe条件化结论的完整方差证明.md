---
title: "习题 ST179：LehmannScheffe条件化结论的完整方差证明"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第7章习题7.56，印刷页296／PDF物理页327"
source_id: "DS011"
source_chapter: 7
source_exercise: "7.56"
source_stars: 0
source_refs: ["DS011 Exercise 7.56，印刷296／PDF物理327", "DS011 定理7.3.23及例7.3.24前的目标断言，印刷280／PDF物理311"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST179：LehmannScheffe条件化结论的完整方差证明

## 题目

### 英文原题

> [!question] 英文原题
> **7.56** Prove the assertion made in the text preceding Example 7.3.24: If $T$ is a complete sufficient statistic for a parameter $\theta$, and $h(X_1,\ldots,X_n)$ is any unbiased estimator of $\tau(\theta)$, then $\phi(T)=E(h(X_1,\ldots,X_n)\mid T)$ is the best unbiased estimator of $\tau(\theta)$.

### 中文转述

> [!question] 中文转述
> **原题7.56。** 证明例7.3.24之前正文中的断言：若$T$是参数$\theta$的完备充分统计量，$h(X_1,\ldots,X_n)$是$\tau(\theta)$的任意无偏估计量，则$\varphi(T)=E(h(X_1,\ldots,X_n)\mid T)$是$\tau(\theta)$的最佳无偏估计量.

## 提示

> [!hint]- 提示
> 充分性保证条件化后的规则合法，完备性让所有无偏条件化结果相同。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 在常规支配模型下，充分性使给定$T$的样本条件分布可选为不依赖$\theta$，故$\phi(T)$确为同一个参数无关估计规则；设涉及的二阶矩有限。迭代期望首先给$E_\theta\phi(T)=E_\theta h=\tau(\theta)$。
>
> 任取另一个有限方差无偏估计$U$，令$\psi(T)=E(U\mid T)$。它也参数无关且无偏，所以$E_\theta[\psi(T)-\phi(T)]=0$对所有$\theta$成立。完备性推出$\psi(T)=\phi(T)$在每个参数下几乎必然。于是全方差恒等式给
> $$
> \operatorname{Var}_\theta U
> =\operatorname{Var}_\theta E(U\mid T)+E_\theta\operatorname{Var}(U\mid T)
> =\operatorname{Var}_\theta\phi(T)+E_\theta\operatorname{Var}(U\mid T)
> \ge\operatorname{Var}_\theta\phi(T).
> $$
> 因为$U$任意，$\phi(T)$在全部参数处同时最优，即最佳无偏估计。等号要求$U=\phi(T)$几乎必然，因此在有限方差类中唯一。只有一阶可积而二阶矩不有限时，条件化仍保持无偏；“最小有限方差”结论则必须先确认存在有限方差无偏估计，不能比较未定义的方差差。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=327|印刷第296页／PDF物理第327页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 英文原文、中文转述与本库独立解答分别保留；实际核对正文位置列于`source_refs`。题内文献引用不表示已查阅其原文。`source_status: verified`只指本题及所列位置的核对范围，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
