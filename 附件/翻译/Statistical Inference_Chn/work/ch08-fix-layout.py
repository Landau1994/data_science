from pathlib import Path
import re
for p in Path('sections-tex').glob('08-*.tex'):
 s=p.read_text(encoding='utf-8-sig')
 s=s.replace('）.','）\\nobreak.')
 s=re.sub(r'(?<!\n)\n(?=\\begin\{(?:figure|table)\})','\n\n',s)
 s=re.sub(r'(\\end\{(?:figure|table)\})\n(?!\n)',r'\1\n\n',s)
 p.write_text(s,encoding='utf-8')
