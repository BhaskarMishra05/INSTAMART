import os
import sys
import pandas as pd
import yaml
from src.logger import logging
from src.exception import CustoamException
from src.utilities import engin_creator

def data_imputation(df, engine, table_name):
    for chunk in df:
        chunk.to_sql(table_name, engine, if_exists='append', index=False)

if __name__ == '__main__':
    for file in os.listdir('./Files/Database_Inhibitor'):
        if '.csv' in file:
            df = pd.read_csv('./Files/Database_Inhibitor/'+file, chunksize=50000)
            data_imputation(df, engine= engin_creator(), table_name=file[:-4])
