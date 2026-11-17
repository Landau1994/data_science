from pathlib import Path
import json,re,hashlib,urllib.parse
B=Path(__file__).resolve().parents[1];R=B.parents[2]
def read(n):return json.loads((B/n).read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
f=read('work/final-artifact-checks.json');m=read('manifest.json');d=read('work/wholebook-visual-delta.json');nav=read('work/final-navigation-check.json');errors=[]
actual=sha(B/'Statistical Inference_Chn.pdf')
assert actual==f['pdf']['sha256']==d['after_pdf_sha256']==m['pdf']['sha256']==nav['pdf_sha256']
assert sha(Path(f['source']['path']))==f['source']['sha256']
for name,h in f['input_hashes'].items():
 if sha(B/name)!=h:errors.append(('input_changed_after_build',name))
for name,h in f['asset_hashes'].items():
 if sha(B/name)!=h:errors.append(('asset_changed_after_build',name))
assert d['status']=='passed' and set(d['changed_pages'])<=set(d['reviewed_pages'])
ds=R/'00 - 首页/教材归档/DS011 - Statistical Inference.md';t=ds.read_text(encoding='utf-8')
for required in ['status: not-started','source_status: verified','translation_status: completed',f'translation_pdf_pages: {f["pdf"]["pages"]}']:
 if required not in t:errors.append(('ledger',required))
readme=(R/'README.md').read_text(encoding='utf-8');tail=readme.split('## 更新日志',1)[1]
assert len(re.findall(r'^### ',tail,re.M))==3
wiki_checked=0
for q in [ds,R/'02 - 数理统计/数理统计导航.md',R/'README.md']:
 text=q.read_text(encoding='utf-8')
 for target in re.findall(r'\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]',text):
  if target.startswith('附件/翻译/Statistical Inference_Chn'):
   dest=R/target;wiki_checked+=1
   if not dest.exists()and not dest.with_suffix('.md').exists():errors.append(('wiki_link',str(q),target))
reports=['核验说明.md','compile-report.md','static-check-report.md','pdf-link-audit-report.md','reference-map.md','source-ledger.md','fidelity-report.md'];md_checked=0
for name in reports:
 text=(B/name).read_text(encoding='utf-8')
 if re.search(r'待总编|最终验收待补|全书尚未完成',text):errors.append(('stale_report',name))
 for target in re.findall(r'\[[^\]]*\]\(([^)]*)\)',text):
  target=urllib.parse.unquote(target.split('#')[0].strip('<>'))
  if not target or re.match(r'\w+://',target):continue
  md_checked+=1
  if not(B/target).exists():errors.append(('markdown_link',name,target))
assert len(f['input_hashes'])==116 and len(f['asset_hashes'])==57
result={'date':'2026-11-04','pdf_sha256':actual,'pdf_pages':f['pdf']['pages'],'source_sha256_unchanged':True,'input_files_unchanged':len(f['input_hashes']),'assets_unchanged':len(f['asset_hashes']),'source_status':'verified','translation_status':'completed','learning_status':'not-started','readme_recent_entries':3,'new_wiki_links_checked':wiki_checked,'report_links_checked':md_checked,'reviewed_delta_pages':len(d['changed_pages']),'pixel_identical_pages':len(d['unchanged_pages']),'errors':errors}
(B/'work/delivery-validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(result,ensure_ascii=False,indent=2));assert not errors
