# 全书静态与编译结构核验

此报告按最终MAIN递归输入图生成，替代原来只含前置与第1章的阶段报告。

入口：`Optimal Transport for Applied Mathematicians_Chn.tex`；实际显式输入文件56个。运行生成的BBL、IDX、IND、ILG及PDF另在full-audit中按其真实文件核对。

静态输入图状态：`passed`。检查环境与数学定界符、花括号（支持index内复杂数学嵌套）、唯一标签和实际引用、图件存在、300条书目、69题与69条提示、有序完整索引与精确锚点。

原页独立编号基线：238编号陈述、102章内数字式、43知识框、27编号图；另3幅无编号正文图和2习题图、154原文proof、67章内脚注＋前置5＋习题1。DP-var及导论(1)/(2)独立核对，不混入章内数字式。所有原数学疑误与编号保持可见，不作静默修正。

全量`check_fidelity_project.py`按同一递归输入图执行，报告为`fidelity-static-full.json`；适配了技能原脚本的目录发现和逗号引用键，并检查全部154个proof，不改技能原文件。此语言/结构扫描不代替root维护的`fidelity-report.md`来源自审与独立cross记录。

实际AUX编号、300条BBL顺序、日志、PDF新鲜度和所有实际链接另见`full-audit.json`。整体自动审计状态：`passed-automated-checks`。存在链接/编译失败时不得把本报告的静态检查称为全稿通过。

未执行Obsidian界面检查；最终PDF目视记录由全书分段PNG审阅单独提供。
