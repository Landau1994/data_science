---
title: "习题 ST420：三点LAD非唯一性与心率耗氧量回归"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第12章习题12.25，印刷页492／PDF物理页523"
source_id: "DS011"
source_chapter: 12
source_exercise: "12.25"
source_stars: 0
source_refs: ["DS011 Exercise 12.25，印刷页492／PDF物理页523", "DS011 所引正文，印刷483／PDF物理514"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST420：三点LAD非唯一性与心率耗氧量回归

## 题目

### 英文原题

> [!question] 英文原题
> **12.25** A problem with the LAD regression line is that it is not always uniquely defined.
> (a) Show that, for a data set with three observations, $(x_1,y_1),(x_1,y_2),$ and $(x_3,y_3)$ (note the first two $x$s are the same), any line that goes through $(x_3,y_3)$ and lies between $(x_1,y_1)$ and $(x_1,y_2)$ is a least absolute deviation line.
> (b) For three individuals, measurements are taken on heart rate ($x$, in beats per minute) and oxygen consumption ($y$, in ml/kg). The $(x,y)$ pairs are $(127,14.4),(127,11.9),$ and $(136,17.9)$. Calculate the slope and intercept of the least squares line and the range of the least absolute deviation lines.
> There seems to be some disagreement over the value of the least absolute deviation line. It is certainly more robust than least squares, but can be very difficult to compute (but see Portnoy and Koenker 1997 for an efficient computing algorithm). It also seems that Ellis (1998) questions its robustness, and in a discussion Portnoy and Miseria (1998) question Ellis.

### 中文转述

> [!question] 中文转述
> **原题12.25。**
> LAD回归直线的一个问题是，它不总有唯一定义.
>
> (a)  对含三个观测$(x_1,y_1)$、$(x_1,y_2)$、$(x_3,y_3)$的数据集，注意前两个$x$相同，证明任何通过$(x_3,y_3)$并位于$(x_1,y_1)$与$(x_1,y_2)$之间的直线，都是最小绝对偏差直线.
>
> (b)  对三名个体测量心率$x$，单位为每分钟心跳次数，以及耗氧量$y$，单位为ml/kg. $(x,y)$数据为$(127,14.4)$、$(127,11.9)$、$(136,17.9)$. 计算最小二乘直线的斜率、截距及最小绝对偏差直线的范围.
>
> 对于最小绝对偏差直线的价值，似乎存在一些分歧. 它肯定比最小二乘稳健，但可能很难计算，不过Portnoy和Koenker（1997）给出了高效算法. Ellis（1998）似乎质疑其稳健性，而Portnoy和Misera（1998）在一篇讨论中又质疑Ellis.

## 提示

> [!hint]- 提示
> 同一横坐标的两个残差绝对值之和下界是两纵坐标之差。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** (a) 设$x_3\ne x_1$，不妨$y_1\le y_2$。任何拟合线在$x_1$的预测值为$u$，前两项损失$|y_1-u|+|y_2-u|\ge y_2-y_1$，等号恰当$u\in[y_1,y_2]$。总损失还加上非负第三项。因此所有通过$(x_3,y_3)$且在$x_1$处预测值落此区间的线达到全局下界，均为LAD。原题没明说$x_3\ne x_1$；若三个横坐标全相同，就只有常量预测问题，须取三个纵坐标中位数，指定通过第三点不一定最优（如$0,1,10$），不能无条件推广。
> (b) OLS在$x=127$处拟合两点平均$13.15$，在$x=136$处拟合$17.9$，故$b=(17.9-13.15)/9=19/36\approx.527777778$，$a=17.9-136b\approx-53.87777778$。直接矩阵最小二乘亦得到同值。
> LAD全部线可写$y=17.9+b(x-136)$，其在127处为$u=17.9-9b\in[11.9,14.4]$，所以$b\in[7/18,2/3]$，$a=17.9-136b$。截距范围为$[-72.76666667,-34.98888889]$，但斜率与截距须按上述联动取值，不能任意在两个区间内独立组合。最小绝对残差和均为$2.5$。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计（parameter estimation）]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]
- [[01 - 概率论/概念/随机变量|随机变量]]

## 备注

- 完整原题已逐页对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=523|印刷492／PDF物理523]]；原题无星号。教材信息与归档进度见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 实际引用输入核对页：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=514|印刷483／PDF物理514]]；所需模型、公式、数据在解答重述。
- 实际计算可复核：[[工具/StatisticalInference/ch12-computations/calc_ch12.py|完整实现与输入数据]]、[[工具/StatisticalInference/ch12-computations/ch12-computations.json|版本与完整结果]]、[[工具/StatisticalInference/ch12-computations/run-manifest.json|运行与文件校验记录]]。
- 来源已核对与解答写成不表示个人学习已完成；学习状态保留`not-started`。未实测Obsidian界面渲染。
