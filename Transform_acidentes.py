import pandas as pd
import numpy as np

import glob

acidentes_csvs = glob.glob("medallion/bronze/acidentes*.csv")


def transform_acidentes():
    df_acidentes = pd.concat((pd.read_csv(acidentes, sep=';', encoding="latin1", index_col="id") for acidentes in acidentes_csvs), ignore_index=True)
    df_acidentes.info()


    df_acidentes["km"] = df_acidentes["km"].str.replace(",", ".").astype(np.float64)
    df_acidentes["latitude"] = df_acidentes["latitude"].str.replace(",", ".").astype(np.float64)
    df_acidentes["longitude"] = df_acidentes["longitude"].str.replace(",", ".").astype(np.float64)
    df_acidentes.info()

    df_acidentes["data_inversa"] = pd.to_datetime(df_acidentes["data_inversa"])
    df_acidentes = df_acidentes.rename(columns={"data_inversa": "data"})

    df_acidentes = df_acidentes.rename(columns={"horario": "hora"})
    df_acidentes.info()

    print(df_acidentes.isna().sum())
    df_acidentes["classificacao_acidente"] = df_acidentes["classificacao_acidente"].fillna("Não Informado")

    df_acidentes["tipo_veiculo"] = df_acidentes["tipo_veiculo"].fillna("Não Informado")

    df_acidentes["tipo_envolvido"] = df_acidentes["tipo_envolvido"].fillna("Não Informado")
    df_acidentes["estado_fisico"] = df_acidentes["estado_fisico"].fillna("Não Informado")

    df_acidentes["sexo"] = df_acidentes["sexo"].fillna("Não Informado")

    df_acidentes["regional"] = df_acidentes["regional"].fillna("Não Informado")
    df_acidentes["delegacia"] = df_acidentes["delegacia"].fillna("Não Informado")
    df_acidentes["uop"] = df_acidentes["uop"].fillna("Não Informado")
    print(df_acidentes.isna().sum())
    df_acidentes.to_csv("medallion/silver/acidentes.csv", index=False)



if __name__ == '__main__':
    transform_acidentes()
