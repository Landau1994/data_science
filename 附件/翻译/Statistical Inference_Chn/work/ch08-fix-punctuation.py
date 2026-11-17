from pathlib import Path
for p in Path('sections-tex').glob('08-*.tex'):
 s=p.read_text(encoding='utf-8-sig').replace('）\\nobreak.','\\mbox{）.}')
 p.write_text(s,encoding='utf-8')
