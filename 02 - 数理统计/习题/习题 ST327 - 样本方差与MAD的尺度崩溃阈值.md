---
title: 习题 ST327：样本方差与MAD的尺度崩溃阈值
topic: mathematical-statistics
topic_label: 数理统计
difficulty: intermediate
status: not-started
tags:
- exercise
- mathematical-statistics
source: George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第10章习题10.21，印刷页411／PDF物理页442
source_id: DS011
source_chapter: 10
source_exercise: '10.21'
source_stars: 0
source_refs:
- DS011 Exercise 10.21，印刷411／PDF物理442
- DS011题内依赖核对：印刷389／PDF物理420
source_status: verified
solution_status: independently-derived
created: '2026-11-13'
---

# 习题 ST327：样本方差与MAD的尺度崩溃阈值

## 题目

### 英文原题

> [!question] 英文原题
> **10.21** The breakdown performance of the mean and the median continues in their scale estimate counterparts. For a sample $X_1,X_2,\ldots,X_n$:
>
> (a) Show that the breakdown value of the sample variance $S^2=\sum(X_i-\bar X)^2/(n-1)$ is 0.
>
> (b) A robust alternative is the median absolute deviation, or MAD, the median of $|X_1-m|,|X_2-m|,\ldots,|X_n-m|$, where $m$ is the sample median. Show that this estimator has a breakdown value of 50%.

### 中文转述

> [!question] 中文转述
> **原题10.21。** 均值与中位数的崩溃表现也延续到对应的尺度估计量. 对样本$X_1, X_2,\ldots, X_n$：
>
> (a)  证明样本方差$S^2=\sum(X_i-\bar X)^2/(n-1)$的崩溃值为0.
>
> (b)  一种稳健替代量是中位数绝对偏差（median absolute deviation，MAD），即$|X_1-m|,|X_2-m|,\ldots,|X_n-m|$的中位数，其中$m$为样本中位数. 证明该估计量的崩溃值为50\%.

## 提示

> [!hint]- 提示
> 尺度崩溃既包括推向无穷，也包括坍缩为0；应排除原样本已全相同等退化情况。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 把0与50%解释为随$n$增长的替换崩溃比例；有限样本整数和中位数约定会产生$O(1/n)$差异。
>
> **(a)** 固定其余$n-1$个值，仅令一个观测为$R\to\infty$。平方离差和$\sum X_i^2-(\sum X_i)^2/n=(1-1/n)R^2+O(R)$，因此$S^2=R^2/n+O(R)\to\infty$。一个污染值即足够，比例$1/n\to0$。
>
> **(b) 爆炸的下界。** 若严格少于一半污染，则中位数$m$被未污染观测的有限范围夹住；至少一半以上未污染点的$|X_i-m|$有统一有限上界，所以这些偏差的中位数MAD也有限。故不足一半不能使MAD爆炸。
>
> **达到上界。** 对$n=2r+1$，替换$r+1$个值为$R,2R,\ldots,(r+1)R$，留下$r$个有界原值。样本中位数为$R$（充分大$R$），除中位点的0偏差外，$r$个原点与其余$r$个污染点的偏差都趋于无穷，所以MAD趋于无穷，爆炸比例$(r+1)/(2r+1)\to1/2$。
>
> 若也把尺度坍缩至0算作崩溃，假定原样本互异、MAD正。替换$r$个观测为某个保留值，可产生$r+1$个完全相同值，使中位数等于该值且MAD为0，比例$r/(2r+1)\to1/2$。反向地少于$r$个替换不能让超过半数数据落在任意短区间：保留互异值有正最小间距，任意足够短区间至多含一个保留值，因此不能使超过半数绝对偏差同时趋零。故无论爆炸或坍缩，极限阈值为50%。若原数据已有大量重合或MAD本已0，有限样本崩溃须另作定义，不能直接套用一般位置结论。

## 相关概念

- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/期望|期望]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[02 - 数理统计/概念/参数估计|参数估计]]

## 备注

- 来源：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=442|印刷第411页／PDF物理第442页]]；版本与归档见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 已实读本题所用正文：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=420|印刷389／PDF物理420]]；其余题内外部文献仅保留原引用，未声称查阅。
- 英文原题逐题对照PDF原始页面，保留原分题、提示、引用及可见疑误；原题无星号。题内引用补充与独立解答不混入原文；未查阅答案册或题内外部文献。
- 来源核对不表示个人学习完成，学习状态保持not-started。公式、链接与元数据检查不等于Obsidian实际渲染检查。
