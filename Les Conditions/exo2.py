import random
feeling=random.randrange(0,30)
# match feeling:
#     case 1 if feeling>=0 and feeling<=10:
#         print("Cool")
    
#     case 2 if feeling>=11 and feeling<=20:
#         print("Tepid")

#     case 3 if feeling>=21 and feeling<=30:
#         print("Warm")

print("Warm" if feeling>20 else "Tepid" if feeling>10 else "Cool")