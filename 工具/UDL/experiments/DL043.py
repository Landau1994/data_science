"""Problem 6.4: specified 20-point experiment and reproducible probability/loss plots."""
from pathlib import Path
import json,platform
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
root=Path(__file__).resolve().parents[3];out=root/'附件/习题图/DS001'
rng=np.random.default_rng(20261028)
x=np.r_[rng.normal(-1,1,10),rng.normal(1,1,10)]
y=np.r_[np.zeros(10),np.ones(10)]
np.savetxt(out/'DL043-样本.csv',np.c_[x,y],delimiter=',',header='x,y',comments='')
a=np.linspace(-4,4,161);b=np.linspace(-2,6,161)
A,B=np.meshgrid(a,b);z=A[...,None]+B[...,None]*x
loss=(np.logaddexp(0,z)-y*z).sum(-1)
fig,ax=plt.subplots(1,2,figsize=(10,4))
xx=np.linspace(-4,4,801)
for p0,p1 in [(0,1),(1,1),(0,2),(0,-1)]:
 ax[0].plot(xx,1/(1+np.exp(-(p0+p1*xx))),label=f'({p0},{p1})')
ax[0].set(xlabel='$x$',ylabel='$p(y=1|x)$');ax[0].legend(title='$(\\phi_0,\\phi_1)$',frameon=False)
im=ax[1].imshow(loss,origin='lower',extent=[a[0],a[-1],b[0],b[-1]],aspect='auto',cmap='viridis')
ax[1].set(xlabel='$\\phi_0$',ylabel='$\\phi_1$');fig.colorbar(im,ax=ax[1],label='NLL')
fig.tight_layout()
for ext in ['png','pdf']:fig.savefig(out/('DL043-逻辑回归曲线与热图.'+ext),dpi=180)
record={'python':platform.python_version(),'numpy':np.__version__,'matplotlib':matplotlib.__version__,
 'seed':20261028,'rng':'PCG64','n_per_class':10,'grid_shape':list(loss.shape),
 'grid_minimum':float(loss.min()),'finite_scope':'Only the stated 20 draws and 161x161 grid; convexity proved analytically in note'}
(out/'DL043-结果.json').write_text(json.dumps(record,indent=2),encoding='utf-8')
print(json.dumps(record))
