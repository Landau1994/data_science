---
title: 习题 P137：对称偏度与正态均匀Laplace峰度
topic: probability-theory
topic_label: 概率论
difficulty: intermediate
status: not-started
tags:
- exercise
- probability-theory
source: George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第2章习题2.28，印刷页65/66／PDF物理页96/97
source_id: DS011
source_chapter: 2
source_exercise: '2.28'
source_stars: 0
source_refs:
- DS011 Exercise 2.28，印刷65/66／PDF物理96/97
source_status: verified
solution_status: independently-derived
created: '2026-11-13'
---

# 习题 P137：对称偏度与正态均匀Laplace峰度

## 题目

### 英文原题

> [!question] 英文原题
> **2.28** Let $\mu_n$ denote the $n$th central moment of a random variable $X$. Two quantities of interest, in addition to the mean and variance, are
> $$
> \alpha_3=\frac{\mu_3}{(\mu_2)^{3/2}}\quad\text{and}\quad\alpha_4=\frac{\mu_4}{\mu_2^2}.
> $$
> The value $\alpha_3$ is called the skewness and $\alpha_4$ is called the kurtosis. The skewness measures the lack of symmetry in the pdf (see Exercise 2.26). The kurtosis, although harder to interpret, measures the peakedness or flatness of the pdf.
>
> (a) Show that if a pdf is symmetric about a point $a$, then $\alpha_3=0$.
>
> (b) Calculate $\alpha_3$ for $f(x)=e^{-x}$, $x\ge0$, a pdf that is skewed to the right.
>
> (c) Calculate $\alpha_4$ for each of the following pdfs and comment on the peakedness of each.
> $$
> \begin{aligned}
> f(x)&=\frac1{\sqrt{2\pi}}e^{-x^2/2},&-\infty<x<\infty\\
> f(x)&=\frac12,&-1<x<1\\
> f(x)&=\frac12e^{-|x|},&-\infty<x<\infty
> \end{aligned}
> $$
> Ruppert (1987) uses influence functions (Section 10.6.4) to further explore the meaning of kurtosis and Groeneveld (1991) uses them to explore skewness; see also Balanda and MacGillivray (1988) for more on the interpretation of $\alpha_4$.

### 中文转述

> [!question] 中文转述
> **原题2.28。** 令 $\mu_n$ 表示随机变量 $X$ 的 $n$ 阶中心矩. 除均值与方差外，另外两个值得关注的量是
>
> $$
> \alpha_3=\frac{\mu_3}{(\mu_2)^{3/2}},\qquad\alpha_4=\frac{\mu_4}{\mu_2^2}.
> $$
>
> $\alpha_3$ 称为偏度（skewness），$\alpha_4$ 称为峰度（kurtosis）. 偏度衡量密度的不对称性（见习题2.26）. 峰度虽然更难解释，但它衡量密度的尖峭或平坦程度.
>
> (a)  证明，如果一个密度关于点 $a$ 对称，则 $\alpha_3=0$.
>
> (b)  计算 $f(x)=e^{-x}$，$x\ge0$ 的 $\alpha_3$；这是一个右偏（skewed to the right）的密度.
>
> (c)  对下列每个密度计算 $\alpha_4$，并评论其尖峭程度.
>
> $$
> \begin{aligned}
> f(x)&=\frac1{\sqrt{2\pi}}e^{-x^2/2},&-\infty<x<\infty,\\
> f(x)&=\frac12,&-1<x<1,\\
> f(x)&=\frac12e^{-|x|},&-\infty<x<\infty.
> \end{aligned}
> $$
>
> Ruppert (1987) 用影响函数（influence function，第10.6.4节）进一步研究峰度的含义，Groeneveld (1991) 用它研究偏度；关于 $\alpha_4$ 的解释，还可参见 Balanda and MacGillivray (1988).

## 提示

> [!hint]- 提示
> 先确认所需中心矩有限且方差正；指数分布原点矩由反复分部积分为$r!$。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 偏度需要有限三阶绝对中心矩与$\mu_2>0$；峰度需要有限四阶中心矩与$\mu_2>0$。原题未明写这些存在条件，以下在定义有意义时作答。
>
> **(a)** 对称性及可积性给均值$a$，而$(x-a)^3f(x)$关于$a$是绝对可积奇函数，所以$\mu_3=0$，从而$\alpha_3=0$。仅有对称性而矩不存在（如Cauchy密度）时，不能宣称偏度等于0。
>
> **(b)** 对单位速率指数分布，$\mathrm EX^r=r!$，由$\int_0^\infty x^re^{-x}dx=r\int_0^\infty x^{r-1}e^{-x}dx$和初值1递推。于是均值1，$\mu_2=2-1=1$，$\mu_3=6-3\cdot2+3\cdot1-1=2$，故$\alpha_3=2$。
>
> **(c)** 三个密度的均值均为0：
>
> - 标准正态：利用$\phi'=-x\phi$分部积分得$\mathrm EX^{2r}=(2r-1)\mathrm EX^{2r-2}$，所以$\mu_2=1,\mu_4=3,\alpha_4=3$。
> - 均匀$(-1,1)$：$\mu_2=\int_0^1x^2dx=1/3$，$\mu_4=1/5$，故$\alpha_4=9/5$。
> - Laplace：偶矩为$\int_0^\infty x^{2r}e^{-x}dx=(2r)!$，所以$\mu_2=2,\mu_4=24,\alpha_4=6$。
>
> 以正态峰度3为基准，均匀密度较平，Laplace密度在中心更尖且尾部更重。峰度本质是标准化四阶矩，不能仅凭一个数字把所有密度的局部峰高或尾形完全排序；上述文字只解释这三个具体密度。

## 相关概念

- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/概率模型|概率模型]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 来源：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=96|印刷第65/66页／PDF物理第96/97页]]；版本与归档见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- (c)与文献讨论跨PDF96–97，均保留；引用文献只照录，并未另行检索。原题对称结论的矩存在条件另行说明。
- 已逐题查看原始页面，英文原题、全部分题与原附提示／引用照录；原题无星号。所列正文定位已经实读，题内补充、原文及独立推导分开。未查阅题内外部文献或答案册。
- 来源核对状态不表示个人学习完成；学习状态保持not-started。公式与链接检查不等于Obsidian实际渲染检查。
