---
title: "习题 ST392：Poisson面积计数的最小二乘与有效无偏估计"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第11章习题11.38，印刷页462／PDF物理页493"
source_id: "DS011"
source_chapter: 11
source_exercise: "11.38"
source_stars: 0
source_refs: ["DS011 Exercise 11.38，印刷462／PDF物理493"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST392：Poisson面积计数的最小二乘与有效无偏估计

## 题目

### 英文原题

> [!question] 英文原题
> **11.38** An ecologist takes data $(x_i,Y_i)$, $i=1,\ldots,n$, where $x_i$ is the size of an area and $Y_i$ is the number of moss plants in the area. We model the data by $Y_i\sim\operatorname{Poisson}(\theta x_i)$, $Y_i$s independent.
> (a) Show that the least squares estimator of $\theta$ is $\sum x_iY_i/\sum x_i^2$. Show that this estimator has variance $\theta\sum x_i^3/(\sum x_i^2)^2$. Also, compute its bias.
> (b) Show that the MLE of $\theta$ is $\sum Y_i/\sum x_i$ and has variance $\theta/\sum x_i$. Compute its bias.
> (c) Find a best unbiased estimator of $\theta$ and show that its variance attains the Cramér–Rao Lower Bound.

### 中文转述

> [!question] 中文转述
> **原题11.38。** 一位生态学家取得数据$(x_i,Y_i)$，$i=1,\ldots,n$，其中$x_i$为区域面积，$Y_i$为该区域的苔藓植株数. 用模型$Y_i\sim\operatorname{Poisson}(\theta x_i)$描述数据，各$Y_i$独立.
>
> (a)  证明$\theta$的最小二乘估计量为$\sum x_iY_i/\sum x_i^2$. 证明它的方差为$\theta\sum x_i^3/(\sum x_i^2)^2$，并计算其偏倚.
>
> (b)  证明$\theta$的MLE为$\sum Y_i/\sum x_i$，方差为$\theta/\sum x_i$. 计算其偏倚.
>
> (c)  求$\theta$的最优无偏估计量，并证明其方差达到Cramér--Rao下界.

## 提示

> [!hint]- 提示
> Poisson似然只通过总计数依赖参数；比较最小二乘的加权总数与似然的未加权总数。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 教材输入与补充假设另行标明。
>
> 设$x_i\ge0$且至少一个正，$T_x=\sum x_i>0$，先取$\theta>0$。
> (a) 求导得$\widetilde\theta=\sum x_iY_i/\sum x_i^2$。独立性及$EY_i=\operatorname{Var}Y_i=\theta x_i$给$E\widetilde\theta=\theta$，偏差0，方差$\theta\sum x_i^3/(\sum x_i^2)^2$。
> (b) 对数似然中含参数项$(\sum Y_i)\log\theta-\theta T_x$，故$\widehat\theta=\sum Y_i/T_x$（全零计数时MLE在参数边界0；若只允许$\theta>0$则为该边界上确界）。$\sum Y_i\sim\mathrm{Pois}(\theta T_x)$，所以无偏且方差$\theta/T_x$。
> (c) 得分$(\sum Y_i)/\theta-T_x$、信息$T_x/\theta$，界$\theta/T_x$被$\widehat\theta$达到，故为最优无偏。也可由总计数的完整性及充分性得到UMVU。Cauchy–Schwarz给$(\sum x_i^2)^2\le(\sum x_i^3)(\sum x_i)$，确认最小二乘方差不更小，所有正面积相等时二者一致。$\theta=0$下计数恒0，估计误差0，信息正则公式用内部参数的极限解释。
>
> 完备性的细节是：若$S=\sum Y_i$且对所有$\theta>0$有$E_\theta|g(S)|<\infty$、$E_\theta g(S)=0$，则令$\lambda=\theta T_x$，有$\sum_{s\ge0}g(s)\lambda^s/s!=0$对所有$\lambda>0$成立。绝对收敛的幂级数唯一性给每个$g(s)=0$；因子分解已给充分性，故Lehmann–Scheffé定理也给$S/T_x$为UMVU。参数端点0的样本全落在$s=0$，也与此结论相容。

## 相关概念

- [[03 - 线性代数与优化/概念/正规方程|正规方程]]
- [[01 - 概率论/概念/期望|期望]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[01 - 概率论/概念/概率模型|概率模型]]

## 备注

- 统一来源见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011教材台账]]；原题位于[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=493|印刷462／PDF物理493]]。已对照原始页面核对完整英文、分题与定位，原题无星号。
- 解答为独立推导；引用的教材结论按source_refs核对，不使用答案册代替证明。
- 来源核对、归档与个人学习分别记录；verified只指所列来源核对范围，学习状态保持not-started。未实测Obsidian渲染。
