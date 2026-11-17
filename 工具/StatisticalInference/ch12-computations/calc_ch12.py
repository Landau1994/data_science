from pathlib import Path
import math,json,csv,sys
import numpy as np,scipy
from scipy.special import expit
from scipy.stats import norm,chi2
from scipy.optimize import linprog
HERE=Path(__file__).resolve().parent
animal_x=np.array([3.385,.480,1.350,1.040,.425,.101,2.000,.023]);animal_y=np.array([44.50,15.50,8.10,5.50,6.40,4,12.30,.30])
flight=np.array([14,9,23,10,1,5,13,15,4,3,8,17,2,11,6,7,16,21,19,22,12,20,18]);temp=np.array([53,57,58,63,66,67,67,68,69,70,70,70,70,70,72,73,75,75,76,76,78,79,81]);fail=np.array([1,1,1,1,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0])
age=np.arange(1,10);birds=np.array([77,149,182,118,78,46,27,10,4]);survive=np.array([35,89,130,79,52,28,14,3,1])
oxygen=np.array([20,19.6,19.6,19.4,18.4,19,19,18.3,18.2,18.6,19.2,18.2,18.7,18.5,18,17.4,16.5,17.2,17.3,17.8,17.3,18.4,16.9]);carbon=np.array([1,1.2,1.1,1.4,2.3,1.7,1.7,2.4,2.1,2.1,1.2,2.3,1.9,2.4,2.6,2.9,4,3.3,3,3.4,2.9,1.9,3.9])
def glm(A,y,n=None,probit=False):
 if n is None:n=np.ones(len(y))
 b=np.zeros(A.shape[1]);history=[]
 def ll(b):
  eta=A@b
  if probit:return float(np.sum(y*norm.logcdf(eta)+(n-y)*norm.logsf(eta)))
  return float(np.sum(y*eta-n*np.logaddexp(0,eta)))
 for it in range(100):
  eta=A@b
  if probit:
   r1=np.exp(norm.logpdf(eta)-norm.logcdf(eta));r0=np.exp(norm.logpdf(eta)-norm.logsf(eta));score=y*r1-(n-y)*r0;w=y*r1*(eta+r1)+(n-y)*r0*(r0-eta)
  else:p=expit(eta);score=y-n*p;w=n*p*(1-p)
  grad=A.T@score;info=A.T@(w[:,None]*A);step=np.linalg.solve(info,grad);old=ll(b);rate=1.
  while ll(b+rate*step)<old-1e-12:rate/=2
  b+=rate*step;history.append(ll(b))
  if np.max(np.abs(grad))<1e-9 or np.max(np.abs(rate*step))<1e-11:break
 else:raise RuntimeError('GLM did not converge')
 return {'coeff_centered':b.tolist(),'log_likelihood_without_binomial_constants':ll(b),'iterations':it+1,'gradient_max_abs':float(np.max(np.abs(A.T@score))),'information':info.tolist()}
At=np.column_stack([np.ones(len(temp)),temp-70]);pro=glm(At,fail,probit=True);log=glm(At,fail)
for row in [pro,log]:
 a,b=row['coeff_centered'];row['coeff_original']=[a-70*b,b];row['fitted_probability_at_31']=float(norm.cdf(a+b*(31-70)) if row is pro else expit(a+b*(31-70)))
Aa=np.column_stack([np.ones(9),age-5]);Aq=np.column_stack([np.ones(9),age-5,(age-5)**2]);lin=glm(Aa,survive,birds);quad=glm(Aq,survive,birds)
lin['coeff_original']=[lin['coeff_centered'][0]-5*lin['coeff_centered'][1],lin['coeff_centered'][1]]
a,b,c=quad['coeff_centered'];quad['coeff_original']=[a-5*b+25*c,b-10*c,c]
lr=2*(quad['log_likelihood_without_binomial_constants']-lin['log_likelihood_without_binomial_constants'])
cx=animal_x-animal_x.mean();cy=animal_y-animal_y.mean();Sxx=float(cx@cx);Syy=float(cy@cy);Sxy=float(cx@cy);beta1=(-(Sxx-Syy)+math.sqrt((Sxx-Syy)**2+4*Sxy*Sxy))/(2*Sxy);alpha1=animal_y.mean()-beta1*animal_x.mean();struct_delta=(Sxx-Sxy/beta1)/8;struct_e=struct_delta;struct_xi=Sxy/(8*beta1);func_delta=struct_delta/2
hx=np.array([127,127,136]);hy=np.array([14.4,11.9,17.9]);hb=np.linalg.lstsq(np.column_stack([np.ones(3),hx]),hy,rcond=None)[0]
result={'created':'2026-11-13','python':sys.version,'numpy':np.__version__,'scipy':scipy.__version__,'heart_rate':{'x':hx.tolist(),'y':hy.tolist(),'OLS':hb.tolist()},'animal':{'n':8,'mean_x':float(animal_x.mean()),'mean_y':float(animal_y.mean()),'Sxx':Sxx,'Syy':Syy,'Sxy':Sxy,'ols_y_on_x':Sxy/Sxx,'inverse_ols_x_on_y':Syy/Sxy,'lambda_1_beta':beta1,'lambda_1_alpha':alpha1,'structural_error_variance_x':struct_delta,'structural_error_variance_y':struct_e,'latent_variance':struct_xi,'functional_error_variance_x':func_delta},'challenger':{'flight':flight.tolist(),'temperature':temp.tolist(),'failure':fail.tolist(),'logistic':log,'probit':pro},'sparrowhawk':{'age':age.tolist(),'birds':birds.tolist(),'survive':survive.tolist(),'linear':lin,'quadratic':quad,'LR_chi_square_1':lr,'p_asymptotic':float(chi2.sf(lr,1))}}
# Fixed design, centered predictor improves conditioning for both robust fits.
z=oxygen-oxygen.mean();A=np.column_stack([np.ones(len(z)),z]);N=len(z)
G=np.column_stack([A,-np.eye(N),np.eye(N)]);objective=np.r_[np.zeros(2),np.ones(2*N)]
def fit_lad(y):
 sol=linprog(objective,A_eq=G,b_eq=y,bounds=[(None,None)]*2+[(0,None)]*(2*N),method='highs')
 if not sol.success:raise RuntimeError(sol.message)
 b=sol.x[:2];return b
