---
title: "书籍目录与阅读路线"
tags:
  - index
aliases:
  - "Book Catalog"
  - "Reading Guide"
created: 2026-10-24
updated: 2026-10-24
---

# 书籍目录与阅读路线

本目录目前有 **17 份 PDF：14 份教材／讲义／题集与 3 份配套答案册**。本说明按“已有一些基础，希望尽快进入深度学习与现代生成模型”的目标安排；阅读建议是本库的选读方案，不是作者规定的先修顺序，也不表示已经完成学习。

**已确定从 UDL 开始，以 Bishop 补概率建模和推导，再接 MIT 的流匹配与扩散讲义。现有资料足够启动这条路线，不必先通读所有概率统计书。** 用户手头有英文纸质版；具体印次、纸书页码及其与附件在线稿的对应关系尚未核对，台账先以附件英文 PDF 为来源锚点。

相关入口：[[00 - 首页/来源台账|来源台账]]、[[06 - 深度学习/深度学习导航|深度学习]]、[[05 - 概率模型与推断/概率模型与推断导航|概率模型与推断]]。

## 一、这些书是否够用

| 目标 | 当前覆盖与建议 |
| --- | --- |
| 神经网络、训练、评估、Transformer 与生成模型的基础 | 已选 UDL 为主线，Bishop 用于对照；按主题推进。 |
| 概率论与数理统计基础 | Ross、Grimmett–Stirzaker 与 Casella–Berger 已相当充足；按问题回查，避免多本基础书同步从头读。 |
| 流匹配与扩散模型入门 | 已有 MIT 专题讲义；结合配套实验，适合在掌握基本网络训练后进入。 |
| 最优传输的统计理论 | 已有研究生层次的 Statistical Optimal Transport；适合专题深入，不是入门深度学习的前置关卡。 |
| 传统统计学习、模型比较与数据分析 | 已补 R 版 ISLR 第二版和 ESL 第二版，通用模型比较与统计学习的资料缺口已补上；Python 版 ISLP 尚未入库，可在需要 Python 实验时选用。 |
| 系统的概率机器学习与推断 | 已补 Murphy Advanced Topics，可按图模型、贝叶斯计算、变分推断或生成模型专题查阅；入门册尚未入库，不必为开始 UDL 额外等待。 |
| 优化、信息论、代码实现与实验习惯 | 已补 Boyd 凸优化、Cover–Thomas 信息论及其答案册；数学参考已更充足，配合 UDL notebooks 和实际实验使用。 |
| 因果推断、系统时间序列、完整强化学习课程 | Murphy 和现有随机过程教材提供部分入口；当前没有单独建立这些方向的完整课程或实践路线，选定专题后再规划。 |

教材适合建立稳定的概念框架。若目标是具体研究问题，还需沿专题讲义的参考文献阅读论文、核对代码与评价方案；本书单不宣称覆盖截至某日的全部研究前沿。

## 二、现有文件与用途

以下版本信息优先依据本地 PDF 的题名页、版权页与目录。PDF 页数指实际文件的物理页数，不等于印刷页码，也不表示已核查全书完整性。每项的核对位置与边界见对应来源笔记。

