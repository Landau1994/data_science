# 《统计推断》中文译稿：来源覆盖记录

更新日期：2026-11-04. 这是翻译项目的技术核验记录，记录源页、输出文件与实际核对范围；不另建教材学习台账，也不改变个人学习状态. 当前阶段：全书翻译、语义索引应用、整合编译及最终PDF核验均已完成；最终输出696页，具体结果见根目录核验说明与报告.

## 权威来源

- 作者：George Casella、Roger L. Berger.
- 书名：*Statistical Inference*, Second Edition，Texts in Statistical Science.
- 版本：2001年第二版的2024年 Chapman & Hall/CRC 重印本. 不将重印年份当作重新修订的版次.
- 本地文件：`附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf`.
- PDF物理页数：566. SHA256：`52e6acfaceca3c7492d6436de2fe25c2b468a3fe74b47c7ecd0a5f130ace0707`，原登记见 `work/source-baseline.json`.
- 正文印刷页与PDF物理页相差31；书前使用罗马页码或无印刷页码. 下表明确区分两种页码.
- `pdftotext -layout` 提取全文，`work/source-layout.txt` 仅作检索、录入和对账辅助. 数学字体、正负号、上下标、分支、图表及疑难文字以实际渲染原页为准；没有用OCR置信度代替原图.

## 全部566页的连续覆盖

下表源页区间互不重叠，合计566页，无未登记页. “自审”指译写者逐页对照原图及译文；另人的独立复核范围在后文单列. 各章的无编号推导、例内计算、习题提示、原附答案和杂录不因没有独立环境而省略.

| 内容 | PDF物理页 | 原印刷页 | 页数 | 对应输出 | 原页核验依据 |
|---|---:|---|---:|---|---|
| 封面及书前全部材料 | 1–31 | 无页码及罗马页码至xxix，末页标志 | 31 | `frontmatter/00-*.tex`及主文件封面 | `front-cross-review.md`、`ch01c-audit.md`、`stage1-核验说明.md` |
| 第1章 概率论 | 32–68 | 1–37 | 37 | `sections-tex/01-00.tex`至`01-08.tex` | `ch01a-audit.md`、`ch01b-audit.md`、`ch01c-audit.md` |
| 第2章 变换与期望 | 69–100 | 38–69 | 32 | `chapters-tex/02.tex`、`sections-tex/02-*.tex` | `ch02-audit.md` |
| 第3章 常见分布族 | 101–144 | 70–113 | 44 | `chapters-tex/03.tex`、`sections-tex/03-*.tex` | `ch03-audit.md` |
| 第4章 多个随机变量 | 145–199 | 114–168 | 55 | `chapters-tex/04.tex`、`sections-tex/04-*.tex` | `ch04-audit.md` |
| 第5章 随机样本的性质 | 200–251 | 169–220 | 52 | `chapters-tex/05.tex`、`sections-tex/05-*.tex` | `ch05-audit.md` |
| 第6章 数据约简原则 | 252–282 | 221–251 | 31 | `chapters-tex/06.tex`、`sections-tex/06-*.tex` | `ch06-audit.md` |
| 第7章 点估计 | 283–332 | 252–301 | 50 | `chapters-tex/07.tex`、`sections-tex/07-*.tex` | `ch07-audit.md` |
| 第8章 假设检验 | 333–367 | 302–336 | 35 | `chapters-tex/08.tex`、`sections-tex/08-*.tex` | `ch08-manifest.json`及第8章独立复核记录 |
| 第9章 区间估计 | 368–407 | 337–376 | 40 | `chapters-tex/09.tex`、`sections-tex/09-*.tex` | `ch09-audit.md` |
| 第10章 渐近评价 | 408–451 | 377–420 | 44 | `chapters-tex/10.tex`、`sections-tex/10-*.tex` | `ch10-audit.md` |
| 第11章 方差分析与回归 | 452–497 | 421–466 | 46 | `chapters-tex/11.tex`、`sections-tex/11-*.tex` | `ch11-audit.md` |
| 第12章 回归模型 | 498–526 | 467–495 | 29 | `chapters-tex/12.tex`、`sections-tex/12-*.tex` | `ch12-audit.md` |
| 出版社重复标志 | 527 | 无印刷页码 | 1 | 以本记录说明，不另占译稿页 | 原图再次目视，见 `work/source-ledger-check/p527.png` |
| 计算机代数 | 528–533 | 497–502 | 6 | `backmatter/01-computer-algebra.tex`、`01-computer-algebra-b.tex` | `back-audit.md`、`back-independent-review.md` |
| 常见分布表及关系图 | 534–539 | 503–508 | 6 | `backmatter/02-distributions.tex` | 同上 |
| 参考文献 | 540–554 | 509–523 | 15 | `backmatter/03-references.tex`、`bib/references.bib` | `back-audit.md`及338项书目清单 |
| 出版社重复标志 | 555 | 无印刷页码 | 1 | 以本记录说明，不另占译稿页 | 原图再次目视，见 `work/source-ledger-check/p555.png` |
| 索引 | 556–566 | 525–535 | 11 | `backmatter/04-index.tex`及语义映射JSON | `back-audit.md`、各章索引映射核验记录 |

