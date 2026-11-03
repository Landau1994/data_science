from pathlib import Path
import json, re, runpy, shutil, hashlib

BASE = Path(__file__).resolve().parents[1]
ROOT = BASE.parents[2]
NAME = 'Statistical Optimal Transport_Chn'

def write(path, text):
    path.write_text(text.strip()+'\n', encoding='utf-8')

# Preserve the verified current build as the public attachment.
shutil.copy2(BASE/'work/full-build'/f'{NAME}.pdf', BASE/f'{NAME}.pdf')
shutil.copy2(BASE/'work/full-build'/f'{NAME}.log', BASE/f'{NAME}.log')
write(BASE/'核验说明.md', r'''
# 《统计最优传输》完整中文译稿

本稿由第1章试译扩展为全书译稿，2026-11-03完成。原作者为 Sinho Chewi、Jonathan Niles-Weed、Philippe Rigollet，Springer，2025（Lecture Notes in Mathematics 2364）。

- 原件：[[附件/books/Statistical Optimal Transport.pdf]]，269个PDF物理页，保持未改动。
- 译稿：[[附件/翻译/Statistical Optimal Transport_Chn/Statistical Optimal Transport_Chn.pdf|完整中文PDF（235页）]]。
- 可编辑主稿：`Statistical Optimal Transport_Chn.tex`；64份分节稿在`sections-tex/`，前后文分别在`frontmatter/`与`backmatter/`，所需图片在`assets/`，全书330条书目在`bib/references-full.bib`。
- [[附件/翻译/Statistical Optimal Transport_Chn/原文疑误与核对边界|原文疑误与核对边界]]单列说明；统一来源与个人学习状态在[[00 - 首页/教材归档/DS006 - Statistical Optimal Transport|DS006台账]]维护。

## 范围与来源对照

覆盖原文件全部269个物理页：封面、丛书信息、Saint-Flour学校介绍、题名与版权、前言、阅读指南及依赖图、致谢、目录、第1–8章、附录A/B、330条参考文献、100个索引词条及出版社编辑方针。书目保留原语言及原编号；索引保留英文并附中文，页码由译稿重新生成。没有新增习题解答。

采用已有`pdf-to-chinese-tex`技能的`personal-notes.tex`及规格，并完成中文字体、书级计数器、目录、附录、索引和链接的兼容处理。原图保留矢量内容或原图像，翻译图注。原文定义、证明、习题、脚注和未编号公式均纳入逐页对照；计数只是对账辅助。

原始页面由分工完整查看，各章逐段翻译自审后又有交叉复核；前后文、附录、书目和全部索引有专门记录。确认保留166个编号陈述、86处证明、177个数字编号公式、13个命名公式，另有第2章的$A_j$特殊标记；共71道习题、9幅原编号图（含前言图1）。详见`work/source-ledger.md`、`work/manifest-full.json`及各章审阅记录。翻译完整性检查不表示已对整书数学结论独立重证，原文疑误与证明省略另有界定。

## 实际验证

- 完整展开全部输入后，环境、数学定界、标签、引用、文件路径及书目键检查通过：590个标签、929处显式引用，330个文献键均有对应条目。技能静态检查的括号数字误报已逐条判断，说明在`work/full-static-check-report.md`。
- 按用户授权在沙盒外使用XeLaTeX编译，最终三遍XeLaTeX、一遍BibTeX及两遍makeindex。无编译错误、未定义引用、缺失文献、重复标签、缺字或Overfull警告。日志保留CJK字体族重登记、Fandol未声明请求的OpenType Script两个配置提示；实际页面未发现缺字。
- 实际查看最终全部235页渲染。发现并修复孤立标点、定义引导句分页等问题，最后一次变更只影响9页，均已定向复查；其余页图像哈希保持。分工记录为`work/visual-full-001-080.md`、`081-160.md`、`161-201.md`及`202-235.md`（后三个文件同样有`visual-full-`前缀）。
- 根据实际编译结果逐项核对陈述、公式、习题、图和330条文献显示编号；全部一致。索引有100个正文页码锚点和4个see写入，合并成100个唯一词条（87个顶层、13个子项）。
- PDF有1782个内部跳转注释、18个外部URI注释；所有内部链接及已定义标签的实际PDF目的地有效，章外引用已转换为全书内部链接。第6章原315个内部注释逐目标审计后译稿为317个，十处漏掉的显式引用均已恢复。计数受换行、同组引文及原PDF重复矩形影响；没有靠新增无关链接补数。详见`work/full-pdf-link-audit-report.md`与`work/link-audit-ch06.md`。
- 原件SHA256：`91E9CB41212ABC18B294283C19CA4B91F51920A532E5CC24B710A1481EEED272`，与开工时一致。
- 最终译稿SHA256：`C476CAA79437841FAAAE53D3786DFC6C133495F376D0AD7D0E50731AFD355C0A`。

上述检查包括文件内容、真实编译及渲染图像；未在Obsidian内实际测试渲染或鼠标点击。原书疑误和未经独立重证的推导边界不能因编译通过而消除。

## 复用与清理

完整构建入口为`work/build_full_source.py`、`work/run_full_build.py`，完整检查入口为`work/audit_full.py`、`work/audit_full_pdf.py`。构建产生候选PDF，正式交付复制到本目录根部；需要重建时保留当前主稿、所有分节稿、素材与全书书目，使用同一TeX环境。旧的简短入口已转接到全书流程，避免误用第1章生成器覆盖全文。

本次临时清理的逐项清单与统计见`work/cleanup-report.json`及`work/cleanup-report.md`。清理范围限于本次制作的拆分页、提取文本、预览图片、检查副本和编译辅助文件；原书、正式PDF、主稿与分节TeX、书目、图件、编译日志、核验报告及构建脚本保留。`work/`内第1章审阅与历史构建记录注明的是此前试译范围，不替代当前以`full-`命名的全书检查结果。

个人学习状态仍为`not-started`。此译稿不代表知识库71题已分别归档，也没有改变每日题单或学习队列。
''')

