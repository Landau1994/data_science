---
title: "习题 ST423：过原点最小二乘CLT及遗漏误差方差"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "advanced"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第12章习题12.28，印刷页492／PDF物理页523"
source_id: "DS011"
source_chapter: 12
source_exercise: "12.28"
source_stars: 0
source_refs: ["DS011 Exercise 12.28，印刷页492／PDF物理页523", "DS011 所引正文，印刷484／PDF物理515", "DS011 所引正文，印刷486／PDF物理517"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST423：过原点最小二乘CLT及遗漏误差方差

## 题目

### 英文原题

> [!question] 英文原题
> **12.28** Show that the least squares estimator is given by $\hat\beta=\sum_{i=1}^nx_iY_i/\sum_{i=1}^nx_i^2$, and $\sqrt n(\hat\beta-\beta)\to\mathrm n(0,1/\sigma_x^2)$.

### 中文转述

> [!question] 中文转述
> **原题12.28。**
> 证明最小二乘估计量为$\hat\beta=\sum_{i=1}^nx_iy_i/\sum_{i=1}^nx_i^2$，并且$\sqrt n(\hat\beta-\beta)\to\mathrm n(0,1/\sigma_x^2)$.

## 提示

> [!hint]- 提示
> 一般误差的渐近方差还应乘其方差；设计二次均值必须正。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 设$Y_i=\beta x_i+\varepsilon_i$，设计固定，$Q_n=\sum x_i^2>0$。对平方损失求导$-2\sum x_i(Y_i-bx_i)=0$，二阶导$2Q_n>0$，所以唯一估计为题列$\hat\beta$。
> 若误差iid且$E\varepsilon_i=0,\operatorname{Var}\varepsilon_i=\tau^2\in(0,\infty)$，$q_n=Q_n/n\to q>0$并$\max|x_i|/\sqrt n\to0$，则
> $$\sqrt n(\hat\beta-\beta)=\frac{n^{-1/2}\sum_i x_i\varepsilon_i}{q_n}.$$
> 分子方差$\tau^2q_n$；Lindeberg条件由阈值$\epsilon\sqrt n/\max|x_i|\to\infty$及误差二阶矩可积推出：截尾二阶矩上界为$q_nE[\varepsilon^2 I(|\varepsilon|>\epsilon\sqrt n/\max|x_i|)]\to0$。因此加权CLT及Slutsky给极限$N(0,\tau^2/q)$。
> 原题$1/\sigma_x^2$版本须额外取单位误差方差$\tau^2=1$。若误差$N(0,4)$且$x_i=1$，估计为样本均值，$\sqrt n(\hat\beta-\beta)$精确为$N(0,4)$，已反驳无条件单位方差断言。误差只有中位数0也不保证OLS无偏，必须另有零均值。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计（parameter estimation）]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]
- [[01 - 概率论/概念/随机变量|随机变量]]

## 备注

- 完整原题已逐页对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=523|印刷492／PDF物理523]]；原题无星号。教材信息与归档进度见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 实际引用输入核对页：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=515|印刷484／PDF物理515]]、[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=517|印刷486／PDF物理517]]；所需模型、公式、数据在解答重述。
- 来源已核对与解答写成不表示个人学习已完成；学习状态保留`not-started`。未实测Obsidian界面渲染。
