import pandas as pd
import numpy as np
import sqlite3



def load_datatran():
    df_acidentes = pd.read_csv("medallion/silver/datatran.csv")

    con_acidentes = sqlite3.connect("medallion/gold/datatran.sqlite")

    df_acidentes.to_sql("datatran", con_acidentes, if_exists="replace", index=False)

    con_acidentes.close()



if __name__ == '__main__':
    load_datatran()
