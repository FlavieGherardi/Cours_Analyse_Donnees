#coding:utf8

import pandas as pd
import matplotlib.pyplot as plt

# Source des données : https://www.data.gouv.fr/datasets/election-presidentielle-des-10-et-24-avril-2022-resultats-definitifs-du-1er-tour/
with open("./data/resultats-elections-presidentielles-2022-1er-tour.csv","r") as fichier:
    contenu = pd.read_csv(fichier)

# Mettre dans un commentaire le numéro de la question
# Question 1
# ...
data = pd.DataFrame(contenu)
#print(data)

# Question 2
nombre_lignes = len(contenu)
print('Le nombre de ligne est égal à ', nombre_lignes)


# a = [[1, 2, 4], [2, 4, 8], [3, 5, 8]]
# ligne1 = a[0]
# b = [[1, 2], 2, 3, 4, 'bcxvkbdfkvbfd']
# print(len(ligne1))

# #nombre de lignes
# print(len(a))

# #nombre de colonnes
# print(len(a[0]))

#Ce commentaire est un test