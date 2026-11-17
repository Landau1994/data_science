---
title: "习题 ST138：逆高斯MLE勘误与均值和残差卡方的完整归纳"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "advanced"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第7章习题7.15，印刷页289／PDF物理页320"
source_id: "DS011"
source_chapter: 7
source_exercise: "7.15"
source_stars: 0
source_refs: ["DS011 Exercise 7.15，印刷289／PDF物理320"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST138：逆高斯MLE勘误与均值和残差卡方的完整归纳

## 题目

### 英文原题

> [!question] 英文原题
> **7.15** Let $X_1,X_2,\ldots,X_n$ be a sample from the inverse Gaussian pdf,
> $$
> f(x\mid\mu,\lambda)=\left(\frac\lambda{2\pi x^3}\right)^{1/2}\exp\{-\lambda(x-\mu)^2/(2\mu^2x)\},\qquad x>0.
> $$
> (a) Show that the ML estimators of $\mu$ and $\lambda$ are
> $$
> \widehat\mu_n=\bar X\quad\text{and}\quad\widehat\lambda_n=\frac n{\sum_i\frac1{X_i}-\frac1{\bar X}}.
> $$
> (b) Tweedie (1957) showed that $\widehat\mu_n$ and $\widehat\lambda_n$ are independent, $\widehat\mu_n$ having an inverse Gaussian distribution with parameters $\mu$ and $n\lambda$, and $n\lambda/\widehat\lambda_n$ having a $\chi^2_{n-1}$ distribution. Schwarz and Samantha (1991) give a proof of these facts using an induction argument.
>
> i. Show that $\widehat\mu_2$ has an inverse Gaussian distribution with parameters $\mu$ and $2\lambda$, $2\lambda/\widehat\lambda_2$ has a $\chi^2_1$ distribution, and they are independent.
>
> ii. Assume the result is true for $n=k$, and that we get a new, independent observation $x$. Establish the induction step used by Schwarz and Samantha (1991), and transform the pdf $f(x,\widehat\mu_k,\widehat\lambda_k)$ to $f(x,\widehat\mu_{k+1},\widehat\lambda_{k+1})$. Show that this density factors in the appropriate way, and that the result of Tweedie follows.

### 中文转述

> [!question] 中文转述
> **原题7.15。** 设$X_1,X_2,\ldots,X_n$为来自逆高斯pdf的样本：
>
> $$
> f(x\mid\mu,\lambda)=\left(\frac\lambda{2\pi x^3}\right)^{1/2}\exp\{-\lambda(x-\mu)^2/(2\mu^2x)\},\qquad x>0.
> $$
>
> (a)  说明$\mu$与$\lambda$的极大似然估计量为
>
> $$
> \widehat\mu_n=\bar X\qquad\text{及}\qquad\widehat\lambda_n=\frac n{\sum_i\frac1{X_i}-\frac1{\bar X}}.
> $$
>
> (b)  Tweedie（1957）说明，$\widehat\mu_n$和$\widehat\lambda_n$独立，$\widehat\mu_n$服从参数为$\mu$和$n\lambda$的逆高斯分布，$n\lambda/\widehat\lambda_n$服从$\chi_{n-1}^2$分布.Schwarz和Samantha（1991）用归纳论证证明了这些事实.
>
> i.  说明$\widehat\mu_2$服从参数为$\mu$与$2\lambda$的逆高斯分布，$2\lambda/\widehat\lambda_2$服从$\chi_1^2$分布，且二者独立.
>
> ii.  假设结果在$n=k$时成立，并得到一个新的独立观测$x$.建立Schwarz和Samantha（1991）所用的归纳步骤，把pdf $f(x,\widehat\mu_k,\widehat\lambda_k)$变换为$f(x,\widehat\mu_{k+1},\widehat\lambda_{k+1})$.说明该密度以适当方式分解，从而得到Tweedie的结果.

## 提示

> [!hint]- 提示
> 先修正从似然真正导出的残差$D_n$，再把一块均值与一个新观测合并。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 设$\mu,\lambda>0$。原(a)的分母漏了$n$，因而原样公式和(b)不能同时成立。以下先从似然推出修正，再对修正后的估计完成全部归纳。
>
> **(a)** 记$S=\sum_i x_i$、$H=\sum_i1/x_i$，则
> $$
> \ell=\frac n2\log\lambda-\frac\lambda2\left(S/\mu^2-2n/\mu+H\right)+C.
> $$
> 括号内关于$u=1/\mu$的二次式$Su^2-2nu+H$在$u=n/S$唯一最小，故$\widehat\mu_n=\bar X$。代入得到$D_n:=H-n/\bar X\ge0$，非全等样本时严格为正，$\ell_p=(n/2)\log\lambda-\lambda D_n/2+C$，所以
> $$
> \widehat\lambda_n=n/D_n=\frac n{\sum_i1/X_i-n/\bar X}.
> $$
> 全等样本$D_n=0$时似然随$\lambda\to\infty$无界；$n=1$必如此。$n\ge2$连续样本下全等事件概率零。
>
> **两块合并密度的计算。** 设相互独立的$x\sim IG(\mu,\lambda)$与$y\sim IG(\mu,k\lambda)$，其中$k\ge1$。定义
> $$
> m=\frac{x+ky}{k+1},\quad
> H=\frac1x+\frac{k}{y}-\frac{k+1}{m}
> =\frac{k(x-y)^2}{xy(x+ky)}\ge0.
> $$
> 原指数中的平方项满足
> $$
> \frac{(x-\mu)^2}{\mu^2x}+k\frac{(y-\mu)^2}{\mu^2y}
> =(k+1)\frac{(m-\mu)^2}{\mu^2m}+H.
> $$
> 令$t=x/[(k+1)m]\in(0,1)$，则$y=(k+1)m(1-t)/k$，$|\partial(x,y)/\partial(m,t)|=(k+1)^2m/k$。联合密度为
> $$
> \frac{k\lambda}{2\pi(k+1)m^2}[t(1-t)]^{-3/2}
> \exp\left[-\frac{(k+1)\lambda(m-\mu)^2}{2\mu^2m}-\frac{\lambda H}{2}\right].
> $$
> 写$A=(k+1)mH$，方程$[1-(k+1)t]^2=A t(1-t)$有两支$t_-,t_+$（$H>0$），它们是$[(k+1)^2+A]t^2-[2(k+1)+A]t+1=0$的根。由根的和与积，直接得到
> $$
> \sum_{\pm}\frac1{1+(k-1)t_\pm}=\frac{k+1}{k}.
> $$
> 另一方面$u=[1-(k+1)t]/\sqrt{t(1-t)}$满足$|du/dt|=[1+(k-1)t]/[2\{t(1-t)\}^{3/2}]$，且$|u|=\sqrt{(k+1)mH}$。所以两分支的Jacobian相加后，上述联合密度变成
> $$
> f_{m,H}(m,h)=
> \underbrace{\sqrt{\frac{(k+1)\lambda}{2\pi m^3}}e^{-(k+1)\lambda(m-\mu)^2/(2\mu^2m)}}_{IG(\mu,(k+1)\lambda)\text{密度}}
> \underbrace{\sqrt{\frac\lambda{2\pi h}}e^{-\lambda h/2}}_{\lambda H\sim\chi_1^2},\quad m,h>0.
> $$
> 这同时证明$m$与$H$独立。
>
> **(b)i：起始步$n=2$。** 取$k=1$，$y=X_1,x=X_2$，则$m=\bar X_2$、$H=D_2$。刚才的密度分解直接给$\bar X_2\sim IG(\mu,2\lambda)$、$\lambda D_2=2\lambda/\widehat\lambda_2\sim\chi_1^2$并独立。$D_2\mapsto\widehat\lambda_2=2/D_2$为一一变换，故两估计量也独立。
>
> **(b)ii：归纳步。** 假设$y=\bar X_k$与$d=D_k=k/\widehat\lambda_k$独立，分别为$IG(\mu,k\lambda)$及$\lambda d\sim\chi^2_{k-1}$；新样本$x$独立于它们。直接变换到$(x,m,v)$，其中$m=\bar X_{k+1}$、$v=D_{k+1}=d+H(x,y)$，逆变换$y=((k+1)m-x)/k,d=v-H$的Jacobian绝对值为$(k+1)/k$，所以
> $$
> f_{x,m,v}=\frac{k+1}{k} f_{IG}(x;\mu,\lambda)f_{IG}(y;\mu,k\lambda)
> f_{D_k}(v-H)\mathbf1\{v>H,\ 0<x<(k+1)m\}.
> $$
> 这就是题目要求保留$x$的三维变换；若改用$\widehat\lambda_{k+1}$再乘$|dv/d\widehat\lambda_{k+1}|=(k+1)/\widehat\lambda_{k+1}^2$。利用前面两分支计算对$x$积分，得到
> $$
> f_{m,v}=f_{IG}(m;\mu,(k+1)\lambda)
> \int_0^v f_{\Gamma(1/2,\,2/\lambda)}(h)
> f_{\Gamma((k-1)/2,\,2/\lambda)}(v-h)\,dh.
> $$
> 卷积积分用$h=vs$化为Beta积分，等于$\Gamma(k/2,2/\lambda)$密度。因此$\lambda D_{k+1}\sim\chi_k^2$且与$\bar X_{k+1}$独立，完成全部归纳。整个证明只用了变量变换、分支Jacobian求和与Gamma卷积，没有借用题引论文的结论。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=320|印刷第289页／PDF物理第320页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 原(a)漏n及Samantha原拼写照录；所有结论明确针对修正后的MLE。与[[02 - 数理统计/习题/习题 ST107 - 逆高斯样本完备充分性与原卡方统计量的修正|习题6.27归档]]衔接，但本题独立给出两分支密度计算及完整归纳。
- 英文原文、中文转述与本库独立解答分别保留；实际核对正文位置列于`source_refs`。题内文献引用不表示已查阅其原文。`source_status: verified`只指本题及所列位置的核对范围，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
