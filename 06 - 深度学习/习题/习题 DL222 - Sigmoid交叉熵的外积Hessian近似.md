---
title: "习题 DL222：Sigmoid交叉熵的外积Hessian近似"
topic: deep-learning
topic_label: 深度学习
difficulty: intermediate
status: not-started
tags: [exercise, deep-learning]
source: "[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Bishop《深度学习：基础与概念》（DS003）]]"
source_id: DS003
source_chapter: 8
source_exercise: "8.10"
source_stars: 2
source_refs: ["DS003 Exercise 8.10，印刷251／PDF物理268", "DS003 §8.1.6，式(8.36)–(8.41)，印刷242–244/PDF259–261"]
source_status: verified
solution_status: independently-derived
created: 2026-11-02
---

# 习题 DL222：Sigmoid交叉熵的外积Hessian近似

## 题目

### 英文原题

> [!question] 英文原题
> **8.10 (★★)** Derive the expression (8.41) for the outer product approximation of a Hessian matrix for a network having a single output with a logistic-sigmoid output-unit activation function and a cross-entropy error function, corresponding to the result (8.40) for the sum-of-squares error function.

### 中文转述

> [!question] 中文转述
> 单输出采用逻辑Sigmoid激活和交叉熵损失。推导对应平方损失外积近似(8.40)的Hessian近似(8.41)。

## 提示

> [!hint]- 提示
> 先在输出预激活 $a_n$ 上求损失的一、二阶导数，再对网络权重使用二阶链式法则。

## 解答

> [!success]- 解答
> **证明范围：独立推导。**
> 设 $y_n=\sigma(a_n(w))$，$E=-\sum_n[t_n\ln y_n+(1-t_n)\ln(1-y_n)]$，其中 $t_n\in\{0,1\}$、预激活有限且二阶可微。对单样本直接求导有 $\partial E_n/\partial a_n=y_n-t_n$、$\partial^2E_n/\partial a_n^2=y_n(1-y_n)$。因此
> $$
> H=\sum_n\left[y_n(1-y_n)g_ng_n^{\mathsf T}+(y_n-t_n)\nabla_w^2a_n\right],\quad g_n=\nabla_wa_n.
> $$
> 舍去残差乘预激活二阶导数的项，得到
> $$
> H\simeq G=\sum_ny_n(1-y_n)\nabla a_n\nabla a_n^{\mathsf T}.\tag{8.41}
> $$
> 权重非负，故 $G\succeq0$。若 $a_n$ 关于参数仿射（逻辑回归），第二项恒为0，近似即精确Hessian。若模型的 $y(x)$ 等于真实条件类别概率，则在给定输入的标签分布下 $\mathbb E[y-T\mid x]=0$，第二项的条件期望为0（需可积）；任意有限样本或任意网络参数下则不必为0。这里的外积是 $\nabla a$ 的加权外积，不是任意情况下的样本损失梯度外积。

## 相关概念

- [[04 - 统计学习/概念/交叉熵|交叉熵]]
- [[06 - 深度学习/概念/激活函数|激活函数]]
- [[03 - 线性代数与优化/概念/链式法则|链式法则]]

## 备注

- 原题已实际查看 [[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=268|印刷251／PDF物理268]]；所列依赖正文亦逐页核对，精确位置见 `source_refs`。
- 解答未使用配套答案册。`source_status: verified` 指本题原文与所列依赖的核对范围；独立推导不代表个人学习完成，状态保持 `not-started`。
