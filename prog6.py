# Soit le programme suivant:

# import turtle

# polygon = turtle.Turtle()

# color = "green"
# num_sides = 6
# side_length = 70
# angle = 360.0 / num_sides

# polygon.color(color)

# for i in range(num_sides):
#     polygon.forward(side_length)
#     polygon.right(angle)

# turtle.exitonclick()

# En vous inspirant du programme précédent, écrivez un programme qui demande à l'utilisateur
# - "quelle figure voulez vous tracer?"
# - "de quelle couleur doit être le contour de la figure?"

# L'utilisateur devra saisir le nom d'un figure puis le nom d'une couleur
# Le programme devra tracer cette figure en respectant la couleur choisie
# Les figures acceptées sont:
# - "cylindre", "cône", "pyramide", "prisme hexagonal"

import turtle

# Liste des figures acceptées
figures = ["cylindre", "cône", "pyramide", "prisme hexagonal"]

# Fonction pour tracer un cercle
def tracer_cercle(rayon, couleur):
    turtle.color(couleur)
    turtle.circle(rayon)

# Fonction pour tracer un cône
def tracer_cone(hauteur, rayon, couleur):
    turtle.color(couleur)
    turtle.begin_fill()
    turtle.circle(rayon)
    turtle.forward(hauteur)
    turtle.end_fill()

# Fonction pour tracer une pyramide
def tracer_pyramide(hauteur, base, couleur):
    turtle.color(couleur)
    turtle.begin_fill()
    turtle.forward(hauteur)
    turtle.right(120)
    turtle.forward(base)
    turtle.right(120)
    turtle.forward(base)
    turtle.right(120)
    turtle.end_fill()

# Fonction pour tracer un prisme hexagonal
def tracer_prisme_hexagonal(hauteur, base, couleur):
    turtle.color(couleur)
    turtle.begin_fill()
    for i in range(6):
        turtle.forward(base)
        turtle.right(60)
    turtle.end_fill()

# Fonction principale
def main():
    # Demande à l'utilisateur la figure à tracer
    figure = input("Quelle figure voulez-vous tracer? ")

    # Vérifie que la figure est valide
    if figure not in figures:
        print("Figure invalide.")
        return

    # Demande à l'utilisateur la couleur du contour
    couleur = input("De quelle couleur doit être le contour de la figure? ")

    # Trace la figure
    if figure == "cylindre":
        rayon = float(input("Rayon du cercle: "))
        tracer_cercle(rayon, couleur)
    elif figure == "cône":
        hauteur = float(input("Hauteur du cône: "))
        rayon = float(input("Rayon de la base du cône: "))
        tracer_cone(hauteur, rayon, couleur)
    elif figure == "pyramide":
        hauteur = float(input("Hauteur de la pyramide: "))
        base = float(input("Base de la pyramide: "))
        tracer_pyramide(hauteur, base, couleur)
    elif figure == "prisme hexagonal":
        hauteur = float(input("Hauteur du prisme hexagonal: "))
        base = float(input("Base du prisme hexagonal: "))
        tracer_prisme_hexagonal(hauteur, base, couleur)

# Appel de la fonction principale
if __name__ == "__main__":
    main()
