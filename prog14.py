# écrire un programme qui :
# - demande à l'utilisateur de saisir le rayon de la base du cylindre,
# - demande à l'utilisateur de saisir la hauteur du cylindre
# - définit une fonction f qui:
#   - prend 3 paramètres: rayon r, hauteur h, nombre n
#   - calcule le volume v du cylindre de rayon r et de hauteur h
#   - renvoie le volume v, arrondi à n chiffres après la virgule
# - utilise la fonction f pour calculer le volume v
# - affiche v

def f(r, h, n):
#       """Calcule le volume d'un cylindre et l'arrondit à n chiffres après la virgule.

#   Args:
#     r: Le rayon du cylindre.
#     h: La hauteur du cylindre.
#     n: Le nombre de chiffres après la virgule.

#   Returns:
#     Le volume du cylindre arrondi à n chiffres après la virgule.
#   """

  volume = math.pi * r ** 2 * h
  return round(volume, n)


# Demande à l'utilisateur de saisir le rayon
rayon = float(input("Entrez le rayon du cylindre : "))

# Demande à l'utilisateur de saisir la hauteur
hauteur = float(input("Entrez la hauteur du cylindre : "))

# Utilise la fonction f pour calculer le volume
volume = f(rayon, hauteur, 3)

# Affiche le volume
print("Le volume du cylindre est de", volume, "mètres cubes.")
