#!/usr/bin/python3

import yaml
import sys
import os

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

params = yaml.safe_load(open("params.yaml"))["split"]

if len(sys.argv) != 2:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write("\tpython3 train_test_split.py data-file\n")
    sys.exit(1)

f_input = sys.argv[1]
f_output_train = os.path.join("data", "stage3", "train.csv")
os.makedirs(os.path.join("data", "stage3"), exist_ok=True)
f_output_test = os.path.join("data", "stage3", "test.csv")
os.makedirs(os.path.join("data", "stage3"), exist_ok=True)

p_split_ratio = params["split_ratio"]
p_seed = params["seed"]

df = pd.read_csv(f_input, delimiter = ',')
df_train, df_test = train_test_split(df, test_size = p_split_ratio, random_state = p_seed)

num_columns = ['Distance', 'Engine_capacity(cm3)','Price(euro)', 'Age', 'km_year']
# нормализуем
scaler = MinMaxScaler()
#scaler.fit(df_train[num_columns])
df_train[num_columns] = scaler.fit_transform(df_train[num_columns]) # для тренировочных "обучаем" и трансформируем
df_test[num_columns] = scaler.transform(df_test[num_columns]) # для тестовой трансформируем обученым скейлером

df_train.to_csv(f_output_train, sep = ',', index=False)
df_test.to_csv(f_output_test, sep = ',', index=False)

