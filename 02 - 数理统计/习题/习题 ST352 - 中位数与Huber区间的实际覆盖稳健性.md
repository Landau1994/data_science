---
title: 习题 ST352：中位数与Huber区间的实际覆盖稳健性
topic: mathematical-statistics
topic_label: 数理统计
difficulty: advanced
status: not-started
tags:
- exercise
- mathematical-statistics
source: George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第10章习题10.46，印刷页416／PDF物理页447
source_id: DS011
source_chapter: 10
source_exercise: '10.46'
source_stars: 0
source_refs:
- DS011 Exercise 10.46，印刷416／PDF物理447
- DS011题内依赖核对：印刷404／PDF物理435；印刷406／PDF物理437；印刷407／PDF物理438
source_status: verified
solution_status: independently-derived
created: '2026-11-13'
---

# 习题 ST352：中位数与Huber区间的实际覆盖稳健性

## 题目

### 英文原题

> [!question] 英文原题
> **10.46** Expand the comparisons made in Example 10.4.8.
>
> (a) Produce a table similar to Table 10.4.8 that examines the robustness of intervals of a location parameter based on the median. (Intervals based on the mean are done in Table 10.4.7.)
>
> (b) Another interval based on Huber's M-estimator would be one that used a variance from a bootstrap calculation. Examine the robustness of such an interval.

### 中文转述

> [!question] 中文转述
> **原题10.46。** 扩展例10.4.8中的比较.
>
> (a)  制作类似10.4.8的表，考察基于中位数的位置参数区间的稳健性. （基于均值的区间已在10.4.7中完成.）
>
> (b)  另一种基于Huber $M$估计量的区间，可以使用自助法计算的方差. 考察这种区间的稳健性.

## 提示

> [!hint]- 提示
> 用声明好的区间规则、四个模型和重复数比较实际覆盖；bootstrap不是自动精确覆盖保证。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 与10.39共用已经实际生成的四模型数据：标准正态、标准$t_5$、标准Logistic、尺度1双指数，各3000个$n=15$样本；所有真位置0，每个原样本199次经验分布重抽样，独立种子及全部样本记录。标准误和区间均预先指定，没有按结果调整临界值。
>
> **(a)** 主比较用中位数bootstrap标准误$s_M^*$，区间$M_n\pm z_{\alpha/2}s_M^*$。另给两种边界对照：已知真实中心密度时的渐近区间$M_n\pm z/[2f(0)\sqrt n]$（仅作为oracle基准），以及分布无关次序区间$[X_{(4)},X_{(12)}]$。后者在$n=15$任意连续、唯一中位数总体下精确覆盖$1-2P(\operatorname{Bin}(15,1/2)\le3)=.96484375$，因离散秩无法同时精确达到.90和.95，作为两名义水平的保守选择。
>
> **(b)** Huber取$k=1.5$，每个重抽样重新求根，用根的样本标准差$s_H^*$，区间$\hat\theta_H\pm z s_H^*$。本次完整实际覆盖表如下：
>
> |总体|名义覆盖|中位数bootstrap|中位数oracle渐近|中位数秩区间|Huber bootstrap|
> |---|---:|---:|---:|---:|---:|
> |正态|0.90|0.8807|0.9027|0.9613|0.8687|
> |正态|0.95|0.9307|0.9503|0.9613|0.9223|
> |t5|0.90|0.8907|0.8953|0.9640|0.8717|
> |t5|0.95|0.9370|0.9487|0.9640|0.9257|
> |Logistic|0.90|0.9033|0.8990|0.9637|0.8837|
> |Logistic|0.95|0.9373|0.9507|0.9637|0.9303|
> |双指数|0.90|0.9177|0.8433|0.9670|0.8847|
> |双指数|0.95|0.9533|0.8990|0.9670|0.9380|
>
> 中位数bootstrap在本例四模型的90%覆盖约.881–.918、95%覆盖约.931–.953，较稳定但不是保证；Huber bootstrap约.869–.885和.922–.938，仍有小样本欠覆盖。oracle中位数渐近区间在双指数$n=15$下也明显不足，说明即使知道中心密度，有限样本中位数还可能偏离渐近正态。分布无关秩区间实际频率接近精确.964844，但更保守，不能把高覆盖本身当作所有长度条件下更优。
>
> 原(10.3.8)打印分母错误的影响已经在10.39分别计算，它不能直接作为一致标准误基准。本次概率在.9附近的Monte Carlo标准误约.00548、最坏.00913；表中小于这些量级的差别不作确定排序。对位置平移，三类区间等变，覆盖不依赖位置；这只是四个已声明分布的有限实验，不覆盖任意不对称污染或依赖数据。

## 相关概念

- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/期望|期望]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/重采样|重采样]]

## 备注

- 来源：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=447|印刷第416页／PDF物理第447页]]；版本与归档见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 实读表10.4.7、例10.4.8及表10.4.8：印刷404、406–407／PDF435、437–438。实际实现[[work/DS011/ch10/robust_simulation.py|稳健模拟]]、[[work/DS011/ch10/robust-results.json|逐模型结果]]；与10.39共享同批数据，未冒称独立第二次实验。
- 已实读本题所用正文：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=435|印刷404／PDF物理435]]；[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=437|印刷406／PDF物理437]]；[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=438|印刷407／PDF物理438]]；其余题内外部文献仅保留原引用，未声称查阅。
- 英文原题逐题对照PDF原始页面，保留原分题、提示、引用及可见疑误；原题无星号。题内引用补充与独立解答不混入原文；未查阅答案册或题内外部文献。
- 来源核对不表示个人学习完成，学习状态保持not-started。公式、链接与元数据检查不等于Obsidian实际渲染检查。