ledger = ROOT/'00 - 首页/教材归档/DS006 - Statistical Optimal Transport.md'
t = ledger.read_text('utf-8').replace('source_status: partially-verified','source_status: verified',1)
start=t.index('PDF 物理页从文件第一面起')
end=t.index('### 本轮概念正文核对入口')
t=t[:start]+'''PDF物理页从文件第一面起按1计数；无印刷页码的页面明确注明。下表为全书翻译实际逐页对照范围，`verified`仅表示该来源核对范围完整，不表示已独立证明整书结论。

| 内容 | 印刷页 | PDF物理页 |
| --- | --- | --- |
| 封面、丛书与学校介绍、题名、版权、前言、阅读指南、致谢与目录 | 无页码及v–xiv | 1–14 |
| 第1章：最优传输（Optimal Transport） | 1–36 | 15–50 |
| 第2章：Wasserstein距离估计（Estimation of Wasserstein Distances） | 37–76 | 51–90 |
| 第3章：传输映射估计（Estimation of Transport Maps） | 77–94 | 91–108 |
| 第4章：熵最优传输（Entropic Optimal Transport） | 95–119 | 109–133 |
| 第5章：Wasserstein梯度流：理论（Wasserstein Gradient Flows: Theory） | 121–149 | 134–162 |
| 第6章：Wasserstein梯度流：应用（Wasserstein Gradient Flows: Applications） | 151–186 | 163–198 |
| 第7章：Wasserstein空间的度量几何（Metric Geometry of the Wasserstein Space） | 187–210 | 199–222 |
| 第8章：Wasserstein重心（Wasserstein Barycenters） | 211–227 | 223–239 |
| 附录A：凸分析（Convex Analysis） | 229–235 | 240–246 |
| 附录B：概率（Probability） | 237–239 | 247–249 |
| 参考文献全部330条 | 241–256 | 250–265 |
| 索引全部100个词条 | 257–258 | 266–267 |
| 出版社编辑方针与联系方式 | 无印刷页码 | 268–269 |

## 中文译稿

2026-11-03在第1章试译基础上，按用户要求完成全书翻译，覆盖原PDF全部269个物理页，含8章、2个附录、全部前后文、71题、330条原编号书目与中英索引；未添加习题解答。

- [[附件/翻译/Statistical Optimal Transport_Chn/Statistical Optimal Transport_Chn.pdf|打开完整中文PDF（235页）]]。
- [[附件/翻译/Statistical Optimal Transport_Chn/核验说明|源稿、范围与实际检查]]；可编辑LaTeX、全部分节稿、书目和图件保留在同目录。
- [[附件/翻译/Statistical Optimal Transport_Chn/原文疑误与核对边界|原文疑误与证明边界]]；原书疑误照录，单列核查意见。

已逐页对照原文并交叉复核，最终235页全部渲染查看；编号、标签、文献、索引及PDF链接检查通过，未在Obsidian界面实际点击测试。临时拆分页、提取文本、预览图与编译辅助文件已清理，正式文件及日志保留。原始PDF哈希保持。

全书来源核对状态为`verified`；个人学习仍为`not-started`。翻译完成与71题在知识库中逐题归档属于不同任务，本次没有新增独立习题笔记或推进学习状态。

'''+t[end:]
t=t.replace('本地 PDF 物理页数与出版社列出的印刷页总数不可直接比较；只记录实际文件，未进行逐页完整性对账。','本地PDF共269个物理页；全书翻译已按实际文件逐页核对，印刷页码跳号与无页码前后文分别登记，不据出版信息补造缺失页面。')
t=t.replace('`source_status: partially-verified` 只指上述局部核对；','`source_status: verified`只指本地文件的全书来源对照范围；')
write(ledger,t)

