

print("Méthode Crout ou LU ")

"""
n=int(input("Quelle est la dimension de l'inconnu ? "))
M=[]
for i in range(n):
    M.append([])
    for j in range(n):
        M[i].append(float(input("Entrer l'élément A["+str(i+1)+","+str(j+1)+"]= ")))

B=[]
for i in range(n):
    #B.append([])
    B[i].append(float(input("Entrer l'élément B["+str(i+1)+"]= ")))

"""

n=4
M=[[1,1,1,1],[2,-1,1,2],[1,-3,1,-1],[5,0,1,0]]
#B=[[10],[9],[-4],[22]]
B=[10,9,-4,22]

import numpy as np
M=12*60*np.matrix(M)
#B=np.matrix(B)
B=12*60*np.array(B)

from numpy import matlib as mat

U=mat.zeros((n, n))
L=12*mat.eye(n, k=0)
#print("U= {0}".format(U))
#print("L= {0}".format(L))

for i in range(n):
    #print(i)
    for j in range(i,n,1):
        U[i,j]=M[i,j]
        for k in range(0,i,1):
            U[i,j]=U[i,j]-L[i,k]*U[k,j]
        U[i,j]=U[i,j]/L[i,i]
    #print(U)
    for j in range(i+1,n,1):
        L[j,i]=M[j,i]
        for k in range(0,i,1):
            L[j,i]=L[j,i]-L[j,k]*U[k,i]
        L[j,i]=L[j,i]/U[i,i]
    #print(L)  

Y=B.copy()
Y[0]=Y[0]/L[0,0]
for i in range(1,n):
    for j in range(0,i):
        Y[i]=Y[i]-L[i,j]*Y[j]
    Y[i]=Y[i]/L[i,i]

X=Y.copy()
X[n-1]=X[n-1]/U[n-1,n-1]
for i in range(2,n+1):
    for j in range(1,i):
        X[n-i]=X[n-i]-U[n-i,n-j]*X[n-j]
    X[n-i]=X[n-i]/U[n-i,n-i]

print(M/(12*60))
print(Y)
X=np.transpose(X)    
print(X)

print("M= {0}".format(M))
print("L= {0}".format(L)) 
print("U= {0}".format(U))
print("B= {0}".format(B))
#print("LU-M= {0}".format(L*U-M))