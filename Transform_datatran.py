import pandas as pd
import numpy as np



df_datatran = pd.read_csv("medallion/bronze/datatran2025.csv", sep=';', encoding="latin1", index_col="id")
df_datatran.info()


df_datatran["km"] = df_datatran["km"].str.replace(",", ".").astype(np.float64)

df_datatran["latitude"] = df_datatran["latitude"].str.replace(",", ".").astype(np.float64)
df_datatran["longitude"] = df_datatran["longitude"].str.replace(",", ".").astype(np.float64)
df_datatran.info()


df_datatran["data_inversa"] = pd.to_datetime(df_datatran["data_inversa"])
df_datatran = df_datatran.rename(columns={"data_inversa": "data"})

df_datatran = df_datatran.rename(columns={"horario": "hora"})
df_datatran.info()


df_datatran.to_csv("medallion/silver/datatran.csv", index=False)
