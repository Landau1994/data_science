---
title: "习题 ST117：尼罗河模型中比率统计量的Fisher信息损失"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "advanced"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第6章习题6.37，印刷页248／PDF物理页279"
source_id: "DS011"
source_chapter: 6
source_exercise: "6.37"
source_stars: 0
source_refs: ["DS011 Exercise 6.37，印刷248／PDF物理279", "DS011 Exercise 6.37，印刷248／PDF279"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST117：尼罗河模型中比率统计量的Fisher信息损失

## 题目

### 英文原题

> [!question] 英文原题
> **6.37** Joshi and Nabar (1989) examine properties of linear estimators for the parameter in the so-called “Problem of the Nile,” where $(X,Y)$ has the joint density
> $$
> f(x,y\mid\theta)=\exp\{-(\theta x+y/\theta)\},\qquad x>0,\quad y>0.
> $$
> (a) For an iid sample of size $n$, show that the Fisher information is $I(\theta)=2n/\theta^2$.
>
> (b) For the estimators
> $$
> T=\sqrt{\sum Y_i/\sum X_i}\qquad\text{and}\qquad U=\sqrt{\sum X_i\sum Y_i},
> $$
> show that
>   (i) the information in $T$ alone is $[2n/(2n+1)]I(\theta)$.
>   (ii) the information in $(T,U)$ is $I(\theta)$.
>   (iii) $(T,U)$ is jointly sufficient but not complete.

### 中文转述

> [!question] 中文转述
> **原题6.37。**
> Joshi和Nabar（1989）研究了所谓“尼罗河问题”（Problem of the Nile）中参数的线性估计量的性质，其中$(X,Y)$具有联合密度
>
> $$
> f(x,y\mid\theta)=\exp\{-(\theta x+y/\theta)\},\qquad x>0,\quad y>0.
> $$
>
> (a)  对样本量为$n$的独立同分布样本，说明Fisher信息为$I(\theta)=2n/\theta^2$.
>
> (b)  对估计量
>
> $$
> T=\sqrt{\sum Y_i/\sum X_i}\qquad\text{及}\qquad U=\sqrt{\sum X_i\sum Y_i},
> $$
>
> 说明
>
> (i)  仅$T$所含的信息为$[2n/(2n+1)]I(\theta)$.
>
> (ii)  $(T,U)$所含的信息为$I(\theta)$.
>
> (iii)  $(T,U)$联合充分，但不完备.

## 提示

> [!hint]- 提示 1
> 先把两个总和变成独立Gamma变量，再用比率和乘积的Jacobian。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 教材输入与补充假设另行标明。
>
> 密度归一化要求$\theta>0$。令$A=\sum_iX_i$、$B=\sum_iY_i$。单个联合密度分解为$\theta e^{-\theta x}\cdot\theta^{-1}e^{-y/\theta}$，所以$A\sim\operatorname{Gamma}(n,\text{rate }\theta)$、$B\sim\operatorname{Gamma}(n,\text{scale }\theta)$，且相互独立。
>
> **(a)** 对数似然的参数部分为$-\theta A-B/\theta$，score为$-A+B/\theta^2$。利用$EA=n/\theta$、$EB=n\theta$及相应方差，score均值为0，
> $$
> I(\theta)=\operatorname{Var}(-A+B/\theta^2)
> =\frac n{\theta^2}+\frac{n\theta^2}{\theta^4}
> =\frac{2n}{\theta^2}.
> $$
>
> **(b)(i)** 变换$A=U/T$、$B=UT$的Jacobian为$2U/T$，故
> $$
> f_{T,U}(t,u)=\frac{2u^{2n-1}}{\Gamma(n)^2t}
> \exp[-u(\theta/t+t/\theta)],\qquad t,u>0.
> $$
> 对$u$积分得
> $$
> f_T(t)=\frac{2\Gamma(2n)}{\Gamma(n)^2}
> \frac{\theta^{2n}t^{2n-1}}{(\theta^2+t^2)^{2n}}.
> $$
> 其score为$\frac{2n}{\theta}(2W-1)$，其中$W=t^2/(\theta^2+t^2)$。由于$\theta A$、$B/\theta$独立且同为Gamma$(n,\text{scale }1)$，$W$服从Beta$(n,n)$。由Beta积分比，
> $$
> EW=\frac12,\quad EW^2=\frac{n(n+1)}{2n(2n+1)},\quad
> E(2W-1)^2=\frac1{2n+1}.
> $$
> 因此
> $$
> I_T(\theta)=\frac{4n^2}{(2n+1)\theta^2}
> =\frac{2n}{2n+1}I(\theta).
> $$
>
> **(b)(ii)** $(T,U)$与$(A,B)$一一对应，其联合密度score为$-U/T+UT/\theta^2=-A+B/\theta^2$，故信息完整保留为$I(\theta)$，不是仅凭“变换”一词省略Jacobian或参数独立性检查。
>
> **(b)(iii)** 原样本联合密度只通过$(A,B)$依赖参数，所以$(T,U)$联合充分。另一方面
> $$
> U=\sqrt{(\theta A)(B/\theta)}
> $$
> 分布不含$\theta$且非退化。令
> $$
> c=EU=\left[\frac{\Gamma(n+1/2)}{\Gamma(n)}\right]^2<\infty.
> $$
> 该期望由两个独立Gamma积分相乘得到。于是$g(T,U)=U-c$对所有$\theta$期望为0却非几乎处处为0，证明不完备。正是这个辅助成分使联合充分量仍可不完备。

## 相关概念

- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[01 - 概率论/概念/概率模型|概率模型]]

## 备注

- 统一来源见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011教材台账]]；原题位于[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=279|印刷248／PDF物理279]]。已对照原始页面核对完整英文、分题与定位，原题无星号。
- 题内文献只保留原引用；Fisher信息与不完备反例均为独立计算。未将参数相关变换当作实际统计量，只用它识别分布与期望。
- 来源核对、归档与个人学习分别记录；verified只指所列来源核对范围，学习状态保持not-started。未实测Obsidian渲染。
