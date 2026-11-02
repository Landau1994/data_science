---
title: 习题 LA015：Woodbury矩阵求逆恒等式的乘法验证
topic: linear-algebra-optimization
topic_label: 线性代数与优化
difficulty: intermediate
status: not-started
tags:
- exercise
- linear-algebra-optimization
source: '[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Bishop《深度学习：基础与概念》（DS003）]]'
source_id: DS003
source_chapter: 3
source_exercise: '3.20'
source_stars: 2
source_refs:
- DS003 Exercise 3.20，印刷108/PDF127
- DS003 §3.2.4–3.2.6，式(3.60)–(3.61)，印刷78/PDF97；边缘与条件高斯及线性高斯模型，印刷81、83/PDF100、102
source_status: verified
solution_status: independently-derived
created: '2026-11-02'
---

# 习题 LA015：Woodbury矩阵求逆恒等式的乘法验证

## 题目

### 英文原题

> [!question] 英文原题
> **3.20 (★★)** A very useful result from linear algebra is the Woodbury matrix inversion formula given by
> $$
> (A+BCD)^{-1}=A^{-1}-A^{-1}B(C^{-1}+DA^{-1}B)^{-1}DA^{-1}.\tag{3.210}
> $$
> By multiplying both sides by $(A+BCD)$, prove the correctness of this result.

### 中文转述

> [!question] 中文转述
> **原题3.20。** 将Woodbury矩阵求逆公式（Woodbury matrix identity）(3.210)两侧乘以 $A+BCD$，证明该公式正确。

## 提示

> [!hint]- 提示
> 令 $S=C^{-1}+DA^{-1}B$，注意 $(A+BCD)A^{-1}B=BCS$。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 令 $A$ 为 $n\times n$、$C$ 为 $m\times m$ 的可逆矩阵，$B$ 为 $n\times m$、$D$ 为 $m\times n$，并假设 $S=C^{-1}+DA^{-1}B$ 可逆。设右侧为 $K$。利用
> $$
> (A+BCD)A^{-1}=I+BCDA^{-1},\qquad
> (A+BCD)A^{-1}B=B+BCDA^{-1}B=BCS,
> $$
> 可得
> $$
> (A+BCD)K=I+BCDA^{-1}-BCSS^{-1}DA^{-1}=I.
> $$
> 这证明 $K$ 是方阵 $A+BCD$ 的右逆，所以它必为双侧逆，恒等式成立。证明也表明在这些条件下 $A+BCD$ 自动可逆。若 $C$ 奇异，本题含 $C^{-1}$ 的版本无定义，需要使用其他等价形式，不能直接代入。

## 相关概念

- [[01 - 概率论/概念/概率模型|概率模型]]
- [[03 - 线性代数与优化/概念/最优性条件|最优性条件]]

## 备注

- 原题已实际对照[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=127|印刷108／PDF127]]；正文引用范围见 `source_refs`。
- 英文原题与中文转述分列，原文疑误另注；未使用配套答案册。`source_status: verified` 仅表示本题及所列公式的实际核对范围；解答写成不表示个人学习完成，状态保持 `not-started`。
