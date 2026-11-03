# 全书编译与版面核验

更新日期：2026-11-03. 实际审计对象为 `work/full-build/Statistical Optimal Transport_Chn.pdf`，235页；对应全269源物理页. 原第1章试译34页及work根部同名历史日志只描述试译. 全书构建PDF已经交付至译稿根目录同名文件，两者校验值相同；run_build.py当前转接全书构建流程. 最终PDF SHA-256为 `c476caa79437841faaae53d3786dfc6c133495f376d0ad7d0e50731afd355c0a`.

## 实际构建

依据最新full-build-events.json，run_full_build.py执行XeLaTeX三次、BibTeX一次、makeindex两次，六个事件退出码均为0. 构建在BibTeX后保留原书ref1..ref330显示号；makeindex在引用解析后重建，并检查索引输入是否稳定，不使用原书旧页码作输出.

最新日志实际检索结果：无Overfull、undefined reference/citation、Missing character、重复标签或LaTeX/Fatal错误. makeindex接受104条、拒绝0条、警告0条；BibTeX使用330条，warning调用0次. 日志仍有2条字体配置提示（CJKfamily重新定义、Fandol所请求Script未声明）与3条Underfull hbox，未把这些隐去或写成“零警告”. 对应成品未见缺字、裁切或重叠.

## 静态、编号与链接

- full-static-check.json：errors为空，590标签、929次对象引用、330文献键；86个proof、71个exercise环境配对. manifest-full.json记录64正文/附录片段，各输入一次，实际全展开输入71文件.
- full-pdf-audit.json：pages=235，bad_numbering为空，invalid_links为空. 166编号陈述、177数字公式、71题显示号、9图及330书目原号实际aux核验通过. 13个命名公式与另1个A_j特殊标记独立保留.
- PDF实际链接类型计数为2:18、4:1782；所有内部页/命名目标有效，已无跨原书PDF占位引用. 第6章十处显式链接恢复后专项审计通过.
- 索引104次写入对应100个逻辑词条，正文页码锚点与4个see经独立语义审阅，输出采用译稿页码.

full-static-check-report.md已与当前929处显式引用同步. 最终全书编译日志已再次运行check_math_overflow，结果为0，报告在work/math-overflow-report.md；上述全书溢出结论同时依据最终日志及逐页视觉.

## 全部输出页的实际视觉

| 范围 | 记录 |
| --- | --- |
| 1–80 | visual-full-001-080.md，含9/11/33/80页最终定向复核 |
| 81–160 | visual-full-081-160.md，含81–90及第6章八个变化页复核 |
| 161–201 | visual-full-161-201.md，含166–172、200–201最终九变化页复核 |
| 202–235 | visual-full-202-235.md，覆盖全部书目、索引和出版方针 |

全部235页实际查看，密集长式、矩阵、图与脚注另放大. 定位并修复了单独句号行、假设3.3和定义7.9的页末孤立引导句；修改后的影响页已按新PNG复核关闭. 目录、原号、图及长式可读，无待处理版面问题. 本报告不把PDF检查说成Obsidian实际渲染或人工点击验收.
