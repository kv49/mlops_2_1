#!/usr/bin/python3

import sys
import os
import yaml
import pickle

import pandas as pd
from sklearn.neighbors import  KNeighborsClassifier # Классификация К-Ближайших соседей от scikit-learn

if len(sys.argv) != 3:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write("\tpython dt.py data-file model \n")
    sys.exit(1)

f_input = sys.argv[1]
f_output = os.path.join("models", sys.argv[2])
os.makedirs(os.path.join("models"), exist_ok=True)

params = yaml.safe_load(open("params.yaml"))["train"]
p_seed = params["seed"]
p_weights = params["weights"]
p_neighbours = params["neighbours"]

df_train = pd.read_csv(f_input, delimiter = ',')
X_train, y_train = df_train.drop(columns = ['Transmission']).values, df_train['Transmission'].values

# создаем объект класса с указанием гиперпараметров
kNN = KNeighborsClassifier(n_neighbors = p_neighbours, weights = p_weights)

# обучаем на тренировочных данных
kNN.fit(X_train, y_train)

with open(f_output, "wb") as fd:
    pickle.dump(kNN, fd)

