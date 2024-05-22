n=int(input("Saisir un nombre entre 5 et 10: "))
print("J'ai saisi ", n," lignes pour mon affichage")
for i in range(1,n+1): #Itère sur les lignes de 1 à n
    for j in range(i): #Affiche i étoiles
        print('*', end='')
    print() #Saut à la ligne 

#Avec Une Map

print(' '.join(list(map(lambda x: x * "*", range(1,6)))))
