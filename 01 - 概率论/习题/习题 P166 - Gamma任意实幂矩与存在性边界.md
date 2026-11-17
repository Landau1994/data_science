---
title: "习题 P166：Gamma任意实幂矩与存在性边界"
topic: "probability-theory"
topic_label: "概率论"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "probability-theory"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第3章习题3.17，印刷页107／PDF物理页138"
source_id: "DS011"
source_chapter: 3
source_exercise: "3.17"
source_stars: 0
source_refs: ["DS011 Exercise 3.17，印刷107／PDF物理138", "DS011 Gamma密度式(3.3.6)，印刷81／PDF物理112"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 P166：Gamma任意实幂矩与存在性边界

## 题目

### 英文原题

> [!question] 英文原题
> **3.17** Establish a formula similar to (3.3.18) for the gamma distribution. If $X\sim\operatorname{gamma}(\alpha,\beta)$, then for any positive constant $\nu$
> $$
> EX^\nu=\frac{\beta^\nu\Gamma(\nu+\alpha)}{\Gamma(\alpha)}.
> $$

### 中文转述

> [!question] 中文转述
> **原题3.17。** 对Gamma分布建立一个类似式3.3.18的公式. 若$X\sim\operatorname{gamma}(\alpha,\beta)$，则对任意正常数$\nu$，
>
> $$
> EX^\nu=\frac{\beta^\nu\Gamma(\nu+\alpha)}{\Gamma(\alpha)}.
> $$

## 提示

> [!hint]- 提示
> 先写明beta为尺度，再在矩积分中作尺度换元。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 采用形状$\alpha>0$、尺度$\beta>0$的密度$f(x)=x^{\alpha-1}e^{-x/\beta}/[\Gamma(\alpha)\beta^\alpha]$，$x>0$。直接积分并令$u=x/\beta$：
> $$
> EX^\nu=\frac1{\Gamma(\alpha)\beta^\alpha}\int_0^\infty x^{\nu+\alpha-1}e^{-x/\beta}dx
> =\frac{\beta^\nu}{\Gamma(\alpha)}\int_0^\infty u^{\nu+\alpha-1}e^{-u}du.
> $$
> 当$\nu+\alpha>0$时末项为$\Gamma(\nu+\alpha)$，得到公式，特别包含原题全部$\nu>0$。对负幂也仅在$\nu>-\alpha$成立；若$\nu\le-\alpha$，原点附近的正积分发散，不能用Gamma解析延拓冒充概率矩。

## 相关概念

- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/期望|期望]]
- [[01 - 概率论/概念/概率模型|概率模型]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=138|印刷第107页／PDF物理第138页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 英文原文、中文转述与本库独立解答分别保留；所用正文实际核对位置列于`source_refs`。题内文献只保留原题引用，不表示已查阅原文献。`source_status: verified`只指本题及所列位置核对，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
