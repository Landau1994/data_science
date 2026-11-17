---
title: "习题 ST401：结构型EIV积分边缘的二元正态参数"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第12章习题12.6，印刷页489／PDF物理页520"
source_id: "DS011"
source_chapter: 12
source_exercise: "12.6"
source_stars: 0
source_refs: ["DS011 Exercise 12.6，印刷页489／PDF物理页520", "DS011 所引正文，印刷469／PDF物理500", "DS011 所引正文，印刷475／PDF物理506"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST401：结构型EIV积分边缘的二元正态参数

## 题目

### 英文原题

> [!question] 英文原题
> **12.6** Show that in the linear structural relationship model (12.2.6), if we integrate out $\xi_i$, the marginal distribution of $(X_i,Y_i)$ is given by (12.2.19).

### 中文转述

> [!question] 中文转述
> **原题12.6。**
> 证明在线性结构关系模型式12.2.6中，积分消去$\xi_i$后，$(X_i,Y_i)$的边际分布由式12.2.19给出.

## 提示

> [!hint]- 提示
> 用独立正态潜变量与两测量误差的线性组合求联合mgf。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 模型为$\xi_i\sim N(\xi,t)$，$\delta_i\sim N(0,d)$，$\varepsilon_i\sim N(0,e)$，三者相互独立，$X_i=\xi_i+\delta_i,Y_i=\alpha+\beta\xi_i+\varepsilon_i$，$d,e>0,t\ge0$。积分潜变量等价于取联合mgf：
> $$E e^{uX_i+vY_i}=\exp\left\{u\xi+v(\alpha+\beta\xi)+\tfrac12[(u+\beta v)^2t+u^2d+v^2e]\right\}.$$
> 这是均值向量$(\xi,\alpha+\beta\xi)$、协方差矩阵$\Sigma=\bigl(\begin{smallmatrix}d+t&\beta t\\\beta t&e+\beta^2t\end{smallmatrix}\bigr)$的二元正态mgf，唯一性证明了积分后的边缘分布。矩阵行列式$de+et+\beta^2dt>0$，所以密度适当。
> 原(12.2.19)写五个参数的最后一项$\beta\sigma_\xi^2$是协方差；若沿用第4章把第五项记为相关系数的记号，应改为$\rho=\beta t/\sqrt{(d+t)(e+\beta^2t)}$。本解用协方差矩阵避免把有量纲协方差误当相关系数，原引用式保留其实际记号。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计（parameter estimation）]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]
- [[01 - 概率论/概念/随机变量|随机变量]]

## 备注

- 完整原题已逐页对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=520|印刷489／PDF物理520]]；原题无星号。教材信息与归档进度见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 实际引用输入核对页：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=500|印刷469／PDF物理500]]、[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=506|印刷475／PDF物理506]]；所需模型、公式、数据在解答重述。
- 来源已核对与解答写成不表示个人学习已完成；学习状态保留`not-started`。未实测Obsidian界面渲染。
