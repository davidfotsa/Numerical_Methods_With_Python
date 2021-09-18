#-*- coding: utf-8 -*-

from math import *
def f(x):
	return (float(exp(x)-1))
def df(x):
	return (float(exp(x)))

e=input("Entrer la précision: ")
x=input("Entrer le terme initial: ")
y=x-f(x)/df(x)
n=0
while (()and()):
	n=n+1
	x=y
	y=y-f(y)/df(y)

print("%d itération(s): "%(n,))	
print("%f est la solution courante: "%(x,))	