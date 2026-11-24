"""Hankel H_0^(2) and differentiated order one from glibc cylindrical functions."""
import ctypes,math
lib=ctypes.CDLL('libm.so.6')
for fun in ['j0','j1','y0','y1']:
    getattr(lib,fun).argtypes=[ctypes.c_double];getattr(lib,fun).restype=ctypes.c_double
def solution(t,p,k):
    k=abs(k)
    z=k*t**(1-p)/(1-p); c=math.sqrt(math.pi/(4*(1-p)))
    return c*complex(lib.j0(z),-lib.y0(z)), -c*k*t**(-p)*complex(lib.j1(z),-lib.y1(z))
