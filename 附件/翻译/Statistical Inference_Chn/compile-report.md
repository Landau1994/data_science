# 全书编译与输出核验

日期：2026-11-04。最终工作PDF：696页；SHA256 `169e9684f3a5f583810e10de61861732290555e3c646a1313e73316876436717`。

实际使用TeX Live 2023的XeLaTeX、多轮目录／引用构建及makeindex。主文件显式加载116份TeX输入；原图57份均存在。`work/full-build-1.txt`等保存构建输出，最终日志为 `work/Statistical Inference_Chn.log`。标准索引输入1174条，全部接受，0拒绝、0警告；正文采用保留原英文顺序与中文译名的动态索引。

未发现编译错误、缺失字符、未定义引用、重复标签或Overfull hbox。保留模板的SimSun字体重定义、Fandol Script提示；索引首面的multicol分页提示已对实际页面、脚注内容及目的地复核。 日志没有Overfull。

对整合稿全部696页以120 dpi渲染，三组分别实际查看物理1–232、233–464、465–696页；修订后重渲染全部696页并比较逐页像素，95个变化页均再次实际查看，其他页像素相同后承接检查。详见 work/wholebook-visual-a、b、c 的JSON／Markdown，以及 work/wholebook-visual-delta.json。

版式问题修复与变化页清单见 `work/final-layout-fixes.json`、`work/wholebook-visual-delta.json`。视觉核验不替代源文忠实性核验。历史代码未执行；原书Mathematica输出不是本次运行结果。
