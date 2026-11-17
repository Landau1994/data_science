---
title: "习题 ST192：Poisson事故数下降证据的单侧精确尾概率"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第8章习题8.2，印刷页326／PDF物理页357"
source_id: "DS011"
source_chapter: 8
source_exercise: "8.2"
source_stars: 0
source_refs: ["DS011 Exercise 8.2，印刷页326／PDF物理页357"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST192：Poisson事故数下降证据的单侧精确尾概率

## 题目

### 英文原题

> [!question] 英文原题
> **8.2** In a given city, it is assumed that the number of automobile accidents in a given year follows a Poisson distribution. In past years, the average number of accidents per year was 15, and this year it was 10. Is it justified to claim that the accident rate has dropped?

### 中文转述

> [!question] 中文转述
> **原题8.2。**
> 假设某城市一年内的汽车事故数服从泊松分布. 以往每年平均事故数为 $15$，今年为 $10$. 据此声称事故率下降，是否有充分依据？

## 提示

> [!hint]- 提示
> 将过去均值15视为已知基准，对今年的计数求左尾概率。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 以过去率15为已知基准，检验$H_0:\lambda\ge15$对$H_1:\lambda<15$，小计数支持下降。由于Poisson计数随参数随机增大，复合原假设的最坏左尾发生在15。观察10的单侧$p$值为
> $$p=P_{15}(X\le10)=e^{-15}\sum_{k=0}^{10}\frac{15^k}{k!}\approx0.1185.$$
> 所以在$.05$或$.10$水平均不能声称下降有充分统计证据。原题没有指定显著性水平，严格答案应报告$p$值及其判断条件，而不是无条件“是/否”；若过去的15本身也是估计值，则还需要过往计数及暴露时间才能建立相应两样本模型。

## 相关概念

- [[02 - 数理统计/概念/假设检验|假设检验（hypothesis testing）]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[01 - 概率论/概念/条件概率|条件概率]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 完整原题已逐页对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=357|印刷326／PDF物理357]]；原题无星号。教材信息及归档进度见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 来源已核对与独立解答写成不等于个人已完成练习；学习状态保留`not-started`。未实测Obsidian界面渲染。
