---
title: 习题 ST344：Gamma尺度参数的标准化得分
topic: mathematical-statistics
topic_label: 数理统计
difficulty: intermediate
status: not-started
tags:
- exercise
- mathematical-statistics
source: George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第10章习题10.38，印刷页415／PDF物理页446
source_id: DS011
source_chapter: 10
source_exercise: '10.38'
source_stars: 0
source_refs:
- DS011 Exercise 10.38，印刷415／PDF物理446
- DS011题内依赖核对：印刷399／PDF物理430
source_status: verified
solution_status: independently-derived
created: '2026-11-13'
---

# 习题 ST344：Gamma尺度参数的标准化得分

## 题目

### 英文原题

> [!question] 英文原题
> **10.38** Let $X_1,\ldots,X_n$ be a random sample from a gamma$(\alpha,\beta)$ population. Assume $\alpha$ is known and $\beta$ is unknown. Consider testing $H_0:\beta=\beta_0$. Derive a score statistic for testing $H_0$.

### 中文转述

> [!question] 中文转述
> **原题10.38。** 设$X_1,\ldots,X_n$为gamma$(\alpha,\beta)$总体的随机样本，假设$\alpha$已知、$\beta$未知. 考虑检验$H_0:\beta=\beta_0$，导出检验$H_0$的得分统计量.

## 提示

> [!hint]- 提示
> 总得分是sumX/β²−nα/β，信息为nα/β²。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 设$\alpha,\beta_0>0$。从$\beta$相关的对数似然$-n\alpha\log\beta-\sum_iX_i/\beta$得到$S(\beta_0)=(\sum_iX_i-n\alpha\beta_0)/\beta_0^2$。期望负二阶导给$I_n(\beta_0)=n\alpha/\beta_0^2$，故
> $$
> Z_S=\frac{\sum_iX_i-n\alpha\beta_0}{\beta_0\sqrt{n\alpha}}=\frac{\sqrt n(\bar X-\alpha\beta_0)}{\sqrt\alpha\beta_0}.
> $$
> 在零假设下其均值0、方差1；固定$\alpha$、$n\to\infty$时CLT给标准正态极限，双侧检验按$|Z_S|$与正态临界值比较。已知$\alpha$时$\sum_iX_i/\beta_0\sim\operatorname{Gamma}(n\alpha,1)$也可精确校准，但题中得分形式如上。

## 相关概念

- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/期望|期望]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/假设检验|假设检验]]

## 备注

- 来源：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=446|印刷第415页／PDF物理第446页]]；版本与归档见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 已实读本题所用正文：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=430|印刷399／PDF物理430]]；其余题内外部文献仅保留原引用，未声称查阅。
- 英文原题逐题对照PDF原始页面，保留原分题、提示、引用及可见疑误；原题无星号。题内引用补充与独立解答不混入原文；未查阅答案册或题内外部文献。
- 来源核对不表示个人学习完成，学习状态保持not-started。公式、链接与元数据检查不等于Obsidian实际渲染检查。