def fit_m(y):
 b=np.linalg.lstsq(A,y,rcond=None)[0];res=y-A@b;s=math.sqrt(float(res@res)/(N-2));k=1.5*s
 if k<1e-12:return b
 for _ in range(200):
  r=y-A@b;w=np.minimum(1,k/np.maximum(abs(r),1e-300));bn=np.linalg.solve(A.T@(w[:,None]*A),A.T@(w*y))
  if np.max(abs(bn-b))<1e-10:return bn
  b=bn
 raise RuntimeError('Huber IRLS did not converge')
def original(b):return np.array([b[0]-oxygen.mean()*b[1],b[1]])
methods={'LAD':fit_lad,'Huber':fit_m};rng=np.random.default_rng(20261113);B=2000;boot={};records=[]
for name,fit in methods.items():
 bh=fit(carbon);pred=A@bh;res=carbon-pred;s=math.sqrt(float(res@res)/(N-2));row={'estimate':original(bh).tolist(),'residual_MSE':s*s,'parametric':{}}
 for fam in ['normal','double-exponential']:
  draws=[]
  for j in range(B):
   error=rng.normal(0,s,N) if fam=='normal' else rng.laplace(0,s/math.sqrt(2),N)
   value=original(fit(pred+error));draws.append(value);records.append([name,fam,j,*value])
  mat=np.asarray(draws);row['parametric'][fam]={'SE':mat.std(axis=0,ddof=1).tolist(),'mean':mat.mean(axis=0).tolist()}
 # Laplace is the same distribution as double exponential; same stored draws.
 row['parametric']['Laplace']=dict(row['parametric']['double-exponential']);row['parametric']['Laplace']['note']='同义分布，复用同一组实际抽样，结果严格相同'
 draws=[];centered_draws=[];shift=float(res.mean());shift_errors=[]
 for j in range(B):
  sampled=rng.choice(res,N,replace=True);value=original(fit(pred+sampled));centered=original(fit(pred+sampled-shift));draws.append(value);centered_draws.append(centered);shift_errors.append(float(np.max(np.abs(value-centered-np.array([shift,0])))));records.append([name,'raw-residual',j,*value]);records.append([name,'centered-residual',j,*centered])
 mat=np.asarray(draws);cmat=np.asarray(centered_draws);row['nonparametric']={'SE':mat.std(axis=0,ddof=1).tolist(),'mean':mat.mean(axis=0).tolist(),'residual_centering':'none, literal fitted-residual resampling'};row['centered_nonparametric']={'SE':cmat.std(axis=0,ddof=1).tolist(),'mean':cmat.mean(axis=0).tolist(),'residual_centering':'subtract arithmetic mean before resampling'};row['fitted_residual_mean']=shift;row['max_translation_equivariance_error']=max(shift_errors);boot[name]=row
result['bootstrap']={'B_per_method_family':B,'seed':20261113,'generator':'numpy.default_rng PCG64','design':'fixed original 23 oxygen values','Huber_threshold':'1.5 times OLS residual SD; recomputed for every generated sample','LAD_solver':'scipy.optimize.linprog(method=highs), deterministic solver-selected minimizer in ties','fits':boot,'scope':'有限Monte Carlo标准误估计；不构成渐近或精确分布证明'}
with (HERE/'ch12-bootstrap-replicates.csv').open('w',encoding='utf8',newline='') as f:
 w=csv.writer(f);w.writerow(['method','error_family','replicate','intercept','slope']);w.writerows(records)
(HERE/'ch12-computations.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps({'animal':result['animal'],'probit':pro,'logistic':log,'sparrowhawk':result['sparrowhawk'],'bootstrap':result['bootstrap']},ensure_ascii=False,indent=2))
