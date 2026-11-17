---
title: "习题 ST407：CreasyWilliams斜率倒数对称及参数边界"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "advanced"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第12章习题12.12，印刷页490／PDF物理页521"
source_id: "DS011"
source_chapter: 12
source_exercise: "12.12"
source_stars: 0
source_refs: ["DS011 Exercise 12.12，印刷页490／PDF物理页521", "DS011 所引正文，印刷473／PDF物理504", "DS011 所引正文，印刷474／PDF物理505", "DS011 所引正文，印刷477／PDF物理508"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST407：CreasyWilliams斜率倒数对称及参数边界

## 题目

### 英文原题

> [!question] 英文原题
> **12.12** Verify the following facts about $\hat\beta$ (the MLE of $\beta$ when we assume $\sigma_\delta^2=\lambda\sigma_\varepsilon^2$), $r_\lambda(\beta)$ of (12.2.23), and $C_\lambda(\hat\beta)$, the Creasy–Williams confidence set of (12.2.24).
> (a) $\hat\beta$ and $-1/(\lambda\hat\beta)$ are the two roots of the quadratic equation defining the zeros of the first derivative of the likelihood function (12.2.14).
> (b) $r_\lambda(\beta)=-r_\lambda(-1/(\lambda\beta))$ for every $\beta$.
> (c) If $\beta\in C_\lambda(\hat\beta)$ then $-1/(\lambda\beta)\in C_\lambda(\hat\beta)$.

### 中文转述

> [!question] 中文转述
> **原题12.12。**
> 验证关于$\hat\beta$（假设$\sigma_\delta^2=\lambda\sigma_\varepsilon^2$时$\beta$的MLE）、式12.2.23的$r_\lambda(\beta)$以及式12.2.24的Creasy–Williams置信集$C_\lambda(\hat\beta)$的下列事实.
>
> (a)  $\hat\beta$与$-1/(\lambda\hat\beta)$是定义似然函数式12.2.14一阶导数零点的二次方程的两个根.
>
> (b)  对每个$\beta$，$r_\lambda(\beta)=-r_\lambda(-1/(\lambda\beta))$.
>
> (c)  若$\beta\in C_\lambda(\hat\beta)$，则$-1/(\lambda\beta)\in C_\lambda(\hat\beta)$.

## 提示

> [!hint]- 提示
> 倒数变换会交换两个线性坐标，并给其中一个加负号。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 设$\lambda>0$、$A=S_{xx},B=S_{yy},C=S_{xy}\ne0$、$AB>C^2$，保证下列分母与样本方差非零。
> (a) 消去截距后的剖面残差为$\lambda(B-2bC+b^2A)/(1+\lambda b^2)$。对$b$求导，零点为$\lambda Cb^2+(A-\lambda B)b-C=0$。两根乘积$-1/\lambda$，若一根为非零MLE$h=\hat\beta$，另一根即$-1/(\lambda h)$。
> (b) 对$b\ne0$，记$U_b=X+\lambda bY,V_b=Y-bX$，$b'=-1/(\lambda b)$。直接有$U_{b'}=-V_b/b$、$V_{b'}=U_b/(\lambda b)$。交换变量不改相关系数，两个尺度系数乘积$-1/(\lambda b^2)<0$，所以$r(b')=-r(b)$，这同时给出代数验证。
> (c) 该置信集由$(n-2)r(b)^2/(1-r(b)^2)\le q$定义，只依赖$r^2$，由(b)在倒数变换下不变，得结论。
> 原文“every$\beta$”在$\beta=0$处倒数无定义，须限$b\ne0$；若愿在斜率的射影直线中加入垂直方向$\infty$，可把0与无穷互换并以极限延拓，不能在普通实数域直接除0。$C=0$也使$a$中的指定根形式失效，须另处理。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计（parameter estimation）]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]
- [[01 - 概率论/概念/随机变量|随机变量]]
- [[02 - 数理统计/概念/区间估计|区间估计]]

## 备注

- 完整原题已逐页对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=521|印刷490／PDF物理521]]；原题无星号。教材信息与归档进度见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 实际引用输入核对页：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=504|印刷473／PDF物理504]]、[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=505|印刷474／PDF物理505]]、[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=508|印刷477／PDF物理508]]；所需模型、公式、数据在解答重述。
- 来源已核对与解答写成不表示个人学习已完成；学习状态保留`not-started`。未实测Obsidian界面渲染。
