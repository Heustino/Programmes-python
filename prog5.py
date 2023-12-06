# Ecrivez un programme qui demande à l'utilisateur
# - "longeur? "
# - "largeur? "

# Le programme devra ensuite calculer et afficher:
# - la surface est ...
# - le perimetre est ...

# Le programme devra ensuite demander à l'utilisateur s'il veut tracer le rectangle:
# - Si l'utilisateur répond "oui", tracer la figure puis afficher "aurevoir"
# - Si l'utilisateur répond "non", afficher un message: "aurevoir"

# Fonction pour calculer la surface d'un rectangle
def surface_rectangle(longueur, largeur):
    return longueur * largeur

# Fonction pour calculer le périmètre d'un rectangle
def perimetre_rectangle(longueur, largeur):
    return 2 * (longueur + largeur)

# Fonction pour tracer un rectangle
def tracer_rectangle(longueur, largeur):
    for i in range(largeur):
        print("*", end="")
    print()
    for i in range(longueur - 2):
        print("*", end="")
        for j in range(largeur - 1):
            print(" ", end="")
        print("*")
    for i in range(largeur):
        print("*", end="")

# Fonction principale
def main():
    # Demande à l'utilisateur de saisir la longueur et la largeur
    longueur = float(input("Longueur? "))
    largeur = float(input("Largeur? "))

    # Calcul de la surface et du périmètre
    surface = surface_rectangle(longueur, largeur)
    perimetre = perimetre_rectangle(longueur, largeur)

    # Affichage de la surface et du périmètre
    print("La surface est de", surface)
    print("Le périmètre est de", perimetre)

    # Demande à l'utilisateur s'il veut tracer le rectangle
    tracer = input("Voulez-vous tracer le rectangle? (oui/non) ")

    # Si l'utilisateur répond "oui", on trace le rectangle
    if tracer == "oui":
        tracer_rectangle(longueur, largeur)

    # Affichage d'un message de fin
    print("Au revoir")

# Appel de la fonction principale
if __name__ == "__main__":
    main()
