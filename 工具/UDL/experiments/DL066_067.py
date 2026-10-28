"""DS001 Problems 7.16/7.17: literal figure-7.8 architecture and binary modification."""
from pathlib import Path
import json,platform
import numpy as np
import torch
from torch import nn
from torch.utils.data import TensorDataset,DataLoader
from torch.optim.lr_scheduler import StepLR
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'附件/习题图/DS001'
torch.set_num_threads(1)
def run(binary):
 torch.manual_seed(20261028)
 di,dk,do=10,40,1 if binary else 5
 layers=[nn.Linear(di,dk),nn.ReLU(),nn.Linear(dk,dk),nn.ReLU(),nn.Linear(dk,do)]
 if binary:layers.append(nn.Sigmoid())
 model=nn.Sequential(*layers)
 for layer in model:
  if isinstance(layer,nn.Linear):
   nn.init.kaiming_normal_(layer.weight);nn.init.zeros_(layer.bias)
 criterion=nn.BCELoss() if binary else nn.MSELoss()
 optimizer=torch.optim.SGD(model.parameters(),lr=0.1,momentum=0.9)
 scheduler=StepLR(optimizer,step_size=10,gamma=0.5)
 x=torch.randn(100,di)
 y=torch.randint(0,2,(100,do)).float() if binary else torch.randn(100,do)
 loader=DataLoader(TensorDataset(x,y),batch_size=10,shuffle=True)
 rows=[]
 for epoch in range(100):
  epoch_loss=0.
  rate=optimizer.param_groups[0]['lr']
  for xb,yb in loader:
   optimizer.zero_grad()
   loss=criterion(model(xb),yb)
   loss.backward();optimizer.step()
   epoch_loss+=loss.item()
  scheduler.step()
  with torch.no_grad():full_loss=criterion(model(x),y).item()
  rows.append((epoch+1,rate,epoch_loss,full_loss))
 prefix='DL067' if binary else 'DL066'
 np.savetxt(OUT/f'{prefix}-训练记录.csv',rows,delimiter=',',header='epoch,learning_rate,sum_of_batch_mean_losses,full_training_loss',comments='')
 fig,ax=plt.subplots(figsize=(6,3.8))
 values=np.array(rows)
 ax.plot(values[:,0],values[:,2],label='Sum of 10 batch means')
 ax.plot(values[:,0],values[:,3],label='Full training-set mean')
 ax.set(xlabel='Epoch',ylabel='BCE' if binary else 'MSE',title='Binary modification' if binary else 'Figure 7.8 implementation')
 ax.legend(frameon=False);ax.grid(alpha=.2);fig.tight_layout()
 for ext in ('png','pdf'):fig.savefig(OUT/f'{prefix}-训练损失.{ext}',dpi=180)
 plt.close(fig)
 rec={'python':platform.python_version(),'torch':torch.__version__,'numpy':np.__version__,'matplotlib':matplotlib.__version__,'seed':20261028,'device':'cpu','threads':1,'architecture':[di,dk,dk,do],'epochs':100,'batch_size':10,'optimizer':'SGD lr=.1 momentum=.9','scheduler':'StepLR step_size=10 gamma=.5','loss':'BCELoss' if binary else 'MSELoss','first_epoch_sum':rows[0][2],'final_epoch_sum':rows[-1][2],'final_full_training_mean':rows[-1][3],'finite_scope':'One seeded synthetic training run, no held-out evaluation'}
 (OUT/f'{prefix}-结果.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2),encoding='utf-8')
 print(json.dumps(rec))
run(False)
run(True)

