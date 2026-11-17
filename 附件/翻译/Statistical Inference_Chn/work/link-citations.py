from pathlib import Path
import re,json
B=Path(__file__).resolve().parents[1]
pages=(B/'work/source-layout.txt').read_text(encoding='utf-8').split('\f')
ids={33,77,114,118,132,154,187,221,223,230,279,280,285,306,314,322,323,332,333}
records=[]
for i in range(539,554):
    for text in re.split(r'\n\s*(?=\[\d+\])',pages[i]):
        m=re.match(r'\[(\d+)\]\s*(.*)',text.strip(),re.S)
        if m and int(m[1]) in ids:
            raw=re.sub(r'\s+',' ',m[2]).strip()
            records.append({'number':int(m[1]),'physical_page':i+1,'printed_page':i-30,'transcription':raw})
(B/'bib').mkdir(exist_ok=True)
# A source-preserving transcription record, not inferred bibliographic metadata.
entries=[]
for r in records:
    raw=r['transcription'].replace('&',r'\&')
    entries.append('@misc{source'+str(r['number'])+',\n  note = {'+raw+'},\n  sourcepage = {'+str(r['physical_page'])+'},\n  sourcenumber = {'+str(r['number'])+'}\n}')
(B/'bib/references.bib').write_text('% 本阶段引用的原书书目逐字转录；note保留原记录，不推断缺失字段。尚未构建全书书目。\n'+'\n\n'.join(entries)+'\n',encoding='utf-8')
(B/'work/citation-map.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')
replacements={
'Miller（1981）':(549,'Miller（1981）'),
'Efron与Tibshirani，1993':(544,'Efron与Tibshirani，1993'),
'Stigler（1983）':(552,'Stigler（1983）'),
'Billingsley，1995，第31节':(541,'Billingsley，1995，第31节'),
'Gardner（1961）':(545,'Gardner（1961）'),
'Feller（1968）':(545,'Feller（1968）'),
'Feller 1968，第IV.1节':(545,'Feller 1968，第IV.1节'),
'Hall 1992，附录I':(546,'Hall 1992，附录I'),
'Selvin（1975）':(551,'Selvin（1975）'),
'vos Savant 1990':(553,'vos Savant 1990'),
'vos Savant 1991':(553,'vos Savant 1991'),
'Tierney 1991':(553,'Tierney 1991'),
'Morgan等（1991）':(549,'Morgan等（1991）'),
'Chun（1999）':(543,'Chun（1999）'),
'Schwager（1984）':(551,'Schwager（1984）'),
'Schwager（1985）':(551,'Schwager（1985）'),
'Worsley（1982）':(553,'Worsley（1982）'),
'Worsley（1985）':(553,'Worsley（1985）'),
'Karlin和Ost 1988':(548,'Karlin和Ost 1988'),
'Naiman和Wynn 1992':(549,'Naiman和Wynn 1992'),
}
for p in B.glob('sections-tex/*.tex'):
    s=p.read_text(encoding='utf-8').replace('杂论','杂录')
    for old,(page,txt) in replacements.items():
        new=r'\sourcepageref{'+str(page)+'}{'+txt+'}'
        if new not in s:s=s.replace(old,new)
    if p.name=='01-02.tex':
        s=s.replace(r'\sourcepageref{523}{例12.6.1}',r'\sourcepageref{528}{例12.6.1}')
        s=re.sub(r'\n\\noindent\\textit\{译注：\}[^\n]*\n','\n',s)
        s=s.replace(r'\footnote{译注：原文使用等号；这里保留.$9/128=0.0703125$，$.07$是保留两位小数的近似值.}','')
    p.write_text(s,encoding='utf-8')
plan=json.loads((B/'work/reference-plan.json').read_text(encoding='utf-8'))
if isinstance(plan,list):
    (B/'work/reference-plan.json').write_text(json.dumps({'source_candidates':plan,'scope':'source PDF pages1–68; internal and sourcepageref targets audited by audit.py'},ensure_ascii=False,indent=2),encoding='utf-8')
print('real source bibliography records',len(records))
