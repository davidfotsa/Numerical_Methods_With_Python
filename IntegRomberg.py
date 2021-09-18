# -*- coding: utf-8 -*-

from math import *
from numpy import *

def f(x):
	#return(x)
	return(exp(x)+4)
#print(f(0))	

def ITrap(a,b,f,n):
	if (n<2):
		return (0)
	else:
		I=(f(a)+f(b))/2
		if (n>2):
			x=linspace(a,b,n)
			for i in range(1,n-1):
				I=I+f(x[i])
		I=I*float(b-a)/(n-1)
		return (I)

def Aitken(X,Y,x):
	n=min(len(X),len(Y))
	A=[]
	for i in range(n):
		A.append([Y[n-i-1]])
	for j in range(1,n):
		for i in range(n-j):
			val=(X[n-i-j-1]-x)*A[i][j-1]
			val-=(X[n-i-1]-x)*A[i+1][j-1]
			val/=float(X[n-i-j-1]-X[n-i-1])
			A[i].append(val)
			#A[i].append(0)
	#print(A)		
	return (A[0][n-1])	

def IRom(a,b,f,n):
	if (n<=0):
		return(ITrap(a,b,f,2))
	else:
		H=[float(b-a)/(2**i) for i in range(n+1)]
		I=[ITrap(a,b,f,(2**i)+1) for i in range(n+1)]
		#print(H)
		#print(I)
		return (Aitken(H,I,0))
		
def IRom2(a,b,f,n):
	H=[b-a]
	I=[ITrap(a,b,f,2)]
	#print(H)
	#print(I)
	if (n>0):
		for i in range(1,n+1):
			H.append((b-a)/(2**i))
			s=0
			for j in range(1,2**(i-1)+1):
				s+=f(a+(2*j-1)*H[i])
			I.append(0.5*I[i-1]+H[i]*s)
			#print(H)
			#print(I)
	return (Aitken(H,I,0))

a=-5
b=6
n=5

#X=[0,1,2,3]
#Y=[1,2,5,10]
#print(Aitken(X,Y,4))

print(ITrap(a,b,f,(2**n)+1))
print(IRom(a,b,f,n))
print(IRom2(a,b,f,n))
#print(float(b**2-a**2)/2)
print(exp(b)-exp(a)+b-a)		