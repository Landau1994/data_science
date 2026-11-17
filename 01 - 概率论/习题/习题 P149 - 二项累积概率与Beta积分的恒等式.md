---
title: 习题 P149：二项累积概率与Beta积分的恒等式
topic: probability-theory
topic_label: 概率论
difficulty: intermediate
status: not-started
tags:
- exercise
- probability-theory
source: George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第2章习题2.40，印刷页67／PDF物理页98
source_id: DS011
source_chapter: 2
source_exercise: '2.40'
source_stars: 0
source_refs:
- DS011 Exercise 2.40，印刷67／PDF物理98
source_status: verified
solution_status: independently-derived
created: '2026-11-13'
---

# 习题 P149：二项累积概率与Beta积分的恒等式

## 题目

### 英文原题

> [!question] 英文原题
> **2.40** Prove
> $$
> \sum_{k=0}^x\binom nk p^k(1-p)^{n-k}
> =(n-x)\binom nx\int_0^{1-p}t^{n-x-1}(1-t)^x\,dt.
> $$
> (Hint: Integrate by parts or differentiate both sides with respect to $p$.)

### 中文转述

> [!question] 中文转述
> **原题2.40。** 证明
>
> $$
> \sum_{k=0}^x\binom nk p^k(1-p)^{n-k}
> =(n-x)\binom nx\int_0^{1-p}t^{n-x-1}(1-t)^x\,dt.
> $$
>
> （提示：分部积分，或两边对 $p$ 求导.）

## 提示

> [!hint]- 提示
> 在$0\le x<n$的整数范围内，两边求导并用相邻组合数关系相消，再比较一个端点。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 明确通常所需条件：$n\ge1$为整数，$x\in\{0,\ldots,n-1\}$，$0\le p\le1$。先取$0<p<1$。令左边为$L(p)$；有限和可以逐项求导，利用$k\binom nk=n\binom{n-1}{k-1}$与$(n-k)\binom nk=n\binom{n-1}k$，相邻项相消后只余
> $$
> L'(p)=-n\binom{n-1}x p^x(1-p)^{n-x-1}
> =-(n-x)\binom nx p^x(1-p)^{n-x-1}.
> $$
> 右边为$R(p)$。其被积函数在$(0,1)$连续且端点可积，微积分基本定理及链式法则给出同一个导数
> $$
> R'(p)=-(n-x)\binom nx(1-p)^{n-x-1}p^x=L'(p).
> $$
> 故两边之差为常数。在$p=1$，由于$x<n$，$L(1)=0$，而积分上限为0使$R(1)=0$。因此常数0，恒等式成立；端点$p=0,1$由连续性延拓。
>
> 原题没有列参数范围。若直接取$x=n$，左边为1，右边却成为零前因子乘含$t^{-1}$的发散积分，不是合法的字面表达式；不能把这点算作同一公式的普通取值。$x<n$的限制是该Beta积分表达式所必需。

## 相关概念

- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/概率模型|概率模型]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 来源：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=98|印刷第67页／PDF物理第98页]]；版本与归档见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 原公式与Hint完整保留；整数参数、概率参数及x<n的限制写在解答中，不回填英文原题。
- 已逐题查看原始页面，英文原题、全部分题与原附提示／引用照录；原题无星号。所列正文定位已经实读，题内补充、原文及独立推导分开。未查阅题内外部文献或答案册。
- 来源核对状态不表示个人学习完成；学习状态保持not-started。公式与链接检查不等于Obsidian实际渲染检查。
