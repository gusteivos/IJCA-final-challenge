import pandas as pd
import numpy as np
import sqlite3



def load_datatran():
    df_datatran = pd.read_csv("medallion/silver/datatran.csv")

    con_datatran = sqlite3.connect("medallion/gold/datatran.sqlite")

    df_datatran.to_sql("datatran", con_datatran, if_exists="replace", index=False)

    con_datatran.close()



if __name__ == '__main__':
    load_datatran()
