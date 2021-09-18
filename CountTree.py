"""
cd C:/Users/DELL/Desktop/TPMNMIP22021
python CountTree.py

"""

#Count tree in a n1xn2xn3 cube using Kirchhoff's Theorem

import numpy as np

print("This program counts trees in a n1 x n2 x n3 cube");
"""
n1=int(input("n1 = "))
n2=int(input("n2 = "))
n3=int(input("n3 = "))
"""

def NextPerm(y):
    # Si x est une permutation, NextPerm(x) la prochaine permutation dans l'ordre lexicographique
    x=y.copy()
    n=len(x)
    if (n>1):
        i=n-1
        #print("n= %d"%(n,))
        #print("i= %d"%(i,))
        while ((i>1) and (x[i-1]>x[i])):
            i=i-1
        if (i==n-1):
            #print("n= %d"%(n,))
            #print("i= %d"%(i,))
            x[i]=x[i-1]+x[i]
            x[i-1]=x[i]-x[i-1]
            x[i]=x[i]-x[i-1]
        #elif (x[i-1]>max([x[j] for j in range(i+1,n)])):
        #    x[i]=x[i-1]+x[i]
        #    x[i-1]=x[i]-x[i-1]
        #    x[i]=x[i]-x[i-1]
        #    x=[x[j] for j in range(0,i)]+list(np.sort([x[j] for j in range(i,n)]))
        elif (x[i-1]<x[i]):
            m=n-1
            for j in range(1,n-i+1):
                if ((x[m]<x[i-1]) or ((x[n-j]>=x[i-1]) and (x[m]>x[n-j]))):
                    m=n-j
            x[m]=x[i-1]+x[m]
            x[i-1]=x[m]-x[i-1]
            x[m]=x[m]-x[i-1]
            x=[x[j] for j in range(0,i)]+list(np.sort([x[j] for j in range(i,n)]))
    return(x)

"""    
print(NextPerm([2,4,5,3,1]))
print(NextPerm([2,5,4,3,1]))
print(NextPerm([5,3,1]))
""" 

def SignPerm(L):
    # Si x est une permutation, SignPerm(x) calcule le signe de x
    y=L.copy()
    res=1
    n=len(y)
    x=list(np.sort(y))
    z=[]
    i=0
    while (n>0):
        if (x[i]!=y[i]):
            if not(y[i] in z):
                res=-res
            z.append(x[i])
            #z.append(y[i])
            tmp=y[i]
            del x[i]
            del y[i]
            n=len(y)
            j=0
            while ((j<n) and (x[j]!=tmp)):
                j=j+1
            if ((tmp in z) and (j<n)):
                del x[j]
                del y[j]
                n=len(y)
            i=max(0,min(j,n-1))
        if (n>0): 
            j=i
            while ((j<n) and ((x[j] in z) or (x[j]==y[j]))):
                del x[j]
                del y[j]
                n=len(y)
                j=max(0,min(j+1,n-1))
            i=j
    return(res)  

"""

print(SignPerm([2,4,5,3,1])) 
print(SignPerm([2,5,4,3,1])) 
print(SignPerm([2,1,3,4,6,5,7,8]))


1 2 3 4 5 
2 4 5 3 1

(12435)
(15)(13)(14)(12)

1 2 3 4 5 
2 5 4 3 1

(125)(34)
(15)(12)(34)

[2,1,3,4,6,5,7,8]
[1,2,3,4,5,6,7,8]
[2,1,3,4,6,5,7,8]
12 56

"""

def matLaplacePave(x,y,z,i,j): 
    """
    x*y*z est le nombre de cellules du pavé
    évalue cellule (i,j) qui vaut le degré de i si i=j , 
    -1 si l'arête {i,j} ou l'un des arcs (i,j) ou (j,i) existe,
    et 0 dans les autres cas
    (i-1)*y*z+(j-1)*z+k est le numéro de l'objet en coordonné 3d (i,j,k)
    """
    if (i==j):
        res=0
        i1=(int(i-1)//int(y*z))+1
        i2=(int(i-1-(i1-1)*y*z)//z)+1
        i3=int(i-1-(i1-1)*y*z-(i2-1)*z)+1
        for k1 in range(-1,2,1):
            if ((i1+k1>=1) and (i1+k1<=x)):
                for k2 in range(-1,2,1):
                    if ((i2+k2>=1) and (i2+k2<=y)):
                        for k3 in range(-1,2,1):
                            if ((i3+k3>=1) and (i3+k3<=z)):
                                if (abs(k1)+abs(k2)+abs(k3)==1):
                                    res=res+1
                                    #print([[i],[i1,i2,i3],[i1+k1,i2+k2,i3+k3],res])
    else:
        res=0
        i1=(int(i-1)//int(y*z))+1
        i2=(int(i-1-(i1-1)*y*z)//z)+1
        i3=int(i-1-(i1-1)*y*z-(i2-1)*z)+1
        j1=(int(j-1)//int(y*z))+1
        j2=(int(j-1-(j1-1)*y*z)//z)+1
        j3=int(j-1-(j1-1)*y*z-(j2-1)*z)+1
        if (abs(j1-i1)+abs(j2-i2)+abs(j3-i3)==1):
            res=-1
        #print([[i,j],[i1,i2,i3],[j1,j2,j3],res])
    return(res)
    
"""
print(matLaplacePave(2,2,2,1,1))
print(matLaplacePave(3,3,3,(2-1)*3*3+(2-1)*3+2,(2-1)*3*3+(2-1)*3+2))
"""

def ProdPerm(n1,n2,n3,y):
    """
    Si y est une permutation, ProdPerm(x) est le terme 
    du déterminant de la matrice laplacienne associé à y
    """
    res=SignPerm(y)
    x=np.sort(y)
    n=len(y)
    i=0
    while ((i<n) and (res!=0)):
        res=res*matLaplacePave(n1,n2,n3,x[i],y[i])
        i=i+1
        #print(i)
    return(res)
 
def NbrTree(n1,n2,n3):
    y=list(np.linspace(2,n1*n2*n3,n1*n2*n3-1))
    #print(y)
    res=0
    while (y!=NextPerm(y)):
        res=res+ProdPerm(n1,n2,n3,y)
        #print(NextPerm(y))
        y=NextPerm(y)
    res=res+ProdPerm(n1,n2,n3,y)
    return(abs(res)) 

from numpy import matlib as mat
n1=2
n2=2
n3=2
n=n1*n2*n3
L=mat.zeros((n,n))    
for i in range(n):
    for j in range(n):
        L[i,j]=matLaplacePave(n1,n2,n3,i+1,j+1)     
print(L)
print(NbrTree(n1,n2,n3))
"""
y=list(np.linspace(2,n1*n2*n3,n1*n2*n3-1))
print(NextPerm(y))
print(y)

print(ProdPerm(2,2,2,[2,1,3,4,6,5,7,8]))
#print(np.linspace(1,10,10))  # suite arithmétique ...
"""