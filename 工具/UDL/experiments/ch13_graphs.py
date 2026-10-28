"""DS001第13章：按原页录入图，整数游走计数与可编辑TikZ解答图。"""
from pathlib import Path
import itertools,json,math,platform,subprocess

ROOT=Path(__file__).resolve().parents[3]
ASSETS=ROOT/'附件/习题图/DS001'
# 图13.14，原PDF281/印刷267；矩阵行列顺序均为原图节点1,2,...。
EA=[(1,2),(1,3),(1,4),(1,6),(1,7),(2,3),(2,4),(2,5),(4,5),(6,7)]
EB=[(1,4),(1,7),(1,8),(2,3),(2,5),(2,6),(3,8),(4,8),(5,6),(5,7),(6,7)]
# Problem13.2 原PDF280/印刷266的两矩阵。
M1=[[0,1,1,0,0,0,0],[1,0,0,1,1,1,0],[1,0,0,0,0,1,1],
    [0,1,0,0,0,1,1],[0,1,0,0,0,0,1],[0,1,1,1,0,0,0],[0,0,1,1,1,0,0]]
M2=[[0,0,1,1,0,0,1],[0,0,1,1,1,0,0],[1,1,0,0,0,0,0],
    [1,1,0,0,1,1,1],[0,1,0,1,0,0,1],[0,0,0,1,0,0,1],[1,0,0,1,1,1,0]]
# 图13.15a的八条边；13.11以端点对命名边图节点。
E15=[(1,2),(1,3),(1,6),(2,4),(2,5),(3,4),(3,6),(4,5)]
# 13.15b的六个节点代表原像图的边1..6。
TARGET=[(1,2),(1,3),(2,3),(2,4),(3,5),(3,6),(4,6),(5,6)]
PREIMAGE=[('a','u'),('u','w'),('u','v'),('w','t'),('v','c'),('v','t')]

def adj(n,edges):
    a=[[0]*n for _ in range(n)]
    for x,y in edges:a[x-1][y-1]=a[y-1][x-1]=1
    return a
