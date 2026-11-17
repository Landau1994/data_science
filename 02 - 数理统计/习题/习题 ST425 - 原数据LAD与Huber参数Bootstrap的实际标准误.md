---
title: "习题 ST425：原数据LAD与Huber参数Bootstrap的实际标准误"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "advanced"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第12章习题12.30，印刷页492／PDF物理页523"
source_id: "DS011"
source_chapter: 12
source_exercise: "12.30"
source_stars: 0
source_refs: ["DS011 Exercise 12.30，印刷页492／PDF物理页523", "DS011 所引正文，印刷485／PDF物理516", "DS011 所引正文，印刷487／PDF物理518"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST425：原数据LAD与Huber参数Bootstrap的实际标准误

## 题目

### 英文原题

> [!question] 英文原题
> **12.30** For the data of Table 12.4.2, use the parametric bootstrap to assess the standard error from the LAD and M-estimator fit. In particular
> (a) Fit the line $y=\alpha+\beta x$ to get estimates $\tilde\alpha$ and $\tilde\beta$.
> (b) Calculate the residual mean squared error $\hat\sigma^2=(n-2)^{-1}\sum_{i=1}^n[y_i-(\tilde\alpha+\tilde\beta x_i)]^2$.
> (c) Generate new residuals from n$(0,\hat\sigma^2)$ and re-estimate $\alpha$ and $\beta$.
> (d) Do (c) $B$ times and calculate the standard deviation of $\tilde\alpha$ and $\tilde\beta$.
> (e) Repeat (a)–(d) using both the Double Exponential and Laplace distributions for the errors. Compare your answers to the normal.

### 中文转述

> [!question] 中文转述
> **原题12.30。**
> 对12.4.2的数据，用参数自助法评价LAD和M估计拟合的标准误. 具体地：
>
> (a)  拟合直线$y=\alpha+\beta x$，得到估计$\tilde\alpha,\tilde\beta$.
>
> (b)  计算残差均方误差$\hat\sigma^2=\frac1{n-2}\sum_{i=1}^n[y_i-(\tilde\alpha+\tilde\beta x_i)]^2$.
>
> (c)  从$\mathrm n(0,\hat\sigma^2)$生成新残差，重新估计$\alpha,\beta$.
>
> (d)  将(c)重复$B$次，计算$\tilde\alpha,\tilde\beta$的标准差.
>
> (e)  分别用双指数和Laplace分布作为误差，重复(a)至(d)，并与正态情形比较.

## 提示

> [!hint]- 提示
> 每次生成完整固定设计样本并重新拟合；两个误差名称Double Exponential和Laplace实际同义。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 实际使用原表23项，$x$为O₂、$y$为CO₂，数据完整如下：
>
> | 动物 | O₂（%） | CO₂（%） |
> | --- | --- | --- |
> | 1 | 20 | 1 |
> | 2 | 19.6 | 1.2 |
> | 3 | 19.6 | 1.1 |
> | 4 | 19.4 | 1.4 |
> | 5 | 18.4 | 2.3 |
> | 6 | 19 | 1.7 |
> | 7 | 19 | 1.7 |
> | 8 | 18.3 | 2.4 |
> | 9 | 18.2 | 2.1 |
> | 10 | 18.6 | 2.1 |
> | 11 | 19.2 | 1.2 |
> | 12 | 18.2 | 2.3 |
> | 13 | 18.7 | 1.9 |
> | 14 | 18.5 | 2.4 |
> | 15 | 18 | 2.6 |
> | 16 | 17.4 | 2.9 |
> | 17 | 16.5 | 4 |
> | 18 | 17.2 | 3.3 |
> | 19 | 17.3 | 3 |
> | 20 | 17.8 | 3.4 |
> | 21 | 17.3 | 2.9 |
> | 22 | 18.4 | 1.9 |
> | 23 | 16.9 | 3.9 |
>
> (a) LAD定义为最小化$\sum|y_i-a-bx_i|$，用线性规划实现。M估计明确采用原书Huber损失$\rho_k(r)=r^2/2$若$|r|\le k$，否则$k|r|-k^2/2$；取$k=1.5s_{OLS}$，$s_{OLS}$是该数据样本OLS残差标准差，每次重拟合也重新计算它。Huber用IRLS求凸损失的解。原数据拟合LAD为$(\tilde a,\tilde b)=(18.58888889,-.8888888889)$，Huber为$(18.49684208,-.8850290700)$，与原书舍入拟合相符。LAD非唯一时沿用确定的HiGHS求解器选取的最小点；这个实现选择也纳入重复规则。
> (b) 按题式分母$n-2=21$，两方法残差MSE分别$.05522633745$与$.05541239499$。对鲁棒估计，这里是工作噪声尺度估计，不宣称同OLS一样无偏。
> (c) 对每方法固定自己的拟合均值$\hat y_i=\tilde a+\tilde b x_i$，独立生成$e_i^*\sim N(0,\hat\sigma^2)$，组成$y_i^*=\hat y_i+e_i^*$，然后按(a)完全重新拟合，不仅计算原残差的标准差。
> (d) 每方法实际运行$B=2000$次，Bootstrap标准误为$s_j^*=[\sum_{b=1}^B(\theta_{jb}^*-\bar\theta_j^*)^2/(B-1)]^{1/2}$。实际结果：
>
> | 方法 | 正态SE(截距) | 正态SE(斜率) | 双指数/Laplace SE(截距) | 双指数/Laplace SE(斜率) |
> | --- | --- | --- | --- | --- |
> | LAD | 1.219442352 | .0666675210 | .8942050850 | .0487489547 |
> | Huber | .9912918453 | .0540828247 | .9055386696 | .0493430216 |
>
> (e) 双指数（Double Exponential）与Laplace是同一分布，不是两个不同误差族。采用同方差参数化$e^*\sim\operatorname{Laplace}(0,\hat\sigma/\sqrt2)$，因此两个名称复用同一组实际生成的样本而结果完全一致，未伪造两个不同家族。该有限实验中LAD在Laplace误差下标准误较正态小，Huber两族差距较小；这只是给定设计、尺度估计及2000次Monte Carlo结果，不证明普遍效率次序。
> 复现信息：Python3.10、NumPy1.26.2、SciPy1.11.4，随机发生器NumPy default_rng的PCG64，种子20261113；固定原设计，不重抽$x$。每次优化需成功才计入，未跳过失败重复。完整实现、输入数据、版本、结果与原始重复记录已持久保存并在备注链接。

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
