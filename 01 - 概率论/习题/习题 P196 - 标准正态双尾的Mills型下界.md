---
title: "习题 P196：标准正态双尾的Mills型下界"
topic: "probability-theory"
topic_label: "概率论"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "probability-theory"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第3章习题3.47，印刷页111／PDF物理页142"
source_id: "DS011"
source_chapter: 3
source_exercise: "3.47"
source_stars: 0
source_refs: ["DS011 Exercise 3.47，印刷111／PDF物理142", "DS011 例3.6.3正态尾上界，印刷101／PDF物理132"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 P196：标准正态双尾的Mills型下界

## 题目

### 英文原题

> [!question] 英文原题
> **3.47** If $Z$ is a standard normal random variable, prove this companion to the inequality in Example 3.6.3:
> $$
> P(|Z|\ge t)\ge\sqrt{\frac2\pi}\frac t{1+t^2}e^{-t^2/2}.
> $$

### 中文转述

> [!question] 中文转述
> **原题3.47。** 若$Z$为标准正态随机变量，证明例3.6.3中不等式的以下对应式：
>
> $$
> P(|Z|\ge t)\ge\sqrt{\frac2\pi}\frac t{1+t^2}e^{-t^2/2}.
> $$

## 提示

> [!hint]- 提示
> 对积分中的e^{-x²/2}=x e^{-x²/2}/x作分部积分，再控制余项。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 对非平凡范围$t>0$，记$I(t)=\int_t^\infty e^{-x^2/2}dx$。分部积分得到
> $$
> I(t)=\frac{e^{-t^2/2}}t-\int_t^\infty\frac{e^{-x^2/2}}{x^2}dx
> \ge\frac{e^{-t^2/2}}t-\frac{I(t)}{t^2}.
> $$
> 移项即$I(t)\ge t e^{-t^2/2}/(1+t^2)$。乘以$2/\sqrt{2\pi}$并用标准正态对称性得所求。$t=0$时右侧0，结论成立；$t<0$时右侧非正、左侧为1，虽仍形式成立但没有尾界信息。全过程的积分边界项在无穷处由高斯衰减为0。

## 相关概念

- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/期望|期望]]
- [[01 - 概率论/概念/概率模型|概率模型]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=142|印刷第111页／PDF物理第142页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 英文原文、中文转述与本库独立解答分别保留；所用正文实际核对位置列于`source_refs`。题内文献只保留原题引用，不表示已查阅原文献。`source_status: verified`只指本题及所列位置核对，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
