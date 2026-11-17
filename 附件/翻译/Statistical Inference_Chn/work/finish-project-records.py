from pathlib import Path
import json,re,hashlib
B=Path(__file__).resolve().parents[1];R=B.parents[2]
f=json.loads((B/'work/final-artifact-checks.json').read_text(encoding='utf-8'));p=json.loads((B/'work/full-pdf-link-audit.json').read_text(encoding='utf-8'));d=json.loads((B/'work/wholebook-visual-delta.json').read_text(encoding='utf-8'))
assert hashlib.sha256((B/'Statistical Inference_Chn.pdf').read_bytes()).hexdigest()==p['sha256']==d['after_pdf_sha256']
assert set(d['changed_pages'])<=set(d['reviewed_pages'])
pages=p['pages'];count=len(d['changed_pages']);sha=p['sha256']
def update(path,fn):
 text=path.read_text(encoding='utf-8');path.write_text(fn(text).rstrip()+'\n',encoding='utf-8')
update(B/'source-ledger.md',lambda t:t.replace('当前阶段：全书正文与书前、书后材料已译出并完成分段原页自审，最后的语义索引应用和全书PDF复检由总编继续完成.','当前阶段：全书翻译、语义索引应用、整合编译及最终PDF核验均已完成；最终输出'+str(pages)+'页，具体结果见根目录核验说明与报告.').replace('最终目录和索引的中文PDF页码应由实际编译目标生成.','最终目录和索引的中文PDF页码已由实际编译目标生成并核验.').replace('最终PDF的整书逐页视觉复检、语义索引应用后的动态页码及实际PDF跳转检查仍由总编补记. 本覆盖记录证明材料范围与来源核验链条，不单独宣告最终出版成品验收.','最终整合稿全部696页已实际目视；修订后'+str(count)+'个变化页均复检，其余页面像素相同后承接检查。1174个索引语义落点与实际PDF跳转检查通过，具体方法、文件哈希及警告见核验说明、compile-report.md与pdf-link-audit-report.md。本覆盖记录说明来源核验链条，不代替独立证明全书数学结论。'))
def fidelity(t):
 t=t.replace('全书内容已译出，语义索引1174处落点已完成映射；最终索引应用、整书重编及最终PDF检查仍由总编完成后补记.','全书翻译、1174处语义索引应用、整书编译与最终PDF检查已完成，正式输出'+str(pages)+'页.').replace('最终中文PDF目标为 `Statistical Inference_Chn.pdf`；工作目录中的预览PDF不作为已完成最后验收的交付版本.','正式中文PDF为 `Statistical Inference_Chn.pdf`，其与最终已核验工作PDF的SHA256一致.').replace('这一结果只说明静态输入与目标存在，不等于最终PDF每条链接已跳到正确语义位置.','静态结果只说明输入与标签目标存在；实际PDF命名目的地与注释另经最终检查，结果见pdf-link-audit-report.md.').replace('最终索引须在映射应用和重编后重新核验页码、落点与点击目标，当前不能用旧预览的索引检查数冒充1174处已完成PDF验收.','最终索引已应用并重编，1174个语义目标全部解析；同条目同译稿页重复定位合并，显示1172处页码。22个交叉指向保留；原索引含义偏宽及原定位偏一页的问题已在索引开头译注说明.').replace('下列数量为本报告汇总时当前TeX的快照，包含总编整合后新增的书目差异说明；因此可能多于早期局部audit所记数量. 之后若新增译注，应同步更新本表.','下表为最终TeX的实际脚注统计，包含整合后新增的书目差异与索引说明，可能多于早期局部audit的快照.').replace('| 计算机代数及分布表 | 0 | 14 |','| 计算机代数、分布表及索引 | 0 | 15 |').replace('287','288').replace('首次54页预览已逐页查看，后续55页版本及整书分页的最终变化页仍以总编复检为准.','早期局部预览之后，最终全书书后物理641–696页已实际目视，并承接修订后的变化页复检.').replace('最后一次索引应用及整书重编后待总编补充最终PDF页数、文件哈希、日志、全页检查范围及链接结果. 不用中间695页预览检查替代最终结果.','最终'+str(pages)+'页，全部页实际查看；修订后'+str(count)+'变化页复检。'+str(p['target_counts']['internal'])+'内部注释、1174索引目标和1688实际编号检查通过。最终SHA256与方法详见核验说明。')
 start=t.index('## 最终验收待补')
 t=t[:start]+f'''## 最终验收结果

正式PDF {pages}页，SHA256 `{sha}`。源PDF哈希保持不变。原始整合稿696页全部实际查看，最终重排后{count}个变化页再次查看，其余页面像素相同。具体页面清单和版本哈希见 `work/wholebook-visual-*.json`。

目录、索引页码已稳定，1174定位与22交叉关系完整；4459标签及1688正式对象实际编号对账通过，全部{p['target_counts']['internal']}个内部注释目标合法。没有未定义引用、重复标签、缺字或横向溢出；完整日志提示、保守静态扫描分类与方法边界在compile-report.md及static-check-report.md中说明。未把自动目的地检查描述为逐条人工点击。

完整源稿、图件、书目、原页与工作预览、日志和检查清单保留用于追溯。旧阶段77页说明另存 `work/stage1-核验说明.md`；根目录说明与manifest均已更新为全书交付，个人学习状态不变。
'''
 return t
