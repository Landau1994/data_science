from pathlib import Path
B=Path(__file__).resolve().parents[1]
p=B/'sections-tex/08-05.tex';s=p.read_text(encoding='utf-8')
for a,b in [
('Berger（James，而非 Roger）与 Sellke (1987)',r'\hyperref[bib:source21]{Berger（James，而非 Roger）与 Sellke (1987)}'),
('Casella 与 Berger（Roger，1987）',r'\hyperref[bib:source66]{Casella 与 Berger（Roger，1987）}')]:
 assert a in s;s=s.replace(a,b)
p.write_text(s,encoding='utf-8')
