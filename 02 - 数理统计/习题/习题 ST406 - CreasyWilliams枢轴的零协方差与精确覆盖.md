---
title: "习题 ST406：CreasyWilliams枢轴的零协方差与精确覆盖"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "advanced"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第12章习题12.11，印刷页489、490／PDF物理页520、521"
source_id: "DS011"
source_chapter: 12
source_exercise: "12.11"
source_stars: 0
source_refs: ["DS011 Exercise 12.11，印刷页489、490／PDF物理页520、521", "DS011 所引正文，印刷475／PDF物理506", "DS011 所引正文，印刷477／PDF物理508"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST406：CreasyWilliams枢轴的零协方差与精确覆盖

## 题目

### 英文原题

> [!question] 英文原题
> **12.11** (a) Show that for random variables $X$ and $Y$ and constants $a,b,c,d$,
> $$\operatorname{Cov}(aY+bX,cY+dX)=ac\operatorname{Var}Y+(bc+ad)\operatorname{Cov}(X,Y)+bd\operatorname{Var}X.$$
> (b) Use the result in part (a) to verify the fact that in the structural relationship model with $\sigma_\delta^2=\lambda\sigma_\varepsilon^2$,
> $$\operatorname{Cov}(\beta\lambda Y_i+X_i,Y_i-\beta X_i)=0,$$
> the identity on which the Creasy–Williams confidence set is based.
> (c) Use the results of part (b) to show that
> $$\frac{\sqrt{n-2}\,r_\lambda(\beta)}{\sqrt{1-r_\lambda^2(\beta)}}\sim t_{n-2},$$
> for any value of $\beta$, where $r_\lambda(\beta)$ is given in (12.2.23). Also, show that the confidence set defined in (12.2.24) has constant coverage probability equal to $1-\alpha$.

### 中文转述

> [!question] 中文转述
> **原题12.11。**
> (a)  证明对随机变量$X,Y$和常数$a,b,c,d$，
>
> $$
> \operatorname{Cov}(aY+bX,cY+dX)=ac\operatorname{Var}Y+(bc+ad)\operatorname{Cov}(X,Y)+bd\operatorname{Var}X.
> $$
>
> (b)  用(a)验证，在$\sigma_\delta^2=\lambda\sigma_\varepsilon^2$的结构关系模型中，
>
> $$
> \operatorname{Cov}(\beta\lambda Y_i+X_i,Y_i-\beta X_i)=0,
> $$
>
> 这就是Creasy–Williams置信集所依据的恒等式.
>
> (c)  用(b)证明，对任意$\beta$，
>
> $$
> \frac{\sqrt{n-2}\,r_\lambda(\beta)}{\sqrt{1-r_\lambda^2(\beta)}}\sim t_{n-2},
> $$
>
> 其中$r_\lambda(\beta)$由式12.2.23给出. 再证明式12.2.24定义的置信集具有恒定覆盖概率$1-\alpha$.

## 提示

> [!hint]- 提示
> 在每个真斜率处变换为独立正态对，再证明零相关样本相关系数的t律。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** (a) 假设二阶矩有限，协方差对两坐标双线性，逐项展开为$ac\operatorname{Cov}(Y,Y)+ad\operatorname{Cov}(Y,X)+bc\operatorname{Cov}(X,Y)+bd\operatorname{Cov}(X,X)$，用对称性即原式。
> (b) 重述结构模型矩：$\operatorname{Var}X=t+d,\operatorname{Var}Y=\beta^2t+e,\operatorname{Cov}(X,Y)=\beta t$，$d=\lambda e$。令$U=\beta\lambda Y+X,V=Y-\beta X$，代(a)得$\operatorname{Cov}(U,V)=\beta\lambda(\beta^2t+e)+(1-\lambda\beta^2)\beta t-\beta(t+d)=\beta(\lambda e-d)=0$。原模型二元正态，故$U,V$独立正态；正误差方差及变换行列式$-(1+\lambda\beta^2)\ne0$保证非退化。
> (c) 取$n\ge3$，$r_\lambda(\beta)$为$U_i,V_i$的样本相关系数。条件于中心化$U$向量$u$，独立正态$V$的中心化噪声在$u/\|u\|$方向投影为$Z\sim N(0,1)$，其在同时正交于常量向量与$u$的$n-2$维分量平方和为$Q\sim\chi^2_{n-2}$，由正交正态分解二者独立。因此$r=Z/\sqrt{Z^2+Q}$，$\sqrt{n-2}r/\sqrt{1-r^2}=Z/\sqrt{Q/(n-2)}\sim t_{n-2}$。条件律不含$u$，故也是无条件律。
> 令$q$为$F_{1,n-2}$分布的$1-\alpha$分位数，即本书右尾下标$F_{1,n-2,\alpha}$。平方上述枢轴得$\{\beta:(n-2)r_\lambda^2(\beta)/(1-r_\lambda^2(\beta))\le q\}$覆盖真斜率的概率恰为$1-\alpha$，与其余参数无关。“any value”指任意**真参数**对应的分布结论；对同一固定真模型随意代入不同候选值时不都中心$t$。区间可能不连通或无界，不影响覆盖证明。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计（parameter estimation）]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]
- [[01 - 概率论/概念/随机变量|随机变量]]
- [[02 - 数理统计/概念/区间估计|区间估计]]

## 备注

- 完整原题已逐页对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=520|印刷489／PDF物理520]]、[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=521|印刷490／PDF物理521]]；原题无星号。教材信息与归档进度见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 实际引用输入核对页：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=506|印刷475／PDF物理506]]、[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=508|印刷477／PDF物理508]]；所需模型、公式、数据在解答重述。
- 来源已核对与解答写成不表示个人学习已完成；学习状态保留`not-started`。未实测Obsidian界面渲染。
