from pathlib import Path
import json
B=Path(__file__).resolve().parents[1]
edits={
'03-03.tex':[(r'\hyperref[bib:source177]{Johnson和Kotz（1969}、1970a、1970b）',r'\hyperref[bib:source177]{Johnson和Kotz（1969、1970a、1970b）}')],
'03-06.tex':[(r'\hyperref[bib:source303]{Stein 1973}、1981',r'\hyperref[bib:source303]{Stein 1973}、\hyperref[bib:source304]{1981}')],
'10-01.tex': [('Lehmann和Casella，第6.1节',r'\hyperref[bib:source200]{Lehmann和Casella，第6.1节}'),('Efron（1979ab）',r'Efron（\hyperref[bib:source106]{1979a}\hyperref[bib:source107]{b}）')],
'10-02.tex': [('Hettmansberger和McKean（1998）',r'\hyperref[bib:source165]{Hettmansberger和McKean（1998）}\footnote{译注：原书正文将第一作者姓氏拼作Hettmansberger，书后对应条目[165]作Hettmansperger；正文拼写保留，链接至该条目.}')],
'10-06.tex': [('Hettmansberger和McKean（1998）',r'\hyperref[bib:source165]{Hettmansberger和McKean（1998）}')],
}
log=[]
for name,pairs in edits.items():
 p=B/'sections-tex'/name;s=p.read_text(encoding='utf-8')
 for old,new in pairs:
  if new in s:continue
  assert s.count(old)==1,(name,old)
  s=s.replace(old,new);log.append({'file':name,'old':old,'new':new})
 p.write_text(s,encoding='utf-8')
(B/'work/citation-manual-edits-ch03-10.json').write_text(json.dumps(log,ensure_ascii=False,indent=2),encoding='utf-8')
print('Applied',len(log),'citation edits.')
