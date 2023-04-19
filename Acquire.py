### IMPORTS
import pandas as pd
import os
import env
directory='/Users/chellyannmoreno/codeup-data-science/Methodologies I/'

### FUNCTIONS
def get_db_url(database):
  return f'mysql+pymysql://{env.username}:{env.password}@{env.host}/{database}'



def titanic_data():
    '''This funcion will:
    -take in a SQL Query
    - create a connect_url to my SQL
    return a df of the given query from the titanic_db'''
    url=get_db_url('titanic_db')
    SQL_query='Select * from passengers'
    filename='titanic.csv'
    return pd.read_sql(SQL_query,url)
    
    
def get_titanic_data():
    SQL_query= 'Select * from passengers'
    filename='titanic.csv'
    url=get_db_url('titanic_db')
    if os.path.exists(directory+filename): 
        df = pd.read_csv(filename)
        return df
    else:
        df = new_titanic_data(SQL_query)

        df.to_csv(filename)
        return df
    

## IRIS DATA
def new_iris_data(SQL_query):
  
    url = get_db_url('iris_db')
    
    return pd.read_sql(SQL_query, url)

def get_iris_data():
    SQL_query="SELECT * FROM iris_db.species left join iris_db.measurements using (species_id);"
    url=get_db_url('iris.db')
    filename = 'iris.csv'
    if os.path.exists(directory+filename): 
        df = pd.read_csv(filename)
        return df
    else:
        df = new_iris_data(SQL_query)

        df.to_csv(filename)
        return df
    
### GET TELCO 
def new_telco_data(SQL_query):
    """
    This function will:
    - take in a SQL_query
    - create a connection_url to mySQL
    - return a df of the given query from the telco_db
    """
    url = get_db_url('telco_churn')
    
    return pd.read_sql(SQL_query, url)



def get_telco_data():
   SQL_query="""SELECT * FROM telco_churn.customers
            left join telco_churn.payment_types using (payment_type_id)
            left join telco_churn.internet_service_types using (internet_service_type_id)
            left join telco_churn.contract_types using (contract_type_id);"""
   url = get_db_url('telco_churn')
   filename='telco.csv'
   if os.path.exists(directory+filename): 
        df = pd.read_csv(filename)
        return df
   else:
        df = new_telco_data(SQL_query)

        df.to_csv(filename)
        return df