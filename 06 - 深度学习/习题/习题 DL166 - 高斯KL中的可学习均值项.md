---
title: "习题 DL166：高斯KL中的可学习均值项"
topic: deep-learning
topic_label: 深度学习
difficulty: advanced
status: not-started
tags:
  - exercise
  - deep-learning
source: "Understanding Deep Learning（2026-02-08 修订稿），Problem 18.8，印刷373／PDF物理387"
source_id: DS001
source_chapter: 18
source_exercise: "18.8"
source_refs: ["DS001 Problem 18.8*，印刷373/PDF387", "DS001 式18.27–18.28，印刷359/PDF373"]
source_status: verified
solution_status: independently-derived
created: 2026-10-28
---

# 习题 DL166：高斯KL中的可学习均值项

## 题目

### 英文原题

> [!question] 英文原题
> **Problem 18.8\*** The KL-divergence between two normal distributions in $D$ dimensions with means $\mathbf a$ and $\mathbf b$ and covariance matrices $\mathbf A$ and $\mathbf B$ is given by:
> $$
> D_{KL}[\operatorname{Norm}_{\mathbf w}[\mathbf a,\mathbf A]\Vert\operatorname{Norm}_{\mathbf w}[\mathbf b,\mathbf B]]
> =\frac12\left(\operatorname{tr}[\mathbf B^{-1}\mathbf A]-d+(\mathbf a-\mathbf b)^T\mathbf B^{-1}(\mathbf a-\mathbf b)+\log\left[\frac{|\mathbf B|}{|\mathbf A|}\right]\right).\tag{18.48}
> $$
> Substitute the definitions from equation 18.27 into this expression and show that the only term that depends on the parameters $\boldsymbol\phi$ is the first term from equation 18.28.

### 中文转述

> [!question] 中文转述
> 将式18.27的两个条件高斯代入式18.48，证明固定方差时仅均值平方误差依赖网络参数，得到式18.28。


## 提示

> [!hint]- 提示
> 记真实后验方差为 $\widetilde\beta_t I$，模型方差为 $\sigma_t^2I$，逐项计算迹、行列式比和二次型。

## 解答

> [!success]- 解答
> 统一把原题公式中小写 $d$ 解释为前文维数 $D$。对 $t\ge2$，式18.27给出
> $$
> a=\widetilde\mu_t=\frac{(1-\alpha_{t-1})\sqrt{1-\beta_t}}{1-\alpha_t}z_t+\frac{\sqrt{\alpha_{t-1}}\beta_t}{1-\alpha_t}x,\quad A=\widetilde\beta_tI,
> $$
> $$
> b=f_t(z_t,\phi_t),\quad B=\sigma_t^2I,\quad\widetilde\beta_t=\frac{\beta_t(1-\alpha_{t-1})}{1-\alpha_t}.
> $$
> 因而
> $$
> \operatorname{tr}(B^{-1}A)=D\frac{\widetilde\beta_t}{\sigma_t^2},\qquad
> (a-b)^TB^{-1}(a-b)=\frac{\|\widetilde\mu_t-f_t(z_t,\phi_t)\|^2}{\sigma_t^2},
> $$
> $$
> \log\frac{|B|}{|A|}=D\log\frac{\sigma_t^2}{\widetilde\beta_t}.
> $$
> 代回得
> $$
> D_{KL}=\frac1{2\sigma_t^2}\|\widetilde\mu_t-f_t(z_t,\phi_t)\|^2+
> \underbrace{\frac D2\left[\frac{\widetilde\beta_t}{\sigma_t^2}-1+\log\frac{\sigma_t^2}{\widetilde\beta_t}\right]}_{C}.
> $$
> 若噪声日程与 $\sigma_t^2>0$ 固定且不依赖 $\phi$，则 $C$ 无参数依赖，第一项即式18.28。若同时学习模型方差，$C$ 与平方误差的系数都可能依赖参数，不能省略这些项。$t=1$ 的退化后验需用单独的重构项处理。

## 相关概念

- [[06 - 深度学习/概念/扩散模型|扩散模型]]：前向加噪、反向条件分布与训练目标。
- [[01 - 概率论/概念/相对熵|相对熵]]：高斯KL散度与证据下界。

## 备注

- 原题：[[附件/books/UnderstandingDeepLearning_02_09_26_C.pdf#page=387|印刷 373／PDF 387]]；教材记录见 [[00 - 首页/教材归档/DS001 - Understanding Deep Learning|DS001]]。
- 题干、公式及所引原页已核对；解答为独立推导。原题文字用大写D、公式用小写d，此处保留原式并在解答统一解释。
