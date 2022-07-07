# -*- coding: utf-8 -*-

def a(i,x,X,Y):
	rep=1
	for j in range(min(len(X),len(Y))):
		if (i!=j):
			rep*=(x-X[j])/(X[i]-X[j])
	return (rep)
	
def P(x,X,Y):
	rep=0
	for i in range(min(len(X),len(Y))):
		rep+=a(i,x,X,Y)*Y[i]
	return (rep)
	
X=[-2,0,1,2]
Y=[49,5,7,49]
#x=float(input(" Vous voulez estimer f(x) pour x= "))
#print(P(x,X,Y))	

from  numpy.polynomial  import  Polynomial as poly
x=poly([0,1]) # Polynôme p(x)=0+x
p=P(x,X,Y)
print(p)

from scipy.interpolate import lagrange
p=lagrange(X,Y)
print(p.coef)
    
import numpy as np
x=np.poly1d([0,1]) # Polynôme p(x)=0+x
x=poly1d([1,0]) # Polynôme p(x)=0+x
p=P(x,X,Y)
print(p)
print(p.order)
print(p.coeffs)
#print(p.roots)
print(roots(p))
print(p(0))
print(np.polyval(p,0))

print("%f"%(p.coef[0],),end=" ")
if (len(p)>1):
	if (p.coef[1]>0):
		print("+%f*x" %(p.coef[1],),end=" ")
	elif (p.coef[1]<0):
		print("%f*x" %(p.coef[1],),end=" ")
		
i=2
while (i<len(p)-1):
	if (p.coef[i]>0):
		print("+%f*x^%d" %(p.coef[i],i,),end=" ")
	elif (p.coef[i]<0):
		print("%f*x^%d" %(p.coef[i],i,),end=" ")
	i=i+1
		
if (len(p)>1):
	if (p.coef[len(p)-1]>0):
		print("+%f*x^%d" %(p.coef[len(p)-1],len(p)-1,),end=" ")
	elif (p.coef[len(p)-1]<0):
		print("%f*x^%d" %(p.coef[len(p)-1],len(p)-1,),end=" ")	
