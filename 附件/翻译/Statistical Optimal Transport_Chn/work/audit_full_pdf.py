from pathlib import Path
from collections import Counter
import re, json, sys, hashlib, shutil
sys.path.insert(0,r'E:/project/math/ant/tmp/pypackages')
import pymupdf as fitz
BASE=Path(__file__).resolve().parents[1]; NAME='Statistical Optimal Transport_Chn'
BUILD=BASE/'work/full-build'
source=BASE.parents[1]/'books/Statistical Optimal Transport.pdf'
a=fitz.open(source); b=fitz.open(BUILD/(NAME+'.pdf'))
aux=(BUILD/(NAME+'.aux')).read_text('utf-8')
nums={m[1]:(m[2],m[3]) for m in re.finditer(r'\\newlabel\{([^}]+)\}\{\{([A-Z0-9]+(?:\.\d+)*)\}\{([^}]+)\}',aux)}
src=json.loads((BASE/'work/full-source-objects.json').read_text('utf-8'))
prefix={'Proposition':'prop','Theorem':'thm','Definition':'def','Example':'ex','Lemma':'lem','Assumption':'assump','Corollary':'cor','Remark':'rem'}
bad=[]
for o in src:
    k=prefix[o['type']]+':'+o['number']
    if nums.get(k,('',))[0]!=o['number']: bad.append(k)
eqs={'1':25,'2':22,'3':9,'4':27,'5':32,'6':29,'7':17,'8':13,'A':3}
for c,count in eqs.items():
    for n in range(1,count+1):
        k=f'eq:{c}.{n}'
        if nums.get(k,('',))[0]!=f'{c}.{n}': bad.append(k)
for c,count in {1:10,2:9,3:5,4:8,5:17,6:12,7:4,8:6}.items():
    for n in range(1,count+1):
        k=f'exer:{c}.{n}'
        if nums.get(k,('',))[0]!=str(n): bad.append(k)
for c,count in {'1':3,'3':2,'5':1,'7':1,'B':1}.items():
    for n in range(1,count+1):
        if nums.get(f'fig:{c}.{n}',('',))[0]!=f'{c}.{n}': bad.append(f'fig:{c}.{n}')
if nums.get('fig:front.1',('',))[0]!='1': bad.append('fig:front.1')
bib=dict(re.findall(r'\\bibcite\{ref(\d+)\}\{(\d+)\}',aux))
if bib!={str(n):str(n) for n in range(1,331)}: bad.append('bibliography labels')
invalid=[]; kinds=Counter()
for i,p in enumerate(b):
    for l in p.get_links():
        kinds[l['kind']]+=1
        if l['kind'] in (fitz.LINK_GOTO,fitz.LINK_NAMED):
            if not 0<=l.get('page',-1)<len(b): invalid.append((i+1,l.get('nameddest'),l.get('page')))
        elif l['kind'] not in (fitz.LINK_URI,): invalid.append((i+1,'unexpected link kind',l['kind']))
names=b.resolve_names()
for line in aux.splitlines():
    m=re.match(r'\\newlabel\{([^}]+)\}.*\}\{([^{}]+)\}\{\}\}$',line)
    if m and m[2] not in names: invalid.append(('label destination',m[1],m[2]))
chapter_pages={str(n):names[f'section.{n}']['page']+1 for n in range(1,9)}
chapter_pages.update({c:names[f'appendix.{c}']['page']+1 for c in ['A','B']})
source_ranges={'front':(1,14),'1':(15,50),'2':(51,90),'3':(91,108),'4':(109,133),'5':(134,162),'6':(163,198),'7':(199,222),'8':(223,239),'A':(240,246),'B':(247,249),'references':(250,265),'index':(266,267),'publisher':(268,269)}
out_starts={'front':1,**chapter_pages}
toc=b.get_toc(); refstart=next(v[2] for v in toc if v[1]=='参考文献'); idxstart=next(v[2] for v in toc if v[1]=='索引')
out_starts.update(references=refstart,index=idxstart)
policy=names['section*.7']['page']+1 if 'section*.7' in names else None
# The policy is unnumbered and intentionally absent from the original TOC.
for i,p in enumerate(b):
    if '编辑方针' in p.get_text() and i>=idxstart-1: policy=i+1; break
