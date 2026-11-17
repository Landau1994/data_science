---
title: "习题 ST400：函数型EIV误差方差MLE与二n分母"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第12章习题12.5，印刷页488／PDF物理页519"
source_id: "DS011"
source_chapter: 12
source_exercise: "12.5"
source_stars: 0
source_refs: ["DS011 Exercise 12.5，印刷页488／PDF物理页519", "DS011 所引正文，印刷473／PDF物理504", "DS011 所引正文，印刷474／PDF物理505"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST400：函数型EIV误差方差MLE与二n分母

## 题目

### 英文原题

> [!question] 英文原题
> **12.5** In the EIV functional relationship model, where $\lambda=\sigma_\delta^2/\sigma_\varepsilon^2$ is assumed known, show that the MLE of $\sigma_\delta^2$ is given by (12.2.18).

### 中文转述

> [!question] 中文转述
> **原题12.5。**
> 在EIV函数关系模型中，假定$\lambda=\sigma_\delta^2/\sigma_\varepsilon^2$已知，证明$\sigma_\delta^2$的MLE由式12.2.18给出.

## 提示

> [!hint]- 提示
> 消去潜变量后似然的尺度幂为$n$，不是$n/2$。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 重述模型：固定潜在$x$真值$\xi_i$，独立$X_i\sim N(\xi_i,s)$、$Y_i\sim N(\alpha+\beta\xi_i,s/\lambda)$，$s=\sigma_\delta^2>0$，已知$\lambda>0$。消去每个$\xi_i$得到加权残差总量$Q(\alpha,\beta)=\lambda\sum_i(y_i-\alpha-\beta x_i)^2/(1+\lambda\beta^2)$。在最优$\hat\alpha,\hat\beta$处记$Q_*>0$，剖面似然为常数乘$s^{-n}e^{-Q_*/(2s)}$。对数导数为$-n/s+Q_*/(2s^2)$，唯一驻点$\hat s=Q_*/(2n)$，它左侧导数正、右侧负，故全局最大：
> $$\hat\sigma_\delta^2=\frac1{2n}\frac\lambda{1+\lambda\hat\beta^2}\sum_i[y_i-(\hat\alpha+\hat\beta x_i)]^2.$$
> 即(12.2.18)。若$Q_*=0$，似然随$s\downarrow0$无界，没有普通正方差MLE。分母$2n$来自每对两个带误差坐标，不能静默用自由度修正$2n-2$代替MLE。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计（parameter estimation）]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]
- [[01 - 概率论/概念/随机变量|随机变量]]

## 备注

- 完整原题已逐页对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=519|印刷488／PDF物理519]]；原题无星号。教材信息与归档进度见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 实际引用输入核对页：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=504|印刷473／PDF物理504]]、[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=505|印刷474／PDF物理505]]；所需模型、公式、数据在解答重述。
- 来源已核对与解答写成不表示个人学习已完成；学习状态保留`not-started`。未实测Obsidian界面渲染。
