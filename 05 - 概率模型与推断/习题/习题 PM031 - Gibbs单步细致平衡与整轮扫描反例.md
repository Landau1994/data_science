---
title: 习题 PM031：Gibbs单步细致平衡与整轮扫描反例
topic: probabilistic-models
topic_label: 概率模型与推断
difficulty: intermediate
status: not-started
tags:
- exercise
- probabilistic-models
source: '[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Bishop《深度学习：基础与概念》（DS003）]]'
source_id: DS003
source_chapter: 14
source_exercise: '14.12'
source_stars: 2
source_refs:
- DS003 Exercise 14.12，印刷457/PDF472
- DS003 §14.2.4，Gibbs算法14.3及式(14.45)–(14.46)，印刷448–449/PDF463–464；细致平衡式(14.34)和复合核说明，印刷444/PDF459
source_status: verified
solution_status: independently-derived
created: '2026-11-02'
---

# 习题 PM031：Gibbs单步细致平衡与整轮扫描反例

## 题目

### 英文原题

> [!question] 英文原题
> **14.12 (★★)** Show that the Gibbs sampling algorithm, discussed in Section 14.2.4, satisfies detailed balance as defined by (14.34).

### 中文转述

> [!question] 中文转述
> **原题14.12。** 证明§14.2.4讨论的Gibbs抽样（Gibbs sampling）算法满足式(14.34)定义的细致平衡（detailed balance）。

## 提示

> [!hint]- 提示
> 固定其余坐标后，正反流量均含两个条件概率的乘积；但可逆核的顺序乘积不必可逆。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 先考虑固定坐标 $i$ 的单次更新核，保持 $\mathbf z_{-i}$ 不变，从 $p(z_i\mid\mathbf z_{-i})$ 重抽坐标。对只在第 $i$ 坐标不同的两状态，其平稳流量为
> $$
> p(\mathbf z)K_i(\mathbf z,\mathbf z')
> =p(\mathbf z_{-i})p(z_i\mid\mathbf z_{-i})p(z_i'\mid\mathbf z_{-i}),
> $$
> 交换 $z_i,z_i'$ 不变；对其余坐标不同的状态，两边均为0。连续情形以固定其余坐标的Dirac核理解。因此 $K_i$ 满足细致平衡。若以与状态无关的概率 $\alpha_i$ 选坐标，则 $K=\sum_i\alpha_iK_i$ 也由线性性满足细致平衡。
>
> **固定顺序整轮的边界。** 正文算法14.3依次更新全部坐标，整轮核为 $K_1\cdots K_M$。每个 $K_i$ 都保持 $p$，所以乘积仍保持 $p$；但细致平衡一般不成立。给出严格正的二元反例：联合概率表 $p(0,0)=0.4,p(0,1)=0.1,p(1,0)=0.2,p(1,1)=0.3$，每轮先更新 $x$ 再更新 $y$。则
> $$
> K((0,0),(1,1))=\frac{0.2}{0.6}\frac{0.3}{0.5}=0.2,
> $$
> $$
> K((1,1),(0,0))=\frac{0.1}{0.4}\frac{0.4}{0.5}=0.2.
> $$
> 正反平稳流量分别为 $0.4\times0.2=0.08$ 与 $0.3\times0.2=0.06$，不相等。
>
> 所以原题若指一个条件更新或随机扫描，命题正确；若指算法14.3的一整轮固定扫描，命题需要修正。正文印刷444／PDF459也明确提示复合核不自动可逆，与此反例一致。

## 相关概念

- [[05 - 概率模型与推断/概念/概率推断|概率推断]]
- [[01 - 概率论/概念/条件概率|条件概率]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已实际对照[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=472|印刷457／PDF472]]；正文引用范围见 `source_refs`。
- 保留原题笼统断言，解答区分单步、随机混合与固定扫描，不将平稳性混同于可逆性。
- 英文原题与中文转述分列，原文疑误另注；未使用配套答案册。`source_status: verified` 仅表示本题及所列公式的实际核对范围；解答写成不表示个人学习完成，状态保持 `not-started`。
