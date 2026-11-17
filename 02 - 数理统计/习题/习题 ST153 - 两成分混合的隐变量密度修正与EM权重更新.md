---
title: "习题 ST153：两成分混合的隐变量密度修正与EM权重更新"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "advanced"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第7章习题7.30，印刷页292／PDF物理页323"
source_id: "DS011"
source_chapter: 7
source_exercise: "7.30"
source_stars: 0
source_refs: ["DS011 Exercise 7.30，印刷292／PDF物理323"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST153：两成分混合的隐变量密度修正与EM权重更新

## 题目

### 英文原题

> [!question] 英文原题
> **7.30** The EM algorithm is useful in a variety of situations, and the definition of “missing data” can be stretched to accommodate many different models. Suppose that we have a mixture density $pf(x)+(1-p)g(x)$, where $p$ is unknown. If we observe $\mathbf X=(X_1,X_2,\ldots,X_n)$, the sample density is
> $$
> \prod_{i=1}^n[pf(x_i)+(1-p)g(x_i)],
> $$
> which could be difficult to deal with. (Actually, a mixture of two is not terrible, but consider what the likelihood would look like with a mixture $\sum_{i=1}^k p_i f_i(x)$, for large $k$.)
>
> The EM solution is to augment the observed (or incomplete) data with $\mathbf Z=(Z_1,Z_2,\ldots,Z_n)$, where $Z_i$ tells which component of the mixture $X_i$ came from. That is,
> $$
> X_i\mid z_i=1\sim f(x_i)\quad\text{and}\quad X_i\mid z_i=0\sim g(x_i),
> $$
> and $P(Z_i=1)=p$.
>
> (a) Show that the joint density of $(\mathbf X,\mathbf Z)$ is given by $\prod_{i=1}^n[pf(x_i)^{z_i}][(1-p)g(x_i)^{1-z_i}]$.
>
> (b) Show that the missing data distribution, the distribution of $Z_i\mid x_i,p$ is Bernoulli with success probability $pf(x_i)/(pf(x_i)+(1-p)g(x_i))$.
>
> (c) Calculate the expected complete-data log likelihood, and show that the EM sequence is given by
> $$
> \widehat p^{(r+1)}=\frac1n\sum_{i=1}^n
> \frac{\widehat p^{(r)}f(x_i)}{\widehat p^{(r)}f(x_i)+(1-\widehat p^{(r)})g(x_i)}.
> $$

### 中文转述

> [!question] 中文转述
> **原题7.30。** EM算法适用于多种情形，“缺失数据”的定义也可以扩展，以容纳许多不同模型.假设混合密度为$pf(x)+(1-p)g(x)$，其中$p$未知.若观测$\boldsymbol X=(X_1,X_2,\ldots,X_n)$，则样本密度为
>
> $$
> \prod_{i=1}^n[pf(x_i)+(1-p)g(x_i)],
> $$
>
> 这可能难以处理.（其实，两种分布的混合还不算太糟；但想想当$k$很大时，混合$\sum_{i=1}^kp_if_i(x)$的似然会是什么样.）
>
> EM解法是用$\boldsymbol Z=(Z_1,Z_2,\ldots,Z_n)$增广已观测（不完全）数据，其中$Z_i$说明$X_i$来自哪个混合成分.即
>
> $$
> X_i\mid z_i=1\sim f(x_i)\qquad\text{且}\qquad X_i\mid z_i=0\sim g(x_i),
> $$
>
> 并且$P(Z_i=1)=p$.
>
> (a)  说明$(\boldsymbol X,\boldsymbol Z)$的联合密度为$\prod_{i=1}^n[pf(x_i)^{z_i}][(1-p)g(x_i)^{1-z_i}]$.
>
> (b)  说明缺失数据分布，即$Z_i\mid x_i,p$的分布，是成功概率为$pf(x_i)/(pf(x_i)+(1-p)g(x_i))$的Bernoulli分布.
>
> (c)  计算期望完全数据对数似然，并说明EM序列为
>
> $$
> \widehat p^{(r+1)}=\frac1n\sum_{i=1}^n\frac{\widehat p^{(r)}f(x_i)}{\widehat p^{(r)}f(x_i)+(1-\widehat p^{(r)})g(x_i)}.
> $$

## 提示

> [!hint]- 提示
> 成分标签的概率也必须被其对应指示变量乘幂。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 假设$f,g$是已知归一化密度，样本独立，$0\le p\le1$。
>
> **(a)** 原式把$p$与$1-p$放在$z_i$幂之外，因而不正确。正确联合密度为
> $$
> f(\mathbf x,\mathbf z\mid p)=\prod_i[pf(x_i)]^{z_i}[(1-p)g(x_i)]^{1-z_i},\quad z_i\in\{0,1\}.
> $$
> 对每个$z_i$求和确实恢复$pf(x_i)+(1-p)g(x_i)$。反之，原式$n=1$时对$z$求和再积分只得到$2p(1-p)$，一般不为1，所以不能作为联合密度。
>
> **(b)** 由Bayes公式，对正边际密度的$x_i$，
> $$
> w_i(p):=P(Z_i=1\mid x_i,p)=\frac{pf(x_i)}{pf(x_i)+(1-p)g(x_i)}.
> $$
> 两个状态概率和为1，故条件分布为Bernoulli；其余观察的独立性使对整份样本条件化也给相同责任权重（responsibility）。
>
> **(c)** 对正确完全密度取对数再对$Z_i$条件期望，
> $$
> Q(p\mid p_r)=\sum_i\{w_i(p_r)\log p+[1-w_i(p_r)]\log(1-p)\}+C_r.
> $$
> 这是分数成功数$W_r=\sum_iw_i(p_r)$的二项对数似然，其导数$W_r/p-(n-W_r)/(1-p)$，内点唯一极大值$W_r/n$；$W_r=0,n$时在闭边界0或1。由此得到原(c)更新式。若$f=g$，似然对$p$恒定、参数不可识别，更新保持初值；若某观测在当前混合密度下为零，则该步条件概率未定义，须换有效初值。一般EM单调性不等于每个模型都存在唯一可识别全局极值。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=323|印刷第292页／PDF物理第323页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 原(a)幂的作用范围错误照录；用归一化反例说明，再按正确模型推导(b)(c)。
- 英文原文、中文转述与本库独立解答分别保留；实际核对正文位置列于`source_refs`。题内文献引用不表示已查阅其原文。`source_status: verified`只指本题及所列位置的核对范围，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
