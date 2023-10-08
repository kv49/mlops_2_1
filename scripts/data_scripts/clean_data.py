#!/usr/bin/python3

import sys
import os
import pandas as pd

if len(sys.argv) != 2:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write("\tpython3 clean_data.py data-file\n")
    sys.exit(1)

f_input = sys.argv[1]
f_output = os.path.join("data", "stage1", "cars.csv")
os.makedirs(os.path.join("data", "stage1"), exist_ok=True)

#df = pd.read_csv("../../data/raw/cars.csv", delimiter = ',')
df = pd.read_csv(f_input, delimiter = ',')


DF = df.drop_duplicates() # Складываем в новый датафрейм результат удаления дубликатов
# обновим индексы в датафрейме DF. если бы мы прописали drop = False, то была бы еще одна колонка - старые индексы
DF = DF.reset_index(drop=True)
df = DF

# Удалим те объекты у которых Расстояние равно 0
question_dist = df[df.Distance == 0] # через логическое индексирование определяем проблемные данные
df = df.drop(question_dist.index) # удаляем данные по проблемным индексам

# здравый смысл
question_dist = df[(df.Year <2021) & (df.Distance < 1100)]
df = df.drop(question_dist.index)

# анализ гистограмм
question_dist = df[(df.Distance > 1e6)]
df = df.drop(question_dist.index)

# здравый смысл
question_engine = df[df["Engine_capacity(cm3)"] < 200]
df = df.drop(question_engine.index)

# здравый смысл
question_engine = df[df["Engine_capacity(cm3)"] > 5000]
df = df.drop(question_engine.index)

# здравый смысл
question_price = df[(df["Price(euro)"] < 101)]
df = df.drop(question_price.index)

# анализ гистограмм
question_price = df[df["Price(euro)"] > 1e5]
df = df.drop(question_price.index)

#анализ гистограмм
question_year = df[df.Year < 1971]
df = df.drop(question_year.index)

#удалим дополнительно еще некоторые очень высокие значения
question_km_year = df[df.Distance/(2022 - df.Year) > 50e3]
df = df.drop(question_km_year.index)

#удалим дополнительно еще некоторые очень низкие значения
question_km_year = df[df.Distance/(2022 - df.Year) < 100]
df = df.drop(question_km_year.index)

# обновим индексы в датафрейме DF. если бы мы прописали drop = False, то была бы еще одна колонка - старые индексы
df = df.reset_index(drop=True)


df.to_csv(f_output, sep = ',', index=False)
