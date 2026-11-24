import cmath,json,math,platform
from pathlib import Path
from hankel import solution
from evolve import march
I=json.loads(Path('/src/input.json').read_text());ts=I['surfaces'];tp,x=I['point']
def run(p,k,n):
    f0,v0=solution(1,p,k)
    def analytic(t):return solution(t,p,k)
    def evolved(t):
        f,v=march(1,f0,v0,t,p,k,max(1,round((t-1)*n)))
        return f,v/t
    def observables(get,omit=False,flip=False):
        def mode(t):
            a,b=get(t);return (a.conjugate(),b.conjugate()) if flip else (a,b)
        F=[mode(t) for t in ts];z=[(1 if omit else math.sqrt(t))*a for t,(a,b) in zip(ts,F)]
        C=[[a*b.conjugate() for b in z] for a in z]; D=[abs(v)**2 for v in z];W=[1/math.sqrt(d) for d in D]
        normal=[(1 if omit else math.sqrt(t))*v for t,(_,v) in zip(ts,F)]
        traces=[a*b.conjugate() for A in (z,normal) for B in (z,normal) for a in A for b in B]
        T=[[W[i]*C[i][j]*W[j] for j in range(3)] for i in range(3)]
        point=mode(tp)[0].conjugate()*cmath.exp(-1j*k*x)/(2*math.pi)**1.5
        e=[W[i]*z[i]*point for i in range(3)]
        charge=[1j*t*(a.conjugate()*b-a*b.conjugate()) for t,(a,b) in zip(ts,F)]
        return dict(mixed=sum(C,[]),diagonal=D,normalizer=W,phase=sum(T,[]),evaluation=e,charge=charge,physical_traces=traces),max(abs(T[i][j]*T[j][l]-T[i][l]) for i in range(3) for j in range(3) for l in range(3)),max(abs(T[i][j].conjugate()-T[j][i]) for i in range(3) for j in range(3)),max(abs(T[i][j]*e[j]-e[i]) for i in range(3) for j in range(3)),max(abs(C[i][j]*C[j][l]/D[j]-C[i][l]) for i in range(3) for j in range(3) for l in range(3))
    ref,*_=observables(analytic);val,*invariants=observables(evolved)
    def errors(v):return {key:max(abs(a-b) for a,b in zip(ref[key],v[key])) for key in ref}
    err=errors(val);err['kg_unit']=max(abs(a-1) for a in val['charge'])
    pair=lambda z:[z.real,z.imag]
    return dict(p=p,k=k,n=n,errors=err,identities=invariants,dropped=errors(observables(analytic,True)[0]),reversed=errors(observables(analytic,flip=True)[0]),reference={key:[pair(complex(v)) for v in vs] for key,vs in ref.items()},measured={key:[pair(complex(v)) for v in vs] for key,vs in val.items()})
pilot=run(I['p'][0],1,32)
assert max(pilot['errors'].values())<1e-4
rows=[run(p,k,n) for n in I['steps_per_unit'] for p in I['p'] for magnitude in I['k'] for k in (-magnitude,magnitude)]
norm=[max(max(v for key,v in r['errors'].items() if key!='physical_traces') for r in rows if r['n']==n) for n in I['steps_per_unit']]
orders=[math.log2(a/b) for a,b in zip(norm,norm[1:])]
controls={k:{m:max(r[k][m] for r in rows) for m in rows[0][k]} for k in ('dropped','reversed')}
for i,row in enumerate(rows):Path(f'mode-{i:02d}.json').write_text(json.dumps(row,separators=(',',':')))
out=dict(mode_files=[f'mode-{i:02d}.json' for i in range(len(rows))],max_errors=norm,observed_orders=orders,controls=controls,pilot=pilot['errors'],python=platform.python_version(),max_identities=[max(r['identities'][i] for r in rows) for i in range(4)])
out['passed']=norm[-1]<I['fine_max_error'] and min(orders)>I['minimum_order'] and max(out['max_identities'])<I['algebra_tolerance'] and min(controls['dropped']['diagonal'],controls['reversed']['phase'],controls['reversed']['charge'])>I['control_minimum']
Path('results.json').write_text(json.dumps(out,indent=2));print(norm,orders,out['passed'])
assert out['passed']
