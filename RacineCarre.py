# -*- coding: utf-8 -*-

def g(x,y):
	return(x**2-y);
def f(y):
	rep=0
	if (y<0) :
		y=-y;
	a=float(0);
	b=float(1);
	while (b*b<y) :
		b=b+1;
	if (g(a,y)==0):
		c=a
	else:
		c=b
	n=0;
	while ((g(a,y)*g(b,y)<0)and(n<50)):
		c=(a+b)/2
		if (g(a,y)*g(c,y)<0):
			b=c
		else:
			a=c
		n=n+1
	rep=c
	return(rep)

print(f(3))
		
	