entry='''### 2026-11-03（统计最优传输全文翻译）

- 将DS006原文件269个物理页完整翻译为235页中文PDF，覆盖8章、附录A/B及全部前后文；保留166个编号陈述、86处证明、177个数字公式、13个命名公式与另1个特殊标记、71题、9幅原编号图、330条原编号书目和100个中英索引词条，没有新增习题解答。
- 逐页来源对照、交叉复核及全部输出页视觉检查完成。最终按用户授权在沙盒外编译，编号、590个标签、929处显式引用、书目、索引及实际PDF目的地检查通过；无未定义引用、缺字或公式溢出，两个字体配置提示和原文疑误另存核验说明。原件哈希保持，未实测Obsidian界面。
- 附件保留正式PDF、可编辑LaTeX、图件、书目、日志与核验记录；按用户要求清理本次拆分页、提取文本、预览图片、检查副本和编译辅助文件。DS006统一台账更新全文入口与全书来源核对范围，个人学习仍为not-started；未创建分支、提交或发布内容。
'''
changelog=ROOT/'CHANGELOG.md'
t=changelog.read_text('utf-8')
if '（统计最优传输全文翻译）' not in t:
    pos=t.index('### ')
    write(changelog,t[:pos]+entry+'\n'+t[pos:])
readme=ROOT/'README.md'; t=readme.read_text('utf-8')
t=t.replace('DS006 - Statistical Optimal Transport#第1章中文试译|《统计最优传输》第1章中文试译（34页）','DS006 - Statistical Optimal Transport#中文译稿|《统计最优传输》完整中文译稿（235页）')
pos=t.index('### ',t.index('## 更新日志'))
old=t[pos:]
blocks=re.split(r'(?=^### )',old,flags=re.M)
blocks=[x for x in blocks if x.strip() and not x.startswith('### 2026-11-03（统计最优传输全文翻译）')]
short='''### 2026-11-03（统计最优传输全文翻译）

- 完成原书269个物理页的全书翻译，生成235页中文PDF、可编辑LaTeX、330条原编号书目和中英索引，放入“附件/翻译”。
- 来源逐页对照、交叉复核、全部输出页视觉及编号／链接检查通过；原文疑误单列，正式文件与日志保留，临时文件已清理。
- DS006统一台账更新全文入口与实际核对范围；个人学习仍为尚未开始。
'''
write(readme,t[:pos]+short+'\n'+'\n'.join(blocks[:2]))

# Retain familiar entrypoints while preventing the pilot generator overwriting the book.
for old,new in {'build_source.py':'build_full_source.py','run_build.py':'run_full_build.py','audit.py':'audit_full.py','pdf_audit.py':'audit_full_pdf.py'}.items():
    write(BASE/'work'/old, f'"""全书流程兼容入口；当前交付不再使用第1章生成器。"""\nfrom pathlib import Path\nimport runpy\nrunpy.run_path(str(Path(__file__).with_name({new!r})), run_name="__main__")')

print('Final PDF installed; full-book records and attachment links updated.')
