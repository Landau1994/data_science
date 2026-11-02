---
title: "习题 LA027：Nesterov与普通动量的小步近似"
topic: linear-algebra-optimization
topic_label: 线性代数与优化
difficulty: beginner
status: not-started
tags: [exercise, linear-algebra-optimization]
source: "[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Bishop《深度学习：基础与概念》（DS003）]]"
source_id: DS003
source_chapter: 7
source_exercise: "7.11"
source_stars: 1
source_refs: ["DS003 Exercise 7.11，印刷231／PDF物理248", "DS003 §7.3.1，式(7.31)、(7.34)，印刷220、222/PDF237、239"]
source_status: verified
solution_status: independently-derived
created: 2026-11-02
---

# 习题 LA027：Nesterov与普通动量的小步近似

## 题目

### 英文原题

> [!question] 英文原题
> **7.11 (★)** Consider a smoothly varying error surface with low curvature such that the gradient varies only slowly with position. Show that, for small values of the learning rate and momentum parameters, the Nesterov momentum gradient update defined by (7.34) is equivalent to the standard gradient descent with momentum defined by (7.31).

### 中文转述

> [!question] 中文转述
> 误差面光滑且曲率低，梯度随位置缓慢变化。证明学习率和动量参数较小时，(7.34)的Nesterov动量更新近似等价于(7.31)的普通梯度下降加动量。

## 提示

> [!hint]- 提示
> 在当前 $w$ 处展开 $\nabla E(w+\mu v)$，估计被忽略项的范数。

## 解答

> [!success]- 解答
> **证明范围：独立推导。**
> 用 $v$ 表示前一步更新。原书两种更新分别为
> $$
> v_{\rm M}=-\eta\nabla E(w)+\mu v,\tag{7.31}\qquad
> v_{\rm N}=-\eta\nabla E(w+\mu v)+\mu v.\tag{7.34}
> $$
> 假设沿连接 $w$ 与 $w+\mu v$ 的线段 $E$ 二阶连续可微，则微积分基本定理给
> $$
> v_{\rm N}-v_{\rm M}=-\eta\mu\int_0^1H(w+t\mu v)v\,dt.
> $$
> 若该区域 $\|H\|_{\rm op}\le L$，便有 $\|v_{\rm N}-v_{\rm M}\|\le\eta|\mu|L\|v\|$。低曲率与小步使这个差异可忽略；忽略梯度在前瞻点的变化即得到普通动量。若 $H$ 连续，还可写 $v_{\rm N}=v_{\rm M}-\eta\mu H(w)v+o(\eta|\mu|\|v\|)$。
>
> 例如固定 $|\mu|<1$、梯度有界且从 $v_0=0$ 开始，普通动量递推满足 $\|v\|\le\eta G/(1-|\mu|)$，因此局部两更新差为 $O(\eta^2|\mu|L/(1-|\mu|))$。这说明题目的“equivalent”是保留低阶项的近似，不是一般函数上的精确恒等；梯度常量时才精确相同。

## 相关概念

- [[03 - 线性代数与优化/概念/梯度下降|梯度下降]]
- [[03 - 线性代数与优化/概念/梯度与驻点|梯度与驻点]]

## 备注

- 原题已实际查看 [[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=248|印刷231／PDF物理248]]；所列依赖正文亦逐页核对，精确位置见 `source_refs`。
- 解答未使用配套答案册。`source_status: verified` 指本题原文与所列依赖的核对范围；独立推导不代表个人学习完成，状态保持 `not-started`。
