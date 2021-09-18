# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

# Mon commentaire 

print(1+1) # addition 
print(2*3) # multiplication
print(2**3) # puissance : 2^3
print(2/3) # division réelle
print(2//3) # division entière
print(2%3) # reste division entière ou modulo

print('B'+"onjour !")
Nom=input("Comment tu t'appelles ?\n")
print("Quel nom spécial %s !\n" %(Nom,))
Age=float(input("Quel est ton âge ?\n"))
print("{1}, tu es bien vieux !\n Comment peux-tu avoir jusqu'à {0} ans ?".format(Age,Nom))

liste=["Nom",10]
print(liste)
print(liste[0])
print(liste[1])
print(liste[-1]) 

liste.append(["jean","Jacques"])
print(liste)
print(liste[2][1])

liste.remove(10) # Enlève l'objet 10 de la liste
print(liste)
print(len(liste)) # Longueur de la liste
del liste[1][0] # supprime l'objet à la position [1][0]
print(liste)

# Faire des recheerches sur les tuples et les dictionnaires

if (Age<18):
    print("%s, tu es parmi la jeunesse qui promet."%(Nom,))
elif(Age<=25):
    print("%s, tu es dans la zone tampon."%(Nom,))
else:
    print("%s, ton cas inquiète."%(Nom,))
    
for i in range(10):
    print(i)
print("Fin.")

for i in range(1,10,2):
    print(i)

for i in liste:
    print(i)

ListeBiss=[2*k+1 for k in range(15)]
print(ListeBiss)

listeBisBis=[]
i=1
while (i<9):
    listeBisBis.append(2*i)
    i=i+1
    
print(listeBisBis)

print(listeBisBis+listeBisBis)


"""

Exercice: 
    
1) Ecricre un programme qui lit une liste de réels 
en entrée et produit en sortie la matrice de Vandermonde 
associée

2) En important les modules numpy, math, 
    linalg, matplotlib, pyplot, écricre un programme qui 
    
    i) Calcule racine carré d'un nombre, les principales 
    opérations sur les matrices (addition, soustraction, 
    multiplication, déterminant, transposition, etc)
    
    ii) Affiche le graphe de la fonction cosinus sur 
    [-3pi,pi]
    
"""