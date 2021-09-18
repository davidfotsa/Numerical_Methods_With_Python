#-*- coding: utf-8 -*-

from math import *
from numpy import *

def f(x):
	return (1)
	#return (float(exp(x)-1))

n=int(input("Entrer un nombre de points inmpair pour la méthode de Simpson: "))
if (n%2==0):
	n=n+1
if (n<3):
	n=3

a=float(input("Borne inférieure de l'intégrale: "))
b=float(input("Borne supérieure de l'intégrale: "))
x=linspace(a,b,n)
print(x)

h=float(b-a)/(n-1)
k=int((n-1)/2)
print("Pas: %f et n=2k+1 avec k=%f ."%(h,k,))
I=f(a)-f(b)
for i in range(k):
	I=I+4*f(x[2*i+1])+2*f(x[2*i+2])
	
I=h*I/3	
print("L'intégrale de f de %f à %f est %f . "%(a,b,I,))	