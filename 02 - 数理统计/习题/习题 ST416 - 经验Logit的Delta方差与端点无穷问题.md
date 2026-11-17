---
title: "习题 ST416：经验Logit的Delta方差与端点无穷问题"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "advanced"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第12章习题12.21，印刷页491／PDF物理页522"
source_id: "DS011"
source_chapter: 12
source_exercise: "12.21"
source_stars: 0
source_refs: ["DS011 Exercise 12.21，印刷页491／PDF物理页522"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST416：经验Logit的Delta方差与端点无穷问题

## 题目

### 英文原题

> [!question] 英文原题
> **12.21** Let $Y\sim\operatorname{binomial}(n,\pi)$, and let $\hat\pi=Y/n$ denote the MLE of $\pi$. Let $W=\log[\hat\pi/(1-\hat\pi)]$ denote the sample logit, the MLE of $\log[\pi/(1-\pi)]$. Use the delta method to show that $1/[n\hat\pi(1-\hat\pi)]$ is a reasonable estimate of $\operatorname{Var}W$.

### 中文转述

> [!question] 中文转述
> **原题12.21。**
> 设$Y\sim\operatorname{binomial}(n,\pi)$，用$\hat\pi=Y/n$表示$\pi$的MLE. 令$W=\log(\hat\pi/(1-\hat\pi))$为样本logit，即$\log(\pi/(1-\pi))$的MLE. 用Delta方法证明$1/(n\hat\pi(1-\hat\pi))$是$\operatorname{Var}W$的合理估计.

## 提示

> [!hint]- 提示
> Delta法在固定内部参数处给渐近方差；有限样本端点仍有正概率。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 设固定$0<\pi<1$，$g(p)=\log[p/(1-p)]$，$g'(p)=1/[p(1-p)]$。二项CLT给$\sqrt n(\hat\pi-\pi)\Rightarrow N(0,\pi(1-\pi))$。在内部点用一阶Taylor展开，得到$\sqrt n[g(\hat\pi)-g(\pi)]\Rightarrow N(0,1/[\pi(1-\pi)])$，故大样本方差近似为$1/[n\pi(1-\pi)]$。以一致估计$\hat\pi$代入得到题列估计$1/[n\hat\pi(1-\hat\pi)]$，在观察比例远离0、1时是常用Delta标准误平方。
> 严格有限样本边界须说明：$Y=0$或$n$的概率$(1-\pi)^n+\pi^n>0$，原$W$在这些点为无穷，不是有有限无条件方差的实随机变量。因此“估计Var$W$”只能按内部参数的大样本近似理解，不能声称它等于有限$n$真实方差。可先用有限连续性修正$\tilde p=(Y+1/2)/(n+1)$定义有限logit，因$\tilde p-\hat p=O(1/n)$而有同一一阶Delta极限；这是另列的修复，不混入原题定义。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计（parameter estimation）]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]
- [[01 - 概率论/概念/随机变量|随机变量]]

## 备注

- 完整原题已逐页对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=522|印刷491／PDF物理522]]；原题无星号。教材信息与归档进度见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 来源已核对与解答写成不表示个人学习已完成；学习状态保留`not-started`。未实测Obsidian界面渲染。
