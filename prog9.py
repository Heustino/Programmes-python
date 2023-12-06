# Ecrire un programme qui utilise turtle pour écrire (dessiner) votre nom (chaque lettre ayant une couleur différente)

import turtle

# Fonction pour tracer une lettre
def tracer_lettre(lettre, couleur):
    turtle.color(couleur)
    for i in range(len(lettre)):
        turtle.forward(50)
        turtle.left(90)

# Programme principal
nom = "Bard"

# Initialisation de la tortue
turtle.speed(0)
turtle.penup()
turtle.setposition(-200, 0)
turtle.pendown()

# Tracé des lettres
for i, lettre in enumerate(nom):
    couleurs = ["red", "green", "blue", "yellow", "magenta", "cyan"]
    turtle.color(couleurs[i % len(couleurs)])
    tracer_lettre(lettre, couleur)

# Fin du programme
turtle.exitonclick()