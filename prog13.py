# écrire un programme qui :
# - demande à l'utilisateur de saisir le rayon de la base du cylindre,
# - demande à l'utilisateur de saisir la hauteur du cylindre
# - calcule le volume du cylindre
# - affiche le volume du cylindre arrondi à 3 chiffres après la virgule

import math

# Demande à l'utilisateur de saisir le rayon
rayon = float(input("Entrez le rayon du cylindre : "))

# Demande à l'utilisateur de saisir la hauteur
hauteur = float(input("Entrez la hauteur du cylindre : "))

# Calcule le volume du cylindre
volume = math.pi * rayon ** 2 * hauteur

# Arrondit le volume à 3 chiffres après la virgule
volume = round(volume, 3)

# Affiche le volume du cylindre
print("Le volume du cylindre est de", volume, "mètres cubes.")
