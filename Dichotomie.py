"""
python C:/Users/DELL/Desktop/TPMNMIP22021/Dichotomie.py

cd C:/Users/DELL/Desktop/TPMNMIP22021
python Dichotomie.py

"""

from math import *
from numpy import *
from matplotlib import pyplot as plt
from os import getcwd, chdir
 
def f(x):
    return(exp(x)-x-2)
#print(f(0))    
   
x=linspace(-1,2,101)
#print(x)
y=f(x)
#print(y)

z=[0 for i in range(len(x))]
"""
plt.figure(figsize=(5,5)) # Figure 1000 pixels * 800 pixels
plt.clf() # Efface le contenu de la figure courante
plt.plot(x,y)
plt.plot(x,z)
plt.plot(z,x)

Dir="C:/Users/DELL/Desktop/TPMNMIP22021/"
plt.savefig(Dir+"MonImage.png")
plt.savefig(Dir+"MonImage",format="pdf")

Dir=getcwd()
#chdir(Dir)
print(Dir)
plt.savefig(Dir+"/MonImage.png")
plt.savefig(Dir+"/MonImage.pdf",format="pdf")
plt.show()
"""

print([f(0.5),f(2)])
a=0.5
b=2
e=10**(-3)
e2=10**(-1)
r=(a+b)/2
i=1
while (((abs(b-a)>=e) or (abs(f(r)-0)>=e2)) and (i<101)):
    print("Itération %d et valeur %f"%(i,r,))
    i=i+1
    if (f(r)==0):
        a=r
        b=r
    #print([f(a),f(b),f(r)])
    if (f(a)*f(r)<0):
        b=r
    else:
        a=r
    #print([a,b])
    r=(a+b)/2
print(r)    


