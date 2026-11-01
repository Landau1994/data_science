---
title: "习题 P023：alpha散度在两个端点的KL极限"
topic: probability-theory
topic_label: 概率论
difficulty: intermediate
status: not-started
tags:
  - exercise
  - probability-theory
source: "[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Bishop 深度学习（DS003）]]"
source_id: DS003
source_chapter: 2
source_exercise: "2.28"
source_stars: 2
source_refs: ["DS003 Exercise 2.28，印刷61/PDF81", "DS003 §2.5.5，式(2.100)，印刷51/PDF71"]
source_status: verified
solution_status: independently-derived
created: 2026-11-01
---

# 习题 P023：alpha散度在两个端点的KL极限

## 题目

### 英文原题

> [!question] 英文原题
> **2.28 (★★)** The alpha family of divergences is defined by
> $$
> D_\alpha(p\|q)=\frac4{1-\alpha^2}\left(1-\int p(x)^{(1+\alpha)/2}q(x)^{(1-\alpha)/2}\,dx\right)\tag{2.129}
> $$
> where $-\infty<\alpha<\infty$ is a continuous parameter. Show that the Kullback–Leibler divergence $\mathrm{KL}(p\|q)$ corresponds to $\alpha\to1$. This can be done by writing $p^\epsilon=\exp(\epsilon\ln p)=1+\epsilon\ln p+O(\epsilon^2)$ and then taking $\epsilon\to0$. Similarly, show that $\mathrm{KL}(q\|p)$ corresponds to $\alpha\to-1$.

### 中文转述

> [!question] 中文转述
> **原题 2.28。** alpha散度族定义为式(2.129)：
> $$
> D_\alpha(p\|q)=\frac4{1-\alpha^2}\left(1-\int p(x)^{(1+\alpha)/2}q(x)^{(1-\alpha)/2}\,dx\right).
> $$
> 参数 $\alpha\in\mathbb R$。利用 $p^\epsilon=\exp(\epsilon\ln p)=1+\epsilon\ln p+O(\epsilon^2)$ 的展开，证明 $\alpha\to1$ 时得到 $\mathrm{KL}(p\|q)$；类似地证明 $\alpha\to-1$ 时得到 $\mathrm{KL}(q\|p)$。

## 提示

> [!hint]- 提示
> 在 $\alpha=1$ 附近令 $\epsilon=(1-\alpha)/2$，把积分写为 $\int p(q/p)^\epsilon$。注意分母也同时趋于0。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 先给可交换微分与积分的充分条件：$p,q$ 在共同支持上严格为正、归一化，并且在 $\alpha=\pm1$ 的邻域内，积分及其一阶导数被可积函数控制。例如有限共同支持且各点概率严格为正时必满足；连续情形若 $p/q$ 在支持上有正的上下界，也满足。更弱条件下可分别研究单侧极限，本页不把形式展开当成无条件双侧结论。
>
> 当 $\alpha\to1$ 时，置 $\epsilon=(1-\alpha)/2\to0$。有 $1-\alpha^2=4\epsilon(1-\epsilon)$，并且
> $$
> \begin{aligned}
> \int p^{(1+\alpha)/2}q^{(1-\alpha)/2}\,dx
> &=\int p^{1-\epsilon}q^\epsilon\,dx\\
> &=\int p\exp\{\epsilon\ln(q/p)\}\,dx\\
> &=1+\epsilon\int p\ln(q/p)\,dx+o(\epsilon)\\
> &=1-\epsilon\,\mathrm{KL}(p\|q)+o(\epsilon).
> \end{aligned}
> $$
> 代回式(2.129)，得到
> $$
> D_\alpha(p\|q)=\frac{\epsilon\,\mathrm{KL}(p\|q)+o(\epsilon)}{\epsilon(1-\epsilon)}
> \longrightarrow\mathrm{KL}(p\|q).
> $$
> 当 $\alpha\to-1$ 时，置 $\epsilon=(1+\alpha)/2\to0$。同样有 $1-\alpha^2=4\epsilon(1-\epsilon)$，而
> $$
> \int p^\epsilon q^{1-\epsilon}\,dx
> =\int q\exp\{\epsilon\ln(p/q)\}\,dx
> =1-\epsilon\,\mathrm{KL}(q\|p)+o(\epsilon).
> $$
> 因此 $D_\alpha(p\|q)\to\mathrm{KL}(q\|p)$。也可用恒等式 $D_\alpha(p\|q)=D_{-\alpha}(q\|p)$ 核对两个方向。
>
> 原式在 $\alpha=\pm1$ 处直接表现为 $0/0$，须按极限定义延拓；在任意实数 $\alpha$ 下积分也未必有限。若支持不一致，某个KL可能无穷，不能直接使用本页的有限一阶展开。

## 相关概念

- [[01 - 概率论/概念/相对熵|相对熵]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已核对 [[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=81|印刷第61页／PDF物理第81页]]；所引公式按 `source_refs` 记录的原页核对。
- 原书写成连续参数族并不意味着所有参数下散度都有限；端点及换序条件在解答中说明，英文原题与式(2.129)保持原样。
- `source_status: verified` 仅指本题原文、引用公式和定位的核对；解答为本库独立推导，未使用配套答案册。个人学习状态保留 `not-started`。
