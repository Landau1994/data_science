---
title: "习题 P176：均匀Gamma正态与Beta族的单峰性及边界众数"
topic: "probability-theory"
topic_label: "概率论"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "probability-theory"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第3章习题3.27，印刷页108／PDF物理页139"
source_id: "DS011"
source_chapter: 3
source_exercise: "3.27"
source_stars: 0
source_refs: ["DS011 Exercise 3.27，印刷108／PDF物理139", "DS011 Gamma密度，印刷81／PDF物理112", "DS011 习题2.27单峰定义，印刷65／PDF物理96"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 P176：均匀Gamma正态与Beta族的单峰性及边界众数

## 题目

### 英文原题

> [!question] 英文原题
> **3.27** For each of the following families, show whether all the pdfs in the family are unimodal (see Exercise 2.27).
>
> (a) uniform$(a,b)$
>
> (b) gamma$(\alpha,\beta)$
>
> (c) $\mathrm n(\mu,\sigma^2)$
>
> (d) beta$(\alpha,\beta)$

### 中文转述

> [!question] 中文转述
> **原题3.27。** 对下列每个族，说明族中是否所有pdf都是单峰的（见习题2.27）.
>
> (a)  均匀$(a,b)$.
>
> (b)  Gamma$(\alpha,\beta)$.
>
> (c)  $\operatorname n(\mu,\sigma^2)$.
>
> (d)  Beta$(\alpha,\beta)$.

## 提示

> [!hint]- 提示
> 看对数密度导数的符号；平台与边界峰要声明约定。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 这里单峰指在某峰点左侧非递减、右侧非递增，允许平台；边界峰按密度在支持边界的极限版本解释。
>
> **(a)** 均匀密度在$[a,b]$为常数，外部为0，区间内每个点都是峰点，因此全族单峰但众数不唯一。
>
> **(b)** Gamma对数导数为$(\alpha-1)/x-1/\beta$。$\alpha>1$时先正后负，唯一内峰为$(\alpha-1)\beta$；$0<\alpha\le1$时在正半轴递减，边界0为众数。因此按通常包含边界极限众数的约定，全部单峰。若坚持原题2.27的逐点最大值定义并把支持外密度在0定义为0，则$\alpha<1$时最大值不被取到；须说明密度在零测单点的版本或用边界峰约定，不能忽略该定义细节。
>
> **(c)** 正态对数导数为$-(x-\mu)/\sigma^2$，在$\mu$前正后负，所以全族唯一内峰$\mu$。
>
> **(d)** 并非全部。对数导数为$(\alpha-1)/x-(\beta-1)/(1-x)$。两形状都大于1时峰为$(\alpha-1)/(\alpha+\beta-2)$；$\alpha\le1\le\beta$为递减边界峰，$\beta\le1\le\alpha$为递增边界峰，$\alpha=\beta=1$为平台。但$\alpha,\beta<1$时两端高、中间低（如$\alpha=\beta=1/2$），不存在单个先增后减的峰点，故Beta族不是全族单峰。

## 相关概念

- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/期望|期望]]
- [[01 - 概率论/概念/概率模型|概率模型]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=139|印刷第108页／PDF物理第139页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 习题2.27给出的逐点单峰定义位于印刷65／PDF96；该定义的边界版本问题在解答明示。
- 英文原文、中文转述与本库独立解答分别保留；所用正文实际核对位置列于`source_refs`。题内文献只保留原题引用，不表示已查阅原文献。`source_status: verified`只指本题及所列位置核对，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
