---
title: "习题 DL258：DeepDream的输入梯度与能量目标"
topic: deep-learning
topic_label: 深度学习
difficulty: beginner
status: not-started
tags: [exercise, deep-learning]
source: "[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Bishop《深度学习：基础与概念》（DS003）]]"
source_id: DS003
source_chapter: 10
source_exercise: "10.10"
source_stars: 1
source_refs: ["DS003 Exercise 10.10，印刷323／PDF物理339", "DS003 §10.3.5，DeepDream及式(10.12)，印刷308/PDF324"]
source_status: verified
solution_status: independently-derived
created: 2026-11-02
---

# 习题 DL258：DeepDream的输入梯度与能量目标

## 题目

### 英文原题

> [!question] 英文原题
> **10.10 (★)** The DeepDream update procedure involves setting the $\delta$ variables for backpropagation equal to the pre-activations of the nodes in the chosen layer and then running backpropagation to the input layer to get a gradient vector over the pixels of the image. Show that this can be derived as a gradient optimization with respect to the pixels of an image $\mathbf I$ applied to the function (10.12).

### 中文转述

> [!question] 中文转述
> DeepDream把所选层节点的反向传播误差信号 $\delta$ 设为该节点的预激活，再反传至输入像素，得到图像梯度。证明该更新可解释为对图像 $I$ 优化(10.12)的梯度过程。

## 提示

> [!hint]- 提示
> 对预激活平方和求导会出现2；将该常数吸收进学习率，或改用一半平方和。

## 解答

> [!success]- 解答
> **证明范围：独立推导。**
> 固定网络参数，选定层的预激活记为 $a_q(I)$，$q$ 合并空间位置和通道。原(10.12)是 $F(I)=\sum_q a_q(I)^2$。链式法则给
> $$
> \nabla_IF=2\sum_qa_q\nabla_Ia_q=2J_a(I)^{\mathsf T}a(I).
> $$
> 若反向传播从该层设 $\delta_q=a_q$，便得到 $g=J_a^{\mathsf T}a=\tfrac12\nabla_IF$，即一半平方能量 $F/2$ 的精确梯度。更新 $I_{\rm new}=I+\eta g$ 等价于用步长 $\eta/2$ 对 $F$ 做梯度**上升**，不是最小化该平方和。若要求严格得到 $\nabla F$，应把种子设为 $2a_q$。
>
> 在所取输入附近可微、梯度局部Lipschitz且 $\nabla F\ne0$ 时，足够小的正步长沿梯度上升会增加 $F$，由 $F(I+sv)=F(I)+s\nabla F^{\mathsf T}v+o(s)$ 即可看出。网络不可微点需按选定次梯度/分段路径约定计算；任意大步长、像素裁剪或额外平滑后不自动保证原 $F$ 单调。这些后处理是附加约束/正则操作，不是上面链式法则的一部分。

## 相关概念

- [[06 - 深度学习/概念/反向传播|反向传播]]
- [[03 - 线性代数与优化/概念/链式法则|链式法则]]
- [[06 - 深度学习/概念/卷积神经网络|卷积神经网络]]

## 备注

- 原题已实际查看 [[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=339|印刷323／PDF物理339]]；所列依赖正文亦逐页核对，精确位置见 `source_refs`。
- 原书平方和未含1/2，所述δ=a对应半梯度；常数由步长吸收的关系已明示。
- 解答未使用配套答案册。`source_status: verified` 指本题原文与所列依赖的核对范围；独立推导不代表个人学习完成，状态保持 `not-started`。
