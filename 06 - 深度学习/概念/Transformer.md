---
title: "Transformer"
aliases: ["Transformer", "Transformer layer", "Transformer architecture"]
topic: "deep-learning"
topic_label: "深度学习"
tags:
  - concept
  - deep-learning
status: "not-started"
source: "Understanding Deep Learning（2026-02-08修订稿），§12.4式(12.13)及图12.7，印刷216／PDF物理230；§12.3位置编码及多头相关定义，印刷213–214／PDF物理227–228"
source_refs: ["DS001 §12.4式(12.13)及图12.7，印刷216／PDF物理230", "DS001 §12.3位置编码及多头相关定义，印刷213–214／PDF物理227–228"]
source_status: "partially-verified"
created: "2026-10-28"
updated: "2026-10-28"
---

# Transformer

## 定义

> [!info] 注意力、逐token网络与残差的组合
> Transformer是一类堆叠注意力层来处理token表示的网络。按UDL的后归一化（post-norm）层约定，输入$X\in\mathbb R^{D\times N}$时
> $$
> U=\operatorname{LN}(X+\operatorname{MHSA}(X)),\qquad
> Y=\operatorname{LN}(U+\operatorname{MLP}_{\rm col}(U)).
> $$
> MHSA是多头自注意力；同一个MLP独立用于每列；LayerNorm对各token的特征维度归一化。两个残差分支须输出$D\times N$。这是本页采用的具体层型，不是所有Transformer变体的唯一排列。

## 直觉与解释

注意力负责让不同位置交换信息，逐位置MLP负责在每个位置内重组特征，两者分工不同。残差连接提供表示增量，归一化控制计算尺度。输入可以是文本token，也可以是其他离散化单元；网络结构本身没有规定一定要生成语言或采用哪一种损失。

## 主要性质

多头使用各自的查询、键和值，拼接后用输出投影恢复模型宽度。若采用$H$头且每头宽$D/H$，总表示宽度仍为$D$，不是每头都必须具有完整$D$维。
逐列共享MLP满足$\operatorname{MLP}_{\rm col}(XP)=\operatorname{MLP}_{\rm col}(X)P$，逐token LayerNorm也满足此式。结合自注意力的等变性可知，没有位置输入或固定掩码时，整层仍对token置换等变；增加层数不会凭空恢复词序。
LayerNorm的统计沿单个token的特征维度计算，不沿批次计算，所以不同样本之间不会仅因这一统计步骤相互耦合。前归一化（pre-norm）把LN移到各分支内部，公式与导数结构随之改变。

## 例子与边界

> [!example] 同形才能相加
> 若$D=4,N=3$，两头各输出$2\times3$，拼接为$4\times3$，输出投影后可与$X$相加。若分支直接输出$6\times3$，则必须先投影回4维，不能按元素强行相加。

Transformer不等于一个自注意力算子。另须指定token表示、位置方式、可见性掩码、输出头和任务目标；相同层结构可以支持不同任务。本文未把这些选择当作固定不变的定义。

## 相关概念

- [[06 - 深度学习/概念/自注意力|自注意力]]：多头子层的内容聚合。
- [[06 - 深度学习/概念/残差网络|残差网络]]：理解两个相加路径。
- [[06 - 深度学习/概念/批归一化|批归一化]]：对照归一化所跨越的轴。
- [[06 - 深度学习/概念/前向传播|前向传播]]；[[04 - 统计学习/概念/交叉熵|交叉熵]]：分别描述计算过程与可能的训练目标。

## 相关习题

```dataview
TABLE WITHOUT ID file.link AS "习题", difficulty AS "难度", status AS "学习状态"
FROM #exercise
WHERE contains(file.outlinks, this.file.link)
SORT file.name ASC
```

## 来源与证明状态

已查看[[附件/books/UnderstandingDeepLearning_02_09_26_C.pdf#page=230|§12.4，印刷216／PDF230]]的图12.7、式(12.13)及LayerNorm解释，并对照[[附件/books/UnderstandingDeepLearning_02_09_26_C.pdf#page=227|§12.3，印刷213–214／PDF227–228]]的位置与多头定义，见[[00 - 首页/教材归档/DS001 - Understanding Deep Learning|DS001]]。维数例子及整层置换论证为独立推导；pre-norm仅作明确写出的变式，未声称该页证明其训练性质。partially-verified仅覆盖列出内容。
