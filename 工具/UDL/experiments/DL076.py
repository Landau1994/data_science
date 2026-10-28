"""Problem 8.9: seeded Gaussian radius histograms and exact chi density."""
from pathlib import Path
import json,platform
import numpy as np
import scipy
from scipy.stats import chi
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
root=Path(__file__).resolve().parents[3];out=root/'附件/习题图/DS001'
rng=np.random.default_rng(20261028);n=20000
fig,axes=plt.subplots(1,3,figsize=(11,3.5))
stats=[];all_r=[]
for ax,d in zip(axes,[25,100,500]):
 r=np.linalg.norm(rng.standard_normal((n,d)),axis=1);all_r.append(r)
 ax.hist(r,bins=70,density=True,alpha=.55,color='#3f829d',label='Samples')
 x=np.linspace(max(0,r.min()-.5),r.max()+.5,500)
 ax.plot(x,chi.pdf(x,df=d),color='#d1784c',label='Exact chi density')
 ax.set(xlabel='Distance from origin',ylabel='Density',title=f'D={d}')
 stats.append({'dimension':d,'n':n,'sample_mean':float(r.mean()),'sample_std_ddof0':float(r.std()),'sample_relative_std':float(r.std()/r.mean()),'theoretical_mean':float(chi.mean(d)),'theoretical_std':float(chi.std(d))})
axes[0].legend(frameon=False);fig.tight_layout()
for ext in ['png','pdf']:fig.savefig(out/f'DL076-高斯半径直方图.{ext}',dpi=180)
np.savetxt(out/'DL076-半径样本.csv',np.array(all_r).T,delimiter=',',header='D25,D100,D500',comments='')
record={'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__,'matplotlib':matplotlib.__version__,'seed':20261028,'rng':'PCG64','sample_count_per_dimension':n,'statistics':stats,'scope':'Finite independent samples in the three specified dimensions; exact law derived in note'}
(out/'DL076-结果.json').write_text(json.dumps(record,indent=2),encoding='utf-8')
print(json.dumps(record))

