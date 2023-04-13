### IMPORTS
import pandas as pd 
import env
import os
SQL_query='Select * from passengers'
directory='/Users/chellyannmoreno/codeup-data-science/Methodologies I/'
filename="NAME.csv"


### FUNCTIONS
def new_titanic_data(SQL_query):
    '''This funcion will:
    -take in a SQL Query
    - create a connect_url to my SQL
    return a df of the given query from the titanic_db'''
    url=get_db_url('titanic_db')
    return pd.read_sql(SQL_query,url)
    
def get_titanic_data(SQL_query, directory, filename="titanic.csv"):
    '''This function will:
    -Check local directory csv file
      -return if exists
    If csv doesn't exists:
     create a df of the SQL_query
     -write df to csv
     -output titanic df
    '''
    if os.path.exists(directory+filename):
        df=pd.read_csv(filename)
        return df
    else:
        df=new_titanic_data(SQL_query)
        df.to_csv(filename)
    return df
    
