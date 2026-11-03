# 全书来源与覆盖记录

更新日期：2026-11-03. 本记录追踪译稿生产与来源核对，不记录个人学习或知识库习题归档进度. 原第1章试译是本项目历史阶段；下列范围与统计已更新为全书.

## 来源与版本

- 原件：`附件/books/Statistical Optimal Transport.pdf`，269个PDF物理页.
- 作者：Sinho Chewi、Jonathan Niles-Weed、Philippe Rigollet；Springer，2025.
- 原件SHA-256：`91E9CB41212ABC18B294283C19CA4B91F51920A532E5CC24B710A1481EEED272`. 本轮再次读取原件计算，与最初登记一致.
- 范围：前文、全部8章、附录A/B、全部330条书目、全索引及末尾出版方针，即原件物理1–269页.
- 方法：布局文本和内嵌数学TeX仅作检索/转录辅助；段落、公式、图形与纯图像页以原页为依据. 正文/附录分工均有逐页原图记录及独立交叉审阅.
- 模板沿用 `pdf-to-chinese-tex` 的个人笔记模板；章对应section，节对应subsection，按原书修改共享计数、中文环境名与引用名.

## 原页与当前译稿范围

以下译稿范围来自实际PDF审计 `full-pdf-audit.json`，不是按原页数推算. 页码均为PDF物理页；原书印刷页的准确定位另见分章计划与审阅记录，不使用全书统一偏移.

| 单元 | 原物理页 | 当前译稿物理页 | 译文文件 |
| --- | --- | --- | --- |
| 前文与目录 | 1–14 | 1–13 | frontmatter的5片段及主文档动态目录 |
| 第1章 | 15–50 | 14–43 | sections-tex/01-01.tex–01-08.tex |
| 第2章 | 51–90 | 44–75 | sections-tex/02-01.tex–02-10.tex |
| 第3章 | 91–108 | 76–90 | sections-tex/03-01.tex–03-08.tex |
| 第4章 | 109–133 | 91–110 | sections-tex/04-01.tex–04-06.tex |
| 第5章 | 134–162 | 111–134 | sections-tex/05-01.tex–05-10.tex |
| 第6章 | 163–198 | 135–160 | sections-tex/06-01.tex–06-08.tex |
| 第7章 | 199–222 | 161–179 | sections-tex/07-01.tex–07-05.tex |
| 第8章 | 223–239 | 180–193 | sections-tex/08-01.tex–08-05.tex |
| 附录A | 240–246 | 194–199 | sections-tex/A-01.tex–A-03.tex |
| 附录B | 247–249 | 200–201 | sections-tex/B-01.tex |
| 参考文献 | 250–265 | 202–231 | bib/references-full.bib |
| 索引 | 266–267 | 232–233 | 正文index、backmatter/index-crossrefs.tex及动态索引 |
| 出版方针 | 268–269 | 234–235 | backmatter/publisher-policy.tex |

## 覆盖与核对入口

`manifest-full.json`登记正文/附录64个片段，各输入一次；全展开输入共71个文件，另含前文5个及后文2个. 全书保留166个编号陈述、177个数字公式、13个命名公式，另1个A_j特殊标记、86处proof、71道章末习题（全部分题）、9幅编号图（含前言图1）及330条书目. 这些数量是覆盖对账的辅助，不能单独证明翻译忠实.

- 第1章：review-11-12、review-13-14、review-15-16、review-exercises及相应cross-review记录.
- 第2–8章：plan-ch02–08、review-ch02–08、cross-review-ch02–08；第3/4章另有independent-review-ch03/ch04.
- 前后文与附录：plan-front-appendices、cross-review-front-back、cross-review-appendices.
- 索引：full-index-plan.json、full-index-anchor-report.json、cross-review-index；100个逻辑词条、104次写入，使用译稿真实页码.
- 成品：full-static-check.json、full-pdf-audit.json及visual-full-001-080、081-160、161-201、202-235四份视觉报告.

纯图像原物理3页已实际查看并转录暑期学校介绍、支持机构、网址及联系人；未误当空页. 图保留原PDF矢量内容或原图像，图注翻译；目录与索引重建为译稿真实页码. 源疑误在分章审阅及交付核验说明中可见保留，不静默修成译者结论. 第1章试译34页、22条摘录书目及其旧manifest仅为历史，不作为全书当前范围.
