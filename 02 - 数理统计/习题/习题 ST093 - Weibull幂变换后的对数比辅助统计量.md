---
title: "习题 ST093：Weibull幂变换后的对数比辅助统计量"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第6章习题6.13，印刷页245／PDF物理页276"
source_id: "DS011"
source_chapter: 6
source_exercise: "6.13"
source_stars: 0
source_refs: ["DS011 Exercise 6.13，印刷245／PDF物理276"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST093：Weibull幂变换后的对数比辅助统计量

## 题目

### 英文原题

> [!question] 英文原题
> **6.13** Suppose $X_1$ and $X_2$ are iid observations from the pdf $f(x\mid\alpha)=\alpha x^{\alpha-1}e^{-x^\alpha}$, $x>0$, $\alpha>0$. Show that $(\log X_1)/(\log X_2)$ is an ancillary statistic.

### 中文转述

> [!question] 中文转述
> **原题6.13。**
> 设$X_1$和$X_2$为来自pdf $f(x\mid\alpha)=\alpha x^{\alpha-1}e^{-x^\alpha}$、$x>0$、$\alpha>0$的iid观测.说明$(\log X_1)/(\log X_2)$是辅助统计量.

## 提示

> [!hint]- 提示 1
> 先找一个把$\alpha$移到乘法因子上的变换。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 教材输入与补充假设另行标明。
>
> 令$Z_i=X_i^\alpha$。对$z>0$，
> $$
> P_\alpha(Z_i\le z)=P_\alpha(X_i\le z^{1/\alpha})=1-e^{-z}.
> $$
> 故$Z_1,Z_2$为不含$\alpha$的iid exponential$(1)$变量，且
> $$
> \frac{\log X_1}{\log X_2}
> =\frac{\alpha^{-1}\log Z_1}{\alpha^{-1}\log Z_2}
> =\frac{\log Z_1}{\log Z_2}.
> $$
> 右端分布不依赖$\alpha$，所以辅助。$X_2=1$使分母为0，但该事件在所有$\alpha$下概率均为0；可在此共同零概率集合任意定义统计量的值，不能把它误认为正概率的模型缺陷。

## 相关概念

- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[01 - 概率论/概念/概率模型|概率模型]]

## 备注

- 统一来源见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011教材台账]]；原题位于[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=276|印刷245／PDF物理276]]。已对照原始页面核对完整英文、分题与定位，原题无星号。
- 解答为独立推导；引用的教材结论按source_refs核对，不使用答案册代替证明。
- 来源核对、归档与个人学习分别记录；verified只指所列来源核对范围，学习状态保持not-started。未实测Obsidian渲染。
