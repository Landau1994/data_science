# 全书静态检查

日期：2026-11-04。检查对象为真实输入拼接镜像 `work/book-static-input/Combined_Chn.tex`；镜像包含实际引用的57份图件，另由 `audit-book.py` 检查原路径。

- 真实输入：116；标签：4459；显式引用：6458。重复标签、未解析引用、环境不平衡、缺失图件及习题编号缺失／重复／多余均为0。
- 625题各章有序集合与源页清单一致；1688个正式编号对象已检查实际AUX排印号。
- `check_fidelity.py` 通过；`check_math_overflow.py` 返回0，另扫描完整日志检查普通正文溢出。
- `check_tex_static.py` 原始返回1，共569条保守启发式提示；保留原始输出，不修改技能或屏蔽提示。387条为年份、163条为数学表达式，8条在既有hyperref或译注内，2条为本句分项标号，5条为引述原文误号，3条为外部专著节号，1条为书目题名末尾Section与页码57–66相接。前几类按数学／命令上下文分类，余下11项实际逐条阅读上下文。没有未处理的结构、资源或引用错误。

证据：`work/book-static-manifest.json`、`work/final-artifact-checks.json`、`work/final-checks/static-check-run.txt`、`static-findings-classified.json`与`static-findings-summary.json`。不把上述静态检查称作Obsidian实际显示测试，也不以其替代原PDF对照或输出页面目视。
