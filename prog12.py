# Soit la liste de coordonnées de points x,y sous la forme d'une liste de tuples:
coordinates = [(4,5), (9,3), (12,8), (13,7), (18,6), (20,9)]
# - Créez une liste vide d’ordonnées: ordinates = [].
# - Remplissez la liste d’ordonnées en parcourant la liste coordinates.
# - Affichez la liste ordinates.

coordinates = [(4,5), (9,3), (12,8), (13,7), (18,6), (20,9)]
ordinates = []
for x,y in coordinates:
    ordinates.append(y)
print(ordinates)


# - Créez un dictionnaire dict_coordinates à partir de la liste coordinates
coordinates = [(4,5), (9,3), (12,8), (13,7), (18,6), (20,9)]
d1 = dict(coordinates)


# On veut borner à 7 toutes les ordonnées y de la liste coordinates qui sont supérieures à 7
# Après votre traitement, affichez coordinates, qui devrait contenir :
[(4,5), (9,3), (12,7), (13,7), (18,6), (20,7)]
# Vous proposerez trois manières de faire

coordinates_7 =[]
for x, y in coordinates:
    if y > 7:
        coordinates_7.append((x, 7))
    else:
        coordinates_7.append((x, y))


coordinates = [(4,5), (9,3), (12,8), (13,7), (18,6), (20,9)]
ordinates = []
for x,y in coordinates:
    ordinates.append(y)
print(ordinates)

coordinates = [(4,5), (9,3), (12,8), (13,7), (18,6), (20,9)]
d1 = dict(coordinates)

coordinates = [(4,5), (9,3), (12,8), (13,7), (18,6), (20,9)]

# Méthode 1
for x, y in coordinates:
    if y > 7:
        coordinates[coordinates.index((x, y))] = (x, 7)

# Méthode 2
coordinates[:] = [(x, 7) if y > 7 else (x, y) for x, y in coordinates]

# Méthode 3
for i, (x, y) in enumerate(coordinates):
    if y > 7:
        coordinates[i] = (x, 7)

print(coordinates)
