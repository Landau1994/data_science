---
title: 习题 ST009：von Mises浓度估计与平均合向量长度
topic: mathematical-statistics
topic_label: 数理统计
difficulty: beginner
status: not-started
tags:
- exercise
- mathematical-statistics
source: '[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Bishop《深度学习：基础与概念》（DS003）]]'
source_id: DS003
source_chapter: 3
source_exercise: '3.34'
source_stars: 1
source_refs:
- DS003 Exercise 3.34，印刷110/PDF129
- DS003 §3.3，式(3.118)及图3.9，印刷90/PDF109；von Mises分布及MLE式(3.129)–(3.137)，印刷91–93/PDF110–112
source_status: verified
solution_status: independently-derived
created: '2026-11-02'
---

# 习题 ST009：von Mises浓度估计与平均合向量长度

## 题目

### 英文原题

> [!question] 英文原题
> **3.34 (★)** By making use of the result (3.118) together with (3.134) and the trigonometric identity (3.128), show that the maximum likelihood solution $m_{\mathrm{ML}}$ for the concentration of the von Mises distribution satisfies $A(m_{\mathrm{ML}})=\bar r$ where $\bar r$ is the radius of the mean of the observations viewed as unit vectors in the two-dimensional Euclidean plane, as illustrated in Figure 3.9.

### 中文转述

> [!question] 中文转述
> **原题3.34。** 将角度看作平面单位向量，证明浓度MLE满足 $A(m_{\mathrm{ML}})=\bar r$，其中 $\bar r$ 是平均合向量长度（mean resultant length），$A=I_1/I_0$。

## 提示

> [!hint]- 提示
> 把平均余弦差角写成平均向量与估计方向的内积。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 设 $\bar C=N^{-1}\sum_n\cos\theta_n$、$\bar S=N^{-1}\sum_n\sin\theta_n$，$\bar r=\sqrt{\bar C^2+\bar S^2}$。当 $\bar r>0$，取正确象限的估计方向使 $\cos\hat\theta_0=\bar C/\bar r$、$\sin\hat\theta_0=\bar S/\bar r$，于是
> $$
> \frac1N\sum_n\cos(\theta_n-\hat\theta_0)
> =\bar C\cos\hat\theta_0+\bar S\sin\hat\theta_0=\bar r.
> $$
> 对数似然为 $-N\ln(2\pi)-N\ln I_0(m)+m\sum_n\cos(\theta_n-\hat\theta_0)$。以 $I_0'(m)=I_1(m)$ 求导，驻点满足 $A(m)=\bar r$。该导数关系也可从 $I_0$ 的积分定义在积分号下求导得到。
>
> 对 $m\ge0$，$A'(m)=\operatorname{var}_m(\cos\delta)>0$（有限 $m$），并且 $A(0)=0$、$A(m)\to1$。因此 $0<\bar r<1$ 时有唯一有限浓度MLE；$\bar r=0$ 时最优 $m=0$ 且位置不确定；$\bar r=1$ 时所有样本方向一致，似然随 $m\to\infty$ 增长，没有有限浓度MLE。
>
> ![[附件/习题图/DS003/原图-3.9.png]]

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[01 - 概率论/概念/期望|期望]]
- [[03 - 线性代数与优化/概念/最优性条件|最优性条件]]

## 备注

- 原题已实际对照[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=129|印刷110／PDF129]]；正文引用范围见 `source_refs`。
- 原图3.9已实际查看并裁切保留；用atan2处理式(3.134)的象限。
- 英文原题与中文转述分列，原文疑误另注；未使用配套答案册。`source_status: verified` 仅表示本题及所列公式的实际核对范围；解答写成不表示个人学习完成，状态保持 `not-started`。
