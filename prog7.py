# Ecrivez un programme qui demande à l'utilisateur d'entrer
# - t: sa taille en m (convertir t en nombre réel)
# - m: sa masse en kg (convertir m en nombre réel)

# Le programme devra ensuite calculer et afficher l'indice de masse corporelle et l'afficher:
# - IMC = m / t²

# Si IMC est:
# - inférieur à 16,5: le programme devra afficher le message: "dénutrition"
# - compris entre 16,5 et 18,5: "maigreur"
# -         entre 18,5 et 25: "masse normale"
# -         entre 25 et 30: "surpoids"
# - supérieur à 30: "obésité"

def calculer_imc(t, m):
    return m / t ** 2

# Programme principal

t = float(input("Quelle est votre taille en m ? "))
m = float(input("Quel est votre poids en kg ? "))

imc = calculer_imc(t, m)

if imc < 16.5:
    print("Dénutrition")
elif imc <= 18.5:
    print("Migrité")
elif imc <= 25:
    print("Masse normale")
elif imc <= 30:
    print("Surpoids")
else:
    print("Obésité")
