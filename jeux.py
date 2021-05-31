print()
print("Trouvez le nombre entre 1 et 100!")
print()

from random import *
nombre=(randrange(100))
print(nombre)

proposition = int(input("entrez un chiffre :"))
print(proposition)

if proposition < nombre:
    print("Trop petit")
elif proposition>nombre:
    print("Trop grand")
elif proposition==nombre:
    print("C'est gagné!")

