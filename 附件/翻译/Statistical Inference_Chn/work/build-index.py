from pathlib import Path
import re,json,unicodedata
B=Path(__file__).resolve().parents[1]
entries=json.loads((B/'work/index-entries.json').read_text(encoding='utf-8'))
dictionary={}
for l in (B/'work/index-translations.tsv').read_text(encoding='utf-8').splitlines():
    if l.strip():
        en,zh=l.split('|',1);dictionary[en]=zh
lower={k.casefold():v for k,v in dictionary.items()}
missing=set()
def tr(t):
    t=t.strip()
    if t in dictionary:return dictionary[t]
    if t.casefold() in lower:return lower[t.casefold()]
    if t.startswith('relation to '):
        v=tr(t[12:]);return '与'+v+'的关系'
    m=re.search(r'\s*\((see(?: also)?)\s+(.*)',t,re.I)
    if m:
        base=t[:m.start()];rest=m[2].rstrip(')')
        if rest in dictionary:return tr(base)+'（'+('另见' if 'also' in m[1].lower() else '见')+tr(rest)+'）'
        parts=re.split(r';\s*|,\s*',rest)
        return tr(base)+'（'+('另见' if 'also' in m[1].lower() else '见')+'；'.join(tr(x) for x in parts)+'）'
    missing.add(t);return t
for e in entries:e['zh']=tr(e['term'])
(B/'work/index-untranslated.txt').write_text('\n'.join(sorted(missing))+'\n',encoding='utf-8')
if missing:
    print('UNMAPPED',len(missing));print('\n'.join(sorted(missing)));raise SystemExit(1)
(B/'work/index-translated.json').write_text(json.dumps(entries,ensure_ascii=False,indent=2),encoding='utf-8')
print('All',len(entries),'index entries translated.')
def esc(t):
    t=unicodedata.normalize('NFC',t)
    t=re.sub(r"(?<=[A-Za-z])\s*’\s*(?=s\b)",'’',t)
    return ''.join({'&':r'\&','%':r'\%','#':r'\#','_':r'\_','$':r'\$','{':r'\{','}':r'\}','σ':r'\ensuremath{\sigma}','²':r'\ensuremath{{}^2}'}.get(c,c) for c in t)
def base(t):return re.split(r'\s*\(see',t,flags=re.I)[0]
ancestors=[]
for e in entries:
    level=e['level'];ancestors=ancestors[:level]
    while len(ancestors)<level:ancestors.append('')
    ancestors.append(base(e['term']));e['path']=list(ancestors)
aliases={'distribution bernoulli':['distribution','bernoulli'],'distribution beta':['distribution','beta'],'distribution gamma':['distribution','gamma'],'algorithm, em':['algorithm','em'],'point estimator consistent':['point estimator','consistent'],'point estimator, invariant':['point estimator','invariant'],'set operation':['set operations'],'point estimation':['point estimator']}
def dest(t):
    p=aliases.get(t.casefold(),[t.casefold()])
    candidates=[e for e in entries if [v.casefold() for v in e['path']]==p]
    if not candidates:raise ValueError('Missing index see target '+t)
    return candidates[0]['id']
see_targets=[]
def texterm(e):
    t=e['term'];m=re.search(r'\s*\((see(?: also)?)\s+(.*)',t,re.I)
    if not m:return esc(e['zh'])
    rest=m[2].rstrip(')')
    parts=[rest] if rest.casefold() in aliases else re.split(r';\s*|,\s*',rest)
    links=[]
    for v in parts:
        target=dest(v);see_targets.append({'from':e['id'],'term':v,'to':target})
        links.append(r'\hyperref[idx:'+str(target)+']{'+esc(tr(v))+'}')
    return esc(tr(t[:m.start()]))+'（'+('另见' if 'also' in m[1].lower() else '见')+'；'.join(links)+'）'