| 来源 | 本地文件 | 版本与物理页数 | 建议用途 |
| --- | --- | --- | --- |
| [[00 - 首页/教材归档/DS001 - Understanding Deep Learning\|DS001]] | [Understanding Deep Learning（UDL）](<UnderstandingDeepLearning_02_09_26_C.pdf>)，Simon J. D. Prince | 原书 2023；本地题名页 2026-02-08；541 页 | **当前主线**。从网络、损失与训练进入，再选 Transformer 或生成模型；配合作者 notebooks。 |
| [[00 - 首页/教材归档/DS002 - UDL 学生答案册\|DS002]] | [UDL 学生答案册](<UDL_Answer_Booklet_Students.pdf>)，Simon Prince | 2026-02-08；81 页 | 只含部分章末题的答案；独立尝试后查阅。 |
| [[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts\|DS003]] | [Deep Learning: Foundations and Concepts](<Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf>)，Christopher M. Bishop、Hugh Bishop | 2024；656 页 | **对照与深化**。补似然、概率、决策、采样和潜变量之间的联系。 |
| [[00 - 首页/教材归档/DS004 - Bishop 深度学习答案册\|DS004]] | [Bishop 深度学习答案册](<Concepts_in_Deep_Learning_Solutions_v1.0.pdf>) | Version 1.0；110 页 | 明确只覆盖主书第 2–10 章；不是全书答案。 |
| [[00 - 首页/教材归档/DS005 - 流匹配与扩散模型导论\|DS005]] | [An Introduction to Flow Matching and Diffusion Models](<mit_An Introduction to Flow Matching and Diffusion Models.pdf>)，Peter Holderrieth、Ezra Erives | 本地页首标注 MIT 6.S184、2026；84 页 | **专题进阶**。普通／随机微分方程、流匹配、得分匹配、引导与生成模型；结合课程 labs。 |
| [[00 - 首页/教材归档/DS006 - Statistical Optimal Transport\|DS006]] | [Statistical Optimal Transport](<Statistical Optimal Transport.pdf>)，Sinho Chewi、Jonathan Niles-Weed、Philippe Rigollet | Springer，2025，LNM 2364；269 页 | **理论专题**。Wasserstein 距离估计、熵正则化、梯度流等；研究问题需要时进入。 |
| [[00 - 首页/教材归档/DS007 - A First Course in Probability\|DS007]] | [A First Course in Probability](<A First Course in Probability, Sheldon Ross, 8ed, Prentice Hall, 2010.pdf>)，Sheldon Ross | 第 8 版，2010；545 页 | 概率基础回查与练习；已有基础者选读。 |
| [[00 - 首页/教材归档/DS008 - Introduction to Probability Models\|DS008]] | [Introduction to Probability Models](<Introduction to Probability Models.pdf>)，Sheldon M. Ross | 第 13 版，2024；859 页 | 随机过程与应用建模；不必作为神经网络入门的先修全书。 |
| [[00 - 首页/教材归档/DS009 - Probability and Random Processes\|DS009]] | [Probability and Random Processes](<Grimmett&Stirzaker--Probability and Random Processes  Third Ed(2001).pdf>)，Geoffrey R. Grimmett、David R. Stirzaker | 第 3 版，2001；608 页 | 概率与随机过程的理论补充，和 Ross 按风格择一主用。 |
| [[00 - 首页/教材归档/DS010 - One Thousand Exercises in Probability\|DS010]] | [One Thousand Exercises in Probability](<Grimmett&Stirzaker-1000 Probability.pdf>)，Geoffrey R. Grimmett、David R. Stirzaker | 首次出版 2001；448 页 | 概率习题与解答参考；当前只登记书目，未逐题归档。 |
| [[00 - 首页/教材归档/DS011 - Statistical Inference\|DS011]] | [Statistical Inference](<George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf>)，George Casella、Roger L. Berger | 第 2 版（2001）的 2024 CRC 重印；566 页 | 估计、检验与统计推断；需要理论背景时回查。 |
| [[00 - 首页/教材归档/DS012 - Probabilistic Machine Learning Advanced Topics\|DS012]] | [Probabilistic Machine Learning: Advanced Topics](<Probabilistic Machine Learning Advanced Topics.pdf>)，Kevin P. Murphy | 2023；在线稿 2025-12-10，前言另记 2026-01 第二次印刷；1370 页 | **专题参考**。补概率推断、生成模型、决策与因果；围绕 UDL 中的具体问题查阅。 |
| [[00 - 首页/教材归档/DS013 - Introduction to Statistical Learning R\|DS013]] | [An Introduction to Statistical Learning: with Applications in R（ISLR）](<ISLR.pdf>)，Gareth James、Daniela Witten、Trevor Hastie、Robert Tibshirani | R 版第 2 版；2023-06-21 更正印刷；原出版年待核；615 页 | **统计学习伴读**。回归、分类、重采样与模型比较，实验使用 R；不是 Python 版 ISLP。 |
| [[00 - 首页/教材归档/DS014 - The Elements of Statistical Learning\|DS014]] | [The Elements of Statistical Learning（ESL）](<ESLII_print12.pdf>)，Trevor Hastie、Robert Tibshirani、Jerome Friedman | 第 2 版；2017-01-13 更正第 12 次印刷；原出版年待核；764 页 | **统计学习深化**。按需查线性模型、正则化、核方法、树、集成与高维问题。 |
| [[00 - 首页/教材归档/DS015 - Elements of Information Theory\|DS015]] | [Elements of Information Theory](<Elements of information theory.pdf>)，Thomas M. Cover、Joy A. Thomas | 第 2 版，2006；758 页 | **信息论参考**。熵、相对熵、互信息、编码与容量；与学习目标相关时查阅。 |
| [[00 - 首页/教材归档/DS016 - 信息论答案册\|DS016]] | [信息论基础答案册](<solution_Elements of Information Theory.pdf>)，Thomas M. Cover、Joy A. Thomas | 对应第 2 版；2006-10-17；397 页 | 来源前言自述提供全书题目答案；本库尚未逐题验证其完整性或正确性。 |
| [[00 - 首页/教材归档/DS017 - Convex Optimization\|DS017]] | [Convex Optimization](<bv_cvxbook.pdf>)，Stephen Boyd、Lieven Vandenberghe | 2004 年初版；2009 年第 7 次更正印刷；730 页 | **优化参考**。凸性、对偶、最优性条件和算法；不要求先通读再学 UDL。 |

