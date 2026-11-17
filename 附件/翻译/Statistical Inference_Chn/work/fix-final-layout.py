from pathlib import Path
import json,re
B=Path(__file__).resolve().parents[1];fixes=[]
def fix(file,old,new,reason,pages):
 p=B/file;t=p.read_text(encoding='utf-8')
 if new not in t:
  assert t.count(old)==1,(file,old,t.count(old));p.write_text(t.replace(old,new),encoding='utf-8')
 fixes.append({'file':file,'old':old,'new':new,'reason':reason,'before_pdf_pages':pages})
def keep(file,kind,label,lines,pages):
 text=(B/'sections-tex'/file).read_text(encoding='utf-8')
 old=re.search(r'\\begin\{'+kind+r'\}(?:\[[^]]*\])?\\label\{'+re.escape(label)+r'\}',text).group()
 fix('sections-tex/'+file,old,'\\needspace{'+str(lines)+'\\baselineskip}\n'+old,'保留标题、题干与首个分问或公式的衔接',pages)
keep('02-03.tex','theorem','thm:2.3.11',6,[101,102])
keep('02-05.tex','exercise','exercise:2.14',5,[113,114])
keep('03-07.tex','exercise','exercise:3.34',6,[168,169])
keep('04-07.tex','example','ex:4.7.8',6,[222,223])
keep('05-07.tex','exercise','exercise:5.14',5,[286,287])
keep('10-05.tex','exercise','exercise:10.13',6,[535,536])
keep('11-04.tex','exercise','exercise:11.18',6,[594,595])
keep('12-05.tex','exercise','exercise:12.7',6,[630,631])
fix('sections-tex/03-03.tex',r'容易看出，\eqref{eq:3.3.19}对所有',r'\needspace{5\baselineskip}容易看出，\eqref{eq:3.3.19}对所有','避免“因此”二字跨页且单字悬在公式前',[143,144])
fix('sections-tex/04-01.tex',r'\sourcepageanchor{151}',r'\par\pagebreak[4]'+'\n'+r'\sourcepageanchor{151}','为脚注49留出同页空间，使其与标记同页',[180,181])
fix('sections-tex/05-04.tex',r'\autoref{exercise:5.28}）.',r'\autoref{exercise:5.28}\mbox{）.}','避免句点落在行首',[261])
fix('sections-tex/05-05.tex','第22节）.',r'第22节\mbox{）.}','避免句点独占一行',[265])
fix('sections-tex/09-03.tex',r'区间估计“$\theta\in C$”.',r'区间估计“$\theta\in C$\mbox{”.}','避免句点落在行首',[479])
fix('sections-tex/10-06.tex','自助分布（bootstrap distribution）.',r'自助分布（bootstrap distribution\mbox{）.}','避免句点落在行首',[550])
fix('sections-tex/11-01.tex',r'\hyperref[bib:source102]{Draper和Smith（1998）}.',r'\hyperref[bib:source102]{Draper和Smith（1998\mbox{）.}}','避免文献后句点落在行首',[552])
fix('sections-tex/11-05.tex',r'\autoref{exercise:11.23}）.',r'\autoref{exercise:11.23}\mbox{）.}','避免句点落在行首',[602])
fix('sections-tex/11-05.tex','（上述估计量向零收缩）.',r'（上述估计量向零收缩\mbox{）.}','避免句点落在行首',[604])
fix('sections-tex/12-03.tex',r'\begin{example}[挑战者号数据续]',r'\enlargethispage{1pt}'+'\n'+r'\begin{example}[挑战者号数据续]','增加1pt正文页高消除0.5561pt纵向溢出，不压缩公式',[622])
fix('backmatter/01-computer-algebra-b.tex',r'这一步实际上并不必要.）\footnote',r'这一步其实不必要.）\footnote','等义缩短括号内文字，为译注标记保留同行空间；单独nobreak未改变版面，已实际替换验证',[647])
fix('backmatter/02-distributions.tex',r'\autoref{exercise:4.32}）.',r'\autoref{exercise:4.32}\mbox{）.}','避免句点独占一行',[650])
(B/'work/final-layout-fixes.json').write_text(json.dumps(fixes,ensure_ascii=False,indent=2),encoding='utf-8')
print('Applied',len(fixes),'layout fixes')
