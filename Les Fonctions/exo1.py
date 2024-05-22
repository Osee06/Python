#Permet de retourner un String
def myPutStr(myval):
    if type(myval)==int: 
        print("Et pourquoi pas 42")
    else:
        print(myval)

myPutStr(6)
myPutStr("Yes")