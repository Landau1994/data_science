---
title: 习题 ST080：Metropolis目标密度的不变性与拒绝原子
topic: mathematical-statistics
topic_label: 数理统计
difficulty: advanced
status: not-started
tags:
- exercise
- mathematical-statistics
source: George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第5章习题5.69，印刷页217／PDF物理页248
source_id: DS011
source_chapter: 5
source_exercise: '5.69'
source_stars: 0
source_refs:
- DS011 Exercise 5.69，印刷217／PDF物理248
- DS011题内依赖核对：印刷207／PDF物理238
source_status: verified
solution_status: independently-derived
created: '2026-11-13'
---

# 习题 ST080：Metropolis目标密度的不变性与拒绝原子

## 题目

### 英文原题

> [!question] 英文原题
> **5.69** Show that the pdf $f_Y(y)$ is a stable point of the Metropolis algorithm. That is, if $Z_i\sim f_Y(y)$, then $Z_{i+1}\sim f_Y(y)$.

### 中文转述

> [!question] 中文转述
> **原题5.69。** 证明pdf $f_Y(y)$是Metropolis算法的稳定点（stable point）.即若$Z_i\sim f_Y(y)$，则$Z_{i+1}\sim f_Y(y)$.

## 提示

> [!hint]- 提示
> 写出接受转移和留在原点的拒绝质量，验证详细平衡。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 按本书独立提议形式，目标密度$f$、候选密度$g$在共同支持上为正，接受率
> $$
> \alpha(x,y)=\min\{1,f(y)g(x)/[f(x)g(y)]\}.
> $$
> 转移核为$K(x,dy)=g(y)\alpha(x,y)dy+r(x)\delta_x(dy)$，其中$r(x)=1-\int g(y)\alpha(x,y)dy$。不能把拒绝产生的原点原子省掉。
>
> 非对角接受流满足详细平衡
> $$
> f(x)g(y)\alpha(x,y)=\min\{f(x)g(y),f(y)g(x)\}=f(y)g(x)\alpha(y,x).
> $$
> 因此对任意Borel集$B$，用Tonelli交换非负积分，
> $$
> \begin{aligned}
> \int f(x)K(x,B)dx
> &=\int_B\int f(x)g(y)\alpha(x,y)dx\,dy+\int_Bf(y)r(y)dy\\
> &=\int_Bf(y)\left[\int g(x)\alpha(y,x)dx+r(y)\right]dy=\int_Bf(y)dy.
> \end{aligned}
> $$
> 所以若当前$Z_i$已经服从$f$，下一步也服从$f$，即平稳点或不变分布（invariant distribution）。此证明是不变性，不单独证明任意初始状态都收敛；后者还需不可约、非周期等条件。样本平稳也不使相邻状态独立。

## 相关概念

- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/期望|期望]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/重采样|重采样]]

## 备注

- 来源：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=248|印刷第217页／PDF物理第248页]]；版本与归档见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 实读本书Metropolis算法：印刷207／PDF238；证明同时保留接受连续部分与拒绝原子。
- 已实读本题所用正文：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=238|印刷207／PDF物理238]]；其余题内外部文献仅保留原引用，未声称查阅。
- 英文原题逐题对照PDF原始页面，保留原分题、提示、引用及可见疑误；原题无星号。题内引用补充与独立解答不混入原文；未查阅答案册或题内外部文献。
- 来源核对不表示个人学习完成，学习状态保持not-started。公式、链接与元数据检查不等于Obsidian实际渲染检查。
