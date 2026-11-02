---
title: 习题 PM024：圆盘极坐标形式的Box–Muller变换
topic: probabilistic-models
topic_label: 概率模型与推断
difficulty: intermediate
status: not-started
tags:
- exercise
- probabilistic-models
source: '[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Bishop《深度学习：基础与概念》（DS003）]]'
source_id: DS003
source_chapter: 14
source_exercise: '14.5'
source_stars: 2
source_refs:
- DS003 Exercise 14.5，印刷456/PDF471
- DS003 §14.1.2，式(14.5)–(14.12)，印刷431–432/PDF446–447；图14.3，印刷433/PDF448
source_status: verified
solution_status: independently-derived
created: '2026-11-02'
---

# 习题 PM024：圆盘极坐标形式的Box–Muller变换

## 题目

### 英文原题

> [!question] 英文原题
> **14.5 (★★)** Suppose that $z_1$ and $z_2$ are uniformly distributed over the unit circle, as shown in Figure 14.3, and that we make the change of variables given by (14.10) and (14.11). Show that $(y_1,y_2)$ will be distributed according to (14.12).

### 中文转述

> [!question] 中文转述
> **原题14.5。** 设 $z_1,z_2$ 在图14.3所示单位圆内均匀分布，作(14.10)和(14.11)给出的变换。证明 $(y_1,y_2)$ 的联合分布为(14.12)。

## 提示

> [!hint]- 提示
> 圆盘半径平方为均匀变量；变换后半径服从Rayleigh密度，再除极坐标Jacobian。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 设 $R^2=Z_1^2+Z_2^2$、$\Theta$ 为极角。单位圆盘面积密度为 $1/\pi$，所以联合极坐标密度为 $r/\pi$，$0<r<1$、$0\le\theta<2\pi$。因此 $S=R^2\sim U(0,1)$ 与 $\Theta\sim U(0,2\pi)$ 独立。原变换为
> $$
> Y_i=Z_i\sqrt{-2\ln R^2/R^2},\qquad i=1,2.
> $$
> 故输出极半径 $\rho=\sqrt{-2\ln S}$，极角仍为 $\Theta$。由 $S=e^{-\rho^2/2}$ 得半径密度 $f_\rho(\rho)=\rho e^{-\rho^2/2}$。联合极密度为 $\rho e^{-\rho^2/2}/(2\pi)$，除以从直角坐标到极坐标的Jacobian $\rho$，得
> $$
> p(y_1,y_2)=\frac1{2\pi}e^{-(y_1^2+y_2^2)/2}
> =\left(\frac{e^{-y_1^2/2}}{\sqrt{2\pi}}\right)\left(\frac{e^{-y_2^2/2}}{\sqrt{2\pi}}\right),
> $$
> 即(14.12)，从因子分解可见两输出独立。$R=0$ 为零概率事件，实际生成中应丢弃该点。
>
> ![[附件/习题图/DS003/原图-14.3.png]]

## 相关概念

- [[05 - 概率模型与推断/概念/概率推断|概率推断]]
- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已实际对照[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=471|印刷456／PDF471]]；正文引用范围见 `source_refs`。
- 原图和正文明确为圆盘内部均匀，不是周长上的均匀；若仅在周长 $R=1$ 上，输出会退化为0。
- 英文原题与中文转述分列，原文疑误另注；未使用配套答案册。`source_status: verified` 仅表示本题及所列公式的实际核对范围；解答写成不表示个人学习完成，状态保持 `not-started`。
