from pathlib import Path
B=Path(__file__).resolve().parents[1]
p=B/'sections-tex/05-02.tex';s=p.read_text(encoding='utf-8')
a=r'族成员$(1/\sigma)f((x-\mu)/\sigma)$'
assert s.count(a)==1
s=s.replace(a,r'族成员$(1/\sigma)\allowbreak f((x-\mu)/\sigma)$')
p.write_text(s,encoding='utf-8')
print('Added a legal line break inside the inline location-scale density.')
