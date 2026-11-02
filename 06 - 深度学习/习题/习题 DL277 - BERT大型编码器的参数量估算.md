---
title: "习题 DL277：BERT大型编码器的参数量估算"
topic: deep-learning
topic_label: 深度学习
difficulty: beginner
status: not-started
tags:
  - exercise
  - deep-learning
source: "[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Bishop 深度学习（DS003）]]"
source_id: DS003
source_chapter: 12
source_exercise: "12.16"
source_stars: 1
source_refs:
  - "DS003 Exercise 12.16，印刷406/PDF422"
  - "DS003 §12.1.4–12.1.6，式12.10–12.19及图12.7，印刷364–368/PDF380–384"
  - "DS003 §12.1.7，残差、LayerNorm与逐位置MLP，印刷369–370/PDF385–386"
source_status: verified
solution_status: independently-derived
created: 2026-11-02
---

# 习题 DL277：BERT大型编码器的参数量估算

## 题目

### 英文原题

> [!question] 英文原题
> **12.16 (★)** The BERT-Large model (Devlin et al., 2018) has a maximum input length of 512 tokens, each of dimensionality $D=1,024$ and taken from a vocabulary of 30,000. It has 24 transformer layers each with 16 self-attention heads with $D_q=D_k=D_v=64$, and the MLP position-wise networks have two layers with 4,096 hidden nodes. Show that the total number of parameters in the BERT encoder transformer language model is approximately 340 million.

### 中文转述

> [!question] 中文转述
> BERT-Large（Devlin等，2018）最大输入长512，词元维度$D=1024$，词表30000。共有24个Transformer层，每层16个自注意力头且$D_q=D_k=D_v=64$；逐位置MLP有两层，隐藏维度4096。证明该BERT编码器语言模型总参数量约3.4亿。

## 提示

> [!hint]- 提示 1
> 先数每层的Q、K、V和输出投影，再数两层MLP，最后加一次词嵌入与位置嵌入；头数不应把$D\times D$再重复乘16。

## 解答

> [!success]- 解答
> **独立推导。**
>
> 记$D=1024$、$F=4096$、$H=16$、$d_h=64$，有$Hd_h=D$。以下先按含偏置、每层两次带缩放和平移参数的LayerNorm计数。
>
> 每层Q/K/V各需$HDd_h=D^2$个权重，拼接后的输出投影也需$D^2$，加上四组$D$维偏置，注意力部分为
> $$
> 4D^2+4D=4{,}198{,}400.
> $$
> 逐位置MLP有$D\to F\to D$两层，参数为
> $$
> 2DF+F+D=8{,}393{,}728.
> $$
> 两个LayerNorm合计$4D=4096$，所以每个Transformer层为$12{,}596{,}224$，24层共$302{,}309{,}376$。
>
> 词嵌入有$30000D=30{,}720{,}000$个参数；学习式位置嵌入为$512D=524{,}288$。若采用BERT常见的两类句段嵌入和嵌入层LayerNorm，另有$2D+2D=4096$，故输入嵌入部分合计$31{,}248{,}384$。编码器总量为
> $$
> 302{,}309{,}376+31{,}248{,}384=333{,}557{,}760\approx3.34\times10^8.
> $$
> 若计入$D\to D$池化层及其偏置，再加$D^2+D=1{,}049{,}600$，为$334{,}607{,}360$。仅按题面未指明这些小模块时，保留主要项也得到
> $$
> 30000D+512D+24(4D^2+2DF)\approx3.33\times10^8.
> $$
> 因此题目的“约340 million”是模型规模的近似说法，不是仅凭这些配置能唯一推出的精确整数；约3.35亿与3.4亿相差约$1.6\%$。若再计预训练输出头，其常见共享词嵌入版本只增加约$D^2+D+2D+30000$及句间分类参数，约为3.36亿，同样属于约3.4亿的规模。若输出词表投影不共享嵌入，则会另增约3072万，必须说明计数口径。
>
> 最大序列长512只影响位置嵌入参数；注意力权重是输入相关的激活，不是$512^2$个独立学习参数。逐位置MLP对所有位置共享，也不能乘以512。以上算式为所列架构的独立计数，没有声称实际加载或检查某个发布模型的参数文件。

## 相关概念

- [[06 - 深度学习/概念/自注意力|自注意力]]
- [[06 - 深度学习/概念/Transformer|Transformer]]
- [[06 - 深度学习/概念/神经网络|神经网络]]

## 备注

- 原题已核对 DS003 印刷406页／PDF物理422页；正文引用的实际核对范围见 `source_refs`。
- 精确参数总数依赖是否含偏置、句段嵌入、池化与预训练输出头、词表实际大小及权重绑定。解答分别给出口径，不把约340m伪装成由题面唯一确定的精确值。
- 解答为独立推导；归档与个人学习状态分开，学习状态保持 `not-started`。
