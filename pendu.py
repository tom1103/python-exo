#!/usr/pin/python3.4

from getpass import getpass

mot = getpass("Entrez un mot à faire deviner : ").lower()
longeur = len(mot)
car = '*'
inconnu = car * longeur
print("Vous devez deviner un mot de "+str(longeur)+" lettres !")
print(inconnu)


while car in inconnu:

    reponse = input("Entrez une lettre : ")

    i = 0
    while i <= longeur-1:
        if reponse == mot[i]:
            inconnu = list(inconnu)
            inconnu[i] = reponse
            inconnu = ''.join(inconnu)

        i = i+1

    print(inconnu)

print("Bravo vous avez gagné !")
