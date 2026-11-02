---
title: "习题 PM058：证据下界与后验KL的恒等分解"
topic: probabilistic-models
topic_label: 概率模型与推断
difficulty: beginner
status: not-started
tags:
  - exercise
  - probabilistic-models
source: "[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Bishop 深度学习（DS003）]]"
source_id: DS003
source_chapter: 15
source_exercise: "15.21"
source_stars: 1
source_refs:
  - "DS003 Exercise 15.21，印刷493/PDF508"
  - "DS003 §15.4，式15.51–15.54，印刷485/PDF500"
source_status: verified
solution_status: independently-derived
created: 2026-11-02
---

# 习题 PM058：证据下界与后验KL的恒等分解

## 题目

### 英文原题

> [!question] 英文原题
> **15.21 (★)** Verify the relation (15.52) in which $\mathcal L(q,\boldsymbol\theta)$ and $\operatorname{KL}(q\|p)$ are defined by (15.53) and (15.54), respectively.

### 中文转述

> [!question] 中文转述
> 验证关系式(15.52)，其中$\mathcal L(q,\boldsymbol\theta)$与$\operatorname{KL}(q\|p)$分别由(15.53)、(15.54)定义。

## 提示

> [!hint]- 提示 1
> 将$\log p(X,Z\mid\theta)$拆成后验对数与观测证据对数。

## 解答

> [!success]- 解答
> **独立推导。**
>
> 设$0<p(X\mid\theta)<\infty$，$q$是归一化的潜变量分布，并先假设$q$的支持包含在后验支持内、相关对数期望有限。定义
> $$
> \mathcal L(q,\theta)=\sum_Zq(Z)\log\frac{p(X,Z\mid\theta)}{q(Z)},
> $$
> $$
> \operatorname{KL}(q\|p)=\sum_Zq(Z)\log\frac{q(Z)}{p(Z\mid X,\theta)}.
> $$
> 利用$p(X,Z\mid\theta)=p(Z\mid X,\theta)p(X\mid\theta)$，逐项相加得到
> $$
> \mathcal L(q,\theta)+\operatorname{KL}(q\|p)
> =\sum_Zq(Z)\log p(X\mid\theta)
> =\log p(X\mid\theta),\tag{15.52}
> $$
> 其中最后一步用了$\sum_Zq(Z)=1$。KL非负，故$\mathcal L\leq\log p(X\mid\theta)$，且等号在$q=p(Z\mid X,\theta)$几乎处处时成立。
>
> 连续潜变量将求和改为积分；需要相同的绝对连续与可积条件。若$q$给后验零概率集合分配正质量，则KL为$+\infty$、下界为$-\infty$，不能把$(-\infty)+(+\infty)$当成普通已定义的数来运算；此时仍有下界不等式，但上述有限恒等式应在有意义的支持与可积范围内使用。零$q$项按零贡献约定。

## 相关概念

- [[05 - 概率模型与推断/概念/变分推断|变分推断]]
- [[01 - 概率论/概念/相对熵|相对熵]]
- [[05 - 概率模型与推断/概念/潜变量|潜变量]]

## 备注

- 原题已核对 DS003 印刷493页／PDF物理508页；正文引用的实际核对范围见 `source_refs`。
- 解答为独立推导；归档与个人学习状态分开，学习状态保持 `not-started`。
