---
title: 习题 DL290：只生成狗时的最优GAN判别概率
topic: deep-learning
topic_label: 深度学习
difficulty: beginner
status: not-started
tags:
- exercise
- deep-learning
source: '[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Deep Learning: Foundations and Concepts（DS003）]]'
source_id: DS003
source_chapter: 17
source_exercise: '17.3'
source_stars: 1
source_refs:
- DS003 Exercise 17.3，印刷545/PDF558
- DS003 §17.1.1，真实/合成数据标签及式(17.6)，印刷535/PDF548；最优判别器式(17.15)，印刷544/PDF557
source_status: verified
solution_status: independently-derived
created: '2026-11-02'
---

# 习题 DL290：只生成狗时的最优GAN判别概率

## 题目

### 英文原题

> [!question] 英文原题
> **Exercise 17.3（★）** Consider a GAN in which the training set consists of equal numbers of cat and dog images and in which the generator network has learned to produce high quality images of dogs. Show that, when presented with a dog image, the optimal output for the discriminator network (trained to generate the probability that the image is real) is $1/3$.

### 中文转述

> [!question] 中文转述
> **原题17.3。** GAN训练数据中猫图与狗图数量相等，生成器已学会生成高质量狗图。证明给判别器输入狗图时，它输出的“图像为真实数据”的最优概率为 $1/3$。

## 提示

> [!hint]- 提示 1
> 使用最优判别器 $d^*(x)=p_{\mathrm{data}}(x)/(p_{\mathrm{data}}(x)+p_G(x))$。

> [!hint]- 提示 2
> 把真实数据写为猫、狗条件分布各占一半；说明何种分布匹配假设才会使全部狗图的比值固定。

## 解答

> [!success]- 解答
> **证明范围：在明确理想匹配条件下独立推导，并说明题面措辞的不足。** 设猫、狗图像分布分别为 $p_C,p_D$，其类别支持互不重叠，真实数据 $p=\tfrac12p_C+\tfrac12p_D$。按原书GAN目标，真实和合成样本的两项损失使用相同权重。
>
> 将“生成高质量狗图”理想化为生成分布恰等于真实狗图的条件分布，即 $q=p_D$。对于 $p_D(x)>0$ 的狗图，$p_C(x)=0$，所以最优判别器为
> $$
> d^*(x)=\frac{\tfrac12p_D(x)}{\tfrac12p_D(x)+p_D(x)}=\frac13.
> $$
> 等价地，在同等数量的真实／生成样本池中，狗图来源权重分别是 $\tfrac12\cdot\tfrac12=\tfrac14$ 和 $\tfrac12\cdot1=\tfrac12$，条件真实概率为 $(1/4)/(1/4+1/2)=1/3$。
>
> 单凭视觉“高质量”并不推出 $q=p_D$。若生成器只覆盖部分狗品种，则一般输出为 $[\tfrac12p_D(x)]/[\tfrac12p_D(x)+q(x)]$，随图像位置改变，不必恒为 $1/3$。因此本题数值依赖理想条件分布匹配及真实／合成来源等权；这些条件已与照录原题分开说明。

## 相关概念

- [[06 - 深度学习/概念/生成对抗网络|生成对抗网络]]
- [[01 - 概率论/概念/条件概率|条件概率]]
- [[05 - 概率模型与推断/概念/生成模型|生成模型]]

## 备注

- 原题及星数：[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=558|印刷545／PDF558]]；题页及引用正文已实际查看原PDF图像，精确定位见 `source_refs`。
- 有限样本猫狗计数相等在这里被解释为理想数据混合权重各为1/2；不把图像质量描述冒充精确分布相等。
- `source_status: verified` 仅指本题及所列实际核对范围；解答独立推导，不构成用户已完成学习，状态保持 `not-started`。
