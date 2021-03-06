#
#  basic example how to read P(k) output by camb
#
# see also http://matplotlib.org/users/pyplot_tutorial.html
# for matplotlib tutorial
#
#
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy import interpolate as intp



#
# read input file with P(k) output from CAMB
#
fname = './test_matterpower_logintk1000.dat'
k,Pk = np.loadtxt(fname,usecols=(0,1),unpack=True)
lk = np.log10(k); lPk = np.log10(Pk)

#
# construct fitted spline of a given smoothing s
#
slPk = intp.UnivariateSpline (lk, lPk, s=0.1) # play with smoothing!
slPk0 = intp.UnivariateSpline (lk, lPk, s=0.0) # effectively standard interpolated spline

#
#  output first derivatives of the fitted spline
#
ders = []
ders0 = []
for i in range(len(lk)):
    dummy = slPk.derivatives(lk[i]); dummy0 = slPk0.derivatives(lk[i])
    ders.append(dummy[1]); ders0.append(dummy0[1]) # take first derivative only


# plot derivative approximations
#
fig1 = plt.figure()
plt.plot(lk,ders0,linewidth=1.5,c='magenta',label='interpolated spline')
plt.plot(lk,ders,linewidth=1.5,c='cyan',label='fitted spline')

plt.xlabel('$k$')
plt.ylabel('$d\\ln P(k)/d\\ln k$')
plt.title('slope')
plt.legend()

plt.show()
