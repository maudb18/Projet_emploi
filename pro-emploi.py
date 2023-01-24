import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta
import re


names = ['Intitulé_du_poste', 'Date_de_publication',
         'lieu', 'competences', 'Type_de_poste']

fn_data = 'data.json'

df = pd.read_json(fn_data, encoding='utf8')
df.to_csv("data.csv", index=False)

print(df.head())


# Suppression des caracteres "\n"

df['Intitulé du poste'] = df['Intitulé du poste'].apply(
    lambda x: ''.join(map(str, x)).replace("\n", ""))
df['Intitulé du poste']

# Ne garder que les titres des postes

# extraction des caracteres necessaires dans la colonne date de publication
df['Date de publication'] = df['Date de publication'].apply(
    lambda x: x.replace("\n", "").replace("postée il y a", ""))
df['Date de publication']

# Suppression des caracteres "\n"
df['lieu'] = df['lieu'].apply(lambda x: ''.join(map(str, x)).replace("\n", ""))
df['lieu']

# Suppression des caracteres "\n"
df['competences'] = df['competences'].apply(
    lambda x: ''.join(map(str, x)).replace("\n", " "))

df['competences']


# Suppression des caracteres "\n"
df['Type de poste'] = df['Type de poste'].apply(
    lambda x: ''.join(map(str, x)).replace("\n", " "))

df['Type de poste']

# extarction de la string et mettre dans colonne "duree"
df["duree"] = df["Date de publication"].str.extract(r'(\d+)(\D+)')[1]
df['duree']

# extarction de la string et mettre dans colonne "nb_jour"
df['nb_jour'] = df['Date de publication'].str.extract(
    r'(\d+)').fillna(1).astype(int)


# -----------------------------------------------------------------------------
# teste de recuperer une valeur dans une colonne et appliquer une apoeration sur lautre
# ------------------------------------------------------------------------------


df['nb_jour_final'] = df.apply(lambda x: x['nb_jour'] * 31 if x['duree'] == 'mois' else 0 if x['duree']
                               == 'heures' else 1 if pd.isna(x['duree']) else x['nb_jour'], axis=1)
df.head(40)
# Définir la date de référence
datetime_str = '15/01/2023'

datetime_object = datetime.strptime(datetime_str, '%d/%m/%Y')
# Transformer les valeurs de la colonne 1 en liste
col1_list = df['duree'].tolist()

# Transformer les valeurs de la colonne 2 en liste
col2_list = df['nb_jour'].tolist()
print(col2_list)
print(col1_list)

nb_jour_final = []

# Itérer simultanément sur les deux listes
for value1, value2 in zip(col1_list, col2_list):
    if value1 == 'jours':
        continue
    elif value1 == 'mois':
        value2 = value2 * 31
    elif value1 == 'heures':
        value2 = 0
    elif value1 == 'nan':
        value2 = 1

    nb_jour_final.append(value2)


df['nb_jour_final'] = pd.DataFrame(nb_jour_final)

print(df)
