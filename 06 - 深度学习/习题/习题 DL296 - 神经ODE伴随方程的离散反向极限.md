---
title: 习题 DL296：神经ODE伴随方程的离散反向极限
topic: deep-learning
topic_label: 深度学习
difficulty: intermediate
status: not-started
tags:
- exercise
- deep-learning
source: '[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Deep Learning: Foundations and Concepts（DS003）]]'
source_id: DS003
source_chapter: 18
source_exercise: '18.6'
source_stars: 2
source_refs:
- DS003 Exercise 18.6，印刷560/PDF572
- DS003 伴随定义与ODE式(18.24)–(18.25)，印刷556/PDF568
source_status: verified
solution_status: independently-derived
created: '2026-11-02'
---

# 习题 DL296：神经ODE伴随方程的离散反向极限

## 题目

### 英文原题

> [!question] 英文原题
> **Exercise 18.6（★★）** In this exercise and the next we provide an informal derivation of the backpropagation and gradient evaluation equations for a neural ODE. A more formal derivation of these results can be found in Chen et al. (2018). Write down the backpropagation equation corresponding to the forward equation (18.38). By taking the limit $\epsilon\to0$, derive the backward propagation equation (18.25), where $\mathbf a(t)$ is defined by (18.24).

### 中文转述

> [!question] 中文转述
> **原题18.6。** 本题及下一题给出神经ODE反向传播和梯度计算公式的非正式推导，更正式的推导见Chen等(2018)。写出前向公式(18.38)对应的反向传播关系。令步长 $\epsilon\to0$，推导反向传播方程(18.25)，其中伴随量 $\mathbf a(t)$ 由(18.24)定义。

## 提示

> [!hint]- 提示 1
> 统一采用列梯度 $a(t)=\nabla_{z(t)}L$，对单步映射使用Jacobian转置。

## 解答

> [!success]- 解答
> **独立推导，不声称核对题面引用的外部论文。** 设 $z_{k+1}=z_k+\epsilon f(z_k,w)$，终端损失为 $L(z_N)$，定义列伴随 $a_k=\nabla_{z_k}L$，$J_k=\partial f/\partial z(z_k,w)$。链式法则为
> $$a_k=(I+\epsilon J_k)^Ta_{k+1}.$$
> 整理得到 $(a_{k+1}-a_k)/\epsilon=-J_k^Ta_{k+1}$。当轨迹、Jacobian及伴随连续收敛，令 $\epsilon\to0$ 得
> $$a'(t)=-J(t)^Ta(t),\qquad a(T)=\nabla L(z(T)).$$
> 给定终端条件，此方程从 $T$ 向0积分。若改用行伴随 $\bar a=a^T$，等价形式为 $\bar a'=-\bar aJ$。这对应原式(18.25)意图，但原书 $a'$ 与 $-a^T\nabla_zf$ 的行列约定未统一，上面明确尺寸以免误用。
>
> 连续验证：任一线性化状态扰动满足 $\delta z'=J\delta z$，所以 $\frac{\mathrm d}{\mathrm dt}(a^T\delta z)=(-J^Ta)^T\delta z+a^TJ\delta z=0$；终点损失扰动能被伴随正确传回任一时刻。若损失还依赖中间状态，需额外的跳跃／源项，本题仅处理终端损失。

## 相关概念

- [[06 - 深度学习/概念/归一化流|归一化流]]
- [[03 - 线性代数与优化/概念/链式法则|链式法则]]
- [[06 - 深度学习/概念/反向传播|反向传播]]

## 备注

- 原题及星数：[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=572|印刷560／PDF572]]；题页及引用正文已实际查看原PDF图像，精确定位见 `source_refs`。
- `source_status: verified` 仅指本题及所列实际核对范围；解答独立推导，不构成用户已完成学习，状态保持 `not-started`。
