from math import *
from random import *

def f(x):
    return x**4-4*x**3-8*x**2+48*x+3

n=1000
X=[gauss(0,10000) for i in range(n)]
xopt=X[0]
for k in range(1,n):
    if (f(X[k])<f(xopt)):
        xopt=X[k]

r=10**(-1)
imax=100
i=0
while ((i<imax) and (max([abs(X[j]-xopt) for j in range(n)])>=r)):
    for k in range(n):
        a=random()
        X[k]=X[k]+a*(xopt-X[k])
    for k in range(1,n):
        if (f(X[k])<f(xopt)):
            xopt=X[k]
    i+=1
print("i= {0}".format(i))
print("L'optimum est xopt= %f"%(xopt,))