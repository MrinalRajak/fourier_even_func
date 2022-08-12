

#Find the fourier series expansion of the periodic function of period 2pi

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
import scipy.signal as s

def f(t):
    if(-np.pi<=t<=np.pi):
        result=t**2
    return result
ff=np.vectorize(f)
L=np.pi
n=30
t,h=np.linspace(-np.pi,np.pi,1000,retstep=True)
y=s.square(t)
plt.plot(2*t,y)
plt.xlim(-3*np.pi,3*np.pi)
an=[]
bn=[]

#DEtermination of coefficient an and bn
for i in range(n):
    an.append(quad(lambda t:ff(t)*np.cos((i*np.pi*t)/L),-np.pi,np.pi)[0]/L)
    bn.append(quad(lambda t:ff(t)*np.sin((i*np.pi*t)/L),-np.pi,np.pi)[0]/L)

print("an: ",an)
print("bn: ",bn)

s=0
for i in range(n):
    if(i==0):
        s=s+(an[i]/2)
    else:
        s=s+an[i]*np.cos((i*np.pi*t)/L)+bn[i]*np.sin((i*np.pi*t)/L)
#printing the sum
plt.plot(t,0.5*s)
plt.grid(True)
plt.show()
    

