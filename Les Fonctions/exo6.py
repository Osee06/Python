def is_palindrome_mot(mot):
    i=0
    j=len(mot)-1
    mot=mot.lower()
    while i<len(mot) and j>0:
        if mot[i]!=mot[j]:
            return False
        i+=1
        j-=1
    return True
print("Palindrome_word")
print(is_palindrome_mot("ibobi"))
print(is_palindrome_mot("Nanji"))
print(is_palindrome_mot("Kayak"))
print(is_palindrome_mot("bob"))

def is_palindrome_chaine(chaine):
    chaine=chaine.replace(" ", "").lower() #enlève tous les espaces et met toute la chaine en miniscule
    reverse_chaine="".join(reversed(chaine))
    return chaine==reverse_chaine
print("Palindrome_chaine")
print(is_palindrome_chaine("Tatiana"))
print(is_palindrome_chaine("No melon, no lemon"))