---
title: "应用数学家的最优运输（Optimal Transport for Applied Mathematicians）"
tags:
  - source
status: not-started
source_id: DS026
source_kind: book
source_status: partially-verified
archive_status: source-audit-pending
archived_chapters: []
archived_exercise_count: 0
author: "Filippo Santambrogio"
year: 2015
edition: "Progress in Nonlinear Differential Equations and Their Applications 87；2015年出版版"
location: "附件/books/Santambrogio 2015 Optiomal Transport For Applied Mathematicians.pdf"
url: "https://doi.org/10.1007/978-3-319-20828-2"
pdf_pages: 376
checked: 2026-11-03
created: 2026-11-03
---

# 应用数学家的最优运输（Optimal Transport for Applied Mathematicians）

## 文献信息

- 作者：Filippo Santambrogio。
- 完整题名：Optimal Transport for Applied Mathematicians: Calculus of Variations, PDEs, and Modeling。
- 丛书：Progress in Nonlinear Differential Equations and Their Applications，第87卷；Springer International Publishing Switzerland，2015。
- 纸本ISBN：978-3-319-20827-5；电子书ISBN：978-3-319-20828-2。
- 本地原件：[[附件/books/Santambrogio 2015 Optiomal Transport For Applied Mathematicians.pdf|原书PDF（376物理页）]]。保留原文件名，包括其中的拼写。
- 书目信息按题名／版权原页核对；作者站的2015年5月稿不作为本次翻译的底本。

## 内容范围

最优运输（optimal transport）的原问题、对偶、运输映射、一维构造、极限成本、最小流、Wasserstein空间、数值方法、测度上的泛函与梯度流。作者前言明确主要采用确定性与变分法视角，要求测度论和泛函分析背景；第6章不提供收敛证明或完整实现细节。

## 已核对位置

PDF物理页按文件第一面起计。分页中有省去的印刷空白页，禁止把第1章偏移用于全书。

| 实际位置 | 印刷页 | PDF物理页 | 本轮用途 |
| --- | --- | --- | --- |
| 封面、丛书、题名、版权、献词 | 无页码 | 1–7 | 版本与前置内容 |
| 前言、最优运输导论、致谢、目录、记号 | vii–xxvii，含空白页 | 8–28 | 建立全书结构与译名 |
| 第1章：原问题与对偶问题 | 1–57 | 29–85 | 首批翻译，核验进度见下方入口 |
| 第2章起始边界 | 59 | 86 | 确认第1章终点 |
| 完整原编号书目300条 | 339–350 | 362–373 | 原文转录、数学字符与编号核对 |

其余章节的起始标题与目录位置已定位，未因此宣称其正文已核对。

## 中文翻译

2026-11-03按用户要求启动全书翻译。沿用本库已有中文数学排版样式，首批已完成前置内容与第1章，形成94页中文PDF；全书翻译仍在进行中。

- [[附件/翻译/Optimal Transport for Applied Mathematicians_Chn/Optimal Transport for Applied Mathematicians_Chn.pdf|中文PDF（前置内容与第1章，94页）]]。
- [[附件/翻译/Optimal Transport for Applied Mathematicians_Chn/核验说明|可编辑源稿、实际完成范围与检查结果]]。
- [[附件/翻译/Optimal Transport for Applied Mathematicians_Chn/原文疑误与核对边界|原文疑误与核对边界]]。

保留原作者、章节、陈述、知识框、公式、图件、文献及习题引用编号。原文疑误照录并另记；不添加独立证明或习题解答。

## 关键术语

- [[03 - 线性代数与优化/概念/最优传输|最优运输／最优传输]]（optimal transport）。
- [[03 - 线性代数与优化/概念/对偶|对偶]]（duality）。
- [[03 - 线性代数与优化/概念/Wasserstein 距离|Wasserstein距离]]（Wasserstein distance）。
- [[03 - 线性代数与优化/概念/梯度流|梯度流]]（gradient flow）。

## 来源问题与边界

原件376个物理页；正文与书后印刷页截至353，前置材料使用罗马页码且文件省略部分印刷空白页。本次不依据作者公开草稿、文件名或出版社总页数补造页面。翻译完成、原书数学结论的独立核验、习题归档、个人学习进度分别记录。

## 学习与阅读

个人学习保持`not-started`。下表列实际目录及章节起始定位；“未开始”表示个人阅读状态，不表示翻译状态。

| 章 | 中文／英文章名 | 起始印刷页／PDF物理页 | 个人阅读 |
| --- | --- | --- | --- |
| 1 | 原问题与对偶问题／Primal and dual problems | 1／29 | 未开始 |
| 2 | 一维问题／One-dimensional issues | 59／86 | 未开始 |
| 3 | L1与L∞理论／L1 and L∞ theory | 87／113 | 未开始 |
| 4 | 最小流／Minimal flows | 121／146 | 未开始 |
| 5 | Wasserstein空间／Wasserstein spaces | 177／201 | 未开始 |
| 6 | 数值方法／Numerical methods | 219／243 | 未开始 |
| 7 | 概率测度上的泛函／Functionals over probabilities | 249／273 | 未开始 |
| 8 | 梯度流／Gradient flows | 285／309 | 未开始 |

此处章名沿用目录短标题，原章首页较长的标题在译稿中保留。

## 习题归档

本轮尚未建立独立习题笔记；前言所述69题尚未逐题对账。全书归档状态保持`source-audit-pending`。

```dataview
TABLE WITHOUT ID
  source_chapter AS "章节",
  source_exercise AS "原书题号",
  file.link AS "习题",
  choice(difficulty = "beginner", "入门", choice(difficulty = "intermediate", "中级", "进阶")) AS "难度",
  choice(status = "completed", "已完成", choice(status = "in-progress", "正在学习", "尚未开始")) AS "学习状态"
FROM #exercise
WHERE this.source_id AND source_id = this.source_id
SORT number(source_chapter) ASC, number(split(source_exercise, "[.]")[1]) ASC
```
