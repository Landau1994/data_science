---
title: 习题 P051：von Mises分布的局部高斯极限
topic: probability-theory
topic_label: 概率论
difficulty: intermediate
status: not-started
tags:
- exercise
- probability-theory
source: '[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Bishop《深度学习：基础与概念》（DS003）]]'
source_id: DS003
source_chapter: 3
source_exercise: '3.31'
source_stars: 2
source_refs:
- DS003 Exercise 3.31，印刷110/PDF129
- DS003 §3.3，式(3.118)及图3.9，印刷90/PDF109；von Mises分布及MLE式(3.129)–(3.137)，印刷91–93/PDF110–112
source_status: verified
solution_status: independently-derived
created: '2026-11-02'
---

# 习题 P051：von Mises分布的局部高斯极限

## 题目

### 英文原题

> [!question] 英文原题
> **3.31 (★★)** For large $m$, the von Mises distribution (3.129) becomes sharply peaked around the mode $\theta_0$. By defining $\xi=m^{1/2}(\theta-\theta_0)$ and taking the Taylor expansion of the cosine function given by
> $$
> \cos\alpha=1-\frac{\alpha^2}{2}+O(\alpha^4)\tag{3.217}
> $$
> show that as $m\to\infty$, the von Mises distribution tends to a Gaussian.

### 中文转述

> [!question] 中文转述
> **原题3.31。** 令局部缩放角 $\xi=\sqrt m(\theta-\theta_0)$，用余弦展开证明von Mises分布（von Mises distribution）的局部高斯极限。

## 提示

> [!hint]- 提示
> 不仅要展开指数，还要处理归一化常数；原始角本身极限为点质量。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 采用绕众数展开的角差 $\delta\in[-\pi,\pi)$，原密度为 $e^{m\cos\delta}/[2\pi I_0(m)]$。令 $s=\sqrt m\delta$。对固定 $s$，
> $$
> m\{\cos(s/\sqrt m)-1\}=-s^2/2+O(s^4/m).
> $$
> 归一化积分满足
> $$
> 2\pi I_0(m)=\frac{e^m}{\sqrt m}\int_{-\pi\sqrt m}^{\pi\sqrt m}e^{m(\cos(s/\sqrt m)-1)}\,\mathrm ds.
> $$
> 在 $|u|\le\pi$ 上，由正弦在 $[0,\pi/2]$ 的凹性有 $1-\cos u=2\sin^2(u/2)\ge2u^2/\pi^2$。故将积分核在区间外延为0后，被可积函数 $e^{-2s^2/\pi^2}$ 控制。支配收敛给出积分趋于 $\sqrt{2\pi}$，即 $I_0(m)\sim e^m/\sqrt{2\pi m}$。
>
> 因此 $\xi=\sqrt m\delta$ 的密度
> $$
> p_\xi(s)=\frac{e^{m\cos(s/\sqrt m)}}{2\pi I_0(m)\sqrt m}\mathbf1_{\{|s|<\pi\sqrt m\}}
> \longrightarrow\frac{e^{-s^2/2}}{\sqrt{2\pi}}.
> $$
> 同一控制界保证分布收敛，于是局部可近似 $\delta\sim\mathcal N(0,m^{-1})$。原角分布在圆上趋向 $\theta_0$ 的点质量；“趋于高斯”应理解为缩放角差的极限，不能理解为原始角趋于一个固定非退化高斯。

## 相关概念

- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/期望|期望]]
- [[01 - 概率论/概念/概率模型|概率模型]]

## 备注

- 原题已实际对照[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=129|印刷110／PDF129]]；正文引用范围见 `source_refs`。
- 英文原题与中文转述分列，原文疑误另注；未使用配套答案册。`source_status: verified` 仅表示本题及所列公式的实际核对范围；解答写成不表示个人学习完成，状态保持 `not-started`。
