# Ecrire un programme qui utilise turtle pour écrire (dessiner) votre nom

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
for lettre in nom:
    tracer_lettre(lettre, "black")

# Fin du programme
turtle.exitonclick()