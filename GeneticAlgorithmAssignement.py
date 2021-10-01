from random import *

def Order(L=[0.1,0.1,0.5,0.4,0.8]):
    R=[]
    if (len(L)>0):
        for i in range(len(L)):
            n=1
            for j in range(len(L)):
                if (L[i]>L[j]):
                    n+=1
            while n in R:
                n+=1
            R.append(n)
    return R
    
def Generate(n=5,m=2):
    R=[]
    if ((n>0)and(m>0)):
        for i in range(n):
            L=[random() for j in range(m)]
            L=Order(L)
            if not(L in R):
                R.append(L)
    return R
    
def Cost(C=[[5,10],[10,15]],S=[1,2]):
    R=0
    for i in range(len(S)):
        R+=C[i][S[i]-1]
    return R
    
def OrderBis(C=[[15,10],[10,15]],M=[[1,2],[2,1]]):
    R=[[],[]]
    if (len(M)>0):
        R[1]=[1 for i in range(len(M))]
        for i in range(len(M)):
            n=1
            for j in range(len(M)):
                if (Cost(C,M[i])>Cost(C,M[j])):
                    n+=1
            while n in R[0]:
                n+=1
            R[0].append(n)
            R[1][n-1]=i+1
    return R
    
def Selection(C=[[15,10],[10,15]],M=[[1,2],[2,1]],n=1):
    k=min(len(M),n)
    R=OrderBis(C,M)
    S=[]
    for i in range(k):
        S.append(M[R[1][i]-1])
    return S

def Mutation(M=[[1,2,3,4],[3,1,2,4]],p=0.99):
    N=[M[i] for i in range(len(M))]
    for i in range(len(M)):
        if (len(N)>1):
            if (random()<p):
                temp=N[i].copy()
                k1=randint(1,len(temp)-1)
                k2=randint(1,len(temp)-1)
                if (k2<k1):
                    k2+=k1
                    k1=k2-k1
                    k2-=k1
                elif (k1==k2):
                    if (k1>0):
                        k1=randint(0,k1-1)
                    else:
                        k2=randint(k2+1,len(temp)-1)
                temp[k1]+=temp[k2]
                temp[k2]=temp[k1]-temp[k2]
                temp[k1]-=temp[k2]
                if not(temp in N):
                    N.append(temp)
    return N

def CrossOverPair(C=[[10,15,10],[5,11,10],[25,30,10]],M=[[1,2,3],[2,3,1]],i=0,j=1):
    res=[]
    n=min(len(M[i]),len(M[j]))
    for k in range(n):
        if (C[k][M[i][k]-1]<=C[k][M[j][k]-1]):
            l=M[i][k]
            while (l in res):
                l=(l%n)+1
            if not(l in res):
                res.append(l)
        else:
            l=M[j][k]
            while (l in res):
                l=(l%n)+1
            if not(l in res):
                res.append(l)
    return res

def CrossOver(C=[[10,15,10],[5,11,10],[25,30,10]],M=[[1,2,3],[2,3,1]]):
    res=[M[i] for i in range(len(M))]
    if (len(M)>1):
        for i in range(len(M)-1):
            for j in range(1,len(M)):
                temp=CrossOverPair(C,M,i,j)
                if not(temp in res):
                    res.append(temp)           
    return res


############################################################
Cos=[[10,15,11],[15,20,12],[15,20,18]]
Pop=Generate(n=10,m=3)
Rank=OrderBis(Cos,Pop)
#print([Pop[Rank[1][0]],Cost(Cos,Pop[Rank[1][0]-1])])
for i in range(10):
    Selection(Cos,Pop,6)
    Pop=Mutation(Pop,0.9)
    Selection(Cos,Pop,6)
    #print([Pop[Rank[1][0]],Cost(Cos,Pop[Rank[1][0]-1])])
    CrossOver(Cos,Pop)
    Selection(Cos,Pop,6)
    #print([Pop[Rank[1][0]],Cost(Cos,Pop[Rank[1][0]-1])])
    #print(Pop)

for i in range(len(Pop)):
    print([Pop[i],Cost(Cos,Pop[i])])
  
Rank=OrderBis(Cos,Pop)
print("La solution est X= ")
print(Pop[Rank[1][0]-1])
print("Le cout est C= ")
print(Cost(Cos,Pop[Rank[1][0]-1]))