---
title: "习题 ST412：Probit回归似然求解与Challenger数据拟合"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "advanced"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第12章习题12.17，印刷页491／PDF物理页522"
source_id: "DS011"
source_chapter: 12
source_exercise: "12.17"
source_stars: 0
source_refs: ["DS011 Exercise 12.17，印刷页491／PDF物理页522", "DS011 所引正文，印刷480／PDF物理511", "DS011 所引正文，印刷481／PDF物理512"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST412：Probit回归似然求解与Challenger数据拟合

## 题目

### 英文原题

> [!question] 英文原题
> **12.17** In probit regression, the link function is the standard normal cdf $\Phi(x)=P(Z\le x)$, where $Z\sim\mathrm n(0,1)$. This, in this model we observe $(Y_1,x_1),(Y_2,x_2),\ldots,(Y_n,x_n)$ where $Y_i\sim\operatorname{Bernoulli}(\pi_i)$, and $\pi_i=\Phi(\alpha+\beta x_i)$.
> (a) Write the likelihood function and show how to solve for the MLEs of $\alpha$ and $\beta$.
> (b) Fit the probit model to the data of Table 12.3.1. Comment on any differences from the logistic fit.

### 中文转述

> [!question] 中文转述
> **原题12.17。**
> 在probit回归中，连接函数为标准正态cdf $\Phi(x)=P(Z\le x)$，其中$Z\sim\mathrm n(0,1)$. 因而，在这一模型中观测$(Y_1,x_1),\allowbreak(Y_2,x_2),\allowbreak\ldots,\allowbreak(Y_n,x_n)$，其中$Y_i\sim\operatorname{Bernoulli}(\pi_i)$，且$\pi_i=\Phi(\alpha+\beta x_i)$.
>
> (a)  写出似然函数，并说明如何求解$\alpha,\beta$的MLE.
>
> (b)  对12.3.1的数据拟合probit模型，评论它与逻辑回归拟合的任何差异.

## 提示

> [!hint]- 提示
> 用标准正态log-CDF计算稳定似然，中心化温度后作带回溯的Newton迭代。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** (a) 假设各试验独立，写$z_i=(1,x_i)^T,\eta_i=z_i^T\gamma,\gamma=(\alpha,\beta)^T$。似然$L(\gamma)=\prod_i\Phi(\eta_i)^{y_i}\Phi(-\eta_i)^{1-y_i}$；得分为$U=\sum_i z_i\phi(\eta_i)(y_i-\Phi(\eta_i))/[\Phi(\eta_i)\Phi(-\eta_i)]$。可用Newton法求$U=0$：设$a_i=\phi(\eta_i)/\Phi(\eta_i),b_i=\phi(\eta_i)/\Phi(-\eta_i)$，负Hessian权重$w_i=y_i a_i(\eta_i+a_i)+(1-y_i)b_i(b_i-\eta_i)>0$，更新$\gamma\leftarrow\gamma+(\sum_iw_i z_i z_i^T)^{-1}U$，必要时减半步长以增大对数似然。使用log-CDF避免极端尾概率下溢；满秩且非分离时严格凹目标的有限根唯一为MLE，分离时应报告无有限MLE。
> (b) 原表完整23项如下（1为O-ring失败）：
>
> | 航班号 | 温度（°F） | 失败指示 |
> | --- | --- | --- |
> | 14 | 53 | 1 |
> | 9 | 57 | 1 |
> | 23 | 58 | 1 |
> | 10 | 63 | 1 |
> | 1 | 66 | 0 |
> | 5 | 67 | 0 |
> | 13 | 67 | 0 |
> | 15 | 68 | 0 |
> | 4 | 69 | 0 |
> | 3 | 70 | 0 |
> | 8 | 70 | 0 |
> | 17 | 70 | 0 |
> | 2 | 70 | 1 |
> | 11 | 70 | 1 |
> | 6 | 72 | 0 |
> | 7 | 73 | 0 |
> | 16 | 75 | 0 |
> | 21 | 75 | 1 |
> | 19 | 76 | 0 |
> | 22 | 76 | 0 |
> | 12 | 78 | 0 |
> | 20 | 79 | 0 |
> | 18 | 81 | 0 |
>
> 实际以$x-70$中心化、从零向量启动Newton回溯，Probit在6次迭代收敛，最终得分最大绝对分量约$2.2\times10^{-10}$。换回原温度，$\hat\pi_P(x)=\Phi(9.204852223-.1410190147x)$，对数似然$-9.970259045$。同数据Logistic拟合$\hat\pi_L(x)=\Lambda(15.80557452-.2426775764x)$，对数似然$-9.941613829$，与原书四舍五入结果吻合。
> 两者在观测范围53–81°F内曲线接近，斜率系数因链接尺度不同不能直接比较数值大小。极低温尾部不同，例如31°F时Probit约$.9999993284$，Logistic约$.9997471774$；这是模型外推计算，不是新增观测核验。
>
> ![[附件/习题图/DS011/习题12.17-Probit与Logistic拟合.png]]
>
> 计算环境Python3.10、NumPy1.26.2、SciPy1.11.4；精确版本与迭代记录见本章计算附件。英文首句后的“This”按原印保留。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计（parameter estimation）]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]
- [[01 - 概率论/概念/随机变量|随机变量]]

## 备注

- 完整原题已逐页对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=522|印刷491／PDF物理522]]；原题无星号。教材信息与归档进度见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 实际引用输入核对页：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=511|印刷480／PDF物理511]]、[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=512|印刷481／PDF物理512]]；所需模型、公式、数据在解答重述。
- 本题独立新绘图件保留[[附件/习题图/DS011/习题12.17-Probit与Logistic拟合.pdf|矢量PDF]]及[[附件/习题图/DS011/源码/第12章/ch12_17.tex|可编辑绘图源文件]]；按公式及实际拟合值生成。
- 实际计算可复核：[[工具/StatisticalInference/ch12-computations/calc_ch12.py|完整实现与输入数据]]、[[工具/StatisticalInference/ch12-computations/ch12-computations.json|版本与完整结果]]、[[工具/StatisticalInference/ch12-computations/run-manifest.json|运行与文件校验记录]]。
- 来源已核对与解答写成不表示个人学习已完成；学习状态保留`not-started`。未实测Obsidian界面渲染。
