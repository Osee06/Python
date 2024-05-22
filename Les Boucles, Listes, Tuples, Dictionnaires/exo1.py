l1=[]
for i in range(0,11):
    l1.append(1*i)

l2=[]
for i in range(0,11):
    l2.append(2*i)

l3=[]
for i in range(0,11):
    l3.append(3*i)

l5=[]
for i in range(0,11):
    l5.append(5*i)

l8=[]
for i in range(0,11):
    l8.append(8*i)

l_mult=[1,2,3,5,8]
j=0
for i in l_mult:#Essayer de modifier l'afficher quand i change: passer par un res? ou if j==11
    for j in range(0,11):
        print("La table de multiplication de", i," est la suivante:",i,"*",j,"=",i*j)

#Avec Fonction Map
def myfunc(a,b):
    return [a*i for i in range(11)]

liste=[1,2,3,5,8]
list(map(myfunc ,liste))
