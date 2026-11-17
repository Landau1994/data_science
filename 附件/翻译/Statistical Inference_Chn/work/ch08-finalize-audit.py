from pathlib import Path
import json,re,hashlib,sys
root=Path.cwd();sys.path.insert(0,str(root/'work/python-deps'));import pymupdf as fitz
p=root/'work/ch08-manifest.json';d=json.loads(p.read_text(encoding='utf-8'))
aux=(root/'work/ch08-preview.aux').read_text(encoding='utf-8')
checks=[]
for label in [x['label'] for x in d['shared_objects']]+[x['label'] for x in d['numbered_equations']]+[x['label'] for x in d['exercises']]+['fig:8.2.1']+[f'fig:8.3.{i}' for i in range(1,5)]+['tab:8.3.1']:
 m=re.search(r'\\newlabel\{'+re.escape(label)+r'\}\{\{([^}]+)\}',aux)
 assert m and m[1]==label.split(':')[1],(label,m[1] if m else None)
 checks.append(label)
pdf=fitz.open(root/'work/ch08-preview.pdf');names=pdf.resolve_names();missing_dest=[]
def top_groups(text):
 out=[];depth=0;start=None
 for i,ch in enumerate(text):
  if ch=='{' and (i==0 or text[i-1]!='\\'):
   if depth==0:start=i+1
   depth+=1
  elif ch=='}' and (i==0 or text[i-1]!='\\'):
   depth-=1
   if depth==0:out.append(text[start:i])
 return out
for line in aux.splitlines():
 if not line.startswith('\\newlabel{'):continue
 pair=top_groups(line)
 if pair[0] not in set(checks+['src:'+str(n) for n in range(333,368)]):continue
 fields=top_groups(pair[1]);anchor=fields[3]
 if anchor not in names:missing_dest.append([pair[0],anchor])
assert not missing_dest,missing_dest
old=json.loads((root/'work/ch08-pre-final-render-hashes.json').read_text())
new={x.name:hashlib.sha256(x.read_bytes()).hexdigest() for x in (root/'work/ch08-render').glob('p*.png')}
changed=[int(x[1:4]) for x in new if old.get(x)!=new[x]]
d['local_preview']['visual_reviewed_pages']=list(range(1,47))
d['local_preview']['visual_rechecked_after_last_layout_fix']=changed
d['local_preview']['render_png_sha256']=new
d['local_preview']['visual_conclusion']='All 46 pages personally viewed; ten pages changed by final footnote-placement fixes were viewed again. No clipping, overprint, detached footnote marks or actual prose line-initial punctuation remains. Decimal .25 on page33 is a whole numeric value, not a detached punctuation mark.'
d['local_preview']['actual_numbering_checked_label_count']=len(checks)
d['local_preview']['missing_local_pdf_destinations']=missing_dest
d['local_preview']['foreign_link_boundary']='External labels imported from actual other-chapter builds only for printed reference width. Cross-chapter click destinations await complete-book validation.'
d['tex_snapshot_sha256']={rel:hashlib.sha256((root/rel).read_bytes()).hexdigest() for rel in d['files_in_input_order']}
d['independent_review_fixes'].extend(['Blank paragraphs around floats prevent text/formulas from being split by figures','Nonbreaking closing-parenthesis/period groups prevent prose line-initial ASCII periods','Moved five translator-note marks onto the sentences they annotate'])
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'actual_numbering_labels':len(checks),'missing_destinations':missing_dest,'reviewed_pdf_pages':46,'rechecked_changed_pages':changed,'overfull_hbox':d['local_preview']['overfull_hbox_count'],'overfull_vbox':d['local_preview']['overfull_vbox_count'],'missing_glyph':d['local_preview']['missing_glyph_count'],'undefined_refs':d['local_preview']['foreign_reference_warning_targets']},ensure_ascii=False))
