import pandas as pd 

def load_dw_retail(dimension,conn,df):
    try:
        df.to_sql(dimension,conn,if_exists='append', index= False)   #el index=false para que los indices de los df no se cargen a la DB
    except Exception as e:
        print(e)