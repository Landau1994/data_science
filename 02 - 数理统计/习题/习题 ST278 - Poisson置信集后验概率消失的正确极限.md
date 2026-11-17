---
title: "习题 ST278：Poisson置信集后验概率消失的正确极限"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第9章习题9.30，印刷页369／PDF物理页400"
source_id: "DS011"
source_chapter: 9
source_exercise: "9.30"
source_stars: 0
source_refs: ["DS011 Exercise 9.30，印刷369／PDF物理400", "DS011 (9.2.19)–(9.2.21)，印刷352–354／PDF物理383–385"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST278：Poisson置信集后验概率消失的正确极限

## 题目

### 英文原题

> [!question] 英文原题
> **9.30** Complete the credible probability calculation needed in Example 9.2.17.
> (a) Assume that $a$ is an integer, and show that $T=\frac{2(nb+1)}b\lambda\sim\chi^2_{2(a+\Sigma x)}$.
> (b) Show that
> $$
> \frac{\chi^2_\nu-\nu}{\sqrt{2\nu}}\to n(0,1)
> $$
> as $\nu\to\infty$. (Use moment generating functions. The limit is difficult to evaluate – take logs and then do a Taylor expansion. Alternatively, see Example 12.6.8.)
> (c) Standardize the random variable $T$ of part (a), and write the credible probability (9.2.21) in terms this variable. Show that the standardized lower cutoff point $\to\infty$ as $\Sigma x_i\to\infty$, and hence the credible probability goes to zero.

### 中文转述

> [!question] 中文转述
> **原题9.30。**
> 完成例9.2.17所需的可信概率计算.
>
> (a) 假设$a$是整数，证明$T=2(nb+1)\lambda/b\sim\chi^2_{2(a+\sum x)}$.
>
> (b)  证明当$\nu\to\infty$时，
>
> $$
> \frac{\chi^2_\nu-\nu}{\sqrt{2\nu}}\to\mathrm n(0,1).
> $$
>
> （使用矩母函数. 这个极限难以计算：先取对数，再作Taylor展开. 或参见例12.6.8.）
>
> (c)  将(a)中的随机变量$T$标准化，并用这个变量写出可信概率式9.2.21. 证明当$\sum x_i\to\infty$时，标准化后的下侧临界点$\to\infty$，从而可信概率趋于零.

## 提示

> [!hint]- 提示
> 先把Gamma后验变成卡方，再将区间的两个端点分别减自由度并除以其标准差；对题称的极限方向也要实际核算。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 教材输入与补充假设另行标明。
>
> (a) 先验$\lambda\sim\mathrm{Gamma}(a,b)$为尺度参数$b$，Poisson似然给$\lambda\mid x\sim\mathrm{Gamma}(a+s,b/(nb+1))$，$s=\sum x_i$。故$T=2(n+1/b)\lambda\sim\chi^2_{2(a+s)}$。实际上$a>0$即可，不需要整数。
> (b) 对$Z_\nu=(\chi^2_\nu-\nu)/\sqrt{2\nu}$，对固定$t$有
> $$
> \log M_{Z_\nu}(t)=-t\sqrt{\nu/2}-\frac\nu2\log(1-t\sqrt{2/\nu})=\frac{t^2}2+O(\nu^{-1/2}),
> $$
> 其中线性项相消，由矩母函数连续性定理得标准正态极限。
> (c) 写$q_{v,u}$为下侧分位，令$r=(nb+1)/(nb)>1$。频率区间为$[q_{2s,\alpha/2}/(2n),q_{2(s+1),1-\alpha/2}/(2n)]$，所以后验概率为
> $$
> P\!\left\{\frac{rq_{2s,\alpha/2}-2(s+a)}{2\sqrt{s+a}}\le Z_{2(s+a)}\le
> \frac{rq_{2(s+1),1-\alpha/2}-2(s+a)}{2\sqrt{s+a}}\right\}.
> $$
> 由(b)的分位数渐近$q_{2s,u}=2s+2\sqrt s\,\Phi^{-1}(u)+o(\sqrt s)$，下端为$(r-1)\sqrt s+O(1)\to\infty$。标准化卡方族紧，故此区间概率趋0。正文PDF385声称“unless $b=1/n$”不成立：此时$r=2$，仍趋0；消失线性项需要$1/b=0$即无限尺度的平坦极限，而不是$b=1/n$。

## 相关概念

- [[02 - 数理统计/概念/区间估计|区间估计]]
- [[02 - 数理统计/概念/假设检验|假设检验]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[01 - 概率论/概念/概率模型|概率模型]]

## 备注

- 统一来源见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011教材台账]]；原题位于[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=400|印刷369／PDF物理400]]。已对照原始页面核对完整英文、分题与定位，原题无星号。
- 解答为独立推导；引用的教材结论按source_refs核对，不使用答案册代替证明。
- 来源核对、归档与个人学习分别记录；verified只指所列来源核对范围，学习状态保持not-started。未实测Obsidian渲染。
