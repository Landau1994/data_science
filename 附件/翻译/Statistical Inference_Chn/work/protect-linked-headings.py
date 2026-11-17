from pathlib import Path
import re,sys
B=Path(__file__).resolve().parents[1]
chapters=sys.argv[1:]or['01','02','03','05','09','10'];count=0
for p in (B/'sections-tex').glob('*.tex'):
 if p.name[:2]not in chapters:continue
 s=p.read_text(encoding='utf-8');edits=[]
 for m in re.finditer(r'\\begin\{(?:theorem|lemma|corollary|definition|example|proof|exercise|remark)\}\[',s):
  depth=1;i=m.end()
  while depth and i<len(s):
   if s[i]=='[':depth+=1
   elif s[i]==']':depth-=1
   i+=1
  assert depth==0,p
  title=s[m.end():i-1]
  if r'\hyperref['in title and not(title.startswith('{')and title.endswith('}')):edits.append((m.end(),i-1,'{'+title+'}'))
 for a,z,t in reversed(edits):s=s[:a]+t+s[z:]
 if edits:p.write_text(s,encoding='utf-8')
 count+=len(edits)
print('Protected',count,'linked environment titles.')
