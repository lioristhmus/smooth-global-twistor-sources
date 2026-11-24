"""Reinitialize unit scalar field at each emitting carrier and evolve to each receiver."""
import cmath
import json
import math
from pathlib import Path
from evolve import march
from hankel import solution

config=json.loads(Path('/src/input.json').read_text())
times=config['surfaces']
pt,x=config['point']
point_factor=(2*math.pi)**(-1.5)

def measure(p,k,n):
    exact=[solution(t,p,k) for t in times]
    waves=[f/abs(f) for f,d in exact]
    normalizers=[1/(math.sqrt(t)*abs(f)) for t,(f,d) in zip(times,exact)]
    point_exact=solution(pt,p,k)[0]*cmath.exp(1j*k*x)
    adjoint_e=[point_factor*u*point_exact.conjugate() for u in waves]
    transport={}
    e=[]
    for j,(t,(f,d)) in enumerate(zip(times,exact)):
        def propagate(target):
            steps=max(1,round(n*abs(target-t)))
            return march(t,1.,t*d/f,target,p,k,steps)[0]
        # Unit half-density at j. Strip W_j at the emitter and apply W_i at the receiver.
        for i,target in enumerate(times):
            transport[i,j]=normalizers[i]/normalizers[j]*math.sqrt(target/t)*propagate(target)
        # Scalar at the off-surface point, with its dual spatial Fourier basis factor.
        e.append(propagate(pt).conjugate()*point_factor*cmath.exp(-1j*k*x)/(normalizers[j]*math.sqrt(t)))
    phase=max(abs(v-waves[i]/waves[j]) for (i,j),v in transport.items())
    point=max(abs(a-b) for a,b in zip(e,adjoint_e))
    composition=max(abs(transport[i,j]*transport[j,l]-transport[i,l]) for i in range(3) for j in range(3) for l in range(3))
    adjoint=max(abs(v.conjugate()-transport[j,i]) for (i,j),v in transport.items())
    covariance=max(abs(v*e[j]-e[i]) for (i,j),v in transport.items())
    return dict(phase=phase,point=point,composition=composition,adjoint=adjoint,covariance=covariance)

levels=[]
for n in config['steps_per_unit']:
    cases=[measure(p,sign*magnitude,n) for p in config['p'] for magnitude in config['k'] for sign in (-1,1)]
    levels.append({key:max(r[key] for r in cases) for key in cases[0]})
norm=[max(r.values()) for r in levels]
orders=[math.log2(a/b) for a,b in zip(norm,norm[1:])]
passed=norm[-1]<config['fine_max_error'] and min(orders)>config['minimum_order']
Path('results.json').write_text(json.dumps(dict(levels=levels,orders=orders,passed=passed),indent=2))
print(levels,orders,passed)
assert passed
