---
title: "习题 ST274：贝塔形状参数的Gamma后验可信区间"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第9章习题9.26，印刷页368／PDF物理页399"
source_id: "DS011"
source_chapter: 9
source_exercise: "9.26"
source_stars: 0
source_refs: ["DS011 Exercise 9.26，印刷368／PDF物理399"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST274：贝塔形状参数的Gamma后验可信区间

## 题目

### 英文原题

> [!question] 英文原题
> **9.26** Let $X_1,\ldots,X_n$ be iid observations from a $\operatorname{beta}(\theta,1)$ pdf and assume that $\theta$ has a $\operatorname{gamma}(r,\lambda)$ prior pdf. Find a $1-\alpha$ Bayes credible set for $\theta$.

### 中文转述

> [!question] 中文转述
> **原题9.26。**
> 设$X_1,\ldots,X_n$为来自$\operatorname{beta}(\theta,1)$密度的独立同分布观测，并假设$\theta$具有$\operatorname{gamma}(r,\lambda)$先验pdf. 求$\theta$的一个$1-\alpha$贝叶斯可信集.

## 提示

> [!hint]- 提示
> 将Beta样本似然写成$\theta^n\exp\{\theta\sum\log x_i\}$的核，与Gamma先验相乘；注意先验第二参数是尺度还是率。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 教材输入与补充假设另行标明。
>
> 设$W=-\sum_i\log x_i>0$，似然为$\theta^ne^{-\theta W}\prod_i x_i^{-1}$。先验核为$\theta^{r-1}e^{-\theta/\lambda}$，所以后验为形状$r+n$、尺度$\lambda_*=(W+1/\lambda)^{-1}$的Gamma。因此$2\theta/\lambda_*\mid x\sim\chi^2_{2(r+n)}$。取下侧分位数$q_{\nu,u}$，一个等尾可信区间是$[\lambda_*q_{2(r+n),\alpha/2}/2,\lambda_*q_{2(r+n),1-\alpha/2}/2]$。后验质量恰为$1-\alpha$，不等于对每个固定$\theta$的频率覆盖声明。Gamma尺度约定必须保留，不能把$\lambda$当率而写成$W+\lambda$。

## 相关概念

- [[02 - 数理统计/概念/区间估计|区间估计]]
- [[02 - 数理统计/概念/假设检验|假设检验]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[01 - 概率论/概念/概率模型|概率模型]]

## 备注

- 统一来源见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011教材台账]]；原题位于[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=399|印刷368／PDF物理399]]。已对照原始页面核对完整英文、分题与定位，原题无星号。
- 解答为独立推导；引用的教材结论按source_refs核对，不使用答案册代替证明。
- 来源核对、归档与个人学习分别记录；verified只指所列来源核对范围，学习状态保持not-started。未实测Obsidian渲染。
