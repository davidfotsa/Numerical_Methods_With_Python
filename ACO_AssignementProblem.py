from random import *

def Normalize(L=[0,0,0]):
    XX=L.copy()
    res=[[],[]]
    if (len(XX)>0):
        s=min(XX)
        if (s<0):
           for i in range(len(XX)):
                XX[i]-=s 
        s=sum(XX)
        if (s>0):
            for i in range(len(XX)):
                res[0].append(XX[i]/s)
                if (i==0):
                    res[1].append(res[0][-1])
                else:
                    res[1].append(res[1][-1]+res[0][-1])
        else:
            res[0]=L.copy()
            res[1]=L.copy()
    return res
    
def Choice(L=[0,0,0]):
    XX=L.copy()
    if len(XX)>0:
        if sum(XX)==0:
            for i in range(len(XX)):
                XX[i]=1
        XX=Normalize(XX)[1]
        a=random()
        res=0
        while ((res<len(XX)-1)and(a>XX[res])):
            res+=1
    else:
        res=None
    return res

def Generate(M=[[0,1/3,1/3,1/3],[0,0,1/2,1/2],[0,1/2,0,1/2],[0,1/2,1/2,0]]):
    NN=[M[i].copy() for i in range(len(M))]
    p=0
    n=1
    while (n<len(NN)):
        pnew=Choice(NN[p])
        for i in range(len(NN)):
            if (i!=p):
                NN[i][pnew]=0
            if (i!=pnew):
                NN[p][i]=0    
        p=pnew
        n=n+1
    return(NN)

def SolCost(N=[[0,1/2,1/2],[0,0,1],[0,1,0]],C=[[10,15],[15,20]]):
    XX=[]
    Cost=0
    n=0
    p=0
    while (n<len(N)-1):
        i=1
        while ((i<len(N))and(N[p][i]==0)):
            i+=1
        if (i<len(N)):
            XX.append(i)
            p=i
            Cost+=C[n][p-1]  
        n+=1
    return XX,Cost

def Update(Mold,Xold,Cold,N,Cnew):
    MM=[Mold[i].copy() for i in range(len(Mold))]
    XX,cc=SolCost(N,Cnew)
    if (cc<Cold):
        for i in range(len(N)):
            for j in range(len(N)):
                if (N[i][j]>0):
                    MM[i][j]+=N[i][j]      
            MM[i]=Normalize(MM[i])[0]
        return MM,XX,cc
    else:
        return Mold,Xold,Cold

Nmax=10       
C=[[10,15,11],[15,20,12],[15,20,18]]
M=[[0,1/3,1/3,1/3],[0,0,1/2,1/2],[0,1/2,0,1/2],[0,1/2,1/2,0]]
N=Generate(M)

X,c=SolCost(N,C)
print((X,c))
for i in range(Nmax):
    N=Generate(M)
    print(SolCost(N,C))
    M,X,c=Update(M,X,c,N,C)
    
print("La solution est X= ")
print(X)
print("Le coût optimal est c= ")
print(c)