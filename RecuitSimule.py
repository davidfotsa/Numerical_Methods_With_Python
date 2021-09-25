from random import *
from math import *
def f(x):
    return x**4-4*x**3-8*x**2+48*x+3

x=3
s=x
T=10
e=1
k=0.5
while (T>e):
    d=gauss(0,T)
    if (f(x+d)<f(s)):
        x+=d
        s=x
    else:
        D=f(x+d)-f(s)
        a=random()
        if (exp(-D/T)>=a):
            x=x+d
            T=k*T
print("Xopt= %f"%(s,))
