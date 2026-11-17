"""Write delivery records only after the full visual review and delta review pass."""
from pathlib import Path
import json,re,hashlib,shutil
B=Path(__file__).resolve().parents[1]
def read(name):return json.loads((B/name).read_text(encoding='utf-8'))
def put(name,text):
 p=B/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text.rstrip()+'\n',encoding='utf-8')
def archive(name,target):
 if (B/name).exists()and not (B/target).exists():shutil.copyfile(B/name,B/target)
f=read('work/final-artifact-checks.json');p=read('work/full-pdf-link-audit.json');s=read('work/book-static-manifest.json')
v=[read(f'work/wholebook-visual-{x}.json')for x in 'abc'];delta=read('work/wholebook-visual-delta.json')
seen=set(n for r in v for n in r['pages_viewed'])
assert seen==set(range(1,delta['before_pages']+1))
assert {r['pdf_sha256']for r in v}=={delta['before_pdf_sha256']}
assert set(delta['changed_pages'])<=set(delta['reviewed_pages'])
assert delta['after_pdf_sha256']==p['sha256']==hashlib.sha256((B/'work/Statistical Inference_Chn.pdf').read_bytes()).hexdigest()
assert not f['errors']and not p['bad_links']and not p['number_errors']and not p['missing_index_targets']
assert not read('work/final-checks/static-findings-summary.json')['unreviewed']
pages=p['pages'];notes=f['footnotes']['translator'];sha=p['sha256'];changes=len(delta['changed_pages'])
titles=['概率论','变换与期望','常见分布族','多个随机变量','随机样本的性质','数据约简原则','点估计','假设检验','区间估计','渐近评价','方差分析与回归','回归模型']
source_ranges=[(32,68),(69,100),(101,144),(145,199),(200,251),(252,282),(283,332),(333,367),(368,407),(408,451),(452,497),(498,526)]
chapter_rows=[]
for ch,(title,(a,z))in enumerate(zip(titles,source_ranges),1):
 u=next(u for u in p['units']if u['name']==f'chapter{ch}')
 chapter_rows.append(f'| 第{ch}章 {title} | {a-31}–{z-31}／{a}–{z} | {u["target_start"]}–{u["target_end"]} | {f["exercises_by_chapter"][str(ch)]} |')
