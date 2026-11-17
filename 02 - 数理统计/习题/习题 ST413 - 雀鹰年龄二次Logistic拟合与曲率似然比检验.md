---
title: "习题 ST413：雀鹰年龄二次Logistic拟合与曲率似然比检验"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "advanced"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第12章习题12.18，印刷页491／PDF物理页522"
source_id: "DS011"
source_chapter: 12
source_exercise: "12.18"
source_stars: 0
source_refs: ["DS011 Exercise 12.18，印刷页491／PDF物理页522", "DS011 所引正文，印刷479／PDF物理510", "DS011 所引正文，印刷480／PDF物理511", "DS011 所引正文，印刷482／PDF物理513"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST413：雀鹰年龄二次Logistic拟合与曲率似然比检验

## 题目

### 英文原题

> [!question] 英文原题
> **12.18** Brown and Rothery (1993, Chapter 4) discuss a generalization of the linear logistic model to the quadratic model
> $$\log\left(\frac{\pi_i}{1-\pi_i}\right)=\alpha+\beta x_i+\gamma x_i^2.$$
> (a) Write out the likelihood function and show how to solve for the MLEs of $\alpha,\beta,$ and $\gamma$.
> (b) Using the log LRT, show how to test the hypothesis $H_0:\gamma=0$, that is, the hypothesis that the model is really linear logistic.
> (c) Fit the quadratic logistic model to the data in Table 12.5.4 on survival of sparrowhawks of different ages.
> (d) Decide whether the better model for the sparrowhawks is linear or quadratic, that is, test $H_0:\gamma=0$.
>
> Table 12.5.4 Age structured survival of sparrowhawks
>
> | Age | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
> | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
> | No. of birds | 77 | 149 | 182 | 118 | 78 | 46 | 27 | 10 | 4 |
> | No. surviving | 35 | 89 | 130 | 79 | 52 | 28 | 14 | 3 | 1 |

### 中文转述

> [!question] 中文转述
> **原题12.18。**
> Brown和Rothery（1993，第4章）讨论了将线性逻辑模型推广为二次模型：
>
> $$
> \log\left(\frac{\pi_i}{1-\pi_i}\right)=\alpha+\beta x_i+\gamma x_i^2.
> $$
>
> (a)  写出似然函数，并说明如何求解$\alpha,\beta,\gamma$的MLE.
>
> (b)  用对数似然比检验，说明如何检验$H_0:\gamma=0$，即模型实际为线性逻辑模型.
>
> (c)  对12.5.4中不同年龄雀鹰的存活数据拟合二次逻辑模型.
>
> (d)  判断雀鹰数据用线性还是二次模型更好，即检验$H_0:\gamma=0$.
>
>
>
> 表12.5.4：按年龄分组的雀鹰存活情况
>
> | 年龄 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
> | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
> | 鸟数 | 77 | 149 | 182 | 118 | 78 | 46 | 27 | 10 | 4 |
> | 存活数 | 35 | 89 | 130 | 79 | 52 | 28 | 14 | 3 | 1 |

## 提示

> [!hint]- 提示
> 三列设计矩阵$1,x,x^2$给得分与Hessian；零假设少一个曲率参数。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 按题给分组数据，设$S_i$独立$\operatorname{Bin}(n_i,\pi_i)$，固定年龄$x_i$，$z_i=(1,x_i,x_i^2)^T$。
> (a) $L=\prod_i\binom{n_i}{s_i}\exp(s_i z_i^T\theta)/(1+e^{z_i^T\theta})^{n_i}$，$\theta=(\alpha,\beta,\gamma)^T$。得分$U=\sum_i z_i(s_i-n_i\pi_i)$，负Hessian$I=\sum_i n_i\pi_i(1-\pi_i)z_i z_i^T$。设计满秩且无分离时目标严格凹，迭代$\theta\leftarrow\theta+I^{-1}U$并回溯即可找到唯一有限MLE；同样可用中心化$x-5$改善条件数再换回原系数。
> (b) 原假设拟合两参数线性Logistic，统计量$D=2[\ell(\hat\alpha,\hat\beta,\hat\gamma)-\ell(\hat\alpha_0,\hat\beta_0,0)]$。在通常独立分组二项正则大样本条件下$D\Rightarrow\chi^2_1$，所以近似水平$\alpha_0$拒绝当$D>\chi^2_{1,1-\alpha_0}$（此处下标明确为CDF分位数）。不是有限样本精确卡方检验。
> (c) 原表9组全数据实际Newton拟合得到$\hat\alpha=-.8450423413,\hat\beta=.8371981381,\hat\gamma=-.1029613571$，即$\hat\pi(x)=\Lambda(-.8450423413+.8371981381x-.1029613571x^2)$。去掉共同二项组合常数的最大对数似然为$-445.889950626$；5次迭代，中心化得分最大绝对值小于$5\times10^{-13}$。
> (d) 线性拟合为$\Lambda(.4800103469+.0074349883x)$，对数似然$-457.571825488$，故$D=23.36374972$，$\chi^2_1$近似$p\approx1.3408164\times10^{-6}$。在$.05$水平拒绝无线性曲率假设，二次模型显著改善拟合；它描绘中龄存活较高、两端较低，而线性拟合几乎平坦。结论是该指定模型比较，并非证明二次形式为唯一真实机制。
>
> ![[附件/习题图/DS011/习题12.18-雀鹰存活拟合.png]]

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计（parameter estimation）]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]
- [[01 - 概率论/概念/随机变量|随机变量]]
- [[02 - 数理统计/概念/假设检验|假设检验]]

## 备注

- 完整原题已逐页对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=522|印刷491／PDF物理522]]；原题无星号。教材信息与归档进度见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 实际引用输入核对页：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=510|印刷479／PDF物理510]]、[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=511|印刷480／PDF物理511]]、[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=513|印刷482／PDF物理513]]；所需模型、公式、数据在解答重述。
- 本题独立新绘图件保留[[附件/习题图/DS011/习题12.18-雀鹰存活拟合.pdf|矢量PDF]]及[[附件/习题图/DS011/源码/第12章/ch12_18.tex|可编辑绘图源文件]]；按公式及实际拟合值生成。
- 实际计算可复核：[[工具/StatisticalInference/ch12-computations/calc_ch12.py|完整实现与输入数据]]、[[工具/StatisticalInference/ch12-computations/ch12-computations.json|版本与完整结果]]、[[工具/StatisticalInference/ch12-computations/run-manifest.json|运行与文件校验记录]]。
- 来源已核对与解答写成不表示个人学习已完成；学习状态保留`not-started`。未实测Obsidian界面渲染。
