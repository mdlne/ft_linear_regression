# telecharger pantada
# importer panda, pd = on l'appelle "panda" "pd" dans le reste du code

import pandas as pd
from program1 import read_csv_thetas


def read_csv(file_path):
    # df = data frame = tableau excel
    # fonction read_csv que y'a dans la biblo pandas
    df = pd.read_csv(file_path)
    #   print(df)
    return df


# df = tableau excel si je l'affiche
df = read_csv("data.csv")
# print(df)

# créer une liste avec les km
km_list = []
# print(km_list)

for number in df["km"]:
    km_list.append(number)

# print(km_list)

price_list = []
# print(km_list)


for number in df["price"]:
    price_list.append(number)

# print(price_list)


# fonction qui normalise
def normalize(my_list):
    new_list = []
    min_my_list = min(my_list)
    max_my_list = max(my_list)
    for number in my_list:
        norm_number = (number - min_my_list) / (max_my_list - min_my_list)
        new_list.append(norm_number)
    return new_list, min_my_list, max_my_list


norm_km_list, min_km, max_km = normalize(km_list)
# print(norm_km_list)

norm_price_list, min_price, max_price = normalize(price_list)
# print(norm_price_list)


# fonction qui denormalise
def denormalize(my_list, min, max):
    new_list = []
    for number in my_list:
        denorm_number = number * (max - min) + min
        new_list.append(denorm_number)
    return new_list


denorm_km_list = denormalize(norm_km_list, min_km, max_km)
# print(denorm_km_list)

denorm_price_list = denormalize(norm_price_list, min_price, max_price)
# print(denorm_price_list)


def deriver(theta0, theta1):
    m = len(norm_km_list)
    learning_rate = 0.1

    for _ in range(5000):
        sum_derive_theta0 = 0
        sum_derive_theta1 = 0

        for i in range(m):
            sum_derive_theta0 = (
                sum_derive_theta0
                + theta0
                + theta1 * norm_km_list[i]
                - norm_price_list[i]
            )

        theta0 = theta0 - learning_rate * (1 / m) * sum_derive_theta0

        for i in range(m):
            sum_derive_theta1 = sum_derive_theta1 + norm_km_list[i] * (
                +theta0 + theta1 * norm_km_list[i] - norm_price_list[i]
            )
        theta1 = theta1 - learning_rate * (1 / m) * sum_derive_theta1

    return theta0, theta1


theta0, theta1 = read_csv_thetas("thetas.csv")
theta0, theta1 = deriver(theta0, theta1)

print(theta0, theta1)


# print(derive_theta0, derive_theta1)


# ajouter le degré de confiance, à chaque fois, calculer le degré de confiance dans le calcule

# denormalier
# faire la fonction pour que ça retourne le prix
# nettoyer le programme
# trouver dataset
# ajouter visuel
