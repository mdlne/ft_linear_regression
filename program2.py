# telecharger pantada
# importer panda, pd = on l'appelle "panda" "pd" dans le reste du code

import pandas as pd
from program1 import read_csv_thetas
from program1 import estimate_p


def read_csv(file_path):
    # df = data frame = tableau excel
    # fonction read_csv que y'a dans la biblo pandas
    df = pd.read_csv(file_path)
    #   print(df)
    return df


# fonction qui normalise
def normalize(my_list):
    new_list = []
    # new list = liste denormalisée
    min_my_list = min(my_list)
    max_my_list = max(my_list)
    for number in my_list:
        norm_number = (number - min_my_list) / (max_my_list - min_my_list)
        new_list.append(norm_number)
    return new_list, min_my_list, max_my_list


# fonction qui denormalise
def denormalize(my_list, min, max):
    new_list = []
    for number in my_list:
        denorm_number = number * (max - min) + min
        new_list.append(denorm_number)
    return new_list


def deriver(theta0, theta1, norm_km_list, norm_price_list):
    m = len(norm_km_list)
    learning_rate = 0.1

    for _ in range(5000):
        sum_derive_theta0 = 0
        sum_derive_theta1 = 0

        for i in range(m):
            sum_derive_theta0 = (
                sum_derive_theta0
                + theta1 * norm_km_list[i]
                + theta0
                - norm_price_list[i]
            )

        for i in range(m):
            sum_derive_theta1 = sum_derive_theta1 + norm_km_list[i] * (
                theta1 * norm_km_list[i] + theta0 - norm_price_list[i]
            )
        # passer à theta1+1 et theta0+1 avec le learning rate
        theta1 = theta1 - learning_rate * (1 / m) * sum_derive_theta1
        theta0 = theta0 - learning_rate * (1 / m) * sum_derive_theta0
        print(f"-----Iteration {_}------")
        print(f"Theta0: {theta0}")
        print(f"Theta1: {theta1}")

    return theta0, theta1


def write_csv_theta(filename, new_theta0, new_theta1):
    with open(filename, "w") as file:
        file.write("theta0,theta1\n")
        file.write(f"{new_theta0},{new_theta1}")


# EXECUTION

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


norm_km_list, min_km, max_km = normalize(km_list)
# print(norm_km_list)

norm_price_list, min_price, max_price = normalize(price_list)
# print(norm_price_list)


theta0, theta1 = read_csv_thetas("thetas.csv")
new_theta0, new_theta1 = deriver(theta0, theta1, norm_km_list, norm_price_list)

denorm_theta1 = new_theta1 * (max_price - min_price) / (max_km - min_km)
denorm_theta0 = (
    min_price + new_theta0 * (max_price - min_price) - denorm_theta1 * min_km
)


denorm_km_list = denormalize(norm_km_list, min_km, max_km)
# print(denorm_km_list)

denorm_price_list = denormalize(norm_price_list, min_price, max_price)
# print(denorm_price_list)

write_csv_theta("thetas.csv", denorm_theta0, denorm_theta1)

print(estimate_p(denorm_theta0, denorm_theta1))


# ajouter visuel
