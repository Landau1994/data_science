---
title: "习题 ST399：已知测量误差比的EIV斜率单调性与动物数据"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "advanced"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第12章习题12.4，印刷页488／PDF物理页519"
source_id: "DS011"
source_chapter: 12
source_exercise: "12.4"
source_stars: 0
source_refs: ["DS011 Exercise 12.4，印刷页488／PDF物理页519", "DS011 所引正文，印刷471／PDF物理502", "DS011 所引正文，印刷473／PDF物理504", "DS011 所引正文，印刷474／PDF物理505"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST399：已知测量误差比的EIV斜率单调性与动物数据

## 题目

### 英文原题

> [!question] 英文原题
> **12.4** Consider the MLE of the slope in the EIV model
> $$\hat\beta(\lambda)=\frac{-(S_{xx}-\lambda S_{yy})+\sqrt{(S_{xx}-\lambda S_{yy})^2+4\lambda S_{xy}^2}}{2\lambda S_{xy}},$$
> where $\lambda=\sigma_\delta^2/\sigma_\varepsilon^2$ is assumed known.
> (a) Show that $\lim_{\lambda\to0}\hat\beta(\lambda)=S_{xy}/S_{xx}$, the slope of the ordinary regression of $y$ on $x$.
> (b) Show that $\lim_{\lambda\to\infty}\hat\beta(\lambda)=S_{yy}/S_{xy}$, the reciprocal of the slope of the ordinary regression of $x$ on $y$.
> (c) Show that $\hat\beta(\lambda)$ is, in fact, monotone in $\lambda$ and is increasing if $S_{xy}>0$ and decreasing if $S_{xy}<0$.
> (d) Show that the orthogonal least squares line $(\lambda=1)$ is always between the lines given by ordinary regressions of $y$ on $x$ and of $x$ on $y$.
> (e) The data in the table were collected in a study to examine the relationship between brain weight and body weight in a number of animal species. Calculate the MLE of the slope assuming the EIV model. Also, calculate the least squares slopes of the regressions of $y$ on $x$ and of $x$ on $y$, and show how these quantities bound the MLE.
>
> | Species | Body weight (kg) $(x)$ | Brain weight (g) $(y)$ |
> | --- | --- | --- |
> | Arctic fox | 3.385 | 44.50 |
> | Owl monkey | .480 | 15.50 |
> | Mountain beaver | 1.350 | 8.10 |
> | Guinea pig | 1.040 | 5.50 |
> | Chinchilla | .425 | 6.40 |
> | Ground squirrel | .101 | 4.00 |
> | Tree hyrax | 2.000 | 12.30 |
> | Big brown bat | .023 | .30 |

### 中文转述

> [!question] 中文转述
> **原题12.4。**
> 考虑EIV模型中斜率的MLE
>
> $$
> \hat\beta(\lambda)=\frac{-(S_{xx}-\lambda S_{yy})+\sqrt{(S_{xx}-\lambda S_{yy})^2+4\lambda S_{xy}^2}}{2\lambda S_{xy}},
> $$
>
> 其中假定$\lambda=\sigma_\delta^2/\sigma_\varepsilon^2$已知.
>
> (a)  证明$\lim_{\lambda\to0}\hat\beta(\lambda)=S_{xy}/S_{xx}$，即$y$对$x$普通回归的斜率.
>
> (b)  证明$\lim_{\lambda\to\infty}\hat\beta(\lambda)=S_{yy}/S_{xy}$，即$x$对$y$普通回归斜率的倒数.
>
> (c)  证明$\hat\beta(\lambda)$关于$\lambda$单调；当$S_{xy}>0$时递增，当$S_{xy}<0$时递减.
>
> (d)  证明正交最小二乘直线（$\lambda=1$）总在$y$对$x$及$x$对$y$的普通回归直线之间.
>
> (e)  上表数据来自一项研究，旨在考察若干动物物种的脑重与体重的关系. 假设EIV模型，计算斜率的MLE. 再计算$y$对$x$及$x$对$y$回归的最小二乘斜率，说明这些量如何给出MLE的界.
>
> 原题所引完整数据表：
>
> | 物种 | 体重（kg） $(x)$ | 脑重（g） $(y)$ |
> | --- | --- | --- |
> | 北极狐 | 3.385 | 44.50 |
> | 夜猴 | .480 | 15.50 |
> | 山河狸 | 1.350 | 8.10 |
> | 豚鼠 | 1.040 | 5.50 |
> | 毛丝鼠 | .425 | 6.40 |
> | 地松鼠 | .101 | 4.00 |
> | 树蹄兔 | 2.000 | 12.30 |
> | 大棕蝠 | .023 | .30 |

## 提示

> [!hint]- 提示
> 用斜率二次方程的隐函数导数，并区分拟合线的坐标方向。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 记$A=S_{xx}>0,B=S_{yy}>0,C=S_{xy}\ne0$，假设$AB>C^2$，$\lambda>0$。正号根满足$\lambda Cb^2+(A-\lambda B)b-C=0$，且$b$与$C$同号。
> (a) 有理化得$b=2C/[A-\lambda B+\sqrt{(A-\lambda B)^2+4\lambda C^2}]$，令$\lambda\downarrow0$得$C/A$。
> (b) 原式分子分母除以$\lambda$，令$\lambda\to\infty$得$B/C$。
> (c) 隐微分给$b'=b(B-Cb)/[2\lambda Cb+A-\lambda B]$。分母恰为正根判别式平方根$D>0$。从(a)的起点$C/A$到可能碰到$B/C$以前，$B-Cb>0$；而把$b=B/C$代原方程得$AB/C-C\ne0$，所以任何有限$\lambda$均不能碰到该值。由连续性$B-Cb>0$始终成立，因此$b'$与$C$同号。两个极限给出全部范围。若$AB=C^2$，数据完全共线时斜率恒定，故原文“increasing/decreasing”应按非严格或排除完全相关理解。
> (d) 三条拟合线均通过$(\bar x,\bar y)$，而普通$x$对$y$的线改写成$y$对$x$斜率为$B/C$。正交斜率$b(1)$处在$C/A,B/C$之间，故在它们张成的角区间内；$C<0$时数值次序倒转但仍夹在两者之间。
> (e) 原表8对数据计算$A=9.095278,B=1358.255,C=96.1501$，$\bar x=1.1005,\bar y=12.075$。普通$y$对$x$斜率$10.57143058$；普通$x$对$y$斜率$C/B\approx.07078943$，其倒数$14.12640236$。题面未给$\lambda$数值，因此唯一可由原条件确定的是将这3个散布量代入题式的$b(\lambda)$族，夹在上述两数之间。若明确采用$\lambda=1$，得到$b=14.10271611$、截距$-3.445039084$。不能把未知误差比凭空估为1并称无条件唯一MLE；体重kg和脑重g的尺度约定也一并保留。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计（parameter estimation）]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]
- [[01 - 概率论/概念/随机变量|随机变量]]

## 备注

- 完整原题已逐页对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=519|印刷488／PDF物理519]]；原题无星号。教材信息与归档进度见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 实际引用输入核对页：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=502|印刷471／PDF物理502]]、[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=504|印刷473／PDF物理504]]、[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=505|印刷474／PDF物理505]]；所需模型、公式、数据在解答重述。
- 实际计算可复核：[[工具/StatisticalInference/ch12-computations/calc_ch12.py|完整实现与输入数据]]、[[工具/StatisticalInference/ch12-computations/ch12-computations.json|版本与完整结果]]、[[工具/StatisticalInference/ch12-computations/run-manifest.json|运行与文件校验记录]]。
- 来源已核对与解答写成不表示个人学习已完成；学习状态保留`not-started`。未实测Obsidian界面渲染。
