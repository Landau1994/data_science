---
title: "习题 P167：缩放负二项失败数的Gamma矩母函数极限"
topic: "probability-theory"
topic_label: "概率论"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "probability-theory"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第3章习题3.18，印刷页107／PDF物理页138"
source_id: "DS011"
source_chapter: 3
source_exercise: "3.18"
source_stars: 0
source_refs: ["DS011 Exercise 3.18，印刷107／PDF物理138", "DS011 负二项式(3.2.10)，印刷78／PDF物理109", "DS011 Gamma式(3.3.6)，印刷81／PDF物理112"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 P167：缩放负二项失败数的Gamma矩母函数极限

## 题目

### 英文原题

> [!question] 英文原题
> **3.18** There is an interesting relationship between negative binomial and gamma random variables, which may sometimes provide a useful approximation. Let $Y$ be a negative binomial random variable with parameters $r$ and $p$, where $p$ is the success probability. Show that as $p\to0$, the mgf of the random variable $pY$ converges to that of a gamma distribution with parameters $r$ and 1.

### 中文转述

> [!question] 中文转述
> **原题3.18。** 负二项随机变量与Gamma随机变量之间有一个有趣的关系，有时可提供有用的近似. 设$Y$为参数$r,p$的负二项随机变量，其中$p$为成功概率. 证明当$p\to0$时，随机变量$pY$的矩母函数收敛到参数为$r$和1的Gamma分布的矩母函数.

## 提示

> [!hint]- 提示
> 缩放变量的mgf在原mgf中把t换为pt，检查有限域t<1。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 固定$r>0$，$Y$使用成功$r$次前的失败次数参数化。则
> $$
> M_{pY}(t)=\left[\frac p{1-(1-p)e^{pt}}\right]^r.
> $$
> 对固定$t<1$，$e^{pt}=1+pt+O(p^2)$，所以分母$p(1-t)+O(p^2)$为正，mgf最终有定义，且$M_{pY}(t)\to(1-t)^{-r}$。用Gamma$(r,1)$密度积分，
> $$
> \frac1{\Gamma(r)}\int_0^\infty x^{r-1}e^{-(1-t)x}dx=(1-t)^{-r},\quad t<1.
> $$
> 这给出含0的共同邻域内的mgf收敛；对$t\ge1$不能声称有限mgf收敛。若采用总试验次数$Y+r$的另一约定，额外因子$e^{ptr}\to1$不改变极限，但本题沿用失败次数约定。

## 相关概念

- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/期望|期望]]
- [[01 - 概率论/概念/概率模型|概率模型]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=138|印刷第107页／PDF物理第138页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 英文原文、中文转述与本库独立解答分别保留；所用正文实际核对位置列于`source_refs`。题内文献只保留原题引用，不表示已查阅原文献。`source_status: verified`只指本题及所列位置核对，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
