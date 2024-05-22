#Trie à bulle
nbr=[5,4,3,2,1]
for i in nbr:
    for j in range(len(nbr)-1):
        if nbr[j]>nbr[j+1]: #> Ordre Croissant
            #Echange les éléments si ils sont dans le mauvais ordre
            nbr[j], nbr[j+1]=nbr[j+1], nbr[j]

print(nbr)