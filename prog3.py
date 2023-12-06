# Ecrire un programme qui demande à l'utilisateur de saisir un nombre N.
# Le programme devra ensuite calculer puis afficher la somme des nombres compris entre 1 et N.

# Par exemple, si l'utilisateur tape le nombre 10,
# Le programme devra afficher 55 çad: 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10


# Demander à l'utilisateur de saisir un nombre
n = int(input("Entrez un nombre : "))

# Initialiser la somme à 0
somme = 0

# Itérer sur les nombres de 1 à N
for i in range(1, n + 1):
    # Ajouter le nombre courant à la somme
    somme += i

# Afficher la somme
print("La somme des nombres de 1 à", n, "est", somme)
