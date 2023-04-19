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
    df=df.drop(columns=['internet_service_type_id', 'contract_type_id', 'payment_type_id'])
    df['gender_encoded'] = df.gender.map({'Female': 1, 'Male': 0})
    df['partner_encoded'] = df.partner.map({'Yes': 1, 'No': 0})
    df['dependents_encoded'] = df.dependents.map({'Yes': 1, 'No': 0})
    df['phone_service_encoded'] = df.phone_service.map({'Yes': 1, 'No': 0})
    df['paperless_billing_encoded'] = df.paperless_billing.map({'Yes': 1, 'No': 0})
    df['churn_encoded'] = df.churn.map({'Yes': 1, 'No': 0})
    
    
    dummy_df = pd.get_dummies(df[['multiple_lines', 'online_security', 'online_backup','device_protection',  'tech_support', 'streaming_tv', 'streaming_movies', 'contract_type',  'internet_service_type','payment_type']],
                                  drop_first=True)
    
    df = pd.concat( [df,dummy_df], axis=1 )
    
    df.total_charges = df.total_charges.str.replace(' ', '0').astype(float)
    
    return df





def split_data(df,variable):
    train, test = train_test_split(df,
                                   random_state=123, test_size=.20, stratify= df[variable])
    train, validate = train_test_split(train, random_state=123, test_size=.25, stratify= train[variable])
    return train, validate, test


    