aux=B/'work/Statistical Inference_Chn.aux'
pagemap={}
def groups(s):
    out=[];depth=0;start=None
    for i,c in enumerate(s):
        if i and s[i-1]=='\\':continue
        if c=='{':
            if depth==0:start=i+1
            depth+=1
        elif c=='}':
            depth-=1
            if depth==0:out.append(s[start:i])
    return out
if aux.exists():
    for line in aux.read_text(encoding='utf-8').splitlines():
        if line.startswith(r'\newlabel{'):
            a=groups(line)
            if len(a)>=2:
                v=groups(a[1])
                if len(v)>=2:pagemap[a[0]]=v[1]
semantic_file=B/'work/index-semantic-resolved.json'
semantic={r['id']:r['target'] for r in json.loads(semantic_file.read_text(encoding='utf-8'))} if semantic_file.exists() else {}
lines=[r'\clearpage\section*{索引}\phantomsection\label{app:index}',r'\addcontentsline{toc}{section}{索引}',
'按原书英文词条顺序保留主项与子项，附中文译名.下列页码由本译稿中相关概念、定理、公式或习题的位置生成；同一译稿页的重复定位合并.原词条及原书页码的完整映射保存在核验资料中.'+r'\footnote{译注：原索引的“$t$ 检验／一致最强／无偏”（原印刷331页）与“置信区间／一致最准确／正态”（原印刷372页）分类比所引内容的实际陈述更宽. 此处分别定位到\autoref{exercise:8.37}、\autoref{exercise:9.47}的相关讨论，保留原分类，不据索引额外断言其结论. “每次比较错误率”原指印刷458页，明确定义实际在下一页的\hyperref[item:11.17.b]{习题11.17(b)}；“回归／残差”的明确公式同样在原索引所指页的下一页. 页码已按实际语义位置生成.}',
r'\begingroup\small\raggedright\interlinepenalty=10000\setlength{\parskip}{0pt}\setlength{\columnsep}{1.5em}',r'\begin{multicols}{2}']
seenphysical=set()
refcount=0
for e in entries:
    physical=e['physical']
    if physical not in seenphysical:
        lines.append(r'\sourcepageanchor{'+str(physical)+'}');seenphysical.add(physical)
    en=esc(e['term']);zh=texterm(e)
    if e['term']=='r2':en=r'$r^2$';zh=r'$r^2$'
    visible=zh if e['zh']==e['term'] or e['term']=='r2' else zh+'（'+en+'）'
    seenpages=set();refs=[]
    for p in re.findall(r'\d+',e['refs']):
        n=int(p)+31;target=semantic.get(str(e['id'])+':'+str(n),'src:'+str(n));translated=pagemap.get(target,target)
        if translated in seenpages:continue
        seenpages.add(translated)
        refs.append(r'\hyperref['+target+r']{\pageref*{'+target+'}}');refcount+=1
    indent=0 if e['level']==0 else 1 if e['level']==1 else 1.8
    if e['level']==0:lines.append(r'\par\addvspace{2pt}')
    if not refs:lines.append(r'\needspace{3\baselineskip}')
    lines.append(r'\par\noindent\hangindent='+str(indent+1)+'em'+r'\hspace*{'+str(indent)+'em}'+r'\phantomsection\label{idx:'+str(e['id'])+'}'+visible+('，'+', '.join(refs) if refs else '')+r'\par')
lines.extend([r'\end{multicols}',r'\endgroup'])
(B/'backmatter/04-index.tex').write_text('\n'.join(lines)+'\n',encoding='utf-8')
(B/'work/index-build-audit.json').write_text(json.dumps({'entries':len(entries),'source_page_refs':sum(len(re.findall(r'\d+',e['refs'])) for e in entries),'rendered_page_refs':refcount,'source_page_anchors_available':sum(n.startswith('src:') for n in pagemap),'semantic_locations':len(semantic),'see_targets':see_targets},ensure_ascii=False,indent=2),encoding='utf-8')
print('Index TeX generated;',refcount,'page references;',len(see_targets),'see targets.')
