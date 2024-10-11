# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from scipy import optimize
from numpy import power,log

def f(x):
    return -(log(1.3316)+1.3316*log(17.6481)+(1.3316-1)*log(x)-power((17.6481*x),1.3316)-power((3.6497*x),1.1701)-power((27.7654*x),1.1335))

res=optimize.minimize_scalar(f)
if res.success:
    print(res.x)
    print(-res.fun)


def f(t):
    return -(log(1.1701)+1.1701*log(3.6497)+(1.1701-1)*log(t)-power((17.6481*t),1.3316)-power((3.6497*t),1.1701)-power((27.7654*t),1.1335))

res=optimize.minimize_scalar(f)
if res.success:
    print(res.x)
    print(-res.fun)

def f(a):
    return -(log(1.1335)+1.1335*log(27.7654)+(1.1335-1)*log(a)-power((17.6481*a),1.3316)-power((3.6497*a),1.1701)-power((27.7654*a),1.1335))

res=optimize.minimize_scalar(f)
if res.success:
    print(res.x)
    print(-res.fun)

#def f(c):
  #  return -(log(0.9889)+0.9889*log(20.1286)+(0.9889-1)*log(c)-power((17.6481*c),1.3316)-power((3.6497*c),1.1701)-power((27.7654*c),1.1335)-power((20.1286*c),0.9889))

#res=optimize.minimize_scalar(f)
## print(res.x)

def f(b):
    return -(log(1.2244)+1.2244*log(27.8234)+(1.2244-1)*log(b)-power((27.8234*b),1.2244)-power((4.9553*b),1.4903)-power((12.465*b),1.514))

res=optimize.minimize_scalar(f)
if res.success:
    print(res.x)
    print(-res.fun)


def f(d):
    return -(log(1.4903)+1.4903*log(4.9553)+(1.4903-1)*log(d)-power((27.8234*d),1.2244)-power((4.9553*d),1.4903)-power((12.465*d),1.514))

res=optimize.minimize_scalar(f)
if res.success:
    print(res.x)
    print(-res.fun)

def f(e):
    return -(log(1.514)+1.514*log(12.465)+(1.514-1)*log(e)-power((27.8234*e),1.2244)-power((4.9553*e),1.4903)-power((12.465*e),1.514))

res=optimize.minimize_scalar(f)
if res.success:
    print(res.x)
    print(-res.fun)

def f(f):
    return -(log(1.2828)+1.2828*log(4.4729)+(1.2828-1)*log(f)-power((4.4729*f),1.2828)-power((12.3099*f),1.5435)-power((19.0447*f),1.1874))

res=optimize.minimize_scalar(f)
if res.success:
    print(res.x)
    print(-res.fun)

def f(g):
    return -(log(1.5435)+1.5435*log(12.3099)+(1.5435-1)*log(g)-power((4.4729*g),1.2828)-power((12.3099*g),1.5435)-power((19.0447*g),1.1874))

res=optimize.minimize_scalar(f)
if res.success:
    print(res.x)
    print(-res.fun)

def f(h):
    return -(log(1.1874)+1.1874*log(19.0447)+(1.1874-1)*log(h)-power((4.4729*h),1.2828)-power((12.3099*h),1.5435)-power((19.0447*h),1.1874))

res=optimize.minimize_scalar(f)
if res.success:
    print(res.x)
    print(-res.fun)