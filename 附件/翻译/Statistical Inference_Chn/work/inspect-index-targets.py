from pathlib import Path
import sys,json
B=Path(__file__).resolve().parents[1];sys.path.insert(0,str(B/'work/python-deps'))
import pymupdf as fitz
d=fitz.open(json.loads((B/'work/source-baseline.json').read_text(encoding='utf-8'))['path'])
for l in d[555].get_links()[:12]:print({k:str(v) for k,v in l.items()})