table='| 内容 | 原印刷页／原PDF物理页 | 中文PDF物理页 | 习题数 |\n|---|---|---|---:|\n'+'\n'.join(chapter_rows)
visual=f'对整合稿全部{delta["before_pages"]}页以120 dpi渲染，三组分别实际查看物理1–232、233–464、465–696页；修订后重渲染全部{pages}页并比较逐页像素，{changes}个变化页均再次实际查看，其他页像素相同后承接检查。详见 work/wholebook-visual-a、b、c 的JSON／Markdown，以及 work/wholebook-visual-delta.json。'
log=(B/'work/Statistical Inference_Chn.log').read_text(encoding='utf-8',errors='replace')
over=re.findall(r'Overfull \\[hv]box[^\n]*',log)
warn='保留模板的SimSun字体重定义、Fandol Script提示；索引首面的multicol分页提示已对实际页面、脚注内容及目的地复核。'
if over:warn+=' 日志另有：'+'；'.join(over)+'；具体页面已目视复核，见视觉记录。'
else:warn+=' 日志没有Overfull。'
for name,target in [('核验说明.md','work/stage1-核验说明.md'),('manifest.json','work/stage1-manifest.json'),('work/source-inventory.json','work/stage1-source-inventory.json'),('work/continuation-plan.md','work/initial-continuation-plan.md')]:archive(name,target)
manifest={**s,'scope':'全部566源页：书前、12章及全部书后实质材料；重复出版社标志仅登记不重复排印','translation_status':'completed','source_status':'verified','personal_learning_status':'not-started','pdf':f['pdf'],'footnotes':f['footnotes'],'index':f['index'],'bibliography_records':338,'number_checks':p['number_checks'],'visual_review':delta,'input_sha256':f['input_hashes'],'asset_sha256':f['asset_hashes'],'verified_on':'2026-11-04'}
put('manifest.json',json.dumps(manifest,ensure_ascii=False,indent=2))
put('核验说明.md',f'''# 《统计推断》中文译稿核验说明

日期：2026-11-04。全书翻译与个人学习状态统一维护于 [[00 - 首页/教材归档/DS011 - Statistical Inference|DS011教材台账]]。

## 完整交付

- [中文PDF](Statistical%20Inference_Chn.pdf)：{pages}页，覆盖书前、全部12章、计算机代数、常见分布表、参考文献及中英索引。
- [LaTeX主文件](Statistical%20Inference_Chn.tex)：沿用既有中文数学模板；116份真实输入TeX、57份使用的原图矢量文件、书目及[构建脚本](构建.ps1)保留。
- 原书为2001年第二版的2024年CRC重印本，共566物理页；不是内容重新修订的2024版。原件SHA256为 `{f['source']['sha256']}`，核对后未变。
- 正式PDF SHA256：`{sha}`。完整输入、图件及输出哈希见 [manifest.json](manifest.json)。

{table}

书前原物理1–31页全部覆盖。书后原物理528–533为计算机代数，534–539为分布表与关系图，540–554为338条参考文献，556–566为索引。源封面按中文模板重排；重复出版社标志7、19、21、31、527、555页登记后合并保留出版信息，没有删除独有数学内容。原PDF读者高亮不当作作者正文样式。

## 内容与原文疑误

全书625道编号习题、539个编号陈述（92定义、130定理、11引理、7推论、299例）、448个编号公式、54幅编号图、22张编号表、93个显式证明／提纲环境已对账。无编号推导、习题分问、原提示与原附答案也按原页保留；没有新增独立习题解答。计算机代数的8个例计入299例，分布表另有21种分布。

保留4条作者原脚注，并有{notes}条明示“译注”。译注说明排印疑误、缺少条件、原文误引、书目差异或必要的语言边界；这个数量不表示发现了{notes}个已证实的数学错误。原文有误处不静默改写，独立推导、有限计算和待核实事项明确区分。例如第6章完备性陈述的反例、第10章数据表疑误及第12章逻辑回归漏log／截距变换均在对应位置脚注说明。完整译注文本及源文件行号见 `work/all-footnotes.json`。

图件主要保留原矢量图，中文重排图题，图内英文短标签保留。原文特别的表号、公式号和书后12.6.1–12.6.8例号均保留。书目338条不表示本次阅读或复现了338篇外部文献；历史Mathematica输入输出只作忠实转录，未运行Mathematica。

## 实际核验

- 原书566页的连续覆盖及每章逐页对照记录见 [来源记录](source-ledger.md)；对象、分题及证明边界见 [忠实性报告](fidelity-report.md)。异人逐句复核范围为书前和第1章的已记分段、第2章、第8章及计算机代数／分布表等；其他章有完整译写者自审与专项复核，不宣称全12章全部完成第二人逐句审校。
- 真实XeLaTeX多轮编译、目录与索引稳定检查、makeindex语法检查已执行。4459个标签、6458处显式引用、1688个正式对象的实际排印号检查通过；未定义引用、重复标签、缺字和横向溢出为0。{warn}
- 全部{p['target_counts']['internal']}个PDF内部链接目标合法，1174个索引语义落点均有实际命名目标；{len(p['bookmarks'])}个书签。索引保留1071个分层词条、1174个原页定位及22处“见／另见”，同一条目同一译稿页的定位合并，显示1172处页码。原索引含义偏宽或原页偏一页的项目另有脚注说明。
- {visual}
- 技能公式溢出与忠实性检查通过。保守静态扫描仍返回569条启发式提示，已按年份、数学记号、已有链接、原文疑误引述及外部书籍节号分类；无结构或资源缺失错误，没有把原始退出码1写成工具零警告。见 [静态检查报告](static-check-report.md)。

链接通过实际PDF注释、AUX编号及命名目标字典核对；没有声称逐条人工点击{p['target_counts']['internal']}个链接。292个脚注链接的标记与注释均在同页。外部20个网址／邮件目标保留，但未逐项验证当前可达性。未实测Obsidian界面，未把语法检查称为界面渲染。

## 重建及学习状态

在本目录执行 `构建.ps1` 可重建同名PDF；脚本等待目录、索引页码稳定后复制成品。不要运行工作目录内早期初始化或阶段生成脚本覆盖人工校正。源稿、原图、书目、逐章记录、日志与渲染留存，便于追溯；本轮没有清理这些资料。

教材内625题的翻译不等于建立625篇独立习题归档，也不等于已完成练习。个人学习仍为 `not-started`；全书来源覆盖记为 `verified`，仅表示实际核对范围，不代替数学正确性证明。本轮没有创建分支、提交、推送或发布。
''')
put('compile-report.md',f'''# 全书编译与输出核验

日期：2026-11-04。最终工作PDF：{pages}页；SHA256 `{sha}`。

实际使用TeX Live 2023的XeLaTeX、多轮目录／引用构建及makeindex。主文件显式加载116份TeX输入；原图57份均存在。`work/full-build-1.txt`等保存构建输出，最终日志为 `work/Statistical Inference_Chn.log`。标准索引输入1174条，全部接受，0拒绝、0警告；正文采用保留原英文顺序与中文译名的动态索引。

未发现编译错误、缺失字符、未定义引用、重复标签或Overfull hbox。{warn}

{visual}

版式问题修复与变化页清单见 `work/final-layout-fixes.json`、`work/wholebook-visual-delta.json`。视觉核验不替代源文忠实性核验。历史代码未执行；原书Mathematica输出不是本次运行结果。
''')
sc=read('work/final-checks/static-findings-summary.json')
put('static-check-report.md',f'''# 全书静态检查

日期：2026-11-04。检查对象为真实输入拼接镜像 `work/book-static-input/Combined_Chn.tex`；镜像包含实际引用的57份图件，另由 `audit-book.py` 检查原路径。

- 真实输入：116；标签：{s['labels']}；显式引用：{s['references']}。重复标签、未解析引用、环境不平衡、缺失图件及习题编号缺失／重复／多余均为0。
- 625题各章有序集合与源页清单一致；1688个正式编号对象已检查实际AUX排印号。
- `check_fidelity.py` 通过；`check_math_overflow.py` 返回0，另扫描完整日志检查普通正文溢出。
- `check_tex_static.py` 原始返回1，共{sc['findings']}条保守启发式提示；保留原始输出，不修改技能或屏蔽提示。387条为年份、163条为数学表达式，8条在既有hyperref或译注内，2条为本句分项标号，5条为引述原文误号，3条为外部专著节号，1条为书目题名末尾Section与页码57–66相接。前几类按数学／命令上下文分类，余下11项实际逐条阅读上下文。没有未处理的结构、资源或引用错误。

证据：`work/book-static-manifest.json`、`work/final-artifact-checks.json`、`work/final-checks/static-check-run.txt`、`static-findings-classified.json`与`static-findings-summary.json`。不把上述静态检查称作Obsidian实际显示测试，也不以其替代原PDF对照或输出页面目视。
''')
unitrows=[]
for u in p['units']:
 unitrows.append(f'| {u["name"]} | {u["source_start"]}–{u["source_end"]} | {u["target_start"]}–{u["target_end"]} | {u["source_links"].get("internal",0)} | {u["target_links"].get("internal",0)} |')
