---
title: "习题 DL226：Logistic迭代映射的求值轨迹与导数"
topic: deep-learning
topic_label: 深度学习
difficulty: intermediate
status: not-started
tags: [exercise, deep-learning]
source: "[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Bishop《深度学习：基础与概念》（DS003）]]"
source_id: DS003
source_chapter: 8
source_exercise: "8.14"
source_stars: 2
source_refs: ["DS003 Exercise 8.14，印刷252／PDF物理269", "DS003 §8.2，表达式膨胀说明与式(8.42)–(8.43)，印刷245/PDF262"]
source_status: verified
solution_status: independently-derived
created: 2026-11-02
---

# 习题 DL226：Logistic迭代映射的求值轨迹与导数

## 题目

### 英文原题

> [!question] 英文原题
> **8.14 (★★)** The logistic map is a function defined by the iterative relation $L_{n+1}(x)=4L_n(x)(1-L_n(x))$ with $L_1(x)=x$. Write down the evaluation trace equations for $L_2(x)$, $L_3(x)$, and $L_4(x)$, and then write down expressions for the corresponding derivatives $L'_1(x)$, $L'_2(x)$, $L'_3(x)$, and $L'_4(x)$. Do not simplify the expressions but instead simply note how the complexity of the formulae for the derivatives grows much more rapidly than the expressions for the functions themselves.

### 中文转述

> [!question] 中文转述
> Logistic映射由 $L_{n+1}(x)=4L_n(x)(1-L_n(x))$、$L_1(x)=x$ 定义。写出 $L_2,L_3,L_4$ 的求值轨迹，再写出 $L'_1,L'_2,L'_3,L'_4$ 的表达式。不要化简表达式，只需观察导数公式的复杂度如何比函数公式增长得更快。

## 提示

> [!hint]- 提示
> 先保存每个 $L_n$；对导数应用乘积法则并保留重复的子表达式。区分表达式树与复用中间值的计算图。

## 解答

> [!success]- 解答
> **证明范围：独立推导。**
> 前向求值轨迹为
> $$
> v_1=x,\quad v_2=4v_1(1-v_1),\quad v_3=4v_2(1-v_2),\quad v_4=4v_3(1-v_3),
> $$
> 其中 $L_n=v_n$。不合并乘积法则所得项，逐项导数为
> $$
> d_1=1,
> $$
> $$
> d_2=4[1(1-v_1)+v_1(-1)],
> $$
> $$
> d_3=4\{4[1(1-v_1)+v_1(-1)](1-v_2)
> +v_2(-4[1(1-v_1)+v_1(-1)])\},
> $$
> $$
> d_4=4\Big\{4\{4[1(1-v_1)+v_1(-1)](1-v_2)+v_2(-4[1(1-v_1)+v_1(-1)])\}(1-v_3)
> +v_3\big(-4\{4[1(1-v_1)+v_1(-1)](1-v_2)+v_2(-4[1(1-v_1)+v_1(-1)])\}\big)\Big\}.
> $$
> 这里 $d_n=L'_n(x)$。直接复制展开时，前一步导数在每个新式中出现两次；若也把 $v_n$ 全部替换成其 $x$ 表达式，函数和导数的表达式树均迅速变长，导数包含额外重复项。
>
> 这种“表达式膨胀”不是必须的计算成本。只要复用轨迹中的 $v_n,d_n$，前向自动微分递推 $d_{n+1}=4[d_n(1-v_n)-v_nd_n]$ 每步只增加常数次运算，求值总成本随迭代次数线性增长。原题对复杂度的观察应限定为未经共享或化简的符号表达式，不能推成导数求值必比函数快指数增长。

## 相关概念

- [[06 - 深度学习/概念/自动微分|自动微分]]
- [[03 - 线性代数与优化/概念/链式法则|链式法则]]

## 备注

- 原题已实际查看 [[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=269|印刷252／PDF物理269]]；所列依赖正文亦逐页核对，精确位置见 `source_refs`。
- 解答未使用配套答案册。`source_status: verified` 指本题原文与所列依赖的核对范围；独立推导不代表个人学习完成，状态保持 `not-started`。
