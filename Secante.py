# -*- coding: utf-8 -*-

from numpy import *
def g(x,y):
	return(log(x)-y);
	
def f(a,b,y,ex,ey,n):
	if (g(a,y)==0):
		c=a
	else:
		c=b
	i=0;
	print("\n%d: %f"%(i,c,))
	while ((abs(b-a)>ex)and(abs(g(c,y))>ey)and(i<=n)):
		c=a-g(a,y)*(b-a)/(g(b,y)-g(a,y))
		i=i+1
		print("%d: %f"%(i,c,))
		if (abs((g(c,y)-g(a,y))/(c-a))>abs((g(b,y)-g(c,y))/(b-c))):
			b=c
		else:
			a=c
	rep=c
	return(rep)

a=6
b=8
y=1
ex=10**(-5)
ey=10**(-5)
n=10
print("\n\nRéponse: %f \nApproximation: %f"%(exp(y),f(a,b,y,ex,ey,n),))