# 全书最终编译与日志检查

最终交付339页，SHA256为dbccdda368e058abba4fbf8a0a0cd75f2f6c33a41fba5cff7d4df33f6582c540。沿用ctexart、12pt、A4中文模板。build.py以XeLaTeX（nonstopmode、halt-on-error、file-line-error）起编，经BibTeX和makeindex，再多遍XeLaTeX至aux/toc/idx字节完全相同；最终三遍XeLaTeX稳定。原PDF编前／编后SHA256不变。

实际运行makeindex，356条锚点全部接受，0拒绝／0警告；300条书目均按原数字编号。最终日志无未定义引用、重复标签、缺字、文件缺失、编译错误、Emergency stop、Fatal error或任何Overfull（含paragraph型）。技能check_math_overflow.py已对最终build-xelatex-3.log实际执行并审阅，公式溢出0，报告math-overflow-report.md保留。该工具自身Python文档字符串转义SyntaxWarning不是LaTeX警告，未冒充公式问题。

非阻断提示：继承模板的xeCJK默认字体重定义、Fandol Script配置提示；第3章大字号数学标题触发rsfs及bbm的30/15pt备用尺寸替代（未用到的数学字母字体族也会加载），以及其全局尺寸替代汇总。书目有两条Underfull段落提示。实际全部输出页及变化页已查看，不影响已检文字、符号或版面。

输入审计按主稿真实显式input图（56文件）、完整aux、实际编译产物和时间戳核对；没有recorder的fls文件，此方法边界在full-audit.json中明确保留，不声称存在未运行的recorder检查。实际编号及PDF目标验证见全书自动审计，逐页视觉另存visual-report.md。

编译日志、书目/索引编译日志、aux、toc、idx、ind、ilg及工作资料本地保留，未做未请求的清理；中间件按目录忽略规则排除于版本控制。
