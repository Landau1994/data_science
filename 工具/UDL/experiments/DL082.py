"""Problem 9.6: exact two-parameter penalties, with discontinuities drawn explicitly."""
from pathlib import Path
import json,platform
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import BoundaryNorm
root=Path(__file__).resolve().parents[3];out=root/'附件/习题图/DS001'
grid=np.linspace(-2,2,601);a,b=np.meshgrid(grid,grid)
fig,ax=plt.subplots(1,3,figsize=(11,3.8),constrained_layout=True)
cmap=plt.get_cmap('viridis',3);norm=BoundaryNorm([-.5,.5,1.5,2.5],3)
im=ax[0].imshow(np.full_like(a,2),origin='lower',extent=(-2,2,-2,2),cmap=cmap,norm=norm)
ax[0].axhline(0,color=cmap(norm(1)),lw=3);ax[0].axvline(0,color=cmap(norm(1)),lw=3)
ax[0].scatter([0],[0],c=[0],cmap=cmap,norm=norm,s=42,edgecolors='white',zorder=5)
fig.colorbar(im,ax=ax[0],ticks=[0,1,2],label='Nonzero-coordinate count')
ax[0].set_title('$P=0$: discontinuous count')
for axis,p,lev in [(ax[1],.5,[.5,1,1.5,2,2.5]),(ax[2],1,[.5,1,2,3])]:
 z=np.abs(a)**p+np.abs(b)**p
 im=axis.imshow(z,origin='lower',extent=(-2,2,-2,2),cmap='viridis',interpolation='nearest')
 contours=axis.contour(a,b,z,levels=lev,colors='white',linewidths=.65)
 axis.clabel(contours,fontsize=7,inline=True)
 axis.set_title('$P=1/2$: nonconvex' if p==.5 else '$P=1$: convex')
 fig.colorbar(im,ax=axis,label='Penalty')
for axis in ax:axis.set(xlabel='$\\phi_0$',ylabel='$\\phi_1$',aspect='equal')
for ext in ['png','pdf']:fig.savefig(out/f'DL082-正则化项热图.{ext}',dpi=180)
record={'python':platform.python_version(),'numpy':np.__version__,'matplotlib':matplotlib.__version__,'display_domain':[-2,2],'continuous_penalty_grid':[601,601],'L0':'2 off axes; 1 on axes except origin; 0 at origin. Axes and origin are explicitly drawn with visible width, not smoothed neighborhoods.','formula':'sum_j abs(phi_j)^P for P>0; nonzero count for P=0'}
(out/'DL082-作图记录.json').write_text(json.dumps(record,indent=2),encoding='utf-8')
print(json.dumps(record))

