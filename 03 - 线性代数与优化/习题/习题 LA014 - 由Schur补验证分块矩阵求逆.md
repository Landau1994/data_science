---
title: 习题 LA014：由Schur补验证分块矩阵求逆
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
source_exercise: '3.18'
source_stars: 2
source_refs:
- DS003 Exercise 3.18，印刷108/PDF127
- DS003 §3.2.4–3.2.6，式(3.60)–(3.61)，印刷78/PDF97；边缘与条件高斯及线性高斯模型，印刷81、83/PDF100、102
source_status: verified
solution_status: independently-derived
created: '2026-11-02'
---

# 习题 LA014：由Schur补验证分块矩阵求逆

## 题目

### 英文原题

> [!question] 英文原题
> **3.18 (★★)** Prove the identity (3.60) by multiplying both sides by the matrix
> $$
> \begin{pmatrix}A&B\\C&D\end{pmatrix}\tag{3.208}
> $$
> and making use of the definition (3.61).

### 中文转述

> [!question] 中文转述
> **原题3.18。** 利用式(3.61)定义的Schur补（Schur complement），直接分块相乘验证式(3.60)。

## 提示

> [!hint]- 提示
> 设 $M=(A-BD^{-1}C)^{-1}$，逐块计算乘积。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 假设 $D$ 与 $A-BD^{-1}C$ 可逆，各块尺寸相容。记 $S=A-BD^{-1}C$，$M=S^{-1}$，待验证矩阵为
> $$
> K=\begin{pmatrix}M&-MBD^{-1}\\-D^{-1}CM&D^{-1}+D^{-1}CMBD^{-1}\end{pmatrix}.
> $$
> 计算 $\begin{pmatrix}A&B\\C&D\end{pmatrix}K$ 的四块：
> $$
> \begin{aligned}
> (1,1)&=AM-BD^{-1}CM=SM=I,\\
> (1,2)&=-AMBD^{-1}+BD^{-1}+BD^{-1}CMBD^{-1}=-SMBD^{-1}+BD^{-1}=0,\\
> (2,1)&=CM-DD^{-1}CM=0,\\
> (2,2)&=-CMBD^{-1}+I+CMBD^{-1}=I.
> \end{aligned}
> $$
> 所以乘积为单位矩阵；方阵的右逆即双侧逆，得(3.60)。条件中单有整体矩阵可逆并不能保证该 $D^{-1}$ 版本可用，必须确认相应子块可逆。

## 相关概念

- [[01 - 概率论/概念/概率模型|概率模型]]
- [[03 - 线性代数与优化/概念/最优性条件|最优性条件]]

## 备注

- 原题已实际对照[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=127|印刷108／PDF127]]；正文引用范围见 `source_refs`。
- 英文原题与中文转述分列，原文疑误另注；未使用配套答案册。`source_status: verified` 仅表示本题及所列公式的实际核对范围；解答写成不表示个人学习完成，状态保持 `not-started`。
