from pathlib import Path
import sys,json,hashlib
B=Path(__file__).resolve().parents[1];sys.path.insert(0,str(B/'work/python-deps'))
import pymupdf as fitz
d=fitz.open(B/'work/back-preview.pdf');out=B/'work/back-render-revised';out.mkdir(exist_ok=True)
same=[];changed=[]
for i,page in enumerate(d):
 p=out/f'{i+1:03}.png';page.get_pixmap(dpi=100).save(p)
 old=B/'work/back-render'/p.name
 (same if old.exists()and hashlib.sha256(old.read_bytes()).digest()==hashlib.sha256(p.read_bytes()).digest()else changed).append(i+1)
result={'pages':len(d),'identical_pages':same,'changed_pages':changed}
(B/'work/back-render-comparison.json').write_text(json.dumps(result),encoding='utf-8');print(result)
