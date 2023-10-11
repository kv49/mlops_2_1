#!/usr/bin/python3

import os
import sys
import pickle
import json

import pandas as pd
from sklearn.neighbors import  KNeighborsClassifier # Классификация К-Ближайших соседей от scikit-learn

if len(sys.argv) != 3:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write("\tpython evaluate.py data-file model\n")
    sys.exit(1)

f_input_data = sys.argv[1]
f_input_model = sys.argv[2]

df_test = pd.read_csv(f_input_data, delimiter = ',')
X_test, y_test = df_test.drop(columns = ['Transmission']).values, df_test['Transmission'].values

#kNN = KNeighborsClassifier(n_neighbors = 1, weights = 'distance')
with open(f_input_model, "rb") as fd:
    kNN = pickle.load(fd)

score = kNN.score(X_test, y_test)

prc_file = os.path.join("evaluate", "score.json")
os.makedirs(os.path.join("evaluate"), exist_ok=True)

with open(prc_file, "w") as fd:
    json.dump({"score": score}, fd)
