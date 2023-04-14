#Imports'
import pandas as pd
import numpy as np
import env
import acquire as acq
from sklearn.model_selection import train_test_split
#FUNCTIONS
def prep_iris(df):
    df=df.drop(columns=['measurement_id','species_id'])
    df=df.rename(columns={'species_name':'species'})
    dum_species=pd.get_dummies(df.species)
    df=pd.concat([df,dum_species], axis=1)
    return df

def prep_titanic(df):
    df=df.drop(columns=['class','embarked','alone','deck'])
    df.embark_town = df.embark_town.fillna(value='Southampton')
    titanic_dum=pd.get_dummies(df[['sex','embark_town']], drop_first=True)
    df=pd.concat([df,titanic_dum],axis=1)
    return df

def prep_telco(df):
    df=df.drop(columns=['partner','dependents','internet_service_type_id','multiple_lines',
                    'online_backup','payment_type_id'])
    telco_dummies=pd.get_dummies(df[['gender','phone_service','online_security','device_protection','tech_support','streaming_tv','churn']],drop_first=True)
    df=pd.concat([df,telco_dummies],axis=1)
    return df





def split_data(df):
  
    train, test= train_test_split(df,
                                   test_size=.2, 
                                   random_state=123, 
                                   )
    train, validate = train_test_split(train,
                                       test_size=.25, 
                                       random_state=123, 
                                       )
    return train, validate, test