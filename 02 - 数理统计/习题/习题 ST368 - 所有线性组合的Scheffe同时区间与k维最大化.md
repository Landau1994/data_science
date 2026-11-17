---
title: "习题 ST368：所有线性组合的Scheffe同时区间与k维最大化"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "advanced"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第11章习题11.14，印刷页458／PDF物理页489"
source_id: "DS011"
source_chapter: 11
source_exercise: "11.14"
source_stars: 0
source_refs: ["DS011 Exercise 11.14，印刷458／PDF物理489", "DS011 Scheffé对比同时区间定理11.2.10，印刷432／PDF物理463"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST368：所有线性组合的Scheffe同时区间与k维最大化

## 题目

### 英文原题

> [!question] 英文原题
> **11.14** The Scheffé simultaneous interval procedure actually works for all linear combinations, not just contrasts. Show that under the oneway ANOVA assumptions, if $M=\sqrt{kF_{k,N-k,\alpha}}$ (note the change in the numerator degrees of freedom), then the probability is $1-\alpha$ that
> $$
> \sum_{i=1}^k a_i\bar Y_{i\cdot}-M\sqrt{S_p^2\sum_{i=1}^k a_i^2/n_i}
> \le\sum_{i=1}^k a_i\theta_i\le
> \sum_{i=1}^k a_i\bar Y_{i\cdot}+M\sqrt{S_p^2\sum_{i=1}^k a_i^2/n_i},
> $$
> simultaneously for all $\mathbf a=(a_1,\ldots,a_k)$. (It is probably easiest to proceed by first establishing, in the spirit of Lemma 11.2.7, that if $v_1,\ldots,v_k$ are constants and $c_1,\ldots,c_k$ are positive constants, then
> $$
> \max_{\mathbf a}\left\{\frac{(\sum_{i=1}^ka_iv_i)^2}{\sum_{i=1}^ka_i^2/c_i}\right\}=\sum_{i=1}^kc_iv_i^2.
> $$
> The proof of Theorem 11.2.10 can then be adapted to establish the result.)

### 中文转述

> [!question] 中文转述
> **原题11.14。** Scheffé同时区间方法实际上适用于所有线性组合，不仅适用于对比. 证明：在单因素ANOVA假设下，若$M=\sqrt{kF_{k,N-k,\alpha}}$（注意分子自由度的改变），则下列不等式对所有$\boldsymbol a=(a_1,\ldots,a_k)$同时成立的概率为$1-\alpha$：
>
> $$
> \begin{aligned}
> \sum_{i=1}^ka_i\bar Y_{i\cdot}-M\sqrt{S_p^2\sum_{i=1}^k\frac{a_i^2}{n_i}}
> &\le\sum_{i=1}^ka_i\theta_i\\
> &\le\sum_{i=1}^ka_i\bar Y_{i\cdot}+M\sqrt{S_p^2\sum_{i=1}^k\frac{a_i^2}{n_i}}.
> \end{aligned}
> $$
>
> （最容易的做法可能是，仿照引理11.2.7先证明：若$v_1,\ldots,v_k$为常数，$c_1,\ldots,c_k$为正常数，则
>
> $$
> \max_{\boldsymbol a}\left\{\frac{(\sum_{i=1}^ka_iv_i)^2}{\sum_{i=1}^ka_i^2/c_i}\right\}=\sum_{i=1}^kc_iv_i^2.
> $$
>
> 然后调整定理11.2.10的证明，建立所需结果.）

## 提示

> [!hint]- 提示
> 取消对比的和为零约束，最大化空间便保留全部k个正态方向。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 最大化时排除使分母为0的$\mathbf a=0$，其区间本身恒等成立。Cauchy–Schwarz给
> $$
> \left(\sum_i a_i v_i\right)^2
> =\left(\sum_i\frac{a_i}{\sqrt{c_i}}\sqrt{c_i}v_i\right)^2
> \le\left(\sum_i a_i^2/c_i\right)\left(\sum_i c_i v_i^2\right).
> $$
> 若$\mathbf v\ne0$，取$a_i=c_i v_i$即达到上界；若$\mathbf v=0$，所有非零向量均给0。因此提示恒等式成立。
>
> 在独立正态同方差ANOVA下取$v_i=\bar Y_i-\theta_i$、$c_i=n_i$，所有线性组合区间同时覆盖等价于
> $$
> \frac{\sum_i n_i(\bar Y_i-\theta_i)^2}{S_p^2}\le M^2.
> $$
> 分子除以$\sigma^2$为$k$个独立标准正态平方和$\chi_k^2$；分母$S_p^2/\sigma^2=\chi_{N-k}^2/(N-k)$且独立，所以比值服从$kF_{k,N-k}$。选$M^2=kF_{k,N-k,\alpha}$便得**精确**同时覆盖概率$1-\alpha$。不限制系数和为零时保留了总体均值方向，因此分子自由度从对比空间的$k-1$变为$k$。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=489|印刷第458页／PDF物理第489页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 英文原文、中文转述与本库独立解答分别保留；实际核对正文位置列于`source_refs`。题内文献引用不表示已查阅其原文。`source_status: verified`只指本题及所列位置的核对范围，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
