from pathlib import Path
import re, subprocess, unicodedata, json
BASE=Path(__file__).resolve().parents[1]
SOURCE=BASE.parents[1]/'books/Statistical Optimal Transport.pdf'
TEMP=BASE/'work/full-temp'
TEMP.mkdir(exist_ok=True)
p=TEMP/'references-layout.txt'
if not p.exists(): subprocess.run(['pdftotext','-layout','-f','250','-l','265',str(SOURCE),str(p)],check=True)
s=p.read_text('utf-8')
s=re.sub(r'(?m)^\s*(?:\d+\s+References|References\s+\d+)\s*$','',s)
s=re.sub(r'(?m)^.*© The Author.*$','',s)
s=re.sub(r'(?m)^\s*S\. Chewi et al\..*$','',s)
s=re.sub(r'(?m)^\s*Saint-Flour 2364.*$','',s)
# Limit the printed item prefix to 1–3 digits. A line-wrapped arXiv id beginning
# 49760. is part of a citation, not a nonexistent reference 49760.
pat=r'(?ms)^\s*(\d{1,3})\.\s+(.*?)(?=^\s*\d{1,3}\.\s+|\Z)'
entries={int(m[1]):m[2] for m in re.finditer(pat,s)}
assert set(entries)==set(range(1,331)),sorted(set(range(1,331))-set(entries))
def clean(t):
    t=unicodedata.normalize('NFC',t.replace('\x0c',' ').replace('ﬁ','fi').replace('ﬂ','fl'))
    # Keep lexical hyphens; remove only discretionary line-break hyphens.
    t=re.sub(r'\b(log|heavy|mean|max|d’Alché)-\s*\n\s*',lambda m:m[1]+'-',t)
    t=re.sub(r'(?<=\w)-\s*\n\s*(?=\w)','',t)
    t=re.sub(r'\s+',' ',t).strip()
    t=re.sub(r'(?<=\d)–\s+(?=\d)','–',t)
    t=re.sub(r'–\s+(?=[A-Za-z])','–',t)
    t=t.replace('in Rd ..',r'in $\mathbb R^d$.')
    # Literal text from the source; no inferred bibliographic metadata.
    for ch,r in [('&',r'\&'),('%',r'\%'),('_',r'\_'),('#',r'\#')]: t=t.replace(ch,r)
    return t
bib=[]
for n in range(1,331):
    t=clean(entries[n])
    # These three mathematical titles were checked on the rendered source.
    if n==62: t=t.replace('w ∗ .-algebras',r'$w^*$-algebras')
    if n==89: t=t.removesuffix(' √')
    if n==90: t=t.replace('O( n log3/4 n).',r'$O(\sqrt{n}\log^{3/4}n)$')
    if n==235: t=t.replace('O(1/k 2 )..',r'$O(1/k^2)$.')
    t=re.sub(r'(https?://[^\s}]+)',lambda m:r'\url{'+m[1]+'}',t)
    entries[n]=t
    bib.append(f'@misc{{ref{n},\n  key = {{{n:04}}},\n  note = {{{t}}}\n}}\n')
(BASE/'bib/references-full.bib').write_text('\n'.join(bib),encoding='utf-8')
(BASE/'work/full-bibliography-source-map.json').write_text(json.dumps(entries,ensure_ascii=False,indent=2),encoding='utf-8')
print('Created all 330 source bibliography entries without adding external metadata.')
