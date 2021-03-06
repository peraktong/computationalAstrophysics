#
#  first derivative in different approximation and associated errors
#
# see http://matplotlib.org/users/pyplot_tutorial.html
# for matplotlib tutorial
#
#

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn

plt.switch_backend('TkAgg')

def func(x):
    #return x**5
    return np.exp(x)

def dfuncdx(x):
    #return 5.0*x**4
    return np.exp(x)

def der1p(x,h):
    return (func(x+h)-func(x))/h

def der2(x,h):
    return (func(x+h)-func(x-h))/(2.0*h)

def der4(x,h):
    return (8*(func(x+h)-func(x-h))+func(x-2.0*h)-func(x+2.0*h))/(12.0*h)


# set array of steps
ha = np.arange(-15.0,-1.0,0.1); h=10.0**ha

# corresponding vector of x and analytic derivative to compare to
x = np.zeros(len(ha)-1); x=100.0;
# a trick to force h to be a number rerpresentable exactly in floating point
temp = x+h; h=temp-x
dfdx = dfuncdx(x)
# compute approximate derivatives to different order
d1= der1p(x,h); d2 = der2(x,h); d4 = der4(x,h)
# compute fractional errors
err1 = abs((d1-dfdx)/dfdx)
err2 = abs((d2-dfdx)/dfdx)
err4 = abs((d4-dfdx)/dfdx)

model = 2*2.e-16/h/10
#
# now plot fractional error as a function of step
#
#mpl.use("TKAgg")  # allow X windows on midway
fig1 = plt.figure()
plt.plot(ha,np.log10(err1),linewidth=1.5,c='r',label='1st order')
plt.plot(ha,np.log10(err2),linewidth=1.5,c='b',label='2nd order')
plt.plot(ha,np.log10(err4),linewidth=1.5,c='g',label='4th order')

plt.plot(ha,np.log10(model),linewidth=0.75,c='black',label='$\\epsilon_m/h$')

plt.xlabel('$\\log_{10} h$')
plt.ylabel('frac. error')
plt.title('derivative error')
plt.legend(loc='lower left')

plt.show()
