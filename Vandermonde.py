# -*- coding: utf-8 -*-

from numpy import *

def f(x):
	return(x**5-2*x+1);

X=linspace(-2,3,6)
n=len(X)
Y=matrix([f(X[i]) for i in range(n)])
#Y.reshape(3,2)
Y=transpose(Y)
#print(Y)

V=ones((n,n))
V=vander(X,increasing=True) # génère une matrice de vandermonde ...

"""
# Une alternative
if n>1:
	for j in range(1,n,1):
		for i in range(n):
			V[i][j]=(X[i])**j
			
"""
print(V)

a=linalg.solve(V,Y)
a=linalg.inv(V)*Y
coef=[float(a[i]) for i in range(n)]
#print(coef)
#print(poly([0,1])) # par défaut Polynôme dont les racines sont 0 et 1
#print(poly1d([0,1],true)) # par défaut Polynôme dont les racines sont 0 et 1
p=poly1d([float(a[n-i-1]) for i in range(n)])
print(p)
print(p.order)
print(p.coeffs)
print(p.roots)
print(roots(p))
print(p(0))
print(polyval(p,0))

from  numpy.polynomial  import  Polynomial as poly
p=poly(coef)# Polynôme p à coefficients coef
#print(p)

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