put('pdf-link-audit-report.md',f'''# 实际PDF链接核验

最终PDF {pages}页，SHA256 `{sha}`。实际注释：内部{p['target_counts']['internal']}、网址／邮件{p['target_counts']['uri']}；书签{len(p['bookmarks'])}；命名目标{p['named_destinations']}。无越界／不可解析内部跳转，4459个LaTeX标签均能解析到实际目的地；1174个索引语义定位全部解析。编号检查1688项，0差异。

| 范围 | 原PDF物理页 | 中文PDF物理页 | 原内部注释 | 译稿内部注释 |
|---|---|---|---:|---:|
{chr(10).join(unitrows)}

上表第12章范围包含紧随其后的原527页标志，参考文献范围包含555页标志，仅用于连续注释统计；实质内容范围另见source-ledger。原件共2532内部、25外部注释。六处重复出版社标志网址合并保留一次，外部注释净减5，得到20；12个章DOI均保留。原书书目37个错位、无对应语义的链接不机械复制。新增动态目录、语义索引、分题与文献引用导致内部链接数增加，不能用总量差代替逐项语义判断。

检查方法为读取PDF原始注释、命名目标和实际页码，结合源页语义映射及AUX编号；未逐条人工点击，也未验证外部网站当前可达性。注释矩形与目标明细见 `work/full-pdf-link-rectangles.json`，标签目标见 `work/full-pdf-label-destinations.json`。
''')
put('reference-map.md',f'''# 编号与引用映射

全书采用原章／节／对象编号，定义、定理、引理、推论、例共享原序列；公式、图、表分别保留原编号，习题按章编号。原异常号不为连续性重排。真实目标清单为 `work/full-pdf-label-destinations.json`，逐章源对象与题号清单为 `work/chNN-manifest.json`／`chNN-object-inventory.json`。

正文内部引用使用autoref、eqref或hyperref；原文误号在正文保留，链接可指真实目标，并以译注明示。338个书目编号为 `bib:source1` 至 `bib:source338`，正文作者与年份链接到本册书目，原年份／拼写差异保留说明。历史第一版前言的章节指向不伪造成第二版同号内容。

索引1174个源定位全部落实到既有对象标签或唯一语义锚点，详见 `work/index-semantic-resolved.json`。原英文顺序、1071层级词条及22处交叉指向保留。实际同条目同一译稿页合并后显示1172处页码。最终{p['target_counts']['internal']}条内部PDF注释目的地合法，1688个正式对象实际编号与源号一致。

本书的源页锚点533个覆盖原32–526、528–554、556–566页；另33页在来源记录登记（书前31页、重复标志2页）。源页锚点用于溯源，不以粗略页首代替已经建立的索引语义落点。
''')
inv=read('work/source-inventory.json')
inv['scope_note']='全部566源页已经按来源记录核对；实质内容逐页原图对照。独立复核精确范围见source-ledger.md。源页覆盖不表示独立证明全书数学结论。'
inv['source_status']='verified';inv['full_source_visual_checked_pdf_pages']=list(range(1,567));inv['chapter_ranges'][-1]['printed']=[467,495];inv['chapter_ranges'][-1]['pdf']=[498,526]
put('work/source-inventory.json',json.dumps(inv,ensure_ascii=False,indent=2))
put('work/continuation-plan.md',f'''# 全书翻译完成记录

2026-11-04：用户要求的全部剩余章节及书后材料已完成，正式交付为{pages}页中文PDF及完整可编辑LaTeX。早期分工与阶段边界保留于 `initial-continuation-plan.md`，首批77页说明保留于 `stage1-核验说明.md`。

原书566页、12章、625题及全部书前书后内容覆盖；原文疑误以译注脚注说明。语义索引1174定位、338条参考文献、编号和实际PDF链接核验完成；全输出逐页查看及修订变化页复检完成。具体数量、方法、警告与独立复核边界以根目录最新核验报告为准。

个人学习状态仍为not-started。未创建独立习题归档或新增原书没有的解答，未进行Git写入或外部发布。工作材料保留，后续修订从当前人工校正的TeX开始，不重跑早期初始化脚本。
''')
print('Final reports written for',pages,'pages; changed pages reviewed:',changes)
