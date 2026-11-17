---
title: "习题 P172：Pareto幂矩及均值方差不存在的分界"
topic: "probability-theory"
topic_label: "概率论"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "probability-theory"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第3章习题3.23，印刷页108／PDF物理页139"
source_id: "DS011"
source_chapter: 3
source_exercise: "3.23"
source_stars: 0
source_refs: ["DS011 Exercise 3.23，印刷108／PDF物理139"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 P172：Pareto幂矩及均值方差不存在的分界

## 题目

### 英文原题

> [!question] 英文原题
> **3.23** The Pareto distribution, with parameters $\alpha$ and $\beta$, has pdf
> $$
> f(x)=\frac{\beta\alpha^\beta}{x^{\beta+1}},\qquad\alpha<x<\infty,\quad\alpha>0,\quad\beta>0.
> $$
> (a) Verify that $f(x)$ is a pdf.
>
> (b) Derive the mean and variance of this distribution.
>
> (c) Show that the variance does not exist if $\beta\le2$.

### 中文转述

> [!question] 中文转述
> **原题3.23。** 参数为$\alpha,\beta$的Pareto分布具有pdf
>
> $$
> f(x)=\frac{\beta\alpha^\beta}{x^{\beta+1}},\qquad\alpha<x<\infty,\quad\alpha>0,\quad\beta>0.
> $$
>
> (a)  验证$f(x)$是pdf.
>
> (b)  推导这个分布的均值和方差.
>
> (c)  证明若$\beta\le2$，则方差不存在.

## 提示

> [!hint]- 提示
> 先求任意幂矩，积分收敛条件直接给两个分界。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** **(a)** 密度在$x>\alpha$为正，其积分为$\beta\alpha^\beta[-x^{-\beta}/\beta]_{\alpha}^{\infty}=1$，区间外取0。
>
> **(b)** 一般正幂矩满足
> $$
> EX^s=\beta\alpha^\beta\int_\alpha^\infty x^{s-\beta-1}dx
> =\frac{\beta\alpha^s}{\beta-s},\quad s<\beta,
> $$
> 而$s\ge\beta$时正积分发散。因此$\beta>1$时$EX=\beta\alpha/(\beta-1)$；$\beta>2$时
> $$
> \operatorname{Var}X=\frac{\beta\alpha^2}{\beta-2}-\frac{\beta^2\alpha^2}{(\beta-1)^2}
> =\frac{\beta\alpha^2}{(\beta-1)^2(\beta-2)}.
> $$
> **(c)** $1<\beta\le2$时均值有限但中心二阶矩无限；$0<\beta\le1$时均值本身为无穷，通常的有限均值方差定义不成立。两种情形都没有有限方差，不能把(b)的有理式延伸到$\beta\le2$得到负数“方差”。

## 相关概念

- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/期望|期望]]
- [[01 - 概率论/概念/概率模型|概率模型]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=139|印刷第108页／PDF物理第139页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 英文原文、中文转述与本库独立解答分别保留；所用正文实际核对位置列于`source_refs`。题内文献只保留原题引用，不表示已查阅原文献。`source_status: verified`只指本题及所列位置核对，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
