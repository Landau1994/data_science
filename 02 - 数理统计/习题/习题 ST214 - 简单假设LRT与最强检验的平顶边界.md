---
title: "习题 ST214：简单假设LRT与最强检验的平顶边界"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "advanced"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第8章习题8.24，印刷页329／PDF物理页360"
source_id: "DS011"
source_chapter: 8
source_exercise: "8.24"
source_stars: 0
source_refs: ["DS011 Exercise 8.24，印刷页329／PDF物理页360", "DS011 所引正文，印刷303／PDF物理334", "DS011 所引正文，印刷315／PDF物理346"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST214：简单假设LRT与最强检验的平顶边界

## 题目

### 英文原题

> [!question] 英文原题
> **8.24** Find the LRT of a simple $H_0$ versus a simple $H_1$. Is this test equivalent to the one obtained from the Neyman–Pearson Lemma? (This relationship is treated in some detail by Solomon (1975).)

### 中文转述

> [!question] 中文转述
> **原题8.24。**
> 求简单 $H_0$ 对简单 $H_1$ 的似然比检验. 它是否等价于由 Neyman–Pearson 引理得到的检验？（Solomon (1975) 对这一关系有较详细讨论.）

## 提示

> [!hint]- 提示
> 注意本书LRT分母是两个似然的最大值，产生比值为1的平顶。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 写两简单模型密度或pmf为$f_0,f_1$，全参数空间仅含这两个模型。按定义8.2.1，$\lambda(x)=f_0(x)/\max(f_0(x),f_1(x))$，即在$r=f_1/f_0>1$时为$1/r$，在$r\le1$时为1。$f_0=0<f_1$处令$r=\infty,\lambda=0$，两者均0处任意定义。
> 对$0<c<1$，拒绝$\lambda\le c$与$r\ge1/c$等价，正是Neyman–Pearson似然比规则；当该阈值能给所需大小（或仅在同一个比值边界随机化）时二者完全一致并最强。
> 但若逐字限定为一个常数的非随机化$\{\lambda\le c\}$，不能对所有大小无条件声称等价：$r\le1$全部折叠在平顶$\lambda=1$，$c=1$会全拒绝，而某些最强检验需只纳入其中较大的$r$。例如$N(0,1)$对$N(1,1)$有$r=e^{x-1/2}$；当目标$\alpha>1-\Phi(1/2)$时，最强检验拒绝$x>z_\alpha<1/2$，字面LRT在$c<1$下不能取得这么大大小，在$c=1$又大小1。
> 若“等价”允许在$\lambda=1$平顶中继续按原始$r$排序选择，则所有Neyman–Pearson检验均可视为这一广义似然比规则。精确陈述须保留平顶/随机化约定，不能把它略去。

## 相关概念

- [[02 - 数理统计/概念/假设检验|假设检验（hypothesis testing）]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[01 - 概率论/概念/条件概率|条件概率]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 完整原题已逐页对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=360|印刷329／PDF物理360]]；原题无星号。教材信息及归档进度见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 引用输入实际核对页：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=334|印刷303／PDF物理334]]、[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=346|印刷315／PDF物理346]]；解答已重述所需假设及结果。
- 来源已核对与独立解答写成不等于个人已完成练习；学习状态保留`not-started`。未实测Obsidian界面渲染。
