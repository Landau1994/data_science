---
title: "习题 DL032：风向的vonMises损失"
topic: "deep-learning"
topic_label: "深度学习"
difficulty: "intermediate"
status: "not-started"
tags:
  - exercise
  - deep-learning
source: "Understanding Deep Learning（2026-02-08修订稿），Problem 5.3，印刷74、75／PDF物理88、89"
source_id: "DS001"
source_chapter: 5
source_exercise: "5.3"
source_refs: ["DS001 Problem 5.3，印刷74、75/PDF88、89"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-10-28"
---

# 习题 DL032：风向的vonMises损失

## 题目

### 英文原题

> [!question] 英文原题
> **Problem 5.3\*** Suppose we want to build a model that predicts the direction $y$ in radians of the prevailing wind based on local measurements of barometric pressure $x$. A suitable distribution over circular domains is the von Mises distribution (figure 5.13):
> $$
> Pr(y\mid\mu,\kappa)=\frac{\exp[\kappa\cos[y-\mu]]}{2\pi\cdot\operatorname{Bessel}_0[\kappa]},\tag{5.34}
> $$
> where $\mu$ is a measure of the mean direction and $\kappa$ is a measure of concentration (i.e., the inverse of the variance). The term $\operatorname{Bessel}_0[\kappa]$ is a modified Bessel function of the first kind of order 0. Use the recipe from section 5.2 to develop a loss function for learning the parameter $\mu$ of a model $f[x,\phi]$ to predict the most likely wind direction. Your solution should treat the concentration $\kappa$ as constant. How would you perform inference?

### 中文转述

> [!question] 中文转述
> 用气压测量 $x$ 预测弧度风向 $y$，采用图5.13的von Mises圆周分布。固定集中度 $\kappa$，按照§5.2最大似然步骤设计学习均值方向 $\mu=f(x,\phi)$ 的损失，并说明如何推断最可能风向。

![[附件/习题图/DS001/原图-5.13.png]]

## 提示

> [!hint]- 提示
> 独立样本似然连乘，取负对数；固定集中度时归一化项与模型参数无关。

## 解答

> [!success]- 解答
> **独立推导。** 设 $I$ 对训练样本条件独立，固定 $\kappa>0$，令 $\mu_i=f(x_i,\phi)$。负对数似然为
> $$
> L(\phi)=I\log[2\pi\operatorname{Bessel}_0(\kappa)]-\kappa\sum_i\cos(y_i-f(x_i,\phi)).
> $$
> 故可最小化 $-\sum_i\cos(y_i-f_i)$，或等价的 $\sum_i[1-\cos(y_i-f_i)]$。其周期性避免把接近 $-\pi$ 与 $\pi$ 的两个方向误判为相距很远。推断时最大化余弦，得到 $\widehat y=f(x,\widehat\phi)\pmod{2\pi}$，规约到 $(-\pi,\pi]$。若 $\kappa=0$，分布均匀，全部方向同样可能、损失不含方向信息。

## 相关概念

- [[06 - 深度学习/概念/神经网络|神经网络]]

## 备注

- 原题已逐页核对：[[附件/books/UnderstandingDeepLearning_02_09_26_C.pdf#page=88|印刷74／PDF88]]；跨页至 PDF 89。来源核对仅覆盖本题原文和已列定位，学习状态不随归档改变。