## 三、先读 UDL，还是 Bishop

这里的 Bishop 指附件中的 **Deep Learning: Foundations and Concepts（2024）**，不是较早的 Pattern Recognition and Machine Learning（PRML）。

| 比较项 | UDL | Bishop |
| --- | --- | --- |
| 展开方式 | 先讲监督学习、浅层／深层网络，再讲损失、拟合、梯度、评估和正则化。 | 在导论后先讲概率与分布，再连接回归、分类、深层网络及现代架构。 |
| 配套实践 | 作者站提供随章节的 Python notebooks，便于读完就动手。 | 正文结合图、公式与算法框解释建模和算法；也适合推导与习题训练。 |
| 当前最合适的角色 | 用于尽快建立“模型—目标—训练—评价”的完整流程。 | 用于补清“为什么这个损失／分布／推断方法成立”。 |
| 可优先选它的情况 | 想先跑通模型，再逐步加深数学联系。 | 已熟悉似然、矩阵微分和基本网络训练，且更喜欢概率建模的叙述。 |

**本库建议：UDL 为主，Bishop 按主题查阅。** 这是针对当前目标的判断，不是对两书质量作高低排序。若发现 UDL 前几章已经很熟，快速检查后直接进入损失、训练与评价即可。

### 开始前的自查

能够说明矩阵乘法的维度、用链式法则求简单导数、理解条件概率与期望，就可以边读边做。高斯似然与平方误差的联系可以在 UDL 第 5 章边学边补。卡在哪里，就回查 UDL 附录 B／C、Bishop 第 2–3 章或概率教材的对应内容；不要求先完成整套概率统计课程。

若 Python 与张量运算还不熟，先完成一个小模型的完整训练和评价，再增加架构复杂度。

## 四、面向主题的阅读路线

下面的章号已对照本地两本深度学习教材目录；具体公式与习题以相应来源笔记和教材台账的核对范围为准。两书不是逐章一一对应，Bishop 栏表示相关参考内容。