表内未加路径前缀的核验文件均位于 `work/`. 具体有序编号、每题分问、页锚点与图件来源在各章机器清单中；第2–4章使用 `chNN-object-inventory.json`，第5–12章使用 `chNN-manifest.json`，第1章另有分段static清单. 全书输入文件及对象汇总见 `work/book-static-manifest.json`.

## 书前、书后和装饰页的处理

封面保留书名、作者、版次和出版归属，按既有中文模板重排，不逐像素复制红色封面设计. 物理1页的封面和31、527、555页的标志在本次汇总中再次实际目视. 书前物理7、19、21、31页以及书后527、555页为重复出版社标志，出版信息保留一次，不重复描摹装饰图形. PDF中原有的读者高亮不当作作者正文样式复制. 这些处理没有删除独有数学正文.

原目录164个编号条目与10个无编号入口、表目录22项、图目录54项、例目录299项均保留其内容与原顺序. 原印页码与译稿页码分开处理；最终目录和索引的中文PDF页码已由实际编译目标生成并核验.

计算机代数保留全部8例及原Mathematica输入、输出. 原书例12.6.1–12.6.8确实位于这项无编号书后材料中，不据编号将它们移入第12章杂录. 历史代码未执行，原输出不是本次计算结果. 常见分布表共21条，含7个离散、14个连续分布及关系图. 参考文献338项保留原编号与资料；索引1071个分层词条、1174个页码定位和22处“见／另见”关系均已登记.

## 核对边界与独立复核

所有12章及书后实质内容均有实际逐页自审记录. 现有独立复核证据为：

- 书前物理2–23页由另一代理逐张对照；例目录24–30页由负责例目录的代理逐张核对并对账. 书前1–31页的完整首轮查看记录保存在`work/stage1-核验说明.md`中.
- 第1章章引及§1.1–1.2（物理32–47）与§1.3–1.6（47–62）分别完成异人逐段复核，见 `ch01a-cross-review.md`、`ch01b-cross-review.md`. §1.7–1.8的物理62–68页另由总编逐题回查，见`work/stage1-核验说明.md`.
- 第2章物理69–100页全部由总编独立再看原图并对照译文，见 `ch02-independent-review.md`.
- 第8章物理333–367页全部由 `source_inventory` 独立复核正文、公式、习题及译注，精确修订清单见 `ch08-manifest.json`. 本报告不把该章独立复核扩展为其他章已完成异人逐句复核.
- 计算机代数与分布表物理528–539页完成异人逐段复核，见 `back-independent-review.md`. 该记录不覆盖书目540–554页或索引556–566页的异人逐字复核.
- 第4章关联问题、第6章完备性反例、若干书目差异及全书索引落点另有专项复核. 专项核验只支持实际检查的问题，不能替代未执行的整章异人逐句核对.

第3–7、9–12章的完整原页自审与局部PDF检查已记录；没有声称这九章另有第二个人逐句检查全部正文. “来源已核对”也不表示全书数学结论均被独立证明.

## 编号、链接与疑误登记

章节使用section，原节使用subsection；定义、定理、引理、推论和例共享按原节重置的编号，公式、图、表另行编号，习题按章编号. 原书不常规的表号和书后例号以显式计数器保留，不为整齐而重编号.

实质正文物理32–526、书后528–554、556–566各有一次 `sourcepageanchor`，静态清单共533个唯一源页锚点. 书前31页、标志页527与555由本覆盖表登记，因此“533锚点”不等于漏掉33个源页. 跨页公式内部不插页锚，锚点靠近相应页首的自然边界.

书内引用使用 `autoref`、`eqref` 或必要的 `hyperref`. 原文误引的显示编号与对应真实目标可分开保留，并以译注说明. 文献元数据核对与书目跳转不代表已经阅读、复现全部被引论文. 原书书目页37个无对应语义的错位PDF链接已登记于 `work/source-bib-external-links.json`，未机械复制.

原文疑误、数学条件边界与译者独立计算分别记录于各章audit及可见“译注”脚注. 作者原脚注与新增译注分开统计. 不确定归属或尚未回查的外部文献保留“待核实”等限定，不把猜测写成作者正文.

最终整合稿全部696页已实际目视；修订后95个变化页均复检，其余页面像素相同后承接检查。1174个索引语义落点与实际PDF跳转检查通过，具体方法、文件哈希及警告见核验说明、compile-report.md与pdf-link-audit-report.md。本覆盖记录说明来源核验链条，不代替独立证明全书数学结论。
