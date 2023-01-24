import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


fn_data = 'data.json'

df = pd.read_json(fn_data)

print(df)

print(df.isnull().sum())
print(df.isna().sum())
