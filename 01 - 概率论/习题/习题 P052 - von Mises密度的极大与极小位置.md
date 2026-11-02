---
title: 习题 P052：von Mises密度的极大与极小位置
topic: probability-theory
topic_label: 概率论
difficulty: beginner
status: not-started
tags:
- exercise
- probability-theory
source: '[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Bishop《深度学习：基础与概念》（DS003）]]'
source_id: DS003
source_chapter: 3
source_exercise: '3.33'
source_stars: 1
source_refs:
- DS003 Exercise 3.33，印刷110/PDF129
- DS003 §3.3，式(3.118)及图3.9，印刷90/PDF109；von Mises分布及MLE式(3.129)–(3.137)，印刷91–93/PDF110–112
source_status: verified
solution_status: independently-derived
created: '2026-11-02'
---

# 习题 P052：von Mises密度的极大与极小位置

## 题目

### 英文原题

> [!question] 英文原题
> **3.33 (★)** By computing the first and second derivatives of the von Mises distribution (3.129), and using $I_0(m)>0$ for $m>0$, show that the maximum of the distribution occurs when $\theta=\theta_0$ and that the minimum occurs when $\theta=\theta_0+\pi\ (\bmod\ 2\pi)$.

### 中文转述

> [!question] 中文转述
> **原题3.33。** 计算von Mises密度的一阶、二阶导数，证明正浓度时众数在位置参数处、最小值在对径点。

## 提示

> [!hint]- 提示
> 密度处处为正，先求对数导数再转换为密度导数。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 记 $\delta=\theta-\theta_0$、$p=e^{m\cos\delta}/(2\pi I_0(m))$，其中 $m>0$。直接求导得
> $$
> p'=-m\sin\delta\,p,\qquad
> p''=(-m\cos\delta+m^2\sin^2\delta)p.
> $$
> 因 $p>0$，驻点仅有 $\delta=0,\pi\pmod{2\pi}$。前者二阶导数为 $-mp<0$，后者为 $mp>0$。又因 $\cos\delta\in[-1,1]$，这两个点分别是全局最大、全局最小，模 $2\pi$ 唯一。若 $m=0$，密度为 $1/(2\pi)$，每个角都是极大与极小点，严格性消失。

## 相关概念

- [[03 - 线性代数与优化/概念/最优性条件|最优性条件]]
- [[01 - 概率论/概念/概率模型|概率模型]]

## 备注

- 原题已实际对照[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=129|印刷110／PDF129]]；正文引用范围见 `source_refs`。
- 英文原题与中文转述分列，原文疑误另注；未使用配套答案册。`source_status: verified` 仅表示本题及所列公式的实际核对范围；解答写成不表示个人学习完成，状态保持 `not-started`。
