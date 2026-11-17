---
title: "习题 ST111：Basu定理简化正态方差与Gamma条件期望计算"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "advanced"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第6章习题6.31，印刷页247／PDF物理页278"
source_id: "DS011"
source_chapter: 6
source_exercise: "6.31"
source_stars: 0
source_refs: ["DS011 Exercise 6.31，印刷247／PDF物理278", "DS011 Theorems 6.2.24–6.2.25，印刷233–234／PDF264–265"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST111：Basu定理简化正态方差与Gamma条件期望计算

## 题目

### 英文原题

> [!question] 英文原题
> **6.31** Boos and Hughes-Oliver (1998) detail a number of instances where application of Basu's Theorem can simplify calculations. Here are a few.
>
> (a) Let $X_1,X_2,\ldots,X_n$ be iid $n(\mu,\sigma^2)$, where $\sigma^2$ is known.
>
>   (i) Show that $\bar X$ is complete sufficient for $\mu$ and $S^2$ is ancillary. Hence by Basu's Theorem $\bar X$ and $S^2$ are independent.
>
>   (ii) Show that this independence carries over even if $\sigma^2$ is unknown, as knowledge of $\sigma^2$ has no bearing on the distributions. (Compare this proof to the more involved Theorem 5.3.1(a).)
>
> (b) A Monte Carlo swindle is a technique for improving variance estimates. Suppose that $X_1,X_2,\ldots,X_n$ are iid $N(\mu,\sigma^2)$, and that we want to compute the variance of the median, $M$.
>
>   (i) Show that $\operatorname{Var}(M)=\operatorname{Var}(M-\bar X)+\operatorname{Var}(\bar X)$; thus, we only have to simulate the $\operatorname{Var}(M-\bar X)$ piece of $\operatorname{Var}(M)$ (since we know that $\operatorname{Var}(\bar X)=\sigma^2/n$).
>
>   (ii) Show that the swindle estimate is more precise by showing that the asymptotic variance of $M$ is approximately $2[\operatorname{Var}(M)]^2/(N-1)$ and that of $M-\bar X$ is approximately $2[\operatorname{Var}(M-\bar X)]^2/(N-1)$, where $N$ is the number of Monte Carlo samples.
>
> (c) (i) If $X/Y$ and $Y$ are independent random variables, show that
> $$
> E\left(\frac XY\right)^k=\frac{E(X^k)}{E(Y^k)}.
> $$
>
>   (ii) Use this result, and Basu's Theorem, to show that if $X_1,X_2,\ldots,X_n$ are iid gamma$(\alpha,\beta)$, where $\alpha$ is known, then
> $$
> E\left(X_{(i)}\,\middle|\,\sum_iX_i\right)
> =\sum_iX_i\,\frac{E(X_{(i)})}{E(\sum_iX_i)}.
> $$

### 中文转述

> [!question] 中文转述
> **原题6.31。**
> Boos和Hughes-Oliver（1998）详述了应用Basu定理简化计算的若干实例.下面列出其中几个.
>
> (a)  设$X_1,X_2,\ldots,X_n$独立同分布于$n(\mu,\sigma^2)$，其中$\sigma^2$已知.
>
> (i)  说明$\bar X$对于$\mu$完备充分，而$S^2$是辅助统计量.因而由Basu定理，$\bar X$与$S^2$独立.
>
> (ii)  说明即使$\sigma^2$未知，这一独立性仍成立，因为是否知道$\sigma^2$不影响这些分布.（将此证明与较为复杂的定理5.3.1(a)比较.）
>
> (b)  蒙特卡罗巧计（Monte Carlo swindle）是一种改进方差估计的技巧.设随机变量$X_1,X_2,\ldots,X_n$独立同分布于$N(\mu,\sigma^2)$，我们希望计算中位数$M$的方差.
>
> (i)  说明$\operatorname{Var}(M)=\operatorname{Var}(M-\bar X)+\operatorname{Var}(\bar X)$；因此，对于$\operatorname{Var}(M)$，我们只需模拟其中的$\operatorname{Var}(M-\bar X)$部分（因为已知$\operatorname{Var}(\bar X)=\sigma^2/n$）.
>
> (ii)  通过说明$M$的渐近方差约为$2[\operatorname{Var}(M)]^2/(N-1)$，而$M-\bar X$的渐近方差约为$2[\operatorname{Var}(M-\bar X)]^2/(N-1)$，证明巧计估计更为精确，其中$N$是蒙特卡罗样本数.
>
> (c)  
>
> (i)  若$X/Y$与$Y$是独立随机变量，证明
>
> $$
> E\left(\frac XY\right)^k=\frac{E(X^k)}{E(Y^k)}.
> $$
>
> (ii)  利用该结果及Basu定理说明，若$X_1,X_2,\ldots,X_n$独立同分布于$\operatorname{gamma}(\alpha,\beta)$，其中$\alpha$已知，则
>
> $$
> E\left(X_{(i)}\,\middle|\,\sum_iX_i\right)=\sum_iX_i\frac{E(X_{(i)})}{E(\sum_iX_i)}.
> $$

## 提示

> [!hint]- 提示 1
> 固定一个未知量再应用Basu，不等于把辅助性推广到整个双参数族。模拟方差估计的精度需要四阶矩。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 教材输入与补充假设另行标明。
>
> 涉及通常无偏样本方差$S^2$的(a)取$n\ge2$；(b)中比较由Monte Carlo重复得到的样本方差时取重复次数$N\ge2$。
>
> **(a)(i)** 固定$\sigma^2>0$时，正态联合密度对$\mu$的自然参数为$\mu/\sigma^2\in\mathbb R$，自然统计量为$\sum_iX_i$，故$\bar X$充分且完备。$S^2$在平移下不变，分布不含$\mu$，所以辅助。由Basu定理独立。
>
> **(a)(ii)** 前一结论对每个固定的正数$\sigma^2$均成立，故对任一参数对$(\mu,\sigma^2)$成立。未知性是实验者的信息状态，不会改变这个联合分布恒等式。不能因此反说$S^2$在整个双参数族中是辅助的。
>
> **(b)(i)** 通常中位数平移等变，$A=M-\bar X$对$\mu$辅助。固定$\sigma^2$应用Basu，$A$与$B=\bar X$独立，故$\operatorname{Var}(A+B)=\operatorname{Var}A+\operatorname{Var}B$。中位数与残差的正态对称性还给出$EA=0$；有限样本的所有所需矩均存在。
>
> **(b)(ii) 原措辞与近似边界。** 随模拟次数$N$变化的是“用$N$次独立模拟所得的样本方差估计量”的方差，不是$M$本身的方差；而$2v^2/(N-1)$对被模拟统计量正态时精确，一般非正态时不能不检查四阶矩。下面给出无需将中位数当成正态的严格精度比较。
>
> 对任意具有方差$v$、四阶中心矩$\mu_4$的独立重复$Z_1,\ldots,Z_N$，其无偏样本方差$V_Z$满足
> $$
> \operatorname{Var}(V_Z)=\frac1N\left[\mu_4-\frac{N-3}{N-1}v^2\right].
> $$
> 可由$V_Z=[N(N-1)]^{-1}\sum_{r<s}(Z_r-Z_s)^2$验证：单个平方差的方差为$2\mu_4+2v^2$，共享一个下标的两个平方差协方差为$\mu_4-v^2$，无公共下标则独立；分别计数$\binom N2$与$3\binom N3$后即得上式。
>
> 记$v_A=\operatorname{Var}A$、$v_B=\sigma^2/n>0$。独立正态$B-\mu$与$A$相加给出
> $$
> v_M=v_A+v_B,\qquad
> \mu_4(M)=\mu_4(A)+6v_Av_B+3v_B^2.
> $$
> 故普通估计$V_M$与巧计估计$V_A+v_B$的方差之差为
> $$
> \operatorname{Var}(V_M)-\operatorname{Var}(V_A+v_B)
> =\frac{2(2v_Av_B+v_B^2)}{N-1}>0.
> $$
> 这是精确改进结论。若另采用$M$及$A$近似正态的渐近近似，则分别将$\mu_4\approx3v^2$代入才得到原题的两个近似公式；本题没有实际运行模拟，不能将推导写成模拟结果。
>
> **(c)(i)** 需$Y\ne0$几乎处处、相应幂与绝对矩存在，以及$E(Y^k)\ne0$。令$R=X/Y$，则$X^k=R^kY^k$，独立性给出$EX^k=ER^k\,EY^k$，再除得所求。若$EY^k=0$，原比值可能是$0/0$；例如$X=Y$为对称$\pm1$变量、$k=1$，左边为1而右边未定义。因此补充条件必不可少。
>
> **(c)(ii)** $S$是已知形状Gamma尺度族的完备充分统计量；$R=X_{(i)}/S$在尺度变化下不变，故对$\beta$辅助。Basu给出$R$与$S$独立。由$X_{(i)}=RS$、$ES=n\alpha\beta>0$，得$ER=EX_{(i)}/ES$，再条件化得到$E(X_{(i)}\mid S)=S ER$。所有一阶矩均有限，因为$0<X_{(i)}\le S$。

## 相关概念

- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[01 - 概率论/概念/概率模型|概率模型]]

## 备注

- 统一来源见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011教材台账]]；原题位于[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=278|印刷247／PDF物理278]]。已对照原始页面核对完整英文、分题与定位，原题无星号。
- 保留原(b)(ii)的措辞；解答区分统计量方差与方差估计量的方差，并给出无需近似正态的精确比较。题内文献未另行查阅，未声称实际模拟。
- 来源核对、归档与个人学习分别记录；verified只指所列来源核对范围，学习状态保持not-started。未实测Obsidian渲染。
