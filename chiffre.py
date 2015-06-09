#!/usr/bin/python3

import random

nombre = random.randint(1, 99)
proposition = 0

while nombre != proposition:
    proposition = int(input("Entrez  un nombre : "))
    if proposition > nombre:
        print("Le nombre proposé est supérieur !")

    if proposition < nombre:
        print("Le nombre proposé est inférieur ! ")

print("Bravo vous avez trouvé le nombre")
print(nombre)
