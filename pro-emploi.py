#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 14:34:30 2023

@author: greta
"""

import pandas as pd
df = pd.read_json('/home/greta/Téléchargements/data.json')

#print(df)

#print(df.isna().sum())


# new df from the column of lists
split_df = pd.DataFrame(df['lieu'].tolist(), columns=['location', 'salaire'])
# add new cols to df
df = pd.concat([df, split_df], axis=1)

print(df.head())

#print(df['salaire'].iloc[5])

df[['salaire_min', 'salaire_max']] = df.salaire.str.split(" - ", expand = True)

# to be stripped
#please work this time


#df['salaire_max'] = df[salaire_max'].strip("/ an")

print(df.dtypes)

#print(df.isna().sum())

#print(df['Intitulé du poste'].iloc[1][0])

'''
df['Intitulé'] = df['Intitulé du poste'].apply(df['Intitulé du poste'].iloc[1][0])
print(df.head())
'''



