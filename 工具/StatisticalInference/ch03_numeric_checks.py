"""第3章有限计算核验；不修改习题状态，无随机。"""
from pathlib import Path
from math import comb,exp,log1p
from fractions import Fraction
from scipy.stats import binom,poisson,norm
from scipy.optimize import brentq
import scipy,json,platform
HERE=Path(__file__).resolve().parent
def c(n,k):return comb(n,k) if 0<=k<=n else 0
def accept(k,j):return Fraction(sum(c(6,i)*c(94,k-i) for i in range(j+1)),c(100,k))
k0=next(k for k in range(101) if accept(k,0)<Fraction(1,10))
k1=next(k for k in range(101) if accept(k,1)<Fraction(1,10))
drug=sum(Fraction(comb(100,k)*4**k,5**100) for k in range(85,101))
def movie(n):return Fraction(2*sum(comb(1000,k) for k in range(n+1,1001)),2**1000)
seat=next(n for n in range(500,1001) if movie(n)<Fraction(1,100))
single=sum(Fraction(comb(60,k)*89**(60-k),90**60) for k in range(5,61))
def joint(n):return Fraction(c(n,4)*c(496-n,2),c(496,4)*c(492,2))
best=max((joint(n),n) for n in range(4,495))
report={
 'date':'2026-11-13','python':platform.python_version(),'scipy':scipy.__version__,'randomness':'none',
 '3.2':{'worst_defectives':6,'minimum_K_zero':k0,'A0_Kminus1':str(accept(k0-1,0)),'A0_K':str(accept(k0,0)),'minimum_K_one':k1,'A1_Kminus1':str(accept(k1-1,1)),'A1_K':str(accept(k1,1))},
 '3.5':{'tail_exact':str(drug),'tail_decimal':float(drug),'scipy_tail':float(binom.sf(84,100,.8))},
 '3.6':{'poisson_mean':20,'poisson_complement_P_ge100':float(poisson.sf(99,20)),'boundary':'只核本题泊松近似模型，不声称对二项极端尾有小相对误差'},
 '3.7':{'boundary_root':float(brentq(lambda l:(1+l)*exp(-l)-.01,1,10)),'strict_inequality_has_minimum':False},
 '3.8':{'minimum_seats_exact':seat,'tail_Nminus1':float(movie(seat-1)),'tail_N':float(movie(seat)),'normal_continuity_boundary':float(500+norm.ppf(.995)*250**.5-.5)},
 '3.9':{'single_school_tail':float(single),'independent_opportunities_310':-__import__('math').expm1(310*log1p(-float(single))),'independent_155000_log_complement':155000*log1p(-float(single))},
 '3.10':{'N':best[1],'M':496-best[1],'joint_exact':str(best[0]),'joint_decimal':float(best[0])}}
assert k0==32 and k1==51 and seat==541 and best[1]==331
(HERE/'ch03-numeric-results.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,ensure_ascii=False,indent=2))
