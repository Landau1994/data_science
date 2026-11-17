from pathlib import Path
import sys,json
B=Path(__file__).resolve().parents[1]
chapters=list(map(int,sys.argv[1:]))or[1,2,3,5,6,9,10];log=[]
for ch in chapters:
 p=B/'Statistical Inference_Chn.tex'if ch==1 else B/'chapters-tex'/f'{ch:02}.tex'
 s=p.read_text(encoding='utf-8');key=r'\label{sec:'+str(ch)+'}'
 assert s.count(key)==1,(ch,p)
 if r'\chapterdoi{'+str(ch)+'}'not in s:
  s=s.replace(key,key+'\n'+r'\chapterdoi{'+str(ch)+'}')
  p.write_text(s,encoding='utf-8');log.append(ch)
out=B/'work/restored-chapter-dois.json';old=json.loads(out.read_text(encoding='utf-8'))if out.exists()else[]
out.write_text(json.dumps(sorted(set(old+log))),encoding='utf-8')
print('Restored source chapter DOI metadata:',log)
