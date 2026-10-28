"""DL031: plot the two exact binary cross-entropy loss functions."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
root=Path(__file__).resolve().parents[3]
p=np.linspace(1e-4,1-1e-4,2000)
fig,ax=plt.subplots(figsize=(6,4))
ax.plot(p,-np.log1p(-p),label='$y=0$',color='#51838b')
ax.plot(p,-np.log(p),label='$y=1$',color='#bf795c')
ax.set(xlabel='$p$',ylabel='$L(p)$',xlim=(0,1),ylim=(0,5))
ax.legend(frameon=False);fig.tight_layout()
for ext in ['png','pdf']:
    fig.savefig(root/'附件/习题图/DS001'/('DL031-交叉熵曲线.'+ext),dpi=180)
