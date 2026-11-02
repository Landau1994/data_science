---
title: "习题 DL254：奇数核的对称same填充尺寸"
topic: deep-learning
topic_label: 深度学习
difficulty: beginner
status: not-started
tags: [exercise, deep-learning]
source: "[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Bishop《深度学习：基础与概念》（DS003）]]"
source_id: DS003
source_chapter: 10
source_exercise: "10.6"
source_stars: 1
source_refs: ["DS003 Exercise 10.6，印刷323／PDF物理339", "DS003 §10.2.3，padding尺寸说明，印刷294/PDF310"]
source_status: verified
solution_status: independently-derived
created: 2026-11-02
---

# 习题 DL254：奇数核的对称same填充尺寸

## 题目

### 英文原题

> [!question] 英文原题
> **10.6 (★)** Consider an image of size $J\times K$ that is padded with an additional $P$ pixels on all sides and which is then convolved using a kernel of size $M\times M$ where $M$ is an odd number. Show that if we choose $P=(M-1)/2$, then the resulting feature map will have size $J\times K$ and hence will be the same size as the original image.

### 中文转述

> [!question] 中文转述
> 图像尺寸为 $J\times K$，四周各填充 $P$ 个像素，再用奇数宽 $M\times M$ 的核卷积。证明取 $P=(M-1)/2$ 时输出仍为 $J\times K$。

## 提示

> [!hint]- 提示
> 沿每个方向，步长1的完整核窗口数为“填充后输入长−核长+1”。

## 解答

> [!success]- 解答
> **证明范围：独立推导。**
> 设 $J,K,M$ 为正整数、$M$ 为奇数，步长1、无空洞核且只计算完整窗口。填充后输入为 $(J+2P)\times(K+2P)$，所以窗口数为
> $$
> H_{\rm out}=J+2P-M+1,\qquad W_{\rm out}=K+2P-M+1.
> $$
> 取整数 $P=(M-1)/2\ge0$，代入即 $H_{\rm out}=J$、$W_{\rm out}=K$。奇数性保证左右、上下可用相同整数填充。该结论依赖步长1；步长大于1会改变输出窗口数。偶数核若要求输出同尺寸，通常需要两侧不等量填充，其总和为 $M-1$。

## 相关概念

- [[06 - 深度学习/概念/卷积神经网络|卷积神经网络]]
- [[06 - 深度学习/概念/前向传播|前向传播]]

## 备注

- 原题已实际查看 [[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=339|印刷323／PDF物理339]]；所列依赖正文亦逐页核对，精确位置见 `source_refs`。
- 解答未使用配套答案册。`source_status: verified` 指本题原文与所列依赖的核对范围；独立推导不代表个人学习完成，状态保持 `not-started`。
