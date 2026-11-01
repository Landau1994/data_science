---
title: "习题 P002：Efron骰子的非传递胜率"
topic: "probability-theory"
topic_label: "概率论"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "probability-theory"]
source: "[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Bishop《深度学习：基础与概念》（DS003）]]"
source_id: "DS003"
source_chapter: 2
source_exercise: "2.2"
source_stars: 2
source_refs: ["DS003 Exercise 2.2，印刷58/PDF78", "DS003 Figure 2.16，印刷58/PDF78"]
source_status: "verified"
solution_status: "independently-derived"
created: 2026-11-01
---

# 习题 P002：Efron骰子的非传递胜率

## 题目

### 英文原题

> [!question] 英文原题
> **2.2 (★★)** Deterministic numbers satisfy the property of transitivity, so that if $x>y$ and $y>z$ then it follows that $x>z$. When we go to random numbers, however, this property need no longer apply. Figure 2.16 shows a set of four cubical dice that have been arranged in a cyclic order. Show that each of the four dice has a $2/3$ probability of rolling a higher number than the previous die in the cycle. Such dice are known as non-transitive dice, and the specific examples shown here are called Efron dice.
>
> ![[附件/习题图/DS003/原图-2.16.png]]
>
> **Figure 2.16** An example of non-transitive cubical dice, in which each die has been ‘flattened’ to reveal the numbers on each of the faces. The dice have been arranged in a cycle, such that each die has a $2/3$ probability of rolling a higher number than the previous die in the cycle.

### 中文转述

> [!question] 中文转述
> **Bishop 原题 2.2。** 确定的数具有传递性（transitivity）：由 $x>y$、$y>z$ 可知 $x>z$。随机数的优势关系却可能不满足传递性。原书图2.16给出按循环排列的四枚立方体骰子，证明循环中每枚骰子都以 $2/3$ 的概率掷出比前一枚更大的点数。这称为非传递骰子（non-transitive dice），图中这组称为 Efron 骰子（Efron dice）。图2.16将骰子展开，展示了每个面的点数及循环箭头。

## 提示

> [!hint]- 提示 1
> 把图中每枚骰子的六个面完整列出。每次比较有 $6\times6=36$ 个等可能的有序面组合。

> [!hint]- 提示 2
> 沿图中箭头依次比较全为3的骰子、0/4骰子、1/5骰子、2/6骰子，再回到全为3的骰子。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 按通常的掷骰模型，四枚骰子的每个面等可能，不同骰子的掷出结果相互独立。依图中顺时针顺序记
> $$
> A=(3,3,3,3,3,3),\quad B=(0,0,4,4,4,4),
> $$
> $$
> C=(1,1,1,5,5,5),\quad D=(2,2,2,2,6,6).
> $$
> 逐一计算箭头后方骰子胜过前方骰子的概率：
> $$
> P(B>A)=P(B=4)=\frac46=\frac23.
> $$
> 对 $C$ 与 $B$，$C=5$ 时必胜；$C=1$ 时只在 $B=0$ 时胜，因此
> $$
> P(C>B)=\frac36\cdot1+\frac36\cdot\frac26=\frac23.
> $$
> 对 $D$ 与 $C$，$D=6$ 时必胜；$D=2$ 时只在 $C=1$ 时胜，故
> $$
> P(D>C)=\frac26\cdot1+\frac46\cdot\frac36=\frac23.
> $$
> 最后，$A$ 总是3，恰在 $D=2$ 时胜，所以
> $$
> P(A>D)=\frac46=\frac23.
> $$
> 四次比较均没有平局，却形成 $B$ 胜 $A$、$C$ 胜 $B$、$D$ 胜 $C$、$A$ 胜 $D$ 的循环。这里不满足传递性的是“胜率超过一半”的分布间关系；每次实际实现的数值大小仍满足通常的传递性。

## 相关概念

- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/概率模型|概率模型]]

## 备注

- 原题定位：[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=78|印刷第58页／PDF物理第78页]]；题干引用正文的位置见 `source_refs`。
- 原书星号表示习题难度，本笔记保留其星数；解答为本库独立推导，未使用配套答案册作核验。
- `source_status: verified` 只指本题题干、所用公式和定位已对照原始页面；不表示整章或整书理论全部核验。学习状态保留 `not-started`。
