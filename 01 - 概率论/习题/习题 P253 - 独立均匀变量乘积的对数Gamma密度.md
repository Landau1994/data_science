---
title: "习题 P253：独立均匀变量乘积的对数Gamma密度"
topic: "probability-theory"
topic_label: "概率论"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "probability-theory"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第4章习题4.54，印刷页164／PDF物理页195"
source_id: "DS011"
source_chapter: 4
source_exercise: "4.54"
source_stars: 0
source_refs: ["DS011 Exercise 4.54，印刷164／PDF物理195"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 P253：独立均匀变量乘积的对数Gamma密度

## 题目

### 英文原题

> [!question] 英文原题
> **4.54** Find the pdf of $\prod_{i=1}^nX_i$, where the $X_i$s are independent uniform$(0,1)$ random variables. (Hint: Try to calculate the cdf, and remember the relationship between uniforms and exponentials.)

### 中文转述

> [!question] 中文转述
> **原题4.54。**
> 求 $\prod_{i=1}^nX_i$ 的 pdf，其中 $X_i$ 为独立的 $\operatorname{uniform}(0,1)$ 随机变量. 提示：尝试计算 cdf，并记住均匀分布与指数分布的关系.

## 提示

> [!hint]- 提示
> 负对数把乘积变成$n$个独立尺度1指数变量的和。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 设$n\ge1$整数、$U=\prod_iX_i$，令$S=-\log U=\sum_i(-\log X_i)$。每项密度$e^{-s}$，$s>0$，独立卷积或mgf乘积给$S\sim\operatorname{Gamma}(n,1)$，密度$s^{n-1}e^{-s}/\Gamma(n)$。反变换$s=-\log u$的绝对导数为$1/u$，所以
> $$
> f_U(u)=\frac{(-\log u)^{n-1}}{(n-1)!},\quad0<u<1,
> $$
> 其他为0。归一化由$u=e^{-s}$转回Gamma积分验证。若要CDF，$F_U(u)=P(S\ge-\log u)=u\sum_{j=0}^{n-1}(-\log u)^j/j!$，$0<u<1$；这是整数形状Gamma尾积分反复分部积分所得，区间外分别0和1。

## 相关概念

- [[01 - 概率论/概念/概率模型|概率模型]]
- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/条件概率|条件概率]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=195|印刷第164页／PDF物理第195页]]；教材信息与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。原题无星号。
- `source_status: verified`仅指本题题干、公式及所列来源定位已核对，不表示全章正文独立复证。解答写成不等于个人已完成练习，学习状态保持`not-started`；未实测Obsidian界面渲染。
