---
title: 习题 ST317：Gamma均值与尺度的效率比较及原命题纠正
topic: mathematical-statistics
topic_label: 数理统计
difficulty: advanced
status: not-started
tags:
- exercise
- mathematical-statistics
source: George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第10章习题10.11，印刷页409／PDF物理页440
source_id: DS011
source_chapter: 10
source_exercise: '10.11'
source_stars: 0
source_refs:
- DS011 Exercise 10.11，印刷409／PDF物理440
- DS011题内依赖核对：印刷384／PDF物理415；印刷385／PDF物理416；印刷386／PDF物理417
source_status: verified
solution_status: independently-derived
created: '2026-11-13'
---

# 习题 ST317：Gamma均值与尺度的效率比较及原命题纠正

## 题目

### 英文原题

> [!question] 英文原题
> **10.11** This problem will look at some details and extensions of the calculation in Example 10.1.18.
>
> (a) Reproduce Figure 10.1.1, calculating the ARE for known $\beta$. (You can follow the calculations in Example 12.6.7, or do your own programming.)
>
> (b) Verify that the $\operatorname{ARE}(\bar X,\hat\mu)$ comparison is the same whether $\beta$ is known or unknown.
>
> (c) For estimation of $\beta$ with known $\mu$, show that the MOM and ML estimates are the same. (It may be easier to use the $(\alpha,\beta)$ parameterization.)
>
> (d) For estimation of $\beta$ with unknown $\mu$, the MOM and ML estimates are not the same. Compare these estimates using asymptotic relative efficiency, and produce a figure like Figure 10.1.1, where the different curves correspond to different values of $\mu$.

### 中文转述

> [!question] 中文转述
> **原题10.11。** 本题考察例10.1.18计算的若干细节与推广.
>
> (a)  复现10.1.1，计算$\beta$已知时的ARE. （可沿用例12.6.7的计算，或自行编程.）
>
> (b)  验证，无论$\beta$已知还是未知，$\operatorname{ARE}(\bar X,\hat\mu)$的比较都相同.
>
> (c)  对$\mu$已知时$\beta$的估计，证明矩估计与最大似然估计相同. （使用$(\alpha,\beta)$参数化可能更容易.）
>
> (d)  对$\mu$未知时$\beta$的估计，矩估计与最大似然估计不同. 用渐近相对效率比较它们，并作出类似10.1.1的图，不同曲线对应不同$\mu$值.

## 提示

