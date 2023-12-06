# Il s'agit de deviner un nombre n
# Ecrire un programme qui demande à l'utilisateur de saisir un nombre
# - Si le nombre saisi est inférieur à n, afficher "trop petit", puis répéter
# - Si le nombre saisi est supérieur à n, afficher, "trop grand", puis répéter
# - Si le nombre saisi est égal à n, afficher, "trouvé" et interrompre la boucle

# Fonction pour générer un nombre aléatoire entre 1 et 100
def generer_nombre_aleatoire():
    return random.randint(1, 100)

# Fonction pour demander à l'utilisateur de saisir un nombre
def demander_nombre():
    nombre = input("Entrez un nombre : ")
    try:
        nombre = int(nombre)
    except ValueError:
        print("Veuillez saisir un nombre entier.")
        return None
    return nombre

# Fonction principale
def main():
    # Génération d'un nombre aléatoire
    n = generer_nombre_aleatoire()

    # Boucle de jeu
    while True:
        # Demande à l'utilisateur de saisir un nombre
        nombre = demander_nombre()

        # Vérification du nombre saisi
        if nombre is None:
            continue
        elif nombre < n:
            print("Trop petit.")
        elif nombre > n:
            print("Trop grand.")
        else:
            print("Trouvé !")
            break

# Appel de la fonction principale
if __name__ == "__main__":
    main()