update(B/'fidelity-report.md',fidelity)
names=['概率论','变换与期望','常见分布族','多个随机变量','随机样本的性质','数据约简原则','点估计','假设检验','区间估计','渐近评价','方差分析与回归','回归模型'];ranges=[(32,68),(69,100),(101,144),(145,199),(200,251),(252,282),(283,332),(333,367),(368,407),(408,451),(452,497),(498,526)]
rows=[]
for ch,(name,(a,z))in enumerate(zip(names,ranges),1):
 rows.append(f'| 第{ch}章 {name} | {a-31}–{z-31}／{a}–{z} | 全章完成；{f["exercises_by_chapter"][str(ch)]}道完整习题 |')
ledger=R/'00 - 首页/教材归档/DS011 - Statistical Inference.md'
def ds(t):
 t=t.replace('source_status: partially-verified','source_status: verified').replace('translation_status: in-progress','translation_status: completed').replace('translated_chapters: [1]','translated_chapters: [1,2,3,4,5,6,7,8,9,10,11,12]').replace('translation_pdf_pages: 77',f'translation_pdf_pages: {pages}')
 t=t.replace('| 本批译稿的书前材料与完整第 1 章 | 未编号及前置页码；正文1–37 | 1–68；逐页原件对照及独立复核，详见下方中文译稿 |','| 全书翻译来源核对 | 无编号、罗马页码及正文／书后1–535 | 全部1–566；逐页对照范围、重复标志页处理及独立复核边界见下方中文译稿 |')
 t=t.replace('本轮未审计全书公式、题目与证明。','本次全译已逐章对照正文、公式、题目、证明及书后材料；不把来源核对当作独立证明全书数学结论。')
 t=t.replace('`source_status: partially-verified` 指已记录的局部正文及本批翻译范围核对；','`source_status: verified` 指全书实际来源覆盖核对；')
 a=t.index('## 中文译稿');z=t.index('## 相关入口',a)
 section=f'''## 中文译稿

沿用本库已有中文数学LaTeX模板，**全书中文翻译已完成，共{pages}页**，覆盖书前、全部12章及全部书后实质材料。

- [[附件/翻译/Statistical Inference_Chn/Statistical Inference_Chn.pdf|打开完整中文PDF]]。
- [[附件/翻译/Statistical Inference_Chn/Statistical Inference_Chn.tex|LaTeX主文件]]；分章源稿、图件、书目及重建脚本在同目录。
- [[附件/翻译/Statistical Inference_Chn/核验说明|核验范围、原文疑误与重建说明]]；[[附件/翻译/Statistical Inference_Chn/source-ledger|连续来源覆盖]]及[[附件/翻译/Statistical Inference_Chn/fidelity-report|忠实性报告]]。

| 翻译范围 | 原印刷页／PDF物理页 | 结果 |
|---|---|---|
| 书前全部材料 | 无编号及罗马页码／1–31 | 出版信息、献辞、两版前言、作者、原目录及22表／54图／299例目录完整保留 |
{chr(10).join(rows)}
| 计算机代数与常见分布表 | 497–508／528–539 | 8例、21种分布及关系图；历史代码未执行 |
| 参考文献 | 509–523／540–554 | 338条原编号书目 |
| 索引 | 525–535／556–566 | 1071分层中英词条，1174原页定位、22处交叉关系 |

原PDF正文印刷页加31等于物理页；527、555为重复出版社标志，另在来源记录说明。全书625道编号习题、539个编号陈述、448个编号公式已对账，保留全部分问、原提示及原附答案。4条作者脚注与288条明示译注分开；疑似原文错误、条件边界及文献差异在对应脚注说明，不静默修正原文。

已实际完成逐章原页对照、整合编译、全输出逐页视觉及变化页复检、1688正式对象实际编号与PDF链接目标检查。异人逐句复核的精确范围在报告列出，未声称全12章都经过第二人逐句检查。未实测Obsidian界面或逐项核验外部网站当前可达性。

来源核对状态为 `verified`；个人学习仍为 `not-started`。书内625题的翻译不等于新增625篇独立习题归档，更不等于完成练习。本轮未新增习题笔记、独立解答或学习记录，未进行Git写入或发布。

'''
 return t[:a]+section+t[z:]
