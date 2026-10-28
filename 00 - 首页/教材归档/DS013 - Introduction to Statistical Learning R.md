---
title: "统计学习导论：R 应用（An Introduction to Statistical Learning: with Applications in R）"
tags:
  - source
  - exercise-archive
  - reading-ledger
status: not-started
source_id: DS013
source_kind: book
archive_status: in-progress
archived_chapters: []
partially_archived_chapters: [6]
archived_exercise_count: 9
source_status: partially-verified
author: ["Gareth James","Daniela Witten","Trevor Hastie","Robert Tibshirani"]
year: null
edition: "R 版第二版；扉页图像注明 2023-06-21 更正印刷；原出版年待核定"
location: "附件/books/ISLR.pdf"
url: "https://www.statlearning.com/"
pdf_pages: 615
checked: 2026-10-25
updated: 2026-10-25
created: 2026-10-24
---

# 统计学习导论：R 应用（An Introduction to Statistical Learning: with Applications in R）

## 文献信息

- 来源编号：DS013。
- 作者：Gareth James、Daniela Witten、Trevor Hastie、Robert Tibshirani。
- 版本：R 版第二版；扉页图像注明 2023-06-21 更正印刷；原出版年待核定。
- 本地文件：[[附件/books/ISLR.pdf|打开 PDF]]；物理页数 615。
- 官方参考入口：[作者／课程书页](https://www.statlearning.com/)；链接沿用书目说明，本轮以本地文件为核对依据。

## 内容范围

前言强调统计学习的应用与方法理解，配套实验使用 R。目录涵盖回归、分类、重采样、模型选择、非线性方法、树、支持向量机、深度学习、生存分析、无监督学习与多重检验。可补充 UDL 之外的统计学习模型比较与数据分析。

## 已核对位置

PDF 物理页从文件第一面起按 1 计数；下表区分印刷页码与物理页。没有显示页码的页面明确注明，未据此假定整书固定偏移。

| 内容 | 印刷页 | PDF 物理页 |
| --- | --- | --- |
| 扉页：作者、R 版第二版与图像中的更正印刷日期 | 未印页码 | 1 |
| 前言：读者定位与 R 实验说明 | vii–viii（首面未显页码） | 3–4 |
| 目录 | ix–xv（首面未显页码） | 5–11 |
| 第 1 章起始页 | 1（本页未显页码） | 12 |
| §6.2.1 岭回归定义、截距与尺度；§6.2.2 Lasso 定义及约束形式 | 237–239、241–243 | 248–250、252–254 |
| 式 (6.12)–(6.15)：单位设计下岭解与软阈值 | 247–248 | 258–259 |
| §6.4 高维定义、最小二乘风险及解释与评价边界（未列页未作核对声明） | 262–264、266–267 | 273–275、277–278 |
| §6.5.2：`glmnet` 的 `alpha=0/1` 端点约定 | 275 | 286 |
| §6.6 全部编号题目页面：1–11，含本轮选题的完整分题 | 283–288 | 294–299 |

### 本轮概念正文核对入口

以下笔记逐项记录实际读过的定义或应用位置；书目核对、局部正文核对、独立推导与个人学习状态分别维护。

- [[02 - 数理统计/概念/重采样#来源与证明状态|重采样的核对位置与证明边界]]
- [[04 - 统计学习/概念/模型选择#来源与证明状态|模型选择的核对位置与证明边界]]
- [[04 - 统计学习/概念/统计学习#来源与证明状态|统计学习的核对位置与证明边界]]

## 关键术语

- [[04 - 统计学习/概念/统计学习|统计学习]]（statistical learning）。
- [[02 - 数理统计/概念/重采样|重采样]]（resampling）。
- [[04 - 统计学习/概念/模型选择|模型选择]]（model selection）。
- [[04 - 统计学习/概念/岭回归|岭回归]]（ridge regression）。
- [[04 - 统计学习/概念/Lasso回归|Lasso回归]]（least absolute shrinkage and selection operator）。
- [[04 - 统计学习/概念/高维回归|高维回归]]（high-dimensional regression）。
- [[04 - 统计学习/概念/弹性网络|弹性网络]]（elastic net）：本书仅核对软件参数端点；正式定义与补充题依据 ESL，不能归作本书原题。
- R 实验（R lab）：资料使用用语，保留原词，不建立学科概念占位。

## 学习与归档

第 6 章“线性模型选择与正则化”（Linear Model Selection and Regularization）的原页有序题号为 6.1–6.11，共 11 题。本轮按正则化主题选取 **6.2–6.9、6.11，共 9 题**，对应本库 ML004–ML012；6.1 与 6.10 未归档，整章不标完成。选题集合的映射检查：预期 9、实际 9，缺失、重复、多余、无法解析均为 0；全章仍有 2 题不在本轮范围。

前六题附独立解析解答；6.6 实际生成了一维目标函数图。应用题 6.8、6.9、6.11 已用 [[工具/ISLR/islr_ch6_applied.R|独立 R 脚本]] 在 WSL Ubuntu 20.04.6、R 4.3.1 中实际运行，完整数值、图、数据快照、划分与环境见 [[工具/ISLR/README|运行说明与结果入口]]。`College`、`Boston` 来自本次临时安装的教材配套 `ISLR2 1.3.2`；没有用其他包的同名数据替代。结果只支持本次版本、随机性与评价设计，不是官方答案。脚本不改学习状态，不是每日题单生成器。

“高维方法”不表示这九题都设置了 $p>n$；其中多项式模拟与 College、Boston 练习用于学习相关工具。纸书／PDF 的题号与来源位置以每篇习题的字段及备注为准，动态表展示个人学习状态，归档不表示已学完。

### 习题归档

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

## 来源问题与边界

本地是 R 版 ISLR，不能按 Python 版 ISLP 登记；作者列表也不加入 Python 版作者 Jonathan Taylor。本地前置页缺常规版权页，2023-06-21 是扉页图像明确标出的更正印刷日期，不据此推断首次出版年份，因此 year 保持 null。该日期没有进入 pypdf 文本层，已查看原始页面。未逐章运行 R 实验，也未核对全部题目。

本条采用来源笔记模板的字段与结构。`source_status: partially-verified` 仅表示上述局部核对；`status: not-started` 未被当作读书完成记录。本轮运行了上述三道应用题的独立脚本，没有复现本书全套配套实验，也没有记录个人学习进度。

全文文本层未检出“elastic”或“elastic net”，并查看第 6 章全部原题页面，未发现单独的弹性网络编号题。相关的 [[04 - 统计学习/习题/习题 ML013 - 弹性网络的增广数据表示|增广数据练习 ML013]] 来源为 [[00 - 首页/教材归档/DS014 - The Elements of Statistical Learning|ESL 第 3 章第 30 题]]，不计入本书的九题。ISLR 第 6 章原题中的典型误差趋势、Lasso 不唯一等概括的适用条件，在各题解答与备注中显式讨论；英文原文保持。

## 相关入口

[[04 - 统计学习/统计学习导航|统计学习导航]]；[[00 - 首页/教材归档/DS014 - The Elements of Statistical Learning|统计学习原理]]。

[[附件/books/README|书籍目录与阅读路线]]。

