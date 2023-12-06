# Soit le programme suivant:

counter = 0
end_value = 100
print("counter value", counter)
while counter <= end_value:
    print(counter)
    counter = counter + 1
print("counter value", counter)

# - Expliquez ce que fait le programme, ligne par ligne
# - Quelle est la différence entre une boucle for et une boucle while?
# - Ecrivez le programme précédent en utilisant une boucle for
# - Inspirez vous du programme précédent pour en écrire un qui:
#   - affiche les nombres allant de 10 à 20 en comptant de 2 en 2
#   - affiche les nombres allant de 20 à 10 en comptant de 4 en 4


# **Explication ligne par ligne**
    # La première ligne initialise la variable `counter` à 0.
    # La deuxième ligne affiche la valeur actuelle de la variable `counter`.
    # La troisième ligne est la condition de la boucle `while`. Tant que la valeur de `counter` est inférieure ou égale à la valeur de `end_value`, la boucle s'exécute.
    # La quatrième ligne affiche la valeur actuelle de la variable `counter`.
    # La cinquième ligne incrémente la valeur de la variable `counter` de 1.
    # La sixième ligne affiche la valeur actuelle de la variable `counter`.

# **Différence entre une boucle for et une boucle while**

    # La principale différence entre une boucle `for` et une boucle `while` est que la boucle `for` s'exécute un nombre défini de fois, tandis que la boucle `while` s'exécute tant que la condition est vraie.
    # Une boucle `for` est généralement utilisée lorsque l'on sait à l'avance combien de fois la boucle doit s'exécuter. Par exemple, pour afficher les nombres de 1 à 10, on peut utiliser une boucle `for` avec une plage de 1 à 11 :

for i in range(1, 11):
    print(i)

    # Une boucle `while` est généralement utilisée lorsque l'on ne sait pas à l'avance combien de fois la boucle doit s'exécuter. Par exemple, pour afficher les nombres jusqu'à ce qu'un utilisateur entre un nombre négatif, on peut utiliser une boucle `while` avec une condition qui vérifie si le nombre saisi est positif :

while True:
    nombre = int(input("Entrez un nombre: "))
    if nombre < 0:
        break
    print(nombre)

# **Version avec une boucle for**

    # Voici la version du programme précédent avec une boucle `for` :

counter = 0
end_value = 100

for counter in range(end_value + 1):
    print(counter)

    # Cette version est plus concise et plus facile à lire. La ligne `counter in range(end_value + 1)` initialise la variable `counter` à 0 et initialise ensuite une plage de nombres allant de 0 à `end_value`. La boucle `for` s'exécute ensuite pour chaque nombre de la plage.

# **Programme qui affiche les nombres de 10 à 20 en comptant de 2 en 2**

for counter in range(10, 21, 2):
    print(counter)

    # Cette version utilise la même boucle `for` que la version précédente, mais la plage est modifiée pour aller de 10 à 21 en incrémentant de 2 en 2.

# **Programme qui affiche les nombres de 20 à 10 en comptant de 4 en 4**

for counter in range(20, 0, -4):
    print(counter)

    # Cette version utilise la même boucle `for` que la version précédente, mais la plage est modifiée pour aller de 20 à 0 en décrémentant de 4 en 4.