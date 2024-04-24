prix_initial=float(input("Saisir le prix initial: \n"))
pourcentage_remise=float(input("Saisir le pourcentage de remise: \n"))
#prix_initial,pourcentage_remise=float(input("Saisir le prix initial: \n")),float(input("Saisir le pourcentage de remise: \n"))

#Montant de la remise 
montant_remise=prix_initial *(pourcentage_remise/100)

#Prix final
prix_final=prix_initial-montant_remise

if prix_final>(prix_initial/2):
    print(f'Le prix final est {prix_final}')
else:
    print("La remise est trop élevée")
