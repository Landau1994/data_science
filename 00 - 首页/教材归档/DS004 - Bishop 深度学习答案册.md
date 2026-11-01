---
title: "Bishop 深度学习答案册（Solutions to Exercises）"
tags:
  - source
status: not-started
source_id: DS004
source_kind: solutions
source_status: partially-verified
author: ["Christopher M. Bishop","Hugh Bishop"]
year: null
edition: "Version 1.0；对应主书 2024 年版本；答案册发布日期未明确"
location: "附件/books/Concepts_in_Deep_Learning_Solutions_v1.0.pdf"
url: "https://www.bishopbook.com/"
pdf_pages: 110
checked: 2026-11-01
updated: 2026-11-01
created: 2026-10-24
---

# Bishop 深度学习答案册（Solutions to Exercises）

## 文献信息

- 来源编号：DS004。
- 作者：Christopher M. Bishop、Hugh Bishop。
- 版本：Version 1.0；对应主书 2024 年版本；答案册发布日期未明确。
- 本地文件：[[附件/books/Concepts_in_Deep_Learning_Solutions_v1.0.pdf|打开 PDF]]；物理页数 110。
- 官方入口：[作者／出版／课程页面](https://www.bishopbook.com/)（访问：2026-10-24）。

## 内容范围

Deep Learning: Foundations and Concepts 的配套解答。封面、说明与目录均限定为主书第 2–10 章，包括概率、分布、回归、分类、网络与训练等内容。

## 已核对位置

PDF 物理页从文件第一面起按 1 计数；没有印刷页码的页面明确注明。下表只声明实际核对范围，不代表已核验整书数学内容。

| 内容 | 印刷页 | PDF 物理页 |
| --- | --- | --- |
| 封面、版本与章范围 | 未印页码 | 1 |
| 版本及覆盖范围说明 | 2 | 2 |
| 目录 | 3 | 3 |
| 第2章解答起止及第3章起始边界（仅确认覆盖范围） | 4、25–26 | 4、25–26 |
| 2.39–2.41解答，含2.40先验订正说明和式(87)–(95) | 23–25 | 23–25 |

## 关键术语

- 习题解答（solutions to exercises）：资料使用用语，保留原词，不建立学科概念占位。
- 版本（version）：资料使用用语，保留原词，不建立学科概念占位。

## 来源问题与边界

不能据说明中对将来完整答案册的表述，认定当前文件已含全书答案。年份保持 null，避免将主书出版年冒充此答案册的实际发布日期。第2章解答位于印刷／PDF4–25，仅逐题读取了2.39–2.41；其他题未因目录或边界核对而视作答案已核验。

2.40的说明建议将主书先验中的 convex 改为 concave，本库保留两种先验分别作答。答案册式(90)以单次边际概率0.42构造十次独立二项似然，但十次观测共享同一个未知硬币朝向；正确证据应是两项二项似然的加权和。因此其后验0.825与预测0.565未被采作正确结果，具体独立推导见DS003的2.40习题。

`source_status: partially-verified` 只指上述局部核对；`status: not-started` 表示个人学习状态。主书习题采用独立推导，答案册仅按实际读取范围作对照。

## 相关入口

[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Bishop 主书]]。

[[附件/books/README|书籍目录与阅读路线]]。

