---
title: "习题 P184：重参数化与共同均值Gamma参数空间"
topic: "probability-theory"
topic_label: "概率论"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "probability-theory"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第3章习题3.35，印刷页109–110／PDF物理页140,141"
source_id: "DS011"
source_chapter: 3
source_exercise: "3.35"
source_stars: 0
source_refs: ["DS011 Exercise 3.35，印刷109–110／PDF物理140,141", "DS011 Gamma尺度密度，印刷81／PDF物理112", "DS011 例3.4.9，印刷95／PDF物理126"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 P184：重参数化与共同均值Gamma参数空间

## 题目

### 英文原题

> [!question] 英文原题
> **3.35** (a) The normal family that approximates a Poisson can also be parameterized as $\mathrm n(e^\theta,e^\theta)$, where $-\infty<\theta<\infty$. Sketch a graph of the parameter space, and compare with the approximation in Exercise 3.34(a).
>
> (b) Suppose that $X\sim\operatorname{gamma}(\alpha,\beta)$ and we assume that $EX=\mu$. Sketch a graph of the parameter space.
>
> (c) Suppose $X_i\sim\operatorname{gamma}(\alpha_i,\beta_i)$, $i=1,2,\ldots,n$, and we assume that $EX_i=\mu$. Describe the parameter space $(\alpha_1,\ldots,\alpha_n,\beta_1,\ldots,\beta_n)$.

### 中文转述

> [!question] 中文转述
> **原题3.35。** (a)  近似Poisson的正态族也可参数化为$\operatorname n(e^\theta,e^\theta)$，其中$-\infty<\theta<\infty$. 画出参数空间的图形，并与习题3.34(a)中的近似比较.
>
> (b)  假设$X\sim\operatorname{gamma}(\alpha,\beta)$，并假定$EX=\mu$. 画出参数空间的示意图.
>
> (c)  假设$X_i\sim\operatorname{gamma}(\alpha_i,\beta_i)$，$i=1,2,\ldots,n$，并假定$EX_i=\mu$. 描述参数空间$(\alpha_1,\ldots,\alpha_n,\beta_1,\ldots,\beta_n)$.

## 提示

> [!hint]- 提示
> 先检查正态式是否少了样本量n，再用Gamma均值alpha beta写约束。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** **(a)** 在$(\mu,v)$平面，$(\mu,v)=(e^\theta,e^\theta)$遍历全部$\mu>0,v=\mu$。重参数化只改变运行该射线的速度，不改变几何集合。习题3.34(a)却是$v=\mu/n$；只有$n=1$两者相同。若要表示同一个固定样本量$n$的样本均值近似，应写$\mathrm n(e^\theta,e^\theta/n)$；原式也可解释为单个泊松变量的正态近似，不能默默删去这个差别。
>
> **(b)** Gamma尺度参数化给$EX=\alpha\beta$。给定$\mu>0$时参数空间为$\{(\alpha,\mu/\alpha):\alpha>0\}$，是正象限双曲线；若$\mu\le0$无合法参数。若$\mu$也可任意未知，则这些曲线的并是整个正象限，应区分“给定均值约束”与“均值重新命名”。
>
> **(c)** 当$\mu>0$固定，空间为
> $$
> \{(\alpha_1,\ldots,\alpha_n,\mu/\alpha_1,\ldots,\mu/\alpha_n):\alpha_i>0\},
> $$
> 由$n$个自由正参数确定。若只是共同但未知均值，空间为所有$\alpha_i,\beta_i>0$且$\alpha_1\beta_1=\cdots=\alpha_n\beta_n$的点，可用$n$个$\alpha_i$及一个共同$\mu>0$参数化，维数为$n+1$。只给各自边缘分布未指定$X_i$之间独立，本参数约束不需要独立性。
>
> ![[附件/习题图/DS011/习题3.35-重参数化与均值约束.png]]
>
> 图的Gamma部分明示$\mu=1$，正态部分以$n=5$对照原式与3.34(a)；一般方程已完整列出。

## 相关概念

- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/期望|期望]]
- [[01 - 概率论/概念/概率模型|概率模型]]

## 备注

- 图为本库按已推导公式独立构造，已检查参数约束、开放端点及实际渲染；可编辑源见[[工具/StatisticalInference/ch03-figures/exercise-3-35.tex|TeX源]]，[[附件/习题图/DS011/习题3.35-重参数化与均值约束.pdf|矢量PDF]]与嵌入PNG对应，未声称复刻教材原图。
- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=140|印刷第109页／PDF物理第140页]]及[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=141|续页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 原题(a)与所引3.34(a)的方差缩放差别可见保留；(b)(c)固定与未知共同均值分别处理。
- 英文原文、中文转述与本库独立解答分别保留；所用正文实际核对位置列于`source_refs`。题内文献只保留原题引用，不表示已查阅原文献。`source_status: verified`只指本题及所列位置核对，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
