import pandas as pd
import numpy as np



df_acidentes = pd.read_csv("medallion/bronze/acidentes2025.csv", sep=';', encoding="latin1", index_col="id")
df_acidentes.info()


df_acidentes["km"] = df_acidentes["km"].str.replace(",", ".").astype(np.float64)
df_acidentes["latitude"] = df_acidentes["latitude"].str.replace(",", ".").astype(np.float64)
df_acidentes["longitude"] = df_acidentes["longitude"].str.replace(",", ".").astype(np.float64)
df_acidentes.info()

df_acidentes["data_inversa"] = pd.to_datetime(df_acidentes["data_inversa"])
df_acidentes = df_acidentes.rename(columns={"data_inversa": "data"})

df_acidentes = df_acidentes.rename(columns={"horario": "hora"})
df_acidentes.info()


df_acidentes.to_csv("medallion/silver/acidentes.csv", index=False)
