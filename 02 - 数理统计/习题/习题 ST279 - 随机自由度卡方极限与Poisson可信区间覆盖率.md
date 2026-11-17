---
title: "习题 ST279：随机自由度卡方极限与Poisson可信区间覆盖率"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第9章习题9.31，印刷页369／PDF物理页400"
source_id: "DS011"
source_chapter: 9
source_exercise: "9.31"
source_stars: 0
source_refs: ["DS011 Exercise 9.31，印刷369／PDF物理400", "DS011 Example 9.2.17及(9.2.22)，印刷354／PDF物理385"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST279：随机自由度卡方极限与Poisson可信区间覆盖率

## 题目

### 英文原题

> [!question] 英文原题
> **9.31** Complete the coverage probability calculation needed in Example 9.2.17.
> (a) If $\chi^2_{2Y}$ is a chi squared random variable with $Y\sim\operatorname{Poisson}(\lambda)$, show that $E(\chi^2_{2Y})=2\lambda$, $\operatorname{Var}(\chi^2_{2Y})=8\lambda$, the mgf of $\chi^2_Y$ is given by $\exp(-\lambda+\frac\lambda{1-2t})$, and
> $$
> \frac{\chi^2_{2Y}-2\lambda}{\sqrt{8\lambda}}\to n(0,1)
> $$
> as $\lambda\to\infty$. (Use moment generating functions.)
> (b) Now evaluate (9.2.22) as $\lambda\to\infty$ by first standardizing $\chi^2_{2Y}$. Show that the standardized upper limit goes to $-\infty$ as $\lambda\to\infty$, and hence the coverage probability goes to zero.

### 中文转述

> [!question] 中文转述
> **原题9.31。**
> 完成例9.2.17所需的覆盖概率计算.
>
> (a)  若$\chi^2_{2Y}$为卡方随机变量，且$Y\sim\operatorname{Poisson}(\lambda)$，证明$E(\chi^2_{2Y})=2\lambda$，$\operatorname{Var}(\chi^2_{2Y})=8\lambda$，$\chi^2_Y$的mgf为$\exp(-\lambda+\lambda/(1-2t))$，并且当$\lambda\to\infty$时，
>
> $$
> \frac{\chi^2_{2Y}-2\lambda}{\sqrt{8\lambda}}\to\mathrm n(0,1).
> $$
>
> （使用矩母函数.）
>
> (b)  现在先将$\chi^2_{2Y}$标准化，再计算$\lambda\to\infty$时的式9.2.22. 证明标准化后的上限在$\lambda\to\infty$时趋于$-\infty$，从而覆盖概率趋于零.

## 提示

> [!hint]- 提示
> 给定$Y$先用全期望、全方差求随机自由度卡方的矩；再对复合Poisson的mgf取对数展开，并核对标准化覆盖端点。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 教材输入与补充假设另行标明。
>
> (a) 精确定义为$V\mid Y\sim\chi^2_{2Y}$，$Y=0$时$V=0$。由全期望及全方差，$EV=E(2Y)=2\lambda$，$\operatorname{Var}V=E(4Y)+\operatorname{Var}(2Y)=8\lambda$。矩母函数$M_V(t)=E(1-2t)^{-Y}=\exp\{\lambda[(1-2t)^{-1}-1]\}$，$t<1/2$。原文此处写“mgf of $\chi^2_Y$”少了2，正确对象为$V=\chi^2_{2Y}$。令$Z=(V-2\lambda)/\sqrt{8\lambda}$，展开$(1-u)^{-1}=1+u+u^2+O(u^3)$得$\log M_Z(t)=t^2/2+O(\lambda^{-1/2})$，故趋标准正态。
> (b) 正文中$Y\sim\mathrm{Pois}(n\lambda)$。固定$n,a,b>0$，记$r=nb/(nb+1)<1$。式(9.2.22)的随机上界为$r\,q_{2(Y+a),1-\alpha/2}$，按(a)中心$2n\lambda$标准化后是
> $$
> \frac{r\,q_{2(Y+a),1-\alpha/2}-2n\lambda}{\sqrt{8n\lambda}}
> =-(1-r)\sqrt{n\lambda/2}+O_P(1)\longrightarrow-\infty.
> $$
> 所以该辅助随机卡方事件概率趋0。
> **实际覆盖须另作严格证明：** 正文先用$\lambda/V\to1/(2n)$替代随机比例，把它写成(9.2.22)，这不是有限样本等式，不能仅凭该替代声称精确覆盖。后验等尾区间真正的上端为$U(Y)=b\,q_{2(Y+a),1-\alpha/2}/[2(nb+1)]$。因$Y/(n\lambda)\to_P1$、$q_{2(Y+a),1-\alpha/2}/(2Y)\to_P1$，有$U(Y)/\lambda\to_Pr<1$，从而$P_\lambda(\lambda\le U(Y))\to0$，实际覆盖率也趋0。此证明不需要把依赖$Y$的分位点当常数或把渐近比例当精确等式。

## 相关概念

- [[02 - 数理统计/概念/区间估计|区间估计]]
- [[02 - 数理统计/概念/假设检验|假设检验]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[01 - 概率论/概念/概率模型|概率模型]]

## 备注

- 统一来源见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011教材台账]]；原题位于[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=400|印刷369／PDF物理400]]。已对照原始页面核对完整英文、分题与定位，原题无星号。
- 解答为独立推导；引用的教材结论按source_refs核对，不使用答案册代替证明。
- 来源核对、归档与个人学习分别记录；verified只指所列来源核对范围，学习状态保持not-started。未实测Obsidian渲染。
