# Soit le programme suivant,
# - saisissez le à l'aide de Idle,
# - sauvegardez le dans un fichier nommé triangle_while_loop.py, puis executez le:

import turtle
tr = turtle.Turtle()

pixels = 200
side_count = 0

while side_count < 3:
    if side_count == 0:
        angle = 0
    else:
        angle = 120

    tr.left(angle)
    tr.forward(pixels)
    side_count = side_count + 1

turtle.exitonclick()

# - Expliquez ce que fait le programme, ligne par ligne.
# - Inspirez vous du programme précédent et écrivez en un pour tracer un carré orange incliné de 30 degré sur la gauche
# - Inspirez vous du programme précédent et écrivez en un pour tracer un rectangle bleu incliné de 45 degré sur la droite


# **Explication ligne par ligne**

    # * La première ligne importe le module `turtle`.
    # * La deuxième ligne crée un objet `Turtle` appelé `tr`.
    # * La troisième ligne définit la longueur des côtés du triangle.
    # * La quatrième ligne définit le nombre de côtés du triangle.
    # * La cinquième ligne est la condition de la boucle `while`. Tant que la valeur de `side_count` est inférieure à 3, la boucle s'exécute.
    # * La sixième ligne vérifie si `side_count` est égal à 0. Si c'est le cas, l'angle du prochain côté est de 0 degrés. Sinon, l'angle est de 120 degrés.
    # * La septième ligne tourne la tortue de l'angle spécifié.
    # * La huitième ligne fait avancer la tortue de la longueur spécifiée.
    # * La neuvième ligne incrémente la valeur de `side_count` de 1.
    # * La dixième ligne ferme la fenêtre graphique lorsque l'utilisateur clique dessus.

# **Programme pour tracer un carré orange incliné de 30 degré sur la gauche**

import turtle
tr = turtle.Turtle()

pixels = 200
side_count = 0

while side_count < 4:
    if side_count == 0:
        angle = 0
    else:
        angle = 120 - 30

    tr.left(angle)
    tr.forward(pixels)
    side_count = side_count + 1

tr.color("orange")

turtle.exitonclick()

    # Ce programme est similaire au programme précédent, mais il utilise un angle de 120 - 30 degrés pour le deuxième côté. Cela permet de tracer un carré avec un angle de 30 degrés sur la gauche.

# **Programme pour tracer un rectangle bleu incliné de 45 degré sur la droite**

import turtle
tr = turtle.Turtle()

pixels = 200
side_count = 0

while side_count < 4:
    if side_count == 0:
        angle = 0
    elif side_count == 1:
        angle = 90
    else:
        angle = 135

    tr.left(angle)
    tr.forward(pixels)
    side_count = side_count + 1

tr.color("blue")

turtle.exitonclick()

# Ce programme est similaire au programme précédent, mais il utilise un angle de 90 degrés pour le deuxième côté et un angle de 135 degrés pour le troisième côté. Cela permet de tracer un rectangle avec un angle de 45 degrés sur la droite.
