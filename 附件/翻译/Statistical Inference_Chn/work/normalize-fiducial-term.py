from pathlib import Path
B=Path(__file__).resolve().parents[1]
p=B/'sections-tex/06-03.tex';s=p.read_text(encoding='utf-8')
# Match the established front-matter example title and bilingual index entry.
for a,b in [('基准推断','信仰推断'),('基准分布','信仰分布'),('基准pdf','信仰pdf')]:s=s.replace(a,b)
p.write_text(s,encoding='utf-8')
print('Aligned fiducial terminology with the existing example list and bilingual index.')
