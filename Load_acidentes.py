import pandas as pd
import numpy as np
import sqlite3



def load_acidentes():
    df_acidentes = pd.read_csv("medallion/silver/acidentes.csv")

    con_acidentes = sqlite3.connect("medallion/gold/acidentes.sqlite")

    df_acidentes.to_sql("acidentes", con_acidentes, if_exists="replace", index=False)

    con_acidentes.close()



if __name__ == '__main__':
    load_acidentes()