out_starts['publisher']=policy
order=list(source_ranges)
counts=[]
for j,k in enumerate(order):
    lo,hi=source_ranges[k]; ac=sum(l['kind'] in (fitz.LINK_GOTO,fitz.LINK_NAMED) for p in list(a)[lo-1:hi] for l in p.get_links())
    ob=out_starts[k]; oe=out_starts[order[j+1]]-1 if j+1<len(order) else len(b)
    bc=sum(l['kind'] in (fitz.LINK_GOTO,fitz.LINK_NAMED) for p in list(b)[ob-1:oe] for l in p.get_links())
    counts.append({'unit':k,'source_range':[lo,hi],'output_range':[ob,oe],'source_internal':ac,'output_internal':bc})
idx=(BUILD/(NAME+'.idx')).read_text('utf-8'); idxentries=re.findall(r'\\indexentry\{(.+)\}\{([^}]+)\}',idx)
assert len(idxentries)==104,len(idxentries)
assert len({key.split('|')[0] for key,page in idxentries})==100
assert not bad,bad
assert not invalid,invalid
assert hashlib.sha256(source.read_bytes()).hexdigest().upper()=='91E9CB41212ABC18B294283C19CA4B91F51920A532E5CC24B710A1481EEED272'
log=(BUILD/(NAME+'.log')).read_text('utf-8',errors='replace')
fatal=[w for w in ['undefined','Missing character','multiply defined','LaTeX Error','Fatal error'] if w in log]
assert not fatal,fatal
report=['# 全书实际编号、链接与索引检查','',f'- 输出{len(b)}页；原件269页，SHA256前后相同。', '- 实际aux逐项核对：166个编号陈述、177个数字公式、71题按章重置的显示编号、9幅原编号图（含前言图1）及330条文献原号全部一致。', f'- 全PDF链接类型计数：{dict(kinds)}；内部目标均在有效页范围内。无原书跨文件占位链接。', '- 动态索引：104条实际index写入，合并后100个唯一词条，含87顶层、13子项；其中100个正文页码锚点及4个see条目。全书100词条经独立语义审阅后定位；makeindex在引用解析后重建，采用译稿真实页码。', '', '| 单元 | 原物理页 | 译稿物理页 | 原内部注释 | 译稿内部注释 |','| --- | --- | --- | ---: | ---: |']
for x in counts:
    report.append(f'| {x["unit"]} | {x["source_range"][0]}–{x["source_range"][1]} | {x["output_range"][0]}–{x["output_range"][1]} | {x["source_internal"]} | {x["output_internal"]} |')
report+=['','计数受原PDF重复矩形、目录点击区域、翻译换行和同组引文影响；未通过给普通符号添加链接补数。总数或分单元数量不足时，须逐项核对原注释的实际语义，不得以新目录/索引链接掩盖正文遗漏。','', '本记录验证PDF注释编码及目标，不宣称在Obsidian内实测渲染或点击。原图、原页和译稿页的人工检查另有视觉复核记录。']
(BASE/'work/full-pdf-link-audit-report.md').write_text('\n'.join(report)+'\n',encoding='utf-8')
(BASE/'work/full-pdf-audit.json').write_text(json.dumps({'pages':len(b),'chapter_pages':chapter_pages,'unit_counts':counts,'link_kinds':dict(kinds),'bad_numbering':bad,'invalid_links':invalid,'index_entries':104,'index_unique':100},ensure_ascii=False,indent=2),encoding='utf-8')
shutil.copy2(BUILD/(NAME+'.log'),BASE/(NAME+'.log'))
print(json.dumps({'pages':len(b),'counts':counts,'bad':bad,'invalid':invalid,'idx':104},ensure_ascii=False))
