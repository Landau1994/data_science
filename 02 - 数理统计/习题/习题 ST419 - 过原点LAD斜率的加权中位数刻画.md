---
title: "习题 ST419：过原点LAD斜率的加权中位数刻画"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "advanced"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第12章习题12.24，印刷页491／PDF物理页522"
source_id: "DS011"
source_chapter: 12
source_exercise: "12.24"
source_stars: 0
source_refs: ["DS011 Exercise 12.24，印刷页491／PDF物理页522", "DS011 所引正文，印刷485／PDF物理516"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST419：过原点LAD斜率的加权中位数刻画

## 题目

### 英文原题

> [!question] 英文原题
> **12.24** For the model $Y_i=\beta x_i+\varepsilon_i$, show that the LAD estimator is given by $t_{(k^*+1)}$, where $t_i=y_i/x_i$, $t_{(1)}\le t_{(2)}\le\cdots\le t_{(n)}$ and, if $x_{(i)}$ is the $x$ value paired with $t_{(i)}$, $k^*$ satisfies $\sum_{i=1}^{k^*}|x_{(i)}|\le\sum_{i=k^*+1}^n|x_{(i)}|$ and $\sum_{i=1}^{k^*+1}|x_{(i)}|>\sum_{i=k^*+2}^n|x_{(i)}|$.

### 中文转述

> [!question] 中文转述
> **原题12.24。**
> 对模型$Y_i=\beta x_i+\varepsilon_i$，证明LAD估计量为$t_{(k^*+1)}$，其中$t_i=y_i/x_i$，$t_{(1)}\le t_{(2)}\le\cdots\le t_{(n)}$，若$x_{(i)}$为与$t_{(i)}$配对的$x$值，则$k^*$满足
>
> $$
> \sum_{i=1}^{k^*}|x_{(i)}|\le\sum_{i=k^*+1}^n|x_{(i)}|\quad\text{和}\quad
> \sum_{i=1}^{k^*+1}|x_{(i)}|>\sum_{i=k^*+2}^n|x_{(i)}|.
> $$

## 提示

> [!hint]- 提示
> 每项绝对残差可写成$|x_i||t_i-\beta|$，求凸分段线性函数的次梯度。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 先去掉$x_i=0$的项：它们的损失恒为$|y_i|$，不影响斜率；剩余总权重$W=\sum|x_i|>0$。若所有$x_i=0$，任意斜率均最优且题内比值不定义。对非零设计，$\sum|y_i-bx_i|=\sum w_i|t_i-b|$，$w_i=|x_i|$。
> 对给定$b$，凸函数的次梯度区间为$[W_{<b}-W_{>b}-W_{=b},W_{<b}-W_{>b}+W_{=b}]$。0在此区间内当且仅当$W_{<b}\le W/2$且$W_{>b}\le W/2$，即加权中位数条件。原题两不等式等价前$k^*$个权重和不超过$W/2$、前$k^*+1$个权重和严格超过$W/2$，所以$t_{(k^*+1)}$满足两侧权重条件，为全局LAD极小点。若有重复$t$可把相同位置的权重合并，结论仍成立。恰好半权重落在相邻两位置之间时整段都可能最优；题式选择该段的一个端点，不证明唯一性。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计（parameter estimation）]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]
- [[01 - 概率论/概念/随机变量|随机变量]]

## 备注

- 完整原题已逐页对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=522|印刷491／PDF物理522]]；原题无星号。教材信息与归档进度见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 实际引用输入核对页：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=516|印刷485／PDF物理516]]；所需模型、公式、数据在解答重述。
- 来源已核对与解答写成不表示个人学习已完成；学习状态保留`not-started`。未实测Obsidian界面渲染。
