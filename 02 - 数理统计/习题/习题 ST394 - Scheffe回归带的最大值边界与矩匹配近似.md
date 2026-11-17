---
title: "习题 ST394：Scheffe回归带的最大值边界与矩匹配近似"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "advanced"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第11章习题11.40，印刷页462／PDF物理页493"
source_id: "DS011"
source_chapter: 11
source_exercise: "11.40"
source_stars: 0
source_refs: ["DS011 Exercise 11.40，印刷462／PDF物理493", "DS011 (11.3.41)–(11.3.44)及Theorem 11.3.6，印刷452–454／PDF物理483–485"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST394：Scheffe回归带的最大值边界与矩匹配近似

## 题目

### 英文原题

> [!question] 英文原题
> **11.40** (a) Prove that if $a,b,c,$ and $d$ are constants, with $c>0$ and $d>0$, then
> $$
> \max_t\frac{(a+bt)^2}{c+dt^2}=\frac{a^2}c+\frac{b^2}d.
> $$
> (b) Use part (a) to verify equation (11.3.44) and hence fill in the gap in Theorem 11.3.6.
> (c) Use part (a) to find a Scheffé-type simultaneous band using the prediction intervals of (11.3.41). That is, rewriting the prediction intervals as was done in Theorem 11.3.6, show
> $$
> \max_t\frac{((\bar Y-\mu_{\bar Y})+(\widehat\beta-\beta)t)^2}{S^2[1+\frac1n+\frac{t^2}{S_{xx}}]}
> =\frac{\frac n{n+1}(\bar Y-\mu_{\bar Y})^2+S_{xx}(\widehat\beta-\beta)^2}{S^2}.
> $$
> (d) The distribution of the maximum is not easy to write down, but we could approximate it. Approximate the statistic by using moment matching, as done in Example 7.2.3.

### 中文转述

> [!question] 中文转述
> **原题11.40。** (a)  证明：若$a,b,c,d$为常数，$c>0,d>0$，则
>
> $$
> \max_t\frac{(a+bt)^2}{c+dt^2}=\frac{a^2}c+\frac{b^2}d.
> $$
>
> (b)  用(a)验证式11.3.44，从而补全定理11.3.6中的空缺.
>
> (c)  用(a)，根据式11.3.41的预测区间求一个Scheffé型同时带. 即仿照定理11.3.6重新表示预测区间，证明
>
> $$
> \max_t\frac{\bigl((\bar Y-\mu_{\bar Y})+(\hat\beta-\beta)t\bigr)^2}{S^2[1+1/n+t^2/S_{xx}]}
> =\frac{\dfrac n{n+1}(\bar Y-\mu_{\bar Y})^2+S_{xx}(\hat\beta-\beta)^2}{S^2}.
> $$
>
> (d)  最大值的分布不容易写出，但可以近似. 像例7.2.3那样使用矩匹配，近似这个统计量.

### 题内引用与条件

取$S^2=\mathrm{RSS}/(n-2)$、$\mu_{\bar Y}=\alpha+\beta\bar x$；正态模型且设计满秩，$n>2$。正文原位置已核对，预测与均值对象的区别在解答另注。

## 提示

> [!hint]- 提示
> 先用加权Cauchy–Schwarz求上确界并追踪能否取得；分布化为独立正态平方和除以残差卡方。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 教材输入与补充假设另行标明。
>
> (a) Cauchy–Schwarz给
> $$
> (a+bt)^2=\left(\frac a{\sqrt c}\sqrt c+\frac b{\sqrt d}\sqrt d\,t\right)^2
> \le(a^2/c+b^2/d)(c+dt^2).
> $$
> $a\ne0$时等号在$t=bc/(ad)$取得；$a=b=0$时恒0。若$a=0,b\ne0$，函数$b^2t^2/(c+dt^2)$严格小于$b^2/d$，但$|t|\to\infty$逼近，只有上确界而无有限最大值。因此原式一般应将max改为sup，这不影响后续连续抽样中几乎处处的结果。
> (b) 令$A=\bar Y-\mu_{\bar Y}$、$B=\widehat\beta-\beta$、$\nu=n-2$。取$c=1/n,d=1/S_{xx}$，得$\sup_t(A+Bt)^2/[S^2(1/n+t^2/S_{xx})]=(nA^2+S_{xx}B^2)/S^2$，即(11.3.44)。中心化正态回归有$Z_1=\sqrt n A/\sigma,Z_2=\sqrt{S_{xx}}B/\sigma$独立标准正态，且独立于$V=\nu S^2/\sigma^2\sim\chi^2_\nu$。故统计量$=(Z_1^2+Z_2^2)/(V/\nu)\sim2F_{2,\nu}$，取平方半宽常数$2F_{2,\nu,\alpha}$即以$1-\alpha$概率同时覆盖整条均值直线。
> (c) 改取$c=1+1/n,d=1/S_{xx}$，得到题中右式；注意只有$A^2$乘$n/(n+1)$。标准化后为
> $$
> M=\frac{wZ_1^2+Z_2^2}{V/\nu},\qquad w=\frac1{n+1}.
> $$
> 若$q_{1-\alpha}(M)$是其分位数，则$\widehat\alpha+\widehat\beta x\pm\sqrt{q_{1-\alpha}(M)}S\sqrt{1+1/n+(x-\bar x)^2/S_{xx}}$同时覆盖均值曲线的概率为$1-\alpha$。分布可由独立$Z_1,Z_2,V$积分计算；也可用下面(d)近似。取较大的$2F_{2,\nu,\alpha}$则有严格可证明的保守覆盖，因为$M\le(Z_1^2+Z_2^2)/(V/\nu)$。
> **预测边界：** 此显示统计量只含回归系数估计误差，覆盖对象仍是条件均值曲线。不能单凭把分母换成预测标准误，就宣称同时覆盖每个$x$处无限多个独立未来响应；后者还有新观测误差，需另行定义联合预测对象。
> (d) 令$W=wZ_1^2+Z_2^2$，其均值$1+w$、方差$2(1+w^2)$。以$\kappa\chi_f^2$匹配前两矩，得
> $$
> f=\frac{(1+w)^2}{1+w^2},\qquad\kappa=\frac{1+w^2}{1+w}.
> $$
> 保留独立残差分母，$M\approx\kappa fF_{f,\nu}=(1+w)F_{f,\nu}$。因此近似平方半宽常数为$(1+w)F_{f,\nu,\alpha}$。当$\nu>4$时，该近似也匹配整个比值的均值与方差；$\nu\le4$时不能称比值有有限二阶矩，但对分子的匹配及保留分母的近似定义仍成立。无题设$n,\alpha$数值，所以这里给参数化公式，不虚构数值运行或覆盖检验。

## 相关概念

- [[03 - 线性代数与优化/概念/正规方程|正规方程]]
- [[02 - 数理统计/概念/区间估计|区间估计]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[01 - 概率论/概念/概率模型|概率模型]]

## 备注

- 统一来源见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011教材台账]]；原题位于[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=493|印刷462／PDF物理493]]。已对照原始页面核对完整英文、分题与定位，原题无星号。
- 解答为独立推导；引用的教材结论按source_refs核对，不使用答案册代替证明。
- 来源核对、归档与个人学习分别记录；verified只指所列来源核对范围，学习状态保持not-started。未实测Obsidian渲染。
