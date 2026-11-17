---
title: "习题 P221：二元独立坐标仿射变换的Jacobian"
topic: "probability-theory"
topic_label: "概率论"
difficulty: "beginner"
status: "not-started"
tags: ["exercise", "probability-theory"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第4章习题4.22，印刷页159／PDF物理页190"
source_id: "DS011"
source_chapter: 4
source_exercise: "4.22"
source_stars: 0
source_refs: ["DS011 Exercise 4.22，印刷159／PDF物理190"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 P221：二元独立坐标仿射变换的Jacobian

## 题目

### 英文原题

> [!question] 英文原题
> **4.22** Let $(X,Y)$ be a bivariate random vector with joint pdf $f(x,y)$. Let $U=aX+b$ and $V=cY+d$, where $a,b,c,$ and $d$ are fixed constants with $a>0$ and $c>0$. Show that the joint pdf of $(U,V)$ is
> $$
> f_{U,V}(u,v)=\frac1{ac}f\left(\frac{u-b}{a},\frac{v-d}{c}\right).
> $$

### 中文转述

> [!question] 中文转述
> **原题4.22。**
> 设 $(X,Y)$ 为联合 pdf 为 $f(x,y)$ 的二元随机向量. 令 $U=aX+b$、$V=cY+d$，其中 $a,b,c,d$ 为固定常数，且 $a>0,c>0$. 证明 $(U,V)$ 的联合 pdf 为
>
> $$
> f_{U,V}(u,v)=\frac1{ac}f\left(\frac{u-b}a,\frac{v-d}c\right).
> $$

## 提示

> [!hint]- 提示
> 逆变换的Jacobian是对角矩阵。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 逆变换为$x=(u-b)/a,y=(v-d)/c$，导数矩阵$\operatorname{diag}(1/a,1/c)$，绝对行列式$1/(ac)$。对任意可测区域$B$，换元给
> $$
> P((U,V)\in B)=\iint_Bf((u-b)/a,(v-d)/c)\frac{du\,dv}{ac},
> $$
> 故被积函数为所求密度，支持为原支持的仿射像。本题不要求$X,Y$独立；这里“独立坐标”只指变换不混合两个坐标。若允许非零负$a,c$，因子改为$1/|ac|$；若任一为0，通常不存在二维密度。

## 相关概念

- [[01 - 概率论/概念/概率模型|概率模型]]
- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/条件概率|条件概率]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=190|印刷第159页／PDF物理第190页]]；教材信息与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。原题无星号。
- `source_status: verified`仅指本题题干、公式及所列来源定位已核对，不表示全章正文独立复证。解答写成不等于个人已完成练习，学习状态保持`not-started`；未实测Obsidian界面渲染。
