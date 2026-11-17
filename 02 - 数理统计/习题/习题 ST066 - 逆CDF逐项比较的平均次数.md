---
title: 习题 ST066：逆CDF逐项比较的平均次数
topic: mathematical-statistics
topic_label: 数理统计
difficulty: intermediate
status: not-started
tags:
- exercise
- mathematical-statistics
source: George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第5章习题5.55，印刷页215／PDF物理页246
source_id: DS011
source_chapter: 5
source_exercise: '5.55'
source_stars: 0
source_refs:
- DS011 Exercise 5.55，印刷215／PDF物理246
- DS011题内依赖核对：印刷203／PDF物理234
source_status: verified
solution_status: independently-derived
created: '2026-11-13'
---

# 习题 ST066：逆CDF逐项比较的平均次数

## 题目

### 英文原题

> [!question] 英文原题
> **5.55** Suppose the method of (5.6.7) is used to generate the random variable $Y$, where $y_i=i$, $i=0,1,2,\ldots$. Show that the expected number of comparisons is $E(Y+1)$. (Hint: Exercise 2.14.)

### 中文转述

> [!question] 中文转述
> **原题5.55。** 设用式(5.6.7)的方法生成随机变量$Y$，其中$y_i=i$，$i=0,1,2,\ldots$.证明比较次数的期望为$E(Y+1)$.（提示：习题2.14.）

### 题内引用与条件

式(5.6.7)按累计概率从$y_0$开始顺序比较均匀随机数；本题的$y_i=i$使扫描索引与输出数值一致。

## 提示

> [!hint]- 提示
> 输出Y=i时已比较F(0),…,F(i)，恰好i+1次。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 式(5.6.7)的顺序逆CDF算法抽$U\sim U(0,1)$，从$i=0$开始依次比较$U\le F_Y(i)$，第一次成立即输出$i$。因此当输出$Y=i$时，比较次数$C=i+1$，逐点有$C=Y+1$。由逆变换$P(Y=i)=F_Y(i)-F_Y(i-1)$（$F_Y(-1)=0$），故
> $$
> EC=\sum_{i=0}^\infty(i+1)P(Y=i)=E(Y+1).
> $$
> 亦可用尾和$EC=\sum_{k=0}^\infty P(C>k)=1+\sum_{k=0}^\infty P(Y>k)=1+EY$。非负项求和在期望无限时仍成立。这里计数的是从0顺序扫描的比较，不是二分查找或预存别名表的成本。

## 相关概念

- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/期望|期望]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/重采样|重采样]]

## 备注

- 来源：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=246|印刷第215页／PDF物理第246页]]；版本与归档见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 已实读本题所用正文：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=234|印刷203／PDF物理234]]；其余题内外部文献仅保留原引用，未声称查阅。
- 英文原题逐题对照PDF原始页面，保留原分题、提示、引用及可见疑误；原题无星号。题内引用补充与独立解答不混入原文；未查阅答案册或题内外部文献。
- 来源核对不表示个人学习完成，学习状态保持not-started。公式、链接与元数据检查不等于Obsidian实际渲染检查。
