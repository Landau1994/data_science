from pathlib import Path
B=Path(__file__).resolve().parents[1]
p=B/'Statistical Inference_Chn.tex';s=p.read_text(encoding='utf-8')
assert r'\input{chapters-tex/02.tex}' not in s
s=s.replace('统计推断：书前材料及第1章中文译稿','统计推断：第二版中文译稿')
s=s.replace('中文译稿：书前材料及第1章.','中文译稿：全12章及前后材料.')
s=s.replace('按章校对，持续汇总全书；原书版权归原权利人.','原书版权归原权利人. 仅作学习参考.')
s=s.replace('原编号与原疑误保留；核验范围及说明见DS011统一台账.','原编号与原疑误保留；疑误及适用条件以译注说明.')
s=s.replace('本册译稿目录','中文译稿目录')
parts=[]
for ch in range(2,13):parts.append(r'\input{chapters-tex/'+f'{ch:02}.tex'+'}')
parts.append(r'\appendix')
for n in ['01-computer-algebra','02-distributions','03-references','04-index']:parts.append(r'\input{backmatter/'+n+'.tex}')
s=s.replace(r'\end{document}','\n'.join(parts)+'\n'+r'\end{document}')
p.write_text(s,encoding='utf-8')
p=B/'frontmatter/00-contents.tex';s=p.read_text(encoding='utf-8')
note='本节及后面的原书表、图、例目录保留原书页码；点击条目可跳到本译稿的对应位置. 译稿自己的页码见后面的“中文译稿目录”.'
if note not in s:
 i=s.find('\n');s=s[:i+1]+note+'\n\n'+s[i+1:];p.write_text(s,encoding='utf-8')
print('Full book assembled; official PDF unchanged until final verification.')