| 阶段 | UDL 主线 | Bishop 对照 | 建议完成的任务（尚未执行） |
| --- | --- | --- | --- |
| 快速确认基础 | 第 1 章浏览，第 2–4 章按熟悉程度选读 | 第 4–6 章 | 能画出小型网络、写明输入输出维度，并解释模型和参数的区别。 |
| 训练与评价核心 | **第 5–9 章优先**：损失、拟合、梯度与初始化、性能、正则化 | 第 4–5、7–9 章及第 6 章误差函数一节；概率疑问回查第 2–3 章 | 训练一个小型分类器；保留训练／验证划分，画学习曲线，说明如何选超参数。 |
| 现代架构 | 第 10–11 章卷积与残差；**第 12 章 Transformer** | 第 10、12 章及第 9 章残差连接一节 | 实现或补全自注意力的小例子，检查张量维度；文本任务再检查因果掩码。 |
| 生成模型 | 第 14 章总览，随后第 16–18 章流模型、VAE 与扩散 | 第 14–16、18–20 章按需查阅 | 能解释变量变换、潜变量、证据下界（ELBO）与去噪训练的不同角色。 |
| 进入专题 | 接 MIT 讲义第 1–6 节；离散扩散第 7 节按兴趣选读 | 第 20 章作对照 | 先复现课程的低维例子或 lab，说明采样器、步长及评价方式。 |

- **如果更想做大语言模型（large language model，LLM）**：优先完成训练与评价核心，再读 Transformer；后续围绕分词、自回归、微调和评价补课程／论文，不必先读完整个生成模型部分。
- **如果更想做图像生成、扩散与流匹配（flow matching）**：完成训练核心，了解卷积与残差后，按“无监督总览 → 流模型／VAE／扩散 → MIT 讲义”推进。归一化流（normalizing flow）与流匹配有关联，但不是同一个训练方法。
- **如果目标已经明确是流匹配，想先进入核心方法**：完成训练核心并补齐所需概率知识后，也可直接进入 MIT 第 1–4 节，先做低维例子；在阅读潜空间图像生成时，再按需补 VAE 等内容。上表保留的是较系统的选读路线。
- UDL 第 13 章图神经网络、第 15 章 GAN、第 19 章强化学习可按方向选读；第 20–21 章用于认识理论问题与技术影响。
- Statistical Optimal Transport 可先从第 1 章建立语言，再按统计估计或梯度流的兴趣选读。它不是阅读 MIT 讲义的必经前置材料。

### 第一轮如何用书

每个主题先读 UDL 正文，再独立尝试一两道概念／推导题并完成对应 notebook；只有出现具体疑问时，再查 Bishop 或基础教材。若要记入知识库，先登记来源，题目与答案核对原页后再归档。当前归档与试运行范围以来源台账和 UDL 教材台账为准；本节建议本身不计入个人学习进度或实验结果。

## 五、补充资料的当前状态

新增资料已登记为 `DS012`–`DS017`。下表区分已入库参考书与尚未入库的可选资料；当前仍以 UDL 为主线，不要求同时开读。官方链接沿用 2026-10-24 已核对的参考入口，本轮新增版本信息以本地原页为准。

