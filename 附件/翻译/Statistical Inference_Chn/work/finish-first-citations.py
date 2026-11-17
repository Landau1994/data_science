from pathlib import Path
import json
B=Path(__file__).resolve().parents[1]
edits={
'05-07.tex': [('Mengersen和Tweedie 1995',r'\hyperref[bib:source218]{Mengersen和Tweedie 1995}\footnote{译注：正文此处引1995年，原书书后同名论文条目[218]列1996年；这里分别保留两处年份，链接至该条目.}')],
'05-08.tex': [('Tanner（1993）',r'\hyperref[bib:source312]{Tanner（1993）}\footnote{译注：正文此处引1993年，原书书后同名著作条目[312]列1996年；这里分别保留两处年份，链接至该条目.}')],
'09-02.tex': [('Barnard（1949，1980）',r'Barnard（\hyperref[bib:source10]{1949}，\hyperref[bib:source11]{1980}）'),('Fraser 1968，1979',r'Fraser \hyperref[bib:source127]{1968}，\hyperref[bib:source128]{1979}')],
'09-05.tex': [('Tsao和Hwang（1998，1999）',r'Tsao和Hwang（\hyperref[bib:source316]{1998}，\hyperref[bib:source317]{1999}）')],
}
log=[]
for name,pairs in edits.items():
 p=B/'sections-tex'/name;s=p.read_text(encoding='utf-8')
 for old,new in pairs:
  if new in s:continue
  assert s.count(old)==1,(name,old)
  s=s.replace(old,new)
  log.append({'file':name,'old':old,'new':new})
 p.write_text(s,encoding='utf-8')
(B/'work/citation-manual-edits.json').write_text(json.dumps(log,ensure_ascii=False,indent=2),encoding='utf-8')
print('Applied',len(log),'source-verified citation edits.')
