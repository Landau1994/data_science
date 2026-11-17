---
title: "习题 ST104：两点参数Poisson族的不完备反例"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "beginner"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第6章习题6.24，印刷页246／PDF物理页277"
source_id: "DS011"
source_chapter: 6
source_exercise: "6.24"
source_stars: 0
source_refs: ["DS011 Exercise 6.24，印刷246／PDF物理277", "DS011 Definition 6.2.21，印刷232／PDF263"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST104：两点参数Poisson族的不完备反例

## 题目

### 英文原题

> [!question] 英文原题
> **6.24** Consider the following family of distributions:
> $$
> \mathcal P=\{P_\lambda(X=x):P_\lambda(X=x)=\lambda^xe^{-\lambda}/x!;\ x=0,1,2,\ldots;\ \lambda=0\text{ or }1\}.
> $$
> This is a Poisson family with $\lambda$ restricted to be 0 or 1. Show that the family $\mathcal P$ is not complete, demonstrating that completeness can be dependent on the range of the parameter. (See Exercises 6.15 and 6.18.)

### 中文转述

> [!question] 中文转述
> **原题6.24。**
> 考虑分布族
>
> $$
> \mathcal P=\{P_\lambda(X=x):P_\lambda(X=x)=\lambda^xe^{-\lambda}/x!;\ x=0,1,2,\ldots;\ \lambda=0\text{或}1\}.
> $$
>
> 这是把$\lambda$限制为0或1的Poisson族.说明$\mathcal P$不完备，从而展示完备性可能依赖参数的取值范围.（见习题6.15和习题6.18.）

## 提示

> [!hint]- 提示 1
> 有限个参数值只给有限个线性约束；尝试只在$1,2$两点非零的函数。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 教材输入与补充假设另行标明。
>
> 定义$g(0)=0,g(1)=1,g(2)=-2$，且对$x\ge3$取$g(x)=0$。在$\lambda=0$下$X=0$，所以$E_0g(X)=0$；在$\lambda=1$下，
> $$
> E_1g(X)=e^{-1}\left(1-\frac2{2!}\right)=0.
> $$
> 但$P_1(g(X)\ne0)=P_1(X=1)+P_1(X=2)>0$，且$g$有界，故满足完备性定义中的可积条件却不几乎处处为0，证明不完备。完整正参数Poisson族在6.18中完备；缩小参数集减少了零期望函数所受的约束，这与两题结论并不矛盾。

## 相关概念

- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[01 - 概率论/概念/概率模型|概率模型]]

## 备注

- 统一来源见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011教材台账]]；原题位于[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=277|印刷246／PDF物理277]]。已对照原始页面核对完整英文、分题与定位，原题无星号。
- 解答为独立推导；引用的教材结论按source_refs核对，不使用答案册代替证明。
- 来源核对、归档与个人学习分别记录；verified只指所列来源核对范围，学习状态保持not-started。未实测Obsidian渲染。
