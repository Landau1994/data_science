# 《统计推断》习题归档核对

教材的文献信息、章节进展、学习状态与归档结果只在[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]维护。本目录保留可重建的来源题号清单与只读核对工具，不另建学习台账。

`source-manifest.json`分别记录12章全部有序题号、归档范围和一题一笔记映射，原书共625题。第1–4章按概率工具归类，使用P前缀；第5–12章按统计推断工具归类，使用ST前缀。核对工具会分别报告范围内缺失、范围外待归档与整章是否完成，不能以部分范围内对账通过代替整章完成。

在知识库根目录运行（Python需要PyYAML）：

```powershell
python -X utf8 工具/StatisticalInference/archive_audit.py
python -X utf8 工具/StatisticalInference/content_audit.py
```

工具检查原PDF的SHA-256、来源题号与映射、重复／多余／无法解析项、主题与必需元数据、双语分题标号、callout结构及数学定界符。英文逐字转录、中文含义和证明正确性仍须人工对照原始页面；程序不代替来源核对，也不表示Obsidian界面渲染测试。

补充内容核对检查每篇唯一折叠解答、数学花括号与环境嵌套、意外控制字符及本库编号重复；它不将原题疑误改成程序“自动修正”。来源清单同时保留部分题的正文实核页、原文疑误与嵌套分问；逐题`source_refs`是具体定位入口。

原图1.2.1是原PDF物理38页中镖盘与图注的忠实裁切，供1.7、1.8独立阅读；来源与使用假设在题内说明。学习状态由用户实际学习后调整，本工具不写笔记或推进每日题单。

## 两道作图题的精确计算

[[工具/StatisticalInference/make_ch1_figures.py|图示生成脚本]]使用Python标准库精确计数，生成PGFPlots源稿与分数形式的CSV；加`--render`会调用XeLaTeX和Poppler输出附件中的矢量PDF及PNG。运行环境为Python3.10.6、TeX Live 2023，无随机抽样，不需要随机种子。

```powershell
python -X utf8 工具/StatisticalInference/make_ch1_figures.py --render
```

| 图示 | 已确定的模型与来源 | 精确数据 | 实际核验 |
| --- | --- | --- | --- |
| 习题1.30样本均值分布 | 原题印刷34／PDF65未给样本量；先给一般公式，再明示以独立等概率有放回抽6次为绘图示例 | [[工具/StatisticalInference/figures/exercise-1.30.csv|85个均值的精确概率]]；46656个有序样本 | 概率和为1，众数26／3、概率35／648；编译并目视PNG，标签与坐标完整 |
| 习题1.51累积分布函数 | 原题印刷36／PDF67，30台中5台缺陷，不放回抽4台 | [[工具/StatisticalInference/figures/exercise-1.51.csv|5个取值的pmf与cdf]] | 精确组合数和为27405；右连续阶梯与端点已检查，附上尾放大图以显示末次1／5481的跳跃 |

[[工具/StatisticalInference/figures/exact-checks.json|参数、环境与精确结果]]及同目录两份`.tex`保留重建依据。这些有限计算只支持所列模型；图中小数坐标用于显示，CSV保留精确分数。已检查独立图件，不宣称已检查Obsidian中的最终嵌入渲染。

## 第2–12章的计算与图示

剩余570题已归档，新增29组独立图示和原题2.12的忠实裁切。独立图均有PGFPlots源稿、矢量PDF及PNG；计算／模拟的数据与其参数保留在下列入口。图件目录中共31组独立PDF／PNG（含原第1章两组）与两幅原图裁切。图件哈希由来源清单核对，图内参数和适用范围在题内说明。

| 章节 | 实际运行与结果入口 | 图示依据 |
|---|---|---|
| 2、4 | [[工具/StatisticalInference/make_rest_figures.py|密度、累积量及Borel邻域重建]] | 第2章2.37使用稳定的累积量差公式；第4章4.61为指定ε的独立集合示意，非概率密度图。原2.12取自PDF物理95页 |
| 3 | [[工具/StatisticalInference/ch03_numeric_checks.py|数值核验]]；[[工具/StatisticalInference/ch03-numeric-results.json|实际结果]] | [[工具/StatisticalInference/ch03_figures.py|3.33–3.36四组图重建]] |
| 5 | [[work/DS011/ch05/computations.py|计算与模拟实现]]；[[work/DS011/ch05/results.json|实际结果]] | [[work/DS011/ch05/figures.py|5.53、5.54、5.66、5.68四组图重建]]；原始样本与方差重复值CSV在同目录 |
| 7 | [[工具/StatisticalInference/ch07_numeric_checks.py|确定性求根与EM]]；[[工具/StatisticalInference/ch07-numeric-results.json|实际结果]] | [[工具/StatisticalInference/ch07_figures.py|风险与LINEX两组图重建]] |
| 8 | [[附件/习题图/DS011/源码/第8章/figure-inventory.json|八组公式图清单与实核状态]] | 清单逐项链接对应TeX源稿和采样数据；保留功效、后验与损失风险图 |
| 9 | [[工具/StatisticalInference/compute_ch9.py|分位数与精确LR求解]]；[[工具/StatisticalInference/ch9-computations/results.json|结果与环境]] | [[工具/StatisticalInference/ch9-computations/exercise-9.18.tex|9.18四条二项概率曲线源稿]] |
| 10 | [[work/DS011/ch10/computations.py|确定性计算与模拟]]；[[work/DS011/ch10/results.json|结果]]；[[work/DS011/ch10/robust_simulation.py|稳健与Bootstrap模拟]]；[[work/DS011/ch10/robust-results.json|实际稳健结果]] | [[work/DS011/ch10/figures.py|五组图重建]]；原始模拟／重抽样CSV在同目录，[[work/DS011/ch10/verification.json|有限核验结果]]另存 |
| 11 | [[工具/StatisticalInference/ch11_numeric_checks.py|ANOVA、回归与缺失EM实现]]；[[工具/StatisticalInference/ch11-numeric-results.json|输入、收敛与直接MLE结果]] | 无题目要求独立作图；11.41同时保留条件与联合正态模型的区别 |
| 12 | [[工具/StatisticalInference/ch12-computations/README|模型、运行与结果说明]] | 三组Logistic／Probit／雀鹰拟合图的TeX与数据保留在附件源码中；16000行Bootstrap记录在计算目录 |

这些运行使用实际记录的Python、NumPy、SciPy、mpmath及TeX Live版本；模拟分别记录自己的随机种子和样本规模。不能把某一数值方法的输出、一次模拟覆盖或有限参数网格当作所有参数上的定理。第9章9.52用mpmath 60位数直接求根，避免默认双精度根容差使较大端点末位偏移；9.23精确离散LR与卡方近似分别列示。

## 最终核验边界

[[工具/StatisticalInference/核验记录/归档核验汇总.json|归档核验汇总]]保留逐章自查、独立复核与最终机器检查。第6、9章全部101题英文另经逐题原页复核；7道指定难题与10.30、10.45另作独立数学检查，具体范围见汇总。不把这些局部复核扩称为全部570题由第二人逐句审查。

源文件与图件版本、有序题号、1068个字母分题及其原位嵌套分问均已登记。全书625篇元数据、公式结构、callout、双语分题与链接检查通过；全库仍仅有前已存在的4条DS026概念来源回链问题，本次未新增。未实测Obsidian界面或最终嵌入渲染，未配置语义索引同步、每日题单或学习状态推进。
