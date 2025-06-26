# Fonction qui donne le prix de la voiture en fonction du kilométrage

import csv


def estimate_p(a, b, min_km, max_km, min_price, max_price):
    km = int(input("Comment de kilométrage a votre voiture ?"))
    norm_km = (km - min_km) / (max_km - min_km)
    denom_price = a * norm_km + b
    norm_price = denom_price * (max_price - min_price) + min_price
    # print(f"Votre voiture est estimée au prix de {price}")
    return norm_price


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
            theta0 = float(ligne[0])
            theta1 = float(ligne[1])
            return (theta0, theta1)