update(ledger,ds)
update(R/'02 - 数理统计/数理统计导航.md',lambda t:t.replace('书前材料与第1章已完成，共77页；附LaTeX源码与核验说明，其余章节待续译。',f'全书12章及前后材料已完成，共{pages}页，含625道完整习题；附LaTeX源码、疑误脚注与核验说明。'))
entry=f'''### 2026-11-04（统计推断全书翻译完成）

- 完成本地566页原书的全译，交付{pages}页中文PDF与完整可编辑LaTeX，覆盖书前、全部12章、计算机代数、21种分布、338条书目及中英索引。保留625道编号习题全部分问、原提示与原附答案，539个编号陈述、448个编号公式、54图、22表、93个显式证明／提纲；没有新增独立解答或习题归档笔记。
- 按用户要求在对应位置以译注脚注说明疑似原文错误、条件边界与书目差异，共288条译注及4条作者脚注；原文疑误不静默改写。历史Mathematica代码未执行，书目记录不表示已阅读全部外部文献。
- 逐章原页对照完成，独立复核范围在来源与忠实性报告分别记录。全部696页整合稿实际目视；修订后{count}个变化页再次核验，其余页像素相同。实际全量编译、4459标签／6458显式引用、1688实际编号、{p['target_counts']['internal']}内部链接、1174索引语义定位检查通过。静态扫描启发式提示已分类，日志字体及索引提示的实际边界保留报告，未宣称逐条人工点击或Obsidian界面实测。
- DS011唯一台账、数理统计导航及README更新完整交付入口；source_status改为全书来源覆盖verified，个人学习保持not-started。原件SHA256保持；源稿、工作材料与重建记录保留，未创建分支、提交、推送或发布。

'''
update(R/'CHANGELOG.md',lambda t:t if '### 2026-11-04（统计推断全书翻译完成）'in t else t.replace('保留完整历史，最新条目在前。\n','保留完整历史，最新条目在前。\n\n'+entry,1))
def readme(t):
 t=t.replace('沿用中文LaTeX＋PDF，首批完成书前材料及第1章，共77页，含55道完整习题；全书按章续译。',f'全书{pages}页中文PDF及LaTeX已完成，含12章、625道完整习题、参考文献与中英索引；疑似原文错误另有脚注。')
 a=t.index('## 更新日志');old=t[a:]
 blocks=re.findall(r'### .*?(?=\n### |\Z)',old,re.S)
 blocks=[x for x in blocks if '统计推断全书翻译完成'not in x.splitlines()[0]][:2]
 short=f'''### 2026-11-04（统计推断全书翻译完成）

- 完成{pages}页完整中文译稿，覆盖12章及全部前后材料，保留625道完整习题、338条书目与中英索引；提供可编辑LaTeX和重建脚本。
- 逐章原页对照、全输出逐页视觉与变化页复检、实际编号和PDF链接检查完成；疑似原文错误在对应译注脚注中说明，独立复核范围如实列明。
- [[00 - 首页/教材归档/DS011 - Statistical Inference#中文译稿|DS011统一台账]]提供完整交付入口；个人学习状态不变，未提交或发布。

'''
 return t[:a]+'## 更新日志\n\n[完整更新历史](CHANGELOG.md)\n\n'+short+'\n\n'.join(x.rstrip()for x in blocks)+'\n'
update(R/'README.md',readme)
print('Updated final source, fidelity, DS011, navigation, README and CHANGELOG records.')
