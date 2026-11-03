# 编译与日志核验

使用本库现有《统计最优传输》ctexart中文模板，保留其A4、字号、页边距和章标题设计；增加本书独立知识框计数器、无编号陈述环境及必要字体兼容。数学知识框内使用直立正文、零额外上下间距，以避免环境改造造成稀疏排版。

已实际运行XeLaTeX与BibTeX并迭代修复。最终通过build.py完整重建（XeLaTeX→BibTeX→XeLaTeX→XeLaTeX），生成94页PDF并复制至正式入口。构建日志保留work/build-*.log和主稿.log。build.py只负责构建，不冒充内容或视觉检查。

最终主日志：未定义引用0、重复标签0、未定义书目0、缺字0、Overfull 0、LaTeX错误0、PDF书签数学警告0。自动math-overflow检查已实际运行，报告保留；另直接扫描主日志交叉确认零溢出。两处Underfull书目提示属于行距较松，已在最终书目页目视确认可读。

保留两个继承模板的提示：重定义CJK主字体族、FandolSong-Regular不含所请求的Default脚本标签；实际页图无缺字。书目177特殊附加符以局部Times New Roman字体保留原字符，未改写人名或补外部元数据。
