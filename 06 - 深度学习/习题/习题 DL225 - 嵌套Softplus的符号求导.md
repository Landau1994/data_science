---
title: "习题 DL225：嵌套Softplus的符号求导"
topic: deep-learning
topic_label: 深度学习
difficulty: intermediate
status: not-started
tags: [exercise, deep-learning]
source: "[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Bishop《深度学习：基础与概念》（DS003）]]"
source_id: DS003
source_chapter: 8
source_exercise: "8.13"
source_stars: 2
source_refs: ["DS003 Exercise 8.13，印刷252／PDF物理269", "DS003 §8.2，式(8.44)–(8.48)，印刷245–246/PDF262–263"]
source_status: verified
solution_status: independently-derived
created: 2026-11-02
---

# 习题 DL225：嵌套Softplus的符号求导

## 题目

### 英文原题

> [!question] 英文原题
> **8.13 (★★)** Verify that the derivative of (8.47) is given by (8.48).

### 中文转述

> [!question] 中文转述
> 验证式(8.47)关于第一层权重的导数等于(8.48)。

## 提示

> [!hint]- 提示
> 把两个预激活分别命名；Softplus的导数就是Sigmoid。

## 解答

> [!success]- 解答
> **证明范围：独立推导。**
> 所引函数为 $h(a)=\ln(1+e^a)$，$y=h(w_2h(w_1x+b_1)+b_2)$。令 $A=w_1x+b_1$、$B=w_2\ln(1+e^A)+b_2$。对有限实参数，$h'(a)=e^a/(1+e^a)$，链式法则给
> $$
> \frac{\partial y}{\partial w_1}=h'(B)w_2h'(A)x
> =\frac{w_2x e^{A+B}}{(1+e^A)(1+e^B)}.
> $$
> 将 $A,B$ 展回即
> $$
> \frac{\partial y}{\partial w_1}
> =\frac{w_2x\exp(w_1x+b_1+b_2+w_2\ln[1+e^{w_1x+b_1}])}
> {(1+e^{w_1x+b_1})(1+\exp(b_2+w_2\ln[1+e^{w_1x+b_1}]))},\tag{8.48}
> $$
> 与原书一致。命名并缓存 $A,B,h(A)$ 可以避免重复计算；原式较长并不表示链式法则本身要求重复计算这些中间值。

## 相关概念

- [[06 - 深度学习/概念/激活函数|激活函数]]
- [[03 - 线性代数与优化/概念/链式法则|链式法则]]
- [[06 - 深度学习/概念/自动微分|自动微分]]

## 备注

- 原题已实际查看 [[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=269|印刷252／PDF物理269]]；所列依赖正文亦逐页核对，精确位置见 `source_refs`。
- 解答未使用配套答案册。`source_status: verified` 指本题原文与所列依赖的核对范围；独立推导不代表个人学习完成，状态保持 `not-started`。
