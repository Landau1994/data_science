---
title: 习题 PM032：分离支撑下Gibbs抽样的非遍历性
topic: probabilistic-models
topic_label: 概率模型与推断
difficulty: beginner
status: not-started
tags:
- exercise
- probabilistic-models
source: '[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Bishop《深度学习：基础与概念》（DS003）]]'
source_id: DS003
source_chapter: 14
source_exercise: '14.13'
source_stars: 1
source_refs:
- DS003 Exercise 14.13，印刷457/PDF472
- DS003 §14.2.4，Gibbs算法14.3及式(14.45)–(14.46)，印刷448–449/PDF463–464；细致平衡式(14.34)和复合核说明，印刷444/PDF459
- DS003 图14.14，印刷457/PDF472
source_status: verified
solution_status: independently-derived
created: '2026-11-02'
---

# 习题 PM032：分离支撑下Gibbs抽样的非遍历性

## 题目

### 英文原题

> [!question] 英文原题
> **14.13 (★)** Consider the distribution shown in Figure 14.14. Discuss whether the standard Gibbs sampling procedure for this distribution is ergodic and therefore whether it would sample correctly from this distribution

### 中文转述

> [!question] 中文转述
> **原题14.13。** 对图14.14中仅在两片阴影区域上均匀的二维分布，讨论标准单坐标Gibbs抽样是否遍历（ergodic），能否正确抽取整个分布。

## 提示

> [!hint]- 提示
> 固定一个坐标时，查看相应水平或竖直线是否可能同时穿过两块支撑。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 图中两块正面积支撑的横坐标投影彼此分离，纵坐标投影也彼此分离。
>
> ![[附件/习题图/DS003/原图-14.14.png]]
>
> 若初始状态落在左下块，固定 $z_2$ 更新 $z_1$ 时，可行水平截线只能穿过左下块；再固定新 $z_1$ 更新 $z_2$，竖直截线也只能穿过左下块。归纳可见任意有限次单坐标更新均留在该块。右上块同理。因而两块分别是封闭类，链不可约性失败，不能从任意单一初值收敛到同时给两块正概率的目标分布。
>
> 链可能在自身起始块内正确地抽取条件于该块的均匀分布，但会遗漏另一个块的概率质量。如果初始状态恰好按目标分布随机选择块，边缘可以保持目标，却不改变单条轨道无法探索整体的事实。可考虑同时更新两坐标的块Gibbs或具有跨块正概率的其他提议；仅随机更改单坐标更新顺序不能跨过这里的支撑障碍。

## 相关概念

- [[05 - 概率模型与推断/概念/概率推断|概率推断]]
- [[01 - 概率论/概念/条件概率|条件概率]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已实际对照[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=472|印刷457／PDF472]]；正文引用范围见 `source_refs`。
- 原题末尾没有句点，英文按原页保留；原图已实际查看并保存。
- 英文原题与中文转述分列，原文疑误另注；未使用配套答案册。`source_status: verified` 仅表示本题及所列公式的实际核对范围；解答写成不表示个人学习完成，状态保持 `not-started`。
