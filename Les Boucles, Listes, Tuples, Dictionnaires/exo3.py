i=0
l=[] #Liste contenant des éléments de 1 à 10
while i<11:
    l.append(i)
    i+=1
l_mult5=[] #Liste contenant la table de multiplication de 5
j=0
while j<len(l):
    print(5,"*",j,"= ",5*l[j])
    l_mult5.append(5*j)
    j+=1

#Corection 
max=10
i=1
table_cinq=[]
nbr=5
while True:
   if i>max:
       break
   print(f"{nbr} x {i}={nbr*i}")
   i+=1