def multiply(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def power(a,k):
    b=[[int(i==j) for j in range(len(a))] for i in range(len(a))]
    for _ in range(k):b=multiply(b,a)
    return b
def enumerate_walks(n,edges,k):
    neighbors={i:[] for i in range(1,n+1)}
    for x,y in edges:neighbors[x].append(y);neighbors[y].append(x)
    def visit(x,left):
        if not left:return int(x==2)
        return sum(visit(y,left-1) for y in neighbors[x])
    return visit(1,k)
def line_edges(edges):
    return [(i+1,j+1) for i,j in itertools.combinations(range(len(edges)),2) if set(edges[i])&set(edges[j])]
def texmat(a):return '\\begin{bmatrix}'+'\\\\\n'.join(' & '.join(map(str,row)) for row in a)+'\\end{bmatrix}'

def graph(nodes,edges,coords,labels=None,edge_labels=None):
    text=[]
    for n in nodes:
        x,y=coords[n];label=labels[n] if labels else str(n)
        text.append(f'\\node[vertex] (v{n}) at ({x},{y}) {{$'+label+'$};')
    for i,(x,y) in enumerate(edges):
        label=f' node[midway,fill=white,inner sep=1pt] {{$e_{{{i+1}}}$}}' if edge_labels else ''
        text.append(f'\\draw (v{x}) --{label} (v{y});')
    return '\n'.join(text)
def circle(n,r=2):return {i:(round(r*math.cos(math.pi/2-2*math.pi*(i-1)/n),4),round(r*math.sin(math.pi/2-2*math.pi*(i-1)/n),4)) for i in range(1,n+1)}

def main():
    result={'source':'DS001 PDF280–282/印刷266–268','python':platform.python_version(),'graphs':{}}
    for label,n,edges in [('13.14a',7,EA),('13.14b',8,EB)]:
        a=adj(n,edges);walks={str(k):power(a,k)[0][1] for k in (3,7)}
        for k,value in walks.items():assert value==enumerate_walks(n,edges,int(k))
        result['graphs'][label]={'edges':edges,'adjacency':a,'degrees':[sum(row) for row in a],
            'walks_1_to_2':walks,'first_rows_of_powers':{str(k):power(a,k)[0] for k in (3,7)}}
    for m in (M1,M2):assert m==list(map(list,zip(*m))) and all(m[i][i]==0 for i in range(7))
    assert sorted(line_edges(PREIMAGE))==sorted(TARGET)
    result['line_graph_13.15a']={'source_edges':E15,'line_edges':line_edges(E15)}
    result['preimage_13.15b']={'edges_by_index':PREIMAGE,'verified_line_edges':line_edges(PREIMAGE)}
    ASSETS.mkdir(parents=True,exist_ok=True)
    (ASSETS/'第13章-整数图计算.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

    header=r'''\documentclass[tikz,border=7pt]{standalone}
\usepackage{amsmath,amssymb}
\usetikzlibrary{arrows.meta,positioning}
\tikzset{vertex/.style={circle,draw,fill=cyan!12,minimum size=7mm,inner sep=1pt},box/.style={draw,rounded corners,fill=cyan!8,align=center,minimum height=12mm,minimum width=27mm}}
\begin{document}\begin{tikzpicture}[line width=0.8pt,font=\small]
'''
    footer='\n\\end{tikzpicture}\\end{document}\n'
    a1=[(i+1,j+1) for i in range(7) for j in range(i+1,7) if M1[i][j]]
    a2=[(i+1,j+1) for i in range(7) for j in range(i+1,7) if M2[i][j]]
    body=graph(range(1,8),a1,circle(7))+r'\node at (0,2.7) {$A_1$};'
    body+=r'\begin{scope}[xshift=6cm]'+graph(range(1,8),a2,circle(7))+r'\node at (0,2.7) {$A_2$};\end{scope}'
    figures={'DL122-邻接矩阵对应图':body}
    labels={i+1:f'{x}{y}' for i,(x,y) in enumerate(E15)}
    figures['DL131-原图的边图']=graph(range(1,9),line_edges(E15),circle(8,2.5),labels)
    coords={'a':(-1.4,1.9),'u':(0,1),'w':(0,-1),'t':(2.5,-1),'v':(2.5,1),'c':(3.9,1.9)}
    figures['DL132-给定边图的一个原像']=graph(coords,PREIMAGE,coords,edge_labels=True)
    figures['DL130-点积图注意力']=r'''
\node[box] (h) at (0,0) {$H\in\mathbb R^{D\times N}$};
\node[box] (q) at (4,2) {$Q=W_QH$\\$d\times N$};
\node[box] (k) at (4,0) {$K=W_KH$\\$d\times N$};
\node[box] (v) at (4,-2) {$V=W_VH$\\$D'\times N$};
\node[box] (s) at (8,1) {$S=K^TQ/\sqrt d$\\$N\times N$};
\node[box] (mask) at (8,3.2) {$M_{mn}=0\text{ if }m\sim n\text{ or }m=n$\\$M_{mn}=-\infty\text{ otherwise}$};
\node[box] (att) at (12,1) {$T=\operatorname{softmax}_{\rm col}(S+M)$\\$N\times N$};
\node[box] (out) at (12,-2) {$H'=a(VT+b\mathbf1^T)$\\$D'\times N$};
\draw[-{Stealth}] (h.east) -- ++(0.5,0) |- (q.west);
\draw[-{Stealth}] (h.east) -- (k.west);
\draw[-{Stealth}] (h.east) -- ++(0.5,0) |- (v.west);
\draw[-{Stealth}] (q.east) -- ++(0.6,0) |- (s.west);
\draw[-{Stealth}] (k.east) -- ++(0.8,0) |- (s.west);
\draw[-{Stealth}] (s.east) -- (att.west);
\draw[-{Stealth}] (mask.east) -| (att.north);
\draw[-{Stealth}] (att.south) -- (out.north);
\draw[-{Stealth}] (v.east) -- (out.west);
'''
    build=ROOT/'tmp/pdfs/ds001-rest-20261028/root/figure-build'
    build.mkdir(parents=True,exist_ok=True)
    for index,(stem,body) in enumerate(figures.items(),1):
        source=ASSETS/f'{stem}.tex';source.write_text(header+body+footer,encoding='utf-8')
        build_source=build/f'figure-{index}.tex'
        build_source.write_bytes(source.read_bytes())
        run=subprocess.run(['pdflatex','-interaction=nonstopmode','-halt-on-error',build_source.name],cwd=build,capture_output=True)
        if run.returncode:raise RuntimeError(run.stdout.decode('utf-8','replace')[-3500:])
        (ASSETS/f'{stem}.pdf').write_bytes((build/f'figure-{index}.pdf').read_bytes())
        subprocess.run(['pdftoppm','-singlefile','-r','150','-png',str(ASSETS/f'{stem}.pdf'),str(ASSETS/stem)],check=True,capture_output=True)
    print(json.dumps({k:v['walks_1_to_2'] for k,v in result['graphs'].items()}))
    print('verified line graphs; compiled/rendered four figures')

if __name__=='__main__':main()
