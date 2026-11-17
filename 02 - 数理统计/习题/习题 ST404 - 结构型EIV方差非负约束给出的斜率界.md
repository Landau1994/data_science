---
title: "习题 ST404：结构型EIV方差非负约束给出的斜率界"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第12章习题12.9，印刷页489／PDF物理页520"
source_id: "DS011"
source_chapter: 12
source_exercise: "12.9"
source_stars: 0
source_refs: ["DS011 Exercise 12.9，印刷页489／PDF物理页520", "DS011 所引正文，印刷475／PDF物理506"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST404：结构型EIV方差非负约束给出的斜率界

## 题目

### 英文原题

> [!question] 英文原题
> **12.9** In the structural relationship model, the solution to the equations in (12.2.20) implies a restriction on $\hat\beta$, the same restriction we encountered in the functional relationship case (Exercise 12.4).
> (a) Show that in (12.2.20), the MLE of $\sigma_\delta^2$ is nonnegative only if $S_{xx}\ge(1/\hat\beta)S_{xy}$. Also, the MLE of $\sigma_\varepsilon^2$ is nonnegative only if $S_{yy}\ge\hat\beta S_{xy}$.
> (b) Show that the restrictions in part (a), together with the rest of the equations in (12.2.20), imply that
> $$\frac{|S_{xy}|}{S_{xx}}\le|\hat\beta|\le\frac{S_{yy}}{|S_{xy}|}.$$

### 中文转述

> [!question] 中文转述
> **原题12.9。**
> 结构关系模型中，式12.2.20的解对$\hat\beta$施加一个限制，与函数关系情形的限制相同（习题12.4）.
>
> (a)  证明式12.2.20中，$\sigma_\delta^2$的MLE非负仅当$S_{xx}\ge(1/\hat\beta)S_{xy}$；$\sigma_\varepsilon^2$的MLE非负仅当$S_{yy}\ge\hat\beta S_{xy}$.
>
> (b)  证明(a)的限制与式12.2.20其余方程共同推出
>
> $$
> \frac{|S_{xy}|}{S_{xx}}\le|\hat\beta|\le\frac{S_{yy}}{|S_{xy}|}.
> $$

## 提示

> [!hint]- 提示
> 先由潜变量方差非负确定斜率与交叉积同号，再合法除以正数。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 记$A=S_{xx},B=S_{yy},C=S_{xy}$，先设$A,B>0,C\ne0$。(12.2.20)的交叉矩给$t=C/(n\hat\beta)$，所以$t\ge0$要求$\hat\beta$与$C$同号，且此时$t>0$。
> (a) 代入方差方程得$d=(A-C/\hat\beta)/n$、$e=(B-\hat\beta C)/n$，非负性立即给原题两界（在这些方程范围内也是等价条件）。
> (b) 由于$C/\hat\beta=|C|/|\hat\beta|$，第一不等式给$|\hat\beta|\ge|C|/A$；又$\hat\beta C=|\hat\beta||C|$，第二给$|\hat\beta|\le B/|C|$。样本Cauchy–Schwarz保证下界不超过上界。
> 若$C=0$，题内倒数界未定义；方程$\hat\beta t=0$允许斜率0且$t>0$，或$t=0$使斜率不再通过协方差识别，不能硬套除法。完全相关$AB=C^2$使两界相等且至少误差方差落边界，须与正定内部解区分。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计（parameter estimation）]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]
- [[01 - 概率论/概念/随机变量|随机变量]]

## 备注

- 完整原题已逐页对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=520|印刷489／PDF物理520]]；原题无星号。教材信息与归档进度见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 实际引用输入核对页：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=506|印刷475／PDF物理506]]；所需模型、公式、数据在解答重述。
- 来源已核对与解答写成不表示个人学习已完成；学习状态保留`not-started`。未实测Obsidian界面渲染。
