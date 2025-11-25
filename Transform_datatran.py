import pandas as pd
import numpy as np

import glob

datatran_csvs = glob.glob("medallion/bronze/datatran*.csv")


def transform_datatran():
    df_datatran = pd.concat((pd.read_csv(datatran, sep=';', encoding="latin1", index_col="id") for datatran in datatran_csvs), ignore_index=True)
    df_datatran.info()


    df_datatran["km"] = df_datatran["km"].str.replace(",", ".").astype(np.float64)
    df_datatran["latitude"] = df_datatran["latitude"].str.replace(",", ".").astype(np.float64)
    df_datatran["longitude"] = df_datatran["longitude"].str.replace(",", ".").astype(np.float64)
    df_datatran.info()

    df_datatran["data_inversa"] = pd.to_datetime(df_datatran["data_inversa"])
    df_datatran = df_datatran.rename(columns={"data_inversa": "data"})

    df_datatran = df_datatran.rename(columns={"horario": "hora"})
    df_datatran.info()

    print(df_datatran.isna().sum())
    df_datatran["classificacao_acidente"] = df_datatran["classificacao_acidente"].fillna("Não Informado")

    df_datatran["regional"] = df_datatran["regional"].fillna("Não Informado")
    df_datatran["delegacia"] = df_datatran["delegacia"].fillna("Não Informado")
    df_datatran["uop"] = df_datatran["uop"].fillna("Não Informado")
    print(df_datatran.isna().sum())


    df_datatran.to_csv("medallion/silver/datatran.csv", index=False)



if __name__ == '__main__':
    transform_datatran()
