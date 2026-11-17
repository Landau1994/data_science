---
title: 习题 ST354：正态均值比的Delta区间与Fieller边界
topic: mathematical-statistics
topic_label: 数理统计
difficulty: advanced
status: not-started
tags:
- exercise
- mathematical-statistics
source: George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第10章习题10.48，印刷页416／PDF物理页447
source_id: DS011
source_chapter: 10
source_exercise: '10.48'
source_stars: 0
source_refs:
- DS011 Exercise 10.48，印刷416／PDF物理447
- DS011题内依赖核对：印刷199／PDF物理230；印刷375／PDF物理406
source_status: verified
solution_status: independently-derived
created: '2026-11-13'
---

# 习题 ST354：正态均值比的Delta区间与Fieller边界

## 题目

### 英文原题

> [!question] 英文原题
> **10.48** For the case of Fieller's confidence set (see Miscellanea 9.5.3), that is, given a random sample $(X_1,Y_1),\ldots,(X_n,Y_n)$ from a bivariate normal distribution with parameters $(\mu_X,\mu_Y,\sigma_X^2,\sigma_Y^2,\rho)$, find an approximate confidence interval for $\theta=\mu_Y/\mu_X$. Use the approximate moment calculations in Example 5.5.27 and apply the Central Limit Theorem.

### 中文转述

> [!question] 中文转述
> **原题10.48。** 对Fieller置信集的情形（见杂录9.5.3），即给定来自参数为$(\mu_X,\mu_Y,\sigma_X^2,\sigma_Y^2,\rho)$的二元正态分布的随机样本$(X_1,Y_1),\ldots,(X_n,Y_n)$，求$\theta=\mu_Y/\mu_X$的近似置信区间. 使用例5.5.27中的近似矩计算并应用中心极限定理.

## 提示

> [!hint]- 提示
> 对g(x,y)=y/x在µ_X≠0处作多元Delta。分母接近0时有限Wald区间不能表达Fieller的不确定性。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 要求$\mu_X\ne0$、非退化协方差，并令$\sigma_{XY}=\rho\sigma_X\sigma_Y$。估计$\hat\theta=\bar Y/\bar X$，梯度$\nabla g=(-\theta/\mu_X,1/\mu_X)$。多元CLT与Delta方法给
> $$
> \sqrt n(\hat\theta-\theta)\Rightarrow N\left(0,\frac{\sigma_Y^2-2\theta\sigma_{XY}+\theta^2\sigma_X^2}{\mu_X^2}\right).
> $$
> 这是例5.5.27一阶近似矩的正确应用，原例用$X/Y$，此题把分子分母交换。以无偏样本方差$S_X^2,S_Y^2$、协方差$S_{XY}$及$\hat\theta$代入，得到可实现的近似$1-\alpha$区间
> $$
> \hat\theta\ \pm\ z_{\alpha/2}\sqrt{\frac{S_Y^2-2\hat\theta S_{XY}+\hat\theta^2S_X^2}{n\bar X^2}}.
> $$
> 样本协方差矩阵半正定保证根内非负。该一阶局部近似的“均值”是$\theta$；若形式上保留二阶Taylor偏差，另为$[\theta\sigma_X^2-\sigma_{XY}]/(n\mu_X^2)$。但非退化正态$\bar X$在0有正密度，比值一般没有真实有限一、二阶矩，因此这些是局部渐近近似，不是声称有限样本比值矩存在。
>
> **与Fieller集合的边界关系。** 不先把分母固定为观测$\bar X$，而直接反演$\bar Y-t\bar X$的CLT，得到
> $$
> (\bar Y-t\bar X)^2\le\frac{z^2}{n}(S_Y^2-2tS_{XY}+t^2S_X^2),
> $$
> 即$At^2+Bt+C\le0$，其中$A=\bar X^2-z^2S_X^2/n$、$B=-2\bar X\bar Y+2z^2S_{XY}/n$、$C=\bar Y^2-z^2S_Y^2/n$。$A>0$且判别式正时是两根间区间；$A<0$可为两条无界射线或全实线，其他退化按二次不等式处理。它反映分母均值接近0时比值无法可靠定位。题中要求的Delta区间在固定非零$\mu_X$且样本充分大时适用；$\mu_X=0$目标本身未定义，不能硬套。
>
> 二元正态下将$z$换成相应$t_{n-1}$临界值并正确使用投影样本方差，可得到Fieller精确枢轴反演；这里的近似回答不声称已用该精确程序替代所求CLT。

## 相关概念

- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/期望|期望]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[02 - 数理统计/概念/参数估计|参数估计]]

## 备注

- 来源：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=447|印刷第416页／PDF物理第447页]]；版本与归档见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 实读例5.5.27：印刷199／PDF230；Fieller模型及投影均值方差见印刷375／PDF406。原Fieller附件把样本方差缩放处另有n与n−1混写，本解明确使用无偏样本协方差除以n。
- 已实读本题所用正文：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=230|印刷199／PDF物理230]]；[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=406|印刷375／PDF物理406]]；其余题内外部文献仅保留原引用，未声称查阅。
- 英文原题逐题对照PDF原始页面，保留原分题、提示、引用及可见疑误；原题无星号。题内引用补充与独立解答不混入原文；未查阅答案册或题内外部文献。
- 来源核对不表示个人学习完成，学习状态保持not-started。公式、链接与元数据检查不等于Obsidian实际渲染检查。
