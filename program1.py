# Fonction qui donne le prix de la voiture en fonction du kilométrage

import csv


def estimate_p(a, b):
    km = int(input("Comment de kilométrage a votre voiture ?"))
    price = a * km + b
    print(price)
    return price


def read_csv_thetas(csv_file_name):
    # Ouvrir le fichier CSV
    with open(csv_file_name, newline="", encoding="utf-8") as fichier_csv:
        lecteur = csv.reader(fichier_csv)

        # Lire la première ligne comme en-têtes
        # next = il passe à la ligne suivante
        header = next(lecteur)

        # Create new CSV

        # Lire les lignes suivantes numero de la ligne[numéro de la colonne]
        for ligne in lecteur:
            theta0 = int(ligne[0])
            theta1 = int(ligne[1])
            return (theta0, theta1)


# theta0, theta1 = read_csv_thetas("thetas.csv")
# estimate_p(theta1, theta0)
