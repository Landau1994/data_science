---
title: "习题 P097：Bonferroni截断界与原题单调性反例"
topic: probability-theory
topic_label: 概率论
difficulty: advanced
status: not-started
tags: [exercise, probability-theory]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第1章习题1.43，印刷页36／PDF物理页67"
source_id: DS011
source_chapter: 1
source_exercise: "1.43"
source_stars: 0
source_refs: ["DS011 Exercise 1.43，印刷页36／PDF物理页67", "DS011 Miscellanea 1.8.1，印刷37／PDF物理68", "DS011 Theorem 1.2.11，印刷9／PDF物理40；式(1.2.10)，印刷11／PDF物理42"]
source_status: verified
solution_status: independently-derived
created: 2026-11-12
---

# 习题 P097：Bonferroni截断界与原题单调性反例

## 题目

### 英文原题

> [!question] 英文原题
> **1.43** For the inclusion-exclusion identity of Miscellanea 1.8.1:
>
> (a) Derive both Boole’s and Bonferroni’s inequality from the inclusion-exclusion identity.
>
> (b) Show that the $P_i$ satisfy $P_i\ge P_j$ if $i\ge j$, and that the sequence of bounds in Miscellanea 1.8.1 improves as the number of terms increases.
>
> (c) Typically as the number of terms in the bound increases, the bound becomes more useful. However, Schwager (1984) cautions that there are some cases where there is not much improvement, in particular if the $A_i$s are highly correlated. Examine what happens to the sequence of bounds in the extreme case when $A_i=A$ for every $i$. (See Worsley (1982) and the correspondence between Worsley (1985) and Schwager (1985).)

### 中文转述

> [!question] 中文转述
> **Casella–Berger 原题1.43。** 考虑杂录1.8.1的容斥恒等式。
>
> (a) 从容斥恒等式推导Boole不等式和Bonferroni不等式。
>
> (b) 证明原题所声称的：当$i\ge j$时$P_i\ge P_j$，并且杂录中的界限序列随项数增加而得到改进。
>
> (c) 界限中增加项通常被期待更有用，但Schwager（1984）指出高度相关事件可能改善不大。考察所有$A_i=A$的极端情形。（原题引用Worsley（1982）及Worsley（1985）与Schwager（1985）的往来讨论。）本题部分断言并不普遍成立，原文保留，解答给出反例与正确界限。

## 提示

> [!hint]- 提示
> 令$P_j$为全部$j$重交集概率之和，$S_m=\sum_{j=1}^m(-1)^{j+1}P_j$。对恰落入$k$个事件的点，截断和是$1-(-1)^m\binom{k-1}{m}$。检查这个量的符号，而不要预设$P_j$单调。

## 解答

> [!success]- 解答
> **证明范围：独立推导；原题(b)的两项普遍单调性断言均用反例处理。** 定义
> $$
> P_j=\sum_{i_1<\cdots<i_j}P(A_{i_1}\cap\cdots\cap A_{i_j}),\qquad
> S_m=\sum_{j=1}^m(-1)^{j+1}P_j.
> $$
> 杂录原文和习题(b)写了相反方向的$P_i$排序，但两个方向都不能普遍成立。
>
> **先建立正确的截断界。** 若一点恰属于$k\ge1$个事件，则由Pascal恒等式展开后相邻项抵消，得到
> $$
> \sum_{j=0}^m(-1)^j\binom{k}{j}=(-1)^m\binom{k-1}{m},
> $$
> 约定超过上标的组合数为0。故截断后的指示函数和为$1-(-1)^m\binom{k-1}{m}$；当$k=0$时为0。对奇数$m$它不小于并事件的指示函数，对偶数$m$它不大于该指示函数。取期望即得Bonferroni截断界：
> $$
> S_{2r}\le P\left(\bigcup_i A_i\right)\le S_{2r-1}
> $$
> （仅写仍在$1,\ldots,n$范围内的截断次数）。到$m=n$时恢复精确容斥和。
>
> **(a)** 取$m=1$得到有限Boole不等式$P(\bigcup_iA_i)\le P_1=\sum_iP(A_i)$；取$m=2$得到并事件的二阶Bonferroni界$P(\bigcup_iA_i)\ge P_1-P_2$。原书式(1.2.10)称作Bonferroni不等式的交事件形式，则对补事件应用Boole界并取补，得到
> $$
> P\left(\bigcap_{i=1}^n A_i\right)
> \ge1-\sum_{i=1}^nP(A_i^c)
> =\sum_{i=1}^nP(A_i)-(n-1).
> $$
> 原书定理1.2.11还写可数Boole界；由有限并递增至可数并及概率的下连续性，有限界取极限即得可数形式。
>
> **(b)** 字面要求不能证明。取两个互斥的正概率事件，则$P_2=0<P_1$，反驳原题的$P_2\ge P_1$。反方向也不成立：四个事件均等于同一正概率事件$A$时，$P_1=4p$、$P_2=6p$，其中$p=P(A)>0$。
>
> 界限也不必随着增加同奇偶项而单调改善。例如$n=6$且所有事件均为$A$时，$S_1=6p$而$S_3=11p$，后一个上界反而更大。即便再与普遍上界1取最小值，也不能恢复一般单调改善：取$p=1/20$，两界为$0.3$与$0.55$，而真实概率为$0.05$。正确的普遍结论是前述奇偶截断界与最终精确等式，不是$P_j$或同类截断界的单调性。
>
> **(c)** 当全部$A_i=A$时，各$j$重交集都为$A$，所以
> $$
> P_j=\binom nj p,\qquad
> S_m=p\left[1-(-1)^m\binom{n-1}{m}\right].
> $$
> 奇数$m$的上界为$p[1+\binom{n-1}{m}]$，偶数$m$的下界为$p[1-\binom{n-1}{m}]$。组合数会先增大再减小，中间截断可能很差，下界甚至为负；最终$m=n$时组合数为0，才精确等于$p$。若希望随计算量增加保持已有最佳界，可将所有已算下界取最大、所有已算上界取最小，并与$[0,1]$相交；这是独立补充的界限维护方法，不是原题所写的单个截断和单调性。

## 相关概念

- [[01 - 概率论/概念/事件与集合运算|事件与集合运算]]
- [[01 - 概率论/概念/概率模型|概率模型]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 教材信息见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]；原题定位：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=67|印刷第36页／PDF物理第67页]]。
- 已对照原始页面核对完整英文、全部分题及原书引用；无星号。引用正文与独立补充在题内分开，来源定位另见`source_refs`。解答为本库独立推导，不使用答案册代替证明。
- `source_status: verified`仅指本题及所用来源的实际核对范围；归档和写出解答不代表个人已完成练习，学习状态保持`not-started`。未实测Obsidian界面渲染。
