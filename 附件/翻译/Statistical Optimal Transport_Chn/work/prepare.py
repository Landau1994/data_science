from pathlib import Path
import sys, re, json
sys.path.insert(0, r'E:/project/math/ant/tmp/pypackages')
import pymupdf as fitz

BASE = Path(__file__).resolve().parents[1]
SOURCE = BASE.parents[1] / 'books' / 'Statistical Optimal Transport.pdf'
doc = fitz.open(SOURCE)
pages = [p.get_text() for p in doc]
objects=[]
# Manual inventory from the visible source headings: text-layer regex alone
# misreads mentions as headings and misses the fi ligature in Definition.
for typ,num,p in [('Proposition',1,3),('Definition',2,7),('Proposition',3,8),('Example',4,8),('Proposition',5,9),('Theorem',6,10),('Theorem',7,13),('Theorem',8,15),('Definition',9,17),('Theorem',10,17),('Proposition',11,18),('Lemma',12,22),('Proposition',13,24),('Theorem',14,25),('Definition',15,27),('Theorem',16,27),('Example',17,28),('Proposition',18,29),('Example',19,29),('Theorem',20,30),('Theorem',21,31),('Lemma',22,31)]:
    objects.append(dict(type=typ,number=f'1.{num}',physical=p+14,printed=p))
sections = [('1.1',1,3),('1.2',6,6),('1.3',12,7),('1.4',14,7),('1.5',20,9),('1.6',30,3),('1.7',32,2),('1.8',33,4)]
ledger = ['# 原文覆盖记录','', '本记录仅追踪本次第1章译稿生产与核验，不记录个人学习或整书归档进度。', '',
          '- 原件：附件/books/Statistical Optimal Transport.pdf；269 个物理页。',
          '- 作者：Sinho Chewi、Jonathan Niles-Weed、Philippe Rigollet；Springer，2025。',
          '- 范围：第1章全部，印刷1–36／PDF物理15–50；不含全书前言、其他章节、附录和索引。',
          '- 抽取：Poppler pdftotext -layout；PyMuPDF文本用于对象定位，原PDF渲染页为核对依据。',
          '- 原件SHA256：91E9CB41212ABC18B294283C19CA4B91F51920A532E5CC24B710A1481EEED272。',
          '- 模板：pdf-to-chinese-tex/templates/personal-notes.tex及其规格，保留原版式，按原书改计数关系与中文环境名。','',
          '| 小节 | 起始印刷／物理页 | 输出 |','| --- | --- | --- |']
for j,p,_ in sections:
    ledger.append(f'| {j} | {p}／{p+14} | sections-tex/01-{j.split(".")[1].zfill(2)}.tex |')
ledger += ['', '## 原文编号对象（从原文抽取并人工核对）','', '| 类型 | 原号 | 印刷／物理页 |','| --- | --- | --- |']
for o in objects:
    ledger.append(f'| {o["type"]} | {o["number"]} | {o["printed"]}／{o["physical"]} |')
ledger += ['', '- 正式定理类对象共22个，章内共享1.1–1.22；公式独立为1.1–1.25，另有KOT、DKOT等名称标签；图1.1–1.3，表0，习题1–10（全部分题）。',
           '- 所有正文公式（含未编号）、脚注、证明及段落均应完整保留；细项见各范围自审与最终核验。',
           '- 全书参考文献位于印刷241–256／PDF物理250–265；本章只摘录实际引用项，保留原引用数字。',
           '- 提示：PDF书签的目标页与实际可见标题存在偏差，定位依据为原页面内容，不由书签推算页码。']
(BASE/'work/source-ledger.md').write_text('\n'.join(ledger)+'\n',encoding='utf-8')
(BASE/'work/source-objects.json').write_text(json.dumps(objects,ensure_ascii=False,indent=2),encoding='utf-8')
numbering='''# 编号计划与结果待核项

原书章号1；节1.1–1.8；次节1.1.1等。个人笔记模板使用section表示章、subsection表示节。
定理类对象章内共用一个theorem计数器：命题1.1、定义1.2、命题1.3、例1.4、命题1.5、定理1.6–1.8、定义1.9、定理1.10、命题1.11、引理1.12、命题1.13、定理1.14、定义1.15、定理1.16、例1.17、命题1.18、例1.19、定理1.20–1.21、引理1.22。
本章无编号推论、注、问题；环境仍由模板保留。
公式独立章内计数1.1–1.25；KOT、DKOT等命名标签用tag并登记label，不增加数字计数。图独立1.1–1.3。习题独立1–10，不冒充知识库习题归档。
由原始页核对编号流后，改模板theorem环境从按subsection各自计数为按section共享；equation和figure按section；exercise独立计数且只显示阿拉伯数字。
'''
(BASE/'work/numbering-plan.md').write_text(numbering,encoding='utf-8')
prefix={'Proposition':'prop','Theorem':'thm','Definition':'def','Example':'ex','Lemma':'lem'}
refs=['# 交叉引用计划','', '依据原文对象生成；章内目标采用稳定label；范围外目标以externalref链接原PDF真实物理页，保留“原书”提示。','']
for o in objects:
    refs.append(f'- `{prefix[o["type"]]}:{o["number"]}`：{o["type"]} {o["number"]}，原PDF第{o["physical"]}页。')
refs += [f'- `sec:{j}`：原书第{p+14}物理页。' for j,p,_ in sections]
refs += [f'- `eq:1.{n}`：原式（1.{n}），具体页定位见最终清单。' for n in range(1,26)]
refs += [f'- `fig:1.{n}`：原图1.{n}。' for n in range(1,4)]
refs += [f'- `exer:{n}`：章末习题{n}。' for n in range(1,11)]
(BASE/'work/reference-map.md').write_text('\n'.join(refs)+'\n',encoding='utf-8')

# Preserve diagrams by clipping source vector pages, omitting English captions.
for num,physical,rect in [(1,18,(83,445,356,566)),(2,19,(95,60,343,118)),(3,25,(100,60,337,147))]:
    # Cropping boxes are verified against rendered pages before final use.
    out=fitz.open(); src=doc[physical-1]
    region=fitz.Rect(rect); p=out.new_page(width=region.width,height=region.height)
    p.show_pdf_page(p.rect,doc,physical-1,clip=region)
    target=BASE/f'assets/chapter1/fig1-{num}.pdf'
    if target.exists():
        target.unlink()
    out.save(target)
    p.get_pixmap(matrix=fitz.Matrix(1.5,1.5)).save(BASE/f'work/fig1-{num}-crop.png')

print(json.dumps({'objects':objects,'source_path':str(SOURCE)},ensure_ascii=False))
