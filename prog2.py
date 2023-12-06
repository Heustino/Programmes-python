# Écrivez un programme pour vérifier si un nombre
# -est divisible par 3 et 13 ou non, en utilisant if-else.

# Écrire un programme qui demande à l'utilisateur de saisir un entier.
# - Si l'entier est un multiple de 3, afficher “Fizz” au lieu du nombre
# - Si l'entier est un multiple de 5 afficher “Buzz”.
# - Si le nombre est multiple de 3 et 5, afficher “FizzBuzz”.
# - Pour toutes les autres situations, afficher simplement le nombre

# Demander à l'utilisateur de saisir un nombre
n = int(input("Entrez un nombre : "))

# Vérifier si le nombre est divisible par 3
if n % 3 == 0:
    # Si oui, vérifier si le nombre est divisible par 13
    if n % 13 == 0:
        # Si oui, afficher "Le nombre est divisible par 3 et 13"
        print("Le nombre est divisible par 3 et 13")
    else:
        # Si non, afficher "Le nombre est divisible par 3 mais pas par 13"
        print("Le nombre est divisible par 3 mais pas par 13")
else:
    # Si non, afficher "Le nombre n'est pas divisible par 3"
    print("Le nombre n'est pas divisible par 3")
