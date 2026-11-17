---
title: "习题 ST405：已知误差比的结构EIV估计与方差二倍边界"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "advanced"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第12章习题12.10，印刷页489／PDF物理页520"
source_id: "DS011"
source_chapter: 12
source_exercise: "12.10"
source_stars: 0
source_refs: ["DS011 Exercise 12.10，印刷页489／PDF物理页520", "DS011 所引正文，印刷474／PDF物理505", "DS011 所引正文，印刷475／PDF物理506", "DS011 所引正文，印刷476／PDF物理507"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST405：已知误差比的结构EIV估计与方差二倍边界

## 题目

### 英文原题

> [!question] 英文原题
> **12.10** (a) Derive the MLEs for $(\alpha,\beta,\sigma_\varepsilon^2,\sigma_\delta^2,\sigma_\xi^2)$ in the structural relationship model, by solving the equations (12.2.20) under the assumption that $\sigma_\delta^2=\lambda\sigma_\varepsilon^2$.
> (b) Calculate the MLEs for $(\alpha,\beta,\sigma_\varepsilon^2,\sigma_\delta^2,\sigma_\xi^2)$ for the data of Exercise 12.4 by assuming the structural relationship model holds and that $\sigma_\delta^2=\lambda\sigma_\varepsilon^2$.
> (c) Verify the relationship between variance estimates in the functional and structural relationship models. In particular, show that
> $$\widehat{\operatorname{Var}}X_i(\text{structural})=2\widehat{\operatorname{Var}}X_i(\text{functional}).$$
> That is, verify
> $$\left(S_{xx}-\frac{S_{xy}}{\hat\beta}\right)=\frac\lambda{1+\lambda\hat\beta^2}\sum_{i=1}^n(y_i-(\hat\alpha+\hat\beta x_i))^2.$$
> (d) Verify the following equality which is implicit in the MLE variance estimates given in (12.2.21). Show that
> $$S_{xx}-\frac{S_{xy}}{\hat\beta}=\lambda(S_{yy}-\hat\beta S_{xy}).$$

### 中文转述

> [!question] 中文转述
> **原题12.10。**
> (a)  假设$\sigma_\delta^2=\lambda\sigma_\varepsilon^2$，解式12.2.20，推导结构关系模型中$(\alpha,\beta,\sigma_\varepsilon^2,\sigma_\delta^2,\sigma_\xi^2)$的MLE.
>
> (b)  假设结构关系模型成立且$\sigma_\delta^2=\lambda\sigma_\varepsilon^2$，计算习题12.4数据的$(\alpha,\beta,\sigma_\varepsilon^2,\sigma_\delta^2,\sigma_\xi^2)$的MLE.
>
> (c)  验证函数关系模型与结构关系模型中方差估计的关系. 特别地，证明
>
> $$
> \widehat{\operatorname{Var}}X_i(\text{结构})=2\widehat{\operatorname{Var}}X_i(\text{函数}).
> $$
>
> 即验证
>
> $$
> \left(S_{xx}-\frac{S_{xy}}{\hat\beta}\right)=\frac\lambda{1+\lambda\hat\beta^2}\sum_{i=1}^n\bigl(y_i-(\hat\alpha+\hat\beta x_i)\bigr)^2.
> $$
>
> (d)  验证式12.2.21的MLE方差估计中隐含的等式：
>
> $$
> S_{xx}-\frac{S_{xy}}{\hat\beta}=\lambda(S_{yy}-\hat\beta S_{xy}).
> $$

## 提示

> [!hint]- 提示
> 同一斜率方程消去潜变量方差；注意结构边缘方差还含潜变量变异。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 设$\lambda>0$已知，$A=S_{xx},B=S_{yy},C=S_{xy}\ne0$、$AB>C^2$，$n\ge3$。
> (a) 方程给$\hat\xi=\bar x,\hat\alpha=\bar y-b\bar x$、$t=C/(nb)$、$d=(A-C/b)/n$、$e=(B-bC)/n$。代$d=\lambda e$得$\lambda Cb^2+(A-\lambda B)b-C=0$，取与$C$同号的正号根，另一根使$t<0$不合法。这恰为原(12.2.16)的$\hat\beta$；由12.4的界，$d,e,t$非负。所得观测均值与协方差等于正定样本MLE，故不仅解方程，也确为全局MLE。
> (b) 原数据给$A=9.095278,B=1358.255,C=96.1501,n=8$。题面没给$\lambda$数值，完整参数解为把这些数代入(a)的函数族；若明确取$\lambda=1$，则$(\hat\alpha,\hat\beta,e,d,t)\approx(-3.445039084,14.10271611,.2846794135,.2846794135,.8522303365)$。未知均值$\hat\xi=1.1005$。
> (c) $R=\sum(y_i-\hat\alpha-bx_i)^2=B-2bC+b^2A$。斜率方程移项后直接验证$(A-C/b)(1+\lambda b^2)=\lambda R$，即题内第二个等式。结构误差方差$d_S=(A-C/b)/n$，函数型误差MLE$d_F=\lambda R/[2n(1+\lambda b^2)]$，所以$d_S=2d_F$；数值例$d_F=.1423397067$。
> 但原文把这写成边缘$\widehat{\operatorname{Var}}X_i$二倍并不严密：结构模型边缘$\operatorname{Var}X=t+d$，其MLE为$A/n$，函数模型条件于固定潜值的方差才是$d_F$。一般$t+d\ne2d_F$（本数据$A/n=1.13690975$）。等式正确指两种**测量误差方差**估计，不能把潜变量边缘变异漏掉。
> (d) $d=\lambda e$本身即给$A-C/b=\lambda(B-bC)$；反过来它与$b\ne0$也等价于斜率二次方程，故所有列式相容。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计（parameter estimation）]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]
- [[01 - 概率论/概念/随机变量|随机变量]]

## 备注

- 完整原题已逐页对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=520|印刷489／PDF物理520]]；原题无星号。教材信息与归档进度见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 实际引用输入核对页：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=505|印刷474／PDF物理505]]、[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=506|印刷475／PDF物理506]]、[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=507|印刷476／PDF物理507]]；所需模型、公式、数据在解答重述。
- 实际计算可复核：[[工具/StatisticalInference/ch12-computations/calc_ch12.py|完整实现与输入数据]]、[[工具/StatisticalInference/ch12-computations/ch12-computations.json|版本与完整结果]]、[[工具/StatisticalInference/ch12-computations/run-manifest.json|运行与文件校验记录]]。
- 来源已核对与解答写成不表示个人学习已完成；学习状态保留`not-started`。未实测Obsidian界面渲染。
