---
title: "习题 ST409：三组Logistic回归曲线的中心与陡峭度"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "beginner"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第12章习题12.14，印刷页490／PDF物理页521"
source_id: "DS011"
source_chapter: 12
source_exercise: "12.14"
source_stars: 0
source_refs: ["DS011 Exercise 12.14，印刷页490／PDF物理页521", "DS011 所引正文，印刷479／PDF物理510"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST409：三组Logistic回归曲线的中心与陡峭度

## 题目

### 英文原题

> [!question] 英文原题
> **12.14** Graph the logistic regression function $\pi(x)$ from (12.3.2) for the three cases; $\alpha=\beta=1$, $\alpha=\beta=2$, and $\alpha=\beta=3$.

### 中文转述

> [!question] 中文转述
> **原题12.14。**
> 画出式12.3.2的逻辑回归函数$\pi(x)$在以下三种情形的图像：$\alpha=\beta=1$、$\alpha=\beta=2$、$\alpha=\beta=3$.

## 提示

> [!hint]- 提示
> 三个回归函数都在$x=-1$处取1/2，但斜率不同。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 原函数$\pi(x)=e^{\alpha+\beta x}/(1+e^{\alpha+\beta x})$。令共同参数$a=\alpha=\beta\in\{1,2,3\}$，则$\pi_a(x)=1/[1+e^{-a(1+x)}]$。它们都在$x=-1$取$1/2$，导数在该点为$a/4$，所以$a$越大转折越陡；在$x<-1$较大$a$的曲线较低，在$x>-1$较高，左右极限分别0、1。下图按这些精确公式绘制，标出共同中心，未把截距变化误解为三个不同的中点。
>
> ![[附件/习题图/DS011/习题12.14-Logistic曲线.png]]

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计（parameter estimation）]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]
- [[01 - 概率论/概念/随机变量|随机变量]]

## 备注

- 完整原题已逐页对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=521|印刷490／PDF物理521]]；原题无星号。教材信息与归档进度见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 实际引用输入核对页：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=510|印刷479／PDF物理510]]；所需模型、公式、数据在解答重述。
- 本题独立新绘图件保留[[附件/习题图/DS011/习题12.14-Logistic曲线.pdf|矢量PDF]]及[[附件/习题图/DS011/源码/第12章/ch12_14.tex|可编辑绘图源文件]]；按公式及实际拟合值生成。
- 来源已核对与解答写成不表示个人学习已完成；学习状态保留`not-started`。未实测Obsidian界面渲染。
