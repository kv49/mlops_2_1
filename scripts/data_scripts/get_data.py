#!/usr/bin/python3

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/dayekb/Basic_ML_Alg/main/cars.csv', delimiter = ',')
df.to_csv("../../data/raw/cars.csv", sep = ',', index=False)

