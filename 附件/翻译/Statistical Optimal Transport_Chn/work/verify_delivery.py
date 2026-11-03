from pathlib import Path
import json, re, hashlib, sys
sys.path.insert(0, r'E:/project/math/ant/tmp/pypackages')
import pymupdf as fitz

BASE = Path(__file__).resolve().parents[1]
ROOT = BASE.parents[2]
NAME = 'Statistical Optimal Transport_Chn'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest().upper()
checks = {}
source = ROOT/'附件/books/Statistical Optimal Transport.pdf'
checks['source_unchanged'] = sha(source) == '91E9CB41212ABC18B294283C19CA4B91F51920A532E5CC24B710A1481EEED272'
pdf = BASE/(NAME+'.pdf')
checks['final_pdf_hash'] = sha(pdf) == 'C476CAA79437841FAAAE53D3786DFC6C133495F376D0AD7D0E50731AFD355C0A'
checks['delivered_same_as_reviewed'] = sha(pdf) == sha(BASE/'work/full-build'/(NAME+'.pdf'))
checks['pdf_pages_235'] = len(fitz.open(pdf)) == 235
manifest = json.loads((BASE/'work/manifest-full.json').read_text('utf-8'))
checks['all_71_inputs_present'] = len(manifest['input_files']) == 71 and all((BASE/x).is_file() for x in manifest['input_files'])
checks['canonical_fragments_64'] = len(list((BASE/'sections-tex').glob('*.tex'))) == 64
checks['bibliography_330'] = len(re.findall(r'@\w+\{', (BASE/'bib/references-full.bib').read_text('utf-8'))) == 330
log = (BASE/(NAME+'.log')).read_text('utf-8')
checks['no_fatal_reference_glyph_overflow_errors'] = not any(x in log for x in ['Overfull', 'undefined', 'Missing character', 'multiply defined', 'LaTeX Error', 'Fatal error'])
audit = json.loads((BASE/'work/full-pdf-audit.json').read_text('utf-8'))
checks['numbering_and_links_pass'] = not audit['bad_numbering'] and not audit['invalid_links'] and audit['index_unique'] == 100
cleanup = json.loads((BASE/'work/cleanup-report.json').read_text('utf-8'))
checks['cleanup_record_800_files'] = cleanup['removed_files'] == 800 and cleanup['removed_bytes'] == 105302896
checks['all_recorded_temporary_paths_absent'] = all(not (BASE/x['path']).exists() for x in cleanup['removed'])
checks['logs_retained'] = len(list(BASE.rglob('*.log'))) == 3
readme = (ROOT/'README.md').read_text('utf-8')
checks['readme_latest_3_entries'] = len(re.findall(r'(?m)^### ', readme.split('## 更新日志')[1])) == 3
ledger = (ROOT/'00 - 首页/教材归档/DS006 - Statistical Optimal Transport.md').read_text('utf-8')
checks['learning_still_not_started'] = 'status: not-started' in ledger
checks['new_attachment_targets_exist'] = all((BASE/x).is_file() for x in [NAME+'.pdf',NAME+'.tex','核验说明.md','原文疑误与核对边界.md'])
report = {'date':'2026-11-03','checks':checks,'pass':all(checks.values()),'output_sha256':sha(pdf),'output_pages':235,'cleanup_files':800,'cleanup_bytes':105302896}
(BASE/'work/final-delivery-check.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(report,ensure_ascii=False))
assert report['pass'], [k for k,v in checks.items() if not v]
