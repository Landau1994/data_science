from pathlib import Path
import sys
B=Path(__file__).resolve().parents[1];sys.path.insert(0,str(B/'work/python-deps'))
import pymupdf as fitz
p=B/sys.argv[1];d=fitz.open(p);out=B/'work'/('spot-'+p.stem);out.mkdir(exist_ok=True)
for n in map(int,sys.argv[2:]):
 q=out/f'{n:03}.png';d[n-1].get_pixmap(dpi=120).save(q);print(q)
