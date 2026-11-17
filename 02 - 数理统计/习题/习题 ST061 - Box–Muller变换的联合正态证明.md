---
title: 习题 ST061：Box–Muller变换的联合正态证明
topic: mathematical-statistics
topic_label: 数理统计
difficulty: intermediate
status: not-started
tags:
- exercise
- mathematical-statistics
source: George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第5章习题5.50，印刷页214／PDF物理页245
source_id: DS011
source_chapter: 5
source_exercise: '5.50'
source_stars: 0
source_refs:
- DS011 Exercise 5.50，印刷214／PDF物理245
- DS011题内依赖核对：印刷202／PDF物理233
source_status: verified
solution_status: independently-derived
created: '2026-11-13'
---

# 习题 ST061：Box–Muller变换的联合正态证明

## 题目

### 英文原题

> [!question] 英文原题
> **5.50** The Box-Muller method for generating normal pseudo-random variables (Example 5.6.4) is based on the transformation
> $$
> X_1=\cos(2\pi U_1)\sqrt{-2\log U_2},\quad X_2=\sin(2\pi U_1)\sqrt{-2\log U_2},
> $$
> where $U_1$ and $U_2$ are iid uniform$(0,1)$. Prove that $X_1$ and $X_2$ are independent $\operatorname n(0,1)$ random variables.

### 中文转述

> [!question] 中文转述
> **原题5.50。** 生成正态伪随机变量的Box–Muller方法（例5.6.4）基于变换
>
> $$
> X_1=\cos(2\pi U_1)\sqrt{-2\log U_2},\qquad X_2=\sin(2\pi U_1)\sqrt{-2\log U_2},
> $$
>
> 其中$U_1,U_2$为iid $\operatorname{uniform}(0,1)$.证明$X_1,X_2$是独立的$n(0,1)$随机变量.

## 提示

> [!hint]- 提示
> 先令Θ=2πU_1、R=√(−2log U_2)，再由极坐标Jacobian除以r。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** $\Theta=2\pi U_1\sim U(0,2\pi)$；$R=\sqrt{-2\log U_2}$的生存函数对$r\ge0$为$e^{-r^2/2}$，故$f_R(r)=re^{-r^2/2}$，$r>0$。由于分别来自独立均匀变量，$R,\Theta$独立，联合密度$r e^{-r^2/2}/(2\pi)$。
>
> 极坐标变换$x_1=r\cos\theta,x_2=r\sin\theta$在去掉一条射线及原点后几乎处处一一对应，正向Jacobian绝对值$r$。因此
> $$
> f_{X_1,X_2}(x_1,x_2)=\frac1{2\pi}e^{-(x_1^2+x_2^2)/2}=\phi(x_1)\phi(x_2).
> $$
> 它在全平面可取同一连续版本，分解为两个标准正态密度，所以两者独立且各为$N(0,1)$。去掉的零面积集合及$U_2$端点不影响分布。

## 相关概念

- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/期望|期望]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[02 - 数理统计/概念/参数估计|参数估计]]

## 备注

- 来源：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=245|印刷第214页／PDF物理第245页]]；版本与归档见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 已实读本题所用正文：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=233|印刷202／PDF物理233]]；其余题内外部文献仅保留原引用，未声称查阅。
- 英文原题逐题对照PDF原始页面，保留原分题、提示、引用及可见疑误；原题无星号。题内引用补充与独立解答不混入原文；未查阅答案册或题内外部文献。
- 来源核对不表示个人学习完成，学习状态保持not-started。公式、链接与元数据检查不等于Obsidian实际渲染检查。