| 状态 | 资料与官方入口 | 当前用途 |
| --- | --- | --- |
| ISLR、ESL 已入库；ISLP 可选 | **ISLR／ISLP**：[官方站](https://www.statlearning.com/)；ESL 见 DS014 | 当前先用已入库的 R 版 ISLR 和 ESL 理解统计学习。若需要 Python 配套实验，再考虑 ISLP；不影响 UDL 主线。 |
| 进阶册已入库；入门册可选 | Kevin P. Murphy，**Probabilistic Machine Learning: Advanced Topics／An Introduction**：[进阶册](https://probml.github.io/pml-book/book2.html)、[入门册](https://probml.github.io/pml-book/book1.html) | 先按具体问题查已入库进阶册；入门册尚未入库，出现整体框架缺口时再选用。 |
| 已入库，按数学需求查阅 | Stephen Boyd、Lieven Vandenberghe，**Convex Optimization**：[作者课程站](https://web.stanford.edu/~boyd/cvxbook/) | 补凸性、对偶与最优性条件；适合深化优化与最优传输。凸优化结论不能直接套用于所有神经网络训练。 |
| 已入库，按信息论需求查阅 | Cover、Thomas，**Elements of Information Theory** 及答案册，见 DS015–DS016 | 深入熵、KL 散度与信息论联系时选读；不新增整书先修要求。 |
| 尚未入库，编程欠缺时选用 | **Dive into Deep Learning（D2L，动手学深度学习）**：[官方站](https://d2l.ai/) | 先使用 UDL 配套 notebooks；需要更多实现参考时再查 D2L，不要求另开一条全书阅读任务。 |

“经典”解决稳定基础，“现代专题资料”连接具体研究方向。当前书目已经覆盖统计学习、概率推断、优化和信息论等主要参考需求，接下来围绕 UDL 的实际问题使用这些资料即可。

## 六、版本与使用边界

1. **UDL 文件名与题名页日期不一致。** 本地文件名为 `UnderstandingDeepLearning_02_09_26_C.pdf`，题名页写 2026-02-08，作者网页的下载入口标注 09 Feb 2026；本库分别记录，不根据文件名猜成 9 月版本。
2. **答案册有覆盖限制。** UDL 学生答案册自述仅含选定题目，并提醒仍可能有错误；Bishop Version 1.0 的封面与说明明确为第 2–10 章。答案出处不等于已核验正确性。
3. **MIT 本地材料按 2026 页首登记。** 同名 arXiv 记录首次发表于 2025；不能把该记录的版本、页数或章号自动移植到本地文件。
4. **最优传输书的副标题 2019 不是本地出版年份。** 本地版权页为 2025，系列为 Lecture Notes in Mathematics 2364。
5. **不从文件名认定教材版次。** 尤其是再版／重印文件，应以书内题名页、版权页为准；原文件名保留，便于追溯。
6. 本书目登记集中核对书目信息、前言、目录与答案册适用范围，来源状态为 `partially-verified`。具体正文、证明、答案或习题归档的核对范围另见各来源笔记和教材台账，书目登记不代表全书已核验。
7. **Casella–Berger 是第二版的重印。** 本地书籍介绍页明确说明重印 2001 年第二版，版权页列 2024 年 CRC 出版信息；版权页的馆藏编目写 Roger W.，与扉页及版权正文的 Roger L. Berger 不一致，已在来源笔记保留该差异。
8. 两份 Grimmett–Stirzaker 文件的文本层有 OCR 字符错误；可用来搜索，精确公式与题号须看原始页面。
9. **ISLR 与 ESL 分别记录更正印刷信息。** ISLR 扉页图像写 2023-06-21 更正印刷，ESL 封面图像写 2017-01-13 更正第 12 次印刷；两者均缺常规版权页，原出版年尚未核定，来源元数据中的 `year` 保持 `null`。这两项图像注记没有进入文本抽取层。
10. **Murphy 的三个日期分别保留。** 原版权年为 2023，在线页脚写 2025-12-10，前言又注明 2026-01 第二次印刷；不将这些日期合并为新版本年份。
11. **信息论答案册的完整性仅为来源自述。** 尚未对主书题号集合和该答案册逐题核对；日期、目录和前言核对不代表答案内容全部正确。
12. **UDL 英文纸书尚未对齐印次。** 用户已确认持有英文纸质版；具体印次、纸书页码与本地在线稿的对应关系仍待实际核对，不自动套用本地 PDF 的页码偏移。

官方对照：[UDL](https://udlbook.github.io/udlbook/)、[Bishop](https://www.bishopbook.com/)、[MIT 课程](https://diffusion.csail.mit.edu/)、[同名 MIT 讲义的 arXiv 记录](https://arxiv.org/abs/2506.02070)、[Statistical Optimal Transport 出版社页](https://link.springer.com/book/10.1007/978-3-031-85160-5)。

## 七、后续维护

- 新增 PDF 时先检查是否重复版本，再按 [[模板/来源笔记模板|来源笔记模板]] 登记作者、版本、路径和核对范围，并更新本表。
- 引用具体内容时，同时记印刷页与 PDF 物理页；不同文件可能省去空白页，不能假定整书采用固定页码偏移。
- 来源核对、习题归档与个人学习进度分别维护。保留原始文件，不把建议路线标成已完成。
- 本目录以本文件作为完整说明；原 `readme.txt` 保留简短入口。库级改动记录见 [[CHANGELOG|完整更新历史]]。
