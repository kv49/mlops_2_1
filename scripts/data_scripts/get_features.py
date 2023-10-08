#!/usr/bin/python3

import sys
import os
import pandas as pd


def add_columns(p_df):
    p_df['Age'] = 2022 - p_df.Year # новый столбец как Константа минус старый
    p_df['km_year'] = p_df.Distance/p_df.Age # делим один столбец на другой
    return p_df


if len(sys.argv) != 2:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write("\tpython3 get_features.py data-file\n")
    sys.exit(1)

f_input = sys.argv[1]
f_output = os.path.join("data", "stage2", "cars.csv")
os.makedirs(os.path.join("data", "stage2"), exist_ok=True)

df = pd.read_csv(f_input, delimiter = ',')


add_columns(df)

# преобразование бинарного признака
df['Transmission'] = df['Transmission'].map({'Automatic': 1, 'Manual': 0})# в данном случае задаем словарь
# где key (ключ) - исходное значение, value (значение) - на что конкретный ключ будет заменен

columns_to_drop = ['Year', 'Make', 'Style', 'Model', 'Fuel_type']
df.drop(columns=columns_to_drop, inplace = True)


df.to_csv(f_output, sep = ',', index=False)