> [!hint]- 提示
> 先固定ARE的方向。尺度已知与作为未知干扰参数是两个不同信息问题，原(b)(c)需检验。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 采用本书定义10.1.16：$\operatorname{ARE}(V,W)=v_W/v_V$，其中$v$为$\sqrt n$极限方差。模型$X\sim\operatorname{Gamma}(a,b)$，$\mu=ab$、$b=\beta$；记$\psi_0=(\log\Gamma)'$、$\psi_1=\psi_0'$。
>
> **(a)** $b$已知时，得分关于$\mu$为$[\log X-\log b-\psi_0(\mu/b)]/b$，每观测信息$I_{\mu\mu}=\psi_1(a)/b^2$。矩估计$\bar X$的极限方差为$ab^2$，MLE为$b\hat a$，$\psi_0(\hat a)=\overline{\log X}-\log b$，极限方差$b^2/\psi_1(a)$。因此
> $$
> \operatorname{ARE}(\bar X,\hat\mu)=\frac1{a\psi_1(a)}<1,
> $$
> 因为$\psi_1(a)=\sum_{j=0}^\infty(a+j)^{-2}>\int_0^\infty(a+t)^{-2}dt=1/a$。原例与图10.1.1反而画出大于1的相反方向；按图的方向可重现$V_{\rm MOM}/V_{\rm ML}=a\psi_1(a)$，但这不是该定义下标注的ARE。下图分别给正确ARE和原图方向的倒数，$b=1,3,5,10$；保留可审计的数学差异。
>
> ![[附件/习题图/DS011/习题10.11-Gamma效率比较.png]]
>
> **(b) 原句不成立。** $b$未知时联立MLE方程，$\hat b=\bar X/\hat a$且$\log\hat a-\psi_0(\hat a)=\log\bar X-\overline{\log X}$。于是$\hat\mu=\hat a\hat b=\bar X$逐点成立，两估计相同，ARE恰为1，不同于(a)。例如$a=1$时已知$b$的ARE为$6/\pi^2=.6079271$，未知$b$为1。
>
> **(c) 原句一般不成立。** 已知均值$\mu$等价于约束$a=\mu/b$，不是已知形状$a$。自然二阶矩估计为$\tilde b=n^{-1}\sum_i(X_i-\mu)^2/\mu$。MLE则在该约束下最大化Gamma似然，涉及$\psi_0$，通常不同。明确反例：$\mu=1$、数据$.5,1.5$，矩估计$.25$。由于该数据均值恰为1，约束MLE与联合MLE在此一致，解$\log a-\psi_0(a)=-\tfrac12\log(.75)$得$\hat a=3.63430278$、$\hat b=.275155941\ne.25$。这些值已实际数值求根。若把原条件改为“已知形状$a$”，则两法确实都给$\bar X/a$，但那是另一个问题。
>
> **(d)** 均值未知时，令$m_2=n^{-1}\sum(X_i-\bar X)^2$，矩估计$\tilde b=m_2/\bar X$，MLE仍是$\hat b=\bar X/\hat a$，其中$\hat a$解(b)的非线性方程。信息矩阵及逆阵为
> $$
> I(a,b)=\begin{pmatrix}\psi_1(a)&1/b\\1/b&a/b^2\end{pmatrix},\qquad v_{\hat b}=\frac{b^2\psi_1(a)}{a\psi_1(a)-1}.
> $$
> Gamma中心矩$\mu_2=ab^2,\mu_3=2ab^3,\mu_4=3a^2b^4+6ab^4$给$\sqrt n(\bar X-\mu,m_2-\mu_2)$的协方差矩阵$\begin{pmatrix}ab^2&2ab^3\\2ab^3&2a^2b^4+6ab^4\end{pmatrix}$。对$m_2/\bar X$应用梯度$(-1/a,1/(ab))$得到$v_{\tilde b}=b^2(2+3/a)$。因此
> $$
> \operatorname{ARE}(\tilde b,\hat b)=\frac{\psi_1(a)}{[a\psi_1(a)-1](2+3/a)},\quad a=\mu/b.
> $$
> 图的第三面板对$\mu=1,3,5,10$画该效率随$b$的变化，完成所求不同均值曲线。原图方向倒置与(b)(c)错误均未被当成待证明真命题。

## 相关概念

- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/期望|期望]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[02 - 数理统计/概念/参数估计|参数估计]]

## 备注

- 来源：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=440|印刷第409页／PDF物理第440页]]；版本与归档见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 实读定义10.1.16、例10.1.18及原图：印刷384–386／PDF415–417。本解独立计算，没有查附录例12.6.7。公式、反例数值和曲线数据见[[work/DS011/ch10/computations.py|独立计算]]。
- 已实读本题所用正文：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=415|印刷384／PDF物理415]]；[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=416|印刷385／PDF物理416]]；[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=417|印刷386／PDF物理417]]；其余题内外部文献仅保留原引用，未声称查阅。
- 独立图件由真实样本与明确公式制作，PGFPlots源：[[附件/习题图/DS011/习题10.11-Gamma效率比较.tex|可编辑图源]]；[[附件/习题图/DS011/习题10.11-Gamma效率比较.pdf|矢量PDF]]。已编译、渲染并目视检查，图数据及原始样本可追溯；未作Obsidian实际渲染检查。
- 英文原题逐题对照PDF原始页面，保留原分题、提示、引用及可见疑误；原题无星号。题内引用补充与独立解答不混入原文；未查阅答案册或题内外部文献。
- 来源核对不表示个人学习完成，学习状态保持not-started。公式、链接与元数据检查不等于Obsidian实际渲染检查。
