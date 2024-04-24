import random 
age=int(input("Veuillez Saisir un age entre 0 et plus de 18: "))
if age<=17:
    print(f'Vous ne pouvez pas entrer en boîte de nuit car vous n etes pas majeur. Vous avez {age} \n')
else:
    print(f'Vous pouvez entrer, vous etes majeur. Vous avez {age}ans\n')
