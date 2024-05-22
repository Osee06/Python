n=int(input("Saisir un nombre entre 5 et 10: "))
print("J'ai saisi ", n," lignes pour mon affichage")
for i in range(1,n+1): #Itère sur les lignes de 1 à n
    space=" " * (n-i)
    print(space,"["*i, " ","]"*i)

#Correction
for i in range(1,10):
    #Cosntruction de Motif pour chaque ligne
    motif='[' * i + ' ' + ']' * i
    #Center: pour centrer le motif
    print(motif.center(10 * 3))