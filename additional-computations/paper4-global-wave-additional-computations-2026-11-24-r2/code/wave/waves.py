"""Localized signed-frequency and remote-distribution tests."""
import numpy as np
from scipy.special import hankel2
from scipy.integrate import simpson,solve_ivp
from pathlib import Path

def bump(x,w):
    u=x/w;b=np.zeros_like(u);mask=abs(u)<1
    b[mask]=np.exp(1-1/(1-u[mask]**2))
    return b

def branch():
    rows=[]
    for N in [2048,4096,8192]:
        x=(np.arange(N)-N//2)*2*np.pi/N
        chi=bump(x,.75)
        freq=np.arange(1,2*256+1)
        spec=np.zeros(N,complex);spec[-freq]=1/(2*freq)
        exact=np.fft.ifft(spec)*N
        smooth=np.zeros(N,complex);smooth[-freq]=np.exp(-np.sqrt(freq))/(2*freq)
        window=np.fft.ifftshift(chi)
        def coef(y):return np.fft.fft(window*y)/N
        ref=coef(exact);wrong=coef(exact.conj());pert=coef(np.fft.ifft(smooth)*N)
        # Independent physical quadrature of the infinite log kernel, for the
        # localized coefficients, via its convergent smooth-window convolution.
        chi_modes=np.fft.fft(window)/N
        for k in (8,16,32,64,128,256):
            longer=np.arange(1,3*N//8+1)
            oracle=np.sum(chi_modes[(longer-k)%N]/(2*longer))
            rows.append(dict(N=N,k=k,selected=float(abs(ref[-k])),opposite=float(abs(ref[k])),
                    wrong_difference=float(abs(wrong[-k]-ref[-k])),smooth_difference=float(abs(pert[-k])),
                    relative_cutoff=float(abs(ref[-k]-oracle)/abs(oracle))))
    curved=[]
    # Axis Kasner half-wave, anchor at t=1, localized to a bounded optical-time interval.
    for p in [-1/3,2/3]:
        for k in [8,16,32,64,128,256]:
            eta=np.linspace(.03,.43,1601);t=(1+(1-p)*eta)**(1/(1-p))
            f=hankel2(0,k*t**(1-p)/(1-p))
            demod=np.exp(1j*k*eta);w=bump(eta-.23,.18)
            f=f/f[0]
            match=simpson(w*demod*f,x=eta)
            leak=simpson(w*demod*f.conj(),x=eta)
            curved.append(dict(p=p,k=k,matched=float(abs(match)),wrong=float(abs(leak)),ratio=float(abs(leak/match))))
    return rows,curved

def remote():
    a=1.2;N=8192
    s=np.arange(-N//2,N//2)*2*np.pi/N; wrap=lambda x:(x+np.pi)%(2*np.pi)-np.pi
    tests=[bump(s,.41),bump(wrap(s-a),.37)*(1+.2*np.cos(s-a)),
           bump(wrap(s+a),.45)*(1+.1*np.sin(s+a))]
    refs=[0.,1.2,1.]
    rows=[];curves=[]
    for count in (8,16,32,64,128,256):
        k=np.arange(1,count+1)
        val=(1+2*np.cos(s[:,None]*k)@np.cos(a*k))/np.pi
        pairs=[float(np.sum(phi*val)*2*np.pi/N) for phi in tests]
        rows.append(dict(cutoff=count,pair=pairs,error=np.abs(np.array(pairs)-refs).tolist(),
            wrong_shift=float(np.sum(tests[1]*(1+2*np.cos(s[:,None]*k)@np.cos(.7*k))/np.pi)*2*np.pi/N)))
        if count in [8,32,128]:curves.append(val)
    # Reproducible vector plot of actual (unsmoothed) partial sums.
    svg=['<svg xmlns="http://www.w3.org/2000/svg" width="760" height="560" viewBox="0 0 760 560"><rect width="100%" height="100%" fill="white"/>',
         '<text x="68" y="28" font-size="20">Remote shifted delta pair on the circle</text>']
    for j,(y,K) in enumerate(zip(curves,[8,32,128])):
        top=72+j*155;base=top+91;scale=80/np.max(y)
        svg.append(f'<text x="12" y="{top+10}" font-size="14">K={K}</text>')
        for pos in [-a,a]:
            ux=70+660*(pos+np.pi)/(2*np.pi)
            svg.append(f'<path d="M{ux:.2f} {top}v115" stroke="#d45842" stroke-dasharray="4 3"/>')
        line=' '.join(f'{70+660*i/N:.2f},{base-scale*y[i]:.2f}' for i in range(0,N,9))
        svg.extend([f'<path d="M70 {base}h660" stroke="#777"/>',f'<polyline points="{line}" fill="none" stroke="#194f80"/>',
                    f'<text x="70" y="{base+43}" font-size="13">peak = {max(y):.2f}   |   horizontal range −π to π</text>'])
    Path('remote.svg').write_text(''.join(svg)+'</svg>')
    return rows
def curved_remote():
    # Exact Ricci-flat Brinkmann plane wave 2du dv + H du² − dx² − dy².
    # H=α cos(u)(x²−y²), box F(u)=0, independent characteristic test.
    def rhs(s,Y):
        u,v,x,y,U,V,X,Yv=Y
        c=.1*np.cos(u);cu=-.1*np.sin(u)
        return [U,V,X,Yv,0.,-.5*cu*(x*x-y*y)*U*U-2*c*(x*X-y*Yv)*U,-c*x*U*U,c*y*U*U]
    results=[]
    for k in [16,32,64]:
        source=np.array([.4,0.,.2,.3,0.,1.,0.,0.])
        ray=solve_ivp(rhs,(0,1),source,rtol=1/k**4,atol=1e-11)
        # Independent metric divergence stencil acting at a generic peak flank.
        u=.4+1.2+.7/k;v=.8;x=.2;y=.3;q=.4
        def density(point):
            u,v,x,y=point
            return np.array([[0,1,0,0],[1,-.1*np.cos(u)*(x*x-y*y),0,0],[0,0,-1,0],[0,0,0,-1]])
        modes=np.arange(1,k+1)
        def val(p):return (1+2*np.sum(np.cos(modes*(p[0]-q))*np.cos(1.2*modes)))/np.pi
        unit=np.eye(4);point=np.array([u,v,x,y]);h=.002/k
        def current(p):return density(p)@np.array([(val(p+h*e)-val(p-h*e))/(2*h) for e in unit])
        residual=sum((current(point+h*e)[i]-current(point-h*e)[i])/(2*h) for i,e in enumerate(unit))
        results.append(dict(k=k,wave_residual=residual,ray_u_error=float(np.max(abs(ray.y[0]-.4))),
                       remote_u_gap=1.2,curvature_magnitude=abs(.1*np.cos(.4))))
    return results
def run():
    flat,curved=branch()
    return dict(localized=flat,kasner=curved,remote=remote(),curved_remote=curved_remote())
