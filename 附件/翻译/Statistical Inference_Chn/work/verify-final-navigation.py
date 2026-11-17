from pathlib import Path
import json,hashlib,subprocess,sys
B=Path(__file__).resolve().parents[1]
index=B/'backmatter/04-index.tex';before=hashlib.sha256(index.read_bytes()).hexdigest()
r=subprocess.run([sys.executable,'-X','utf8',str(B/'work/build-index.py')],capture_output=True,text=True,encoding='utf-8')
after=hashlib.sha256(index.read_bytes()).hexdigest();assert r.returncode==0 and before==after
links=json.loads((B/'work/full-pdf-link-rectangles.json').read_text(encoding='utf-8'))['target']
notes=[x for x in links if str(x.get('name','')).startswith('Hfootnote.')]
bad=[x for x in notes if x['page']!=x['target_page']]
assert len({x['name']for x in notes})==292 and not bad
result={'index_file_sha256':after,'index_stable':True,'footnote_link_annotations':len(notes),'footnote_distinct_targets':len({x['name']for x in notes}),'footnote_page_mismatches':bad,'pdf_sha256':hashlib.sha256((B/'work/Statistical Inference_Chn.pdf').read_bytes()).hexdigest()}
(B/'work/final-navigation-check.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print('Index stable; 292 footnotes resolve to the same page as their markers.')
