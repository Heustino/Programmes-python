import calendar

# Dictionnaire contenant les informations sur les journées
jours_info = {
    "01/01": {"nom": "Journée internationale de la paix", "type": "événement"},
    "02/02": {"nom": "Journée mondiale de la lutte contre les maladies tropicales négligées", "type": "événement"},
    "03/08": {"nom": "Journée internationale des femmes", "type": "événement"},
    "04/04": {"nom": "Journée mondiale de la sensibilisation à l'autisme", "type": "événement"},
    "05/05": {"nom": "Journée mondiale de la liberté de la presse", "type": "événement"},
    "06/06": {"nom": "Journée internationale des parents", "type": "événement"},
    "07/07": {"nom": "Journée mondiale de la coopération technique", "type": "événement"},
    "08/08": {"nom": "Journée internationale des peuples autochtones", "type": "événement"},
    "09/09": {"nom": "Journée mondiale des premiers secours", "type": "événement"},
    "10/10": {"nom": "Journée mondiale de la santé mentale", "type": "événement"},
    "11/11": {"nom": "Journée internationale des orphelins et des enfants sans famille", "type": "événement"},
    "12/12": {"nom": "Journée mondiale de la solidarité humaine", "type": "événement"},
}

# Fonction pour convertir une date en lettres
def date_en_lettres(date):
  mois = calendar.month_abbr[date.month]
  jour = str(date.day)
  if len(jour) == 1:
    jour = "0" + jour
  return mois + " " + jour

# Affiche la date du jour
date_du_jour = date.today()
print("Aujourd'hui est le", date_en_lettres(date_du_jour))

# Vérifie si la date du jour correspond à une journée mondiale
if date_du_jour in jours_info:
  # Affiche la journée mondiale
  print("C'est la journée mondiale de", jours_info[date_du_jour]["nom"])
else:
  # Affiche un message
  print("Aucune journée mondiale n'est célébrée aujourd'hui.")
