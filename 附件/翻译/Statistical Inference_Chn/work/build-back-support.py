from pathlib import Path
import sys,json,re,unicodedata
B=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(B/'work/python-deps'))
import pymupdf as fitz
source=json.loads((B/'work/source-baseline.json').read_text(encoding='utf-8'))
d=fitz.open(source['path'])
assets=B/'assets/backmatter';assets.mkdir(parents=True,exist_ok=True)
rect=fitz.Rect(54,198,449,652)
out=fitz.open();p=out.new_page(width=rect.width,height=rect.height)
p.show_pdf_page(p.rect,d,538,clip=rect)
out.save(assets/'distribution-relations.pdf');out[0].get_pixmap(dpi=130).save(B/'work/distribution-relations.png')
pages=(B/'work/source-layout.txt').read_text(encoding='utf-8').split('\f')
entries=[];current=None
for physical in range(540,555):
    for line in pages[physical-1].splitlines():
        t=line.strip()
        if not t or t=='References' or re.fullmatch(r'(?:REFERENCES\s+)?\d+(?:\s+REFERENCES)?',t):continue
        m=re.match(r'\[(\d+)\]\s+(.*)',t)
        if m:
            current={'number':int(m[1]),'physical_page':physical,'lines':[m[2]]};entries.append(current)
        elif current is not None:current['lines'].append(t)
for e in entries:
    # Undo typographic line-break hyphens while retaining the unmodified lines.
    e['text']=unicodedata.normalize('NFC',re.sub(r'(?<=[A-Za-z])-\n(?=[a-z])','', '\n'.join(e['lines'])).replace('\n',' '))
    e['text']=re.sub(r'(\d)([–-])\s+(\d)',r'\1\2\3',e['text'])
assert [e['number'] for e in entries]==list(range(1,339))
(B/'work/references-all.json').write_text(json.dumps(entries,ensure_ascii=False,indent=2),encoding='utf-8')
def esc(t):
    t=re.sub(r"(?<=[A-Za-z])\s*’\s*(?=s\b)",'’',t)
    return ''.join({'&':r'\&','%':r'\%','#':r'\#','_':r'\_','$':r'\$','{':r'\{','}':r'\}','α':r'\ensuremath{\alpha}'}.get(c,c) for c in t)
bib=['% 原书338条书目完整转录；保留原编号和可见元数据，不联网补全。']
tex=[r'\clearpage\renewcommand{\refname}{参考文献}',r'\phantomsection\label{app:references}\addcontentsline{toc}{section}{参考文献}',r'\begin{thebibliography}{338}',r'\small\setlength{\itemsep}{3pt plus 1pt minus 1pt}']
lastpage=None
for e in entries:
    n=e['number'];t=esc(e['text'])
    if n==92:t=t.replace('S2',r'$S^2$')
    if n==307:t=t.replace('X and S2',r'$\bar X$ and $S^2$').replace('X̄ and S2',r'$\bar X$ and $S^2$')
    bib.append('@misc{source'+str(n)+',\n  note = {'+t+'},\n  sourcepage = {'+str(e['physical_page'])+'},\n  sourcenumber = {'+str(n)+'}\n}')
    if e['physical_page']!=lastpage:
        tex.append(r'\sourcepageanchor{'+str(e['physical_page'])+'}');lastpage=e['physical_page']
    tex.append(r'\bibitem['+str(n)+']{source'+str(n)+r'}\label{bib:source'+str(n)+'} '+t)
tex.append(r'\end{thebibliography}')
(B/'bib/references.bib').write_text('\n\n'.join(bib)+'\n',encoding='utf-8')
(B/'backmatter/03-references.tex').write_text('\n'.join(tex)+'\n',encoding='utf-8')
print('Bibliography: 338 consecutive entries; relation diagram cropped.')
