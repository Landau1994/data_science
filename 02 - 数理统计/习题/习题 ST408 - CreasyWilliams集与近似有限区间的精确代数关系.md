---
title: "习题 ST408：CreasyWilliams集与近似有限区间的精确代数关系"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "advanced"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第12章习题12.13，印刷页490／PDF物理页521"
source_id: "DS011"
source_chapter: 12
source_exercise: "12.13"
source_stars: 0
source_refs: ["DS011 Exercise 12.13，印刷页490／PDF物理页521", "DS011 所引正文，印刷476／PDF物理507", "DS011 所引正文，印刷477／PDF物理508"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST408：CreasyWilliams集与近似有限区间的精确代数关系

## 题目

### 英文原题

> [!question] 英文原题
> **12.13** There is an interesting connection between the Creasy–Williams confidence set of (12.2.24) and the interval $C_G(\hat\beta)$ of (12.2.22).
> (a) Show that
> $$C_G(\hat\beta)=\left\{\beta:\frac{(\beta-\hat\beta)^2}{\hat\sigma_\beta^2/(n-2)}\le F_{1,n-2,\alpha}\right\},$$
> where $\hat\beta$ is the MLE of $\beta$ and $\hat\sigma_\beta^2$ is the previously defined consistent estimator of $\sigma_\beta^2$.
> (b) Show that the Creasy–Williams set can be written in the form
> $$\left\{\beta:\frac{(\beta-\hat\beta)^2}{\hat\sigma_\beta^2/(n-2)}\left[\frac{(1+\lambda\beta\hat\beta)^2}{(1+\lambda\beta^2)^2}\right]\le F_{1,n-2,\alpha}\right\}.$$
> Hence, $C_G(\hat\beta)$ can be derived by replacing the term in square brackets with 1, its probability limit. (In deriving this representation, the fact that $\hat\beta$ and $-1/(\lambda\hat\beta)$ are roots of the numerator of $r_\lambda(\beta)$ is of great help. In particular, the fact that
> $$\frac{r_\lambda^2(\beta)}{1-r_\lambda^2(\beta)}=\frac{\lambda^2S_{xy}^2(\beta-\hat\beta)^2(\beta+(1/(\lambda\hat\beta)))^2}{(1+\lambda\beta^2)^2(S_{xx}S_{yy}-S_{xy}^2)}$$
> is straightforward to establish. Hint:)

### 中文转述

> [!question] 中文转述
> **原题12.13。**
> 式12.2.24的Creasy–Williams置信集与式12.2.22的区间$C_G(\hat\beta)$之间有一个有趣联系.
>
> (a)  证明
>
> $$
> C_G(\hat\beta)=\left\{\beta:\frac{(\beta-\hat\beta)^2}{\hat\sigma_\beta^2/(n-2)}\le F_{1,n-2,\alpha}\right\},
> $$
>
> 其中$\hat\beta$是$\beta$的MLE，$\hat\sigma_\beta^2$是先前定义的$\sigma_\beta^2$的相合估计量.
>
> (b)  证明Creasy–Williams集合可写为
>
> $$
> \left\{\beta:\frac{(\beta-\hat\beta)^2}{\hat\sigma_\beta^2/(n-2)}
> \left[\frac{(1+\lambda\beta\hat\beta)^2}{(1+\lambda\beta^2)^2}\right]\le F_{1,n-2,\alpha}\right\}.
> $$
>
> 因此，将方括号中的项替换为其概率极限1，即得到$C_G(\hat\beta)$. （推导这一表示时，$\hat\beta$与$-1/(\lambda\hat\beta)$是$r_\lambda(\beta)$分子的根这一事实很有帮助. 特别地，容易建立
>
> $$
> \frac{r_\lambda^2(\beta)}{1-r_\lambda^2(\beta)}
> =\frac{\lambda^2S_{xy}^2(\beta-\hat\beta)^2(\beta+(1/\lambda\hat\beta))^2}
> {(1+\lambda\beta^2)^2(S_{xx}S_{yy}-S_{xy}^2)}.\quad\text{）}
> $$

## 提示

> [!hint]- 提示
> 先利用二次根关系简化渐近方差，再比较$t^2$与F分位数。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 沿用$A=S_{xx},B=S_{yy},C=S_{xy}\ne0,\Delta=AB-C^2>0,h=\hat\beta\ne0$，$n\ge3$。书中定义$s_\beta^2=\hat\sigma_\beta^2=(1+\lambda h^2)^2\Delta/[(A-\lambda B)^2+4\lambda C^2]$，用于$\sqrt n(\hat\beta-\beta)$的渐近方差；区间为$h\pm t_{n-2,\alpha/2}s_\beta/\sqrt{n-2}$。
> (a) 两端不等式等价$(\beta-h)^2/(s_\beta^2/(n-2))\le t_{n-2,\alpha/2}^2$，而中心$t$平方为$F_{1,n-2}$，平方分位数恰为右尾$\alpha$的$F_{1,n-2,\alpha}$，即原式。
> (b) 两线性坐标$U_b=X+\lambda bY,V_b=Y-bX$的样本协方差分子为$N(b)=\lambda bB+(1-\lambda b^2)C-bA=-\lambda C(b-h)(b+1/(\lambda h))$。变换行列式平方给$\operatorname{SS}(U_b)\operatorname{SS}(V_b)-N(b)^2=(1+\lambda b^2)^2\Delta$，所以$r^2/(1-r^2)=N(b)^2/[(1+\lambda b^2)^2\Delta]$，即原题Hint所列恒等式。
> 二次根关系还给$(A-\lambda B)^2+4\lambda C^2=C^2(\lambda h+1/h)^2$，所以$s_\beta^2=h^2\Delta/C^2$。代入上述分解得到
> $$\frac{r^2(b)}{1-r^2(b)}=\frac{(b-h)^2}{s_\beta^2}\frac{(1+\lambda bh)^2}{(1+\lambda b^2)^2}.$$
> 乘$n-2$即所求置信集表示。若在真参数$b=\beta$处有$h\to\beta$依概率，则方括号因子趋1，解释近似区间。但它不是对所有候选$b$的统一极限，不能凭逐点Slutsky把不连通/无界的精确集说成全参数均匀有效的有限区间。英文末尾原印“Hint:”的位置也照录。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计（parameter estimation）]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]
- [[01 - 概率论/概念/随机变量|随机变量]]
- [[02 - 数理统计/概念/区间估计|区间估计]]

## 备注

- 完整原题已逐页对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=521|印刷490／PDF物理521]]；原题无星号。教材信息与归档进度见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 实际引用输入核对页：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=507|印刷476／PDF物理507]]、[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=508|印刷477／PDF物理508]]；所需模型、公式、数据在解答重述。
- 来源已核对与解答写成不表示个人学习已完成；学习状态保留`not-started`。未实测Obsidian界面渲染。
