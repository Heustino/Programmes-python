# écrire un programme qui:
# - définit une fonction h
#   - qui prend en paramètre un nombre n
#   - calcule le reste de la division n/2
# - demande à l'utilisateur un nombre N
# - appelle la fonction h avec le nombre N

# D'après vous, comment écrire une fonction qui vous dit
# - si vrai ou faux un nombre est impair ?
# - si vrai ou faux un nombre est pair ?

def h(n):
#       """Calcule le reste de la division n/2.

#   Args:
#     n: Le nombre dont on veut calculer le reste de la division par 2.

#   Returns:
#     Le reste de la division n/2.
#   """

  return n % 2


N = int(input("Entrez un nombre : "))

print("Le reste de la division de", N, "par 2 est", h(N))


def est_impair(n):
#       """Dit si un nombre est impair.

#   Args:
#     n: Le nombre à tester.

#   Returns:
#     True si le nombre est impair, False sinon.
#   """

  return n % 2 == 1


def est_pair(n):
#   """Dit si un nombre est pair.

#   Args:
#     n: Le nombre à tester.

#   Returns:
#     True si le nombre est pair, False sinon.
#   """

  return n % 2 == 0
