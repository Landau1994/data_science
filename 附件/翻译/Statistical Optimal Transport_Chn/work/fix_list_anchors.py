from pathlib import Path
import re
BASE=Path(__file__).resolve().parents[1]
for name,label in [('01-02.tex','ex:1.4'),('01-08.tex','exer:1.4'),('04-06.tex','exer:4.1'),('04-06.tex','exer:4.2'),('05-10.tex','exer:5.8')]:
    p=BASE/'sections-tex'/name; t=p.read_text('utf-8')
    needle='\\label{'+label+'}'
    start=t.index(needle)+len(needle)
    tail=t[start:]
    # amsthm delays its heading. An immediate list can discard its hyperref
    # destination; enter horizontal mode before that list to retain it.
    if not tail.lstrip().startswith('\\leavevmode'):
        t=t[:start]+'\\leavevmode'+t[start:]
        p.write_text(t,encoding='utf-8')
print('Preserved five deferred theorem/list destinations.')
