# écrire un programme qui
# - demande à l'utilisateur de saisir des nombres séparés par des "@"
# - enregistre chacun de ces nombres dans une liste
# - classe les nombres par ordre décroissant
# - affiche la liste

nombres = []

# Demande à l'utilisateur de saisir des nombres
while True:
  nombre = input("Entrez un nombre (ou @ pour arrêter) : ")
  if nombre == "@":
    break
  nombres.append(int(nombre))

# Classe les nombres par ordre décroissant
nombres.sort(reverse=True)

# Affiche la liste
print("Les nombres, classés par ordre décroissant, sont :", nombres)
