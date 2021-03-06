#
# l07: numerical root finding: scipy vs simple bisect
#
import math
import numpy as np
from scipy.optimize import fsolve
from scipy.optimize import brentq
from scipy.optimize import brenth
from scipy.optimize import ridder
from scipy.optimize import newton
from scipy.optimize import bisect as bsect
from scipy import interpolate as intp
from matplotlib import pylab as plt
import time

   
def rootsearchspline(f,a,b,dx):
    x = np.arange(a,b,dx)
    spl = intp.UnivariateSpline(x,f(x),s=0.0)
    return spl.roots()

f=lambda x: x**4*np.sin(x) #x*math.cos(x-4)
fprime = lambda x: x**4*np.cos(x)+4.0*x**3*np.sin(x)

a = -100; b = 100.0; eps = 1.0e-10; epssp = 10000.0*eps

t1 =time.time()

xroots = rootsearchspline(f,a,b,epssp*(abs(b-a)))
xrootsfinal = []

# refine spline roots
for i in range(len(xroots)):
    dxroot = np.max(100.0*eps*xroots,100.0*eps)
    xr1 = xroots[i] - dxroot; xr2 = xroots[i] + dxroot
    if ( f(xr1)*f(xr2) < 0 ):
        xrootsfinal.append(brenth(f,xr1,xr2,xtol=eps))
    
xrootsfinal = np.array(xrootsfinal)

t2 = time.time()

print "spline-aided root finding over interval",a,b," finished in ",t2-t1," seconds"
#            
# plot results:
#

x = np.linspace(a,b,10000)
plt.plot(x,f(x),xrootsfinal,f(np.array(xrootsfinal)),'ro')
plt.grid(b=1)
plt.show()
