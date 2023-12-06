# écrire un programme qui:
# - définit un dictionnaire contenant des célébrations, ex: {"Nouvel an": "1 Janvier", "Tabaski": "10 Juillet", "Pentecote": "5 Juin"}
# - demande à l'utilisateur de:
#   - saisir le jour
#   - saisir le mois
# - vérifie si la date saisie correspond à une date de célébration
#   - si oui, afficher la célébration en question
#   - si non, afficher le message: "Cette date ne correspond à aucune célébration"

# * Attention:
# - même si l'utilisateur saisit "1 jAnViEr", le programme sera capable de reconnaitre qu'il s'agit du nouvel an

célébrations = {
    "Nouvel an": "1 Janvier",
    "Tabaski": "10 Juillet",
    "Pentecôte": "5 Juin",
}

jour = input("Entrez le jour : ")
mois = input("Entrez le mois : ")

# Convertit les entrées de l'utilisateur en minuscules
jour = jour.lower()
mois = mois.lower()

# Vérifie si la date saisie correspond à une date de célébration
if (jour, mois) in célébrations.items():
  # Affiche la célébration en question
  print("Cette date correspond à la célébration de", célébrations[(jour, mois)])
else:
  # Affiche le message d'erreur
  print("Cette date ne correspond à aucune célébration")
