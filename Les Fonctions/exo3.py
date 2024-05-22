#Détecter l'âge pour entrer en boite de nuit 
def detectMyAgeByNight():
    age=int(input("Saisir un age>0: "))
    if age>17:
        print("Vous pouvez rentrer, vous êtes majeur. Vous avez ",age,"ans")

    else:
        print("Vous ne pouvez pas entrer, vous n'êtes pas majeur. Vous avez ", age,"ans")

detectMyAgeByNight()