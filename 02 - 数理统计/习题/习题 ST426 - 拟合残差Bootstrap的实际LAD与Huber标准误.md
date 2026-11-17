---
title: "习题 ST426：拟合残差Bootstrap的实际LAD与Huber标准误"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "advanced"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第12章习题12.31，印刷页492／PDF物理页523"
source_id: "DS011"
source_chapter: 12
source_exercise: "12.31"
source_stars: 0
source_refs: ["DS011 Exercise 12.31，印刷页492／PDF物理页523", "DS011 所引正文，印刷485／PDF物理516", "DS011 所引正文，印刷487／PDF物理518"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST426：拟合残差Bootstrap的实际LAD与Huber标准误

## 题目

### 英文原题

> [!question] 英文原题
> **12.31** For the data of Table 12.4.2, we could also use the nonparametric bootstrap to assess the standard error from the LAD and M-estimator fit. Now you would
> (a) Fit the line $y=\alpha+\beta x$ to get estimates $\tilde\alpha$ and $\tilde\beta$.
> (b) Generate new residuals by resampling from the fitted residuals and re-estimate $\alpha$ and $\beta$.
> (c) Do (c) $B$ times and calculate the standard deviation of $\tilde\alpha$ and $\tilde\beta$.

### 中文转述

> [!question] 中文转述
> **原题12.31。**
> 对12.4.2的数据，也可以用非参数自助法评价LAD和M估计拟合的标准误. 此时：
>
> (a)  拟合直线$y=\alpha+\beta x$，得到估计$\tilde\alpha,\tilde\beta$.
>
> (b)  对拟合残差重抽样生成新残差，并重新估计$\alpha,\beta$.
>
> (c)  将(c)重复$B$次，计算$\tilde\alpha,\tilde\beta$的标准差.

## 提示

> [!hint]- 提示
> 固定预测变量，均匀有放回抽取23个拟合残差，按完整算法重拟合。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 沿用原表23对O₂、CO₂数据及上题明确的LAD、Huber定义，$n=23$。这里的“非参数”指残差经验分布，不是把观测对整体重抽；固定设计与误差iid的工作模型是所用范围。
> (a) 实际拟合得到LAD$(18.58888889,-.8888888889)$，Huber$(18.49684208,-.8850290700)$。每方法计算自己的残差$r_i=y_i-\tilde a-\tilde b x_i$。
> (b) 对每次重复，独立均匀抽$I_1,\ldots,I_{23}\in\{1,\ldots,23\}$，生成$y_i^*=\tilde a+\tilde b x_i+r_{I_i}$，重新求该方法拟合。另实际运行了中心化残差$r_i-\bar r$版本，作为零均值误差模型的补充；两种版本都保留，不静默改写原要求。
> (c) 原文此处自引“Do(c)”应理解为重复(b)，否则没有可执行步骤。每方法实际$B=2000$，用分母$B-1$的样本标准差得到：
>
> | 方法 | 原残差SE(截距) | 原残差SE(斜率) | 中心化残差SE(截距) | 中心化残差SE(斜率) |
> | --- | --- | --- | --- | --- |
> | LAD | .8856272863 | .0483109495 | .8856272863 | .0483109495 |
> | Huber | .8959871780 | .0488954841 | .8959871780 | .0488954841 |
>
> 同一组索引下，中心化只把每个生成响应减相同$\bar r$；两估计对响应平移等变，因此斜率不变、截距整体平移，标准差不变。本次对全部重复实际核对该性质，最大系数平移误差LAD小于$4.1\times10^{-14}$、Huber小于$1.8\times10^{-14}$。未把“数值相等”误说成两个残差分布完全相同。
> 两方法本数据的残差Bootstrap标准误接近，其斜率约$.048$–$.049$；它们不同于上题正态参数Bootstrap，因为重抽的经验误差分布不同。2000次结果仍有Monte Carlo波动，小样本残差经验分布及固定设计假设也限制外推。
> 复现采用Python3.10、NumPy1.26.2、SciPy1.11.4，PCG64，种子20261113；按持久实现先参数Bootstrap再本残差Bootstrap，单独复现本段时需遵循同一随机流或直接使用保存的原始重复记录。Huber每次重估OLS尺度后取$k=1.5s_{OLS}$，LAD用HiGHS确定选点，均与(a)一致。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计（parameter estimation）]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]
- [[01 - 概率论/概念/随机变量|随机变量]]
- [[02 - 数理统计/概念/重采样|重采样]]

## 备注

- 完整原题已逐页对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=523|印刷492／PDF物理523]]；原题无星号。教材信息与归档进度见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 实际引用输入核对页：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=516|印刷485／PDF物理516]]、[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=518|印刷487／PDF物理518]]；所需模型、公式、数据在解答重述。
- 实际计算可复核：[[工具/StatisticalInference/ch12-computations/calc_ch12.py|完整实现与输入数据]]、[[工具/StatisticalInference/ch12-computations/ch12-computations.json|版本与完整结果]]、[[工具/StatisticalInference/ch12-computations/run-manifest.json|运行与文件校验记录]]。
- 全部原始Bootstrap重复：[[工具/StatisticalInference/ch12-computations/ch12-bootstrap-replicates.csv|系数重复CSV]]；[[工具/StatisticalInference/ch12-computations/README.md|算法、参数与复现范围]]。
- 来源已核对与解答写成不表示个人学习已完成；学习状态保留`not-started`。未实测Obsidian界面渲染。
