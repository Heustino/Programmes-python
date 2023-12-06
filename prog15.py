# écrire un programme qui
# - demande à l'utilisateur de saisir un nombre
# - stocke ce nombre dans une variable n
# - additionne chaque chiffre du nombre n
# - affiche cette somme
# Vous proposerez deux solutions: avec un for et avec un while

def somme_chiffres(n):
#       """Calcule la somme des chiffres d'un nombre.

#   Args:
#     n: Le nombre dont on veut calculer la somme des chiffres.

#   Returns:
#     La somme des chiffres du nombre.
#   """

  somme = 0
  for i in range(len(n)):
    somme += n[i]
  return somme


n = input("Entrez un nombre : ")
print("La somme des chiffres du nombre", n, "est de", somme_chiffres(n))


def somme_chiffres(n):
#       """Calcule la somme des chiffres d'un nombre.

#   Args:
#     n: Le nombre dont on veut calculer la somme des chiffres.

#   Returns:
#     La somme des chiffres du nombre.
#   """

  somme = 0
  i = 0
  while i < len(n):
    somme += n[i]
    i += 1
  return somme


n = input("Entrez un nombre : ")
print("La somme des chiffres du nombre", n, "est de", somme_chiffres(n))
