from pathlib import Path
import re,json,shutil
B=Path(__file__).resolve().parents[1]
# Snapshot the reviewed render hashes before layout corrections.
shutil.copyfile(B/'work/pdf-audit.json',B/'work/pdf-audit-before-refine.json')
for p in B.glob('frontmatter/*.tex'):
    s=p.read_text(encoding='utf-8')
    s=re.sub(r'(\\section\*\{[^}]+\})(?!\\phantomsection)',r'\1\\phantomsection',s)
    p.write_text(s,encoding='utf-8')
p=B/'Statistical Inference_Chn.tex';s=p.read_text(encoding='utf-8')
s=s.replace('xurl,float,multirow','xurl,float,multirow,placeins')
p.write_text(s,encoding='utf-8')
p=B/'sections-tex/01-02.tex';s=p.read_text(encoding='utf-8')
s=s.replace('\\begin{enumerate}\n\\item 对所有',r'\begin{enumerate}[label=\arabic*.]'+'\n\\item 对所有')
s=s.replace('\\begin{enumerate}\n\\item \\emph{有序',r'\begin{enumerate}[label=\arabic*.]'+'\n\\item \\emph{有序')
s=s.replace('\\begin{enumerate}\n\\setcounter{enumi}{3}',r'\begin{enumerate}[label=\arabic*.]'+'\n\\setcounter{enumi}{3}')
p.write_text(s,encoding='utf-8')
p=B/'sections-tex/01-03.tex';s=p.read_text(encoding='utf-8').replace('分割','划分').replace('）.式\\eqref{eq:1.3.8}','）\\nobreak.式\\eqref{eq:1.3.8}')
p.write_text(s,encoding='utf-8')
p=B/'sections-tex/01-06.tex';s=p.read_text(encoding='utf-8').replace('\\end{figure}\n\n\\begin{example}','\\end{figure}\n\\FloatBarrier\n\\begin{example}')
p.write_text(s,encoding='utf-8')
p=B/'sections-tex/01-07.tex';s=p.read_text(encoding='utf-8').replace('的回应）.','的回应）\\nobreak.').replace('Kolmogorov公理','柯尔莫哥洛夫公理')
p.write_text(s,encoding='utf-8')
# Chung (1974) was cited twice, independently of Chun (1999).
pages=(B/'work/source-layout.txt').read_text(encoding='utf-8').split('\f')
for i in range(539,554):
    for text in re.split(r'\n\s*(?=\[\d+\])',pages[i]):
        m=re.match(r'\[(\d+)\]\s*(Chung,.*)',text.strip(),re.S)
        if m and '(1974)' in m[2]:
            raw=re.sub(r'\s+',' ',m[2]).strip();pg=i+1;num=m[1]
            bib=B/'bib/references.bib';bs=bib.read_text(encoding='utf-8')
            if '@misc{source'+num+',' not in bs:
                bib.write_text(bs+'\n@misc{source'+num+',\n note={'+raw+'},\n sourcepage={'+str(pg)+'},\n sourcenumber={'+num+'}\n}\n',encoding='utf-8')
            p=B/'sections-tex/01-05.tex';s=p.read_text(encoding='utf-8')
            s=s.replace('Chung（1974），第27页',r'\sourcepageref{'+str(pg)+'}{Chung（1974），第27页}')
            s=s.replace('Chung，1974，第2.2节',r'\sourcepageref{'+str(pg)+'}{Chung，1974，第2.2节}')
            p.write_text(s,encoding='utf-8')
print('refined headings, numeric lists, floats and punctuation')
