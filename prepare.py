import pandas as pd
import numpy as np
import os

from sklearn.model_selection import train_test_split

import warnings
warnings.filterwarnings("ignore")

from acquire import get_telco_data



def clean_telco_data(df):
    ''' 
    This function takes in the telco data and cleans it
    '''

    # change dtype in column from string so it can be used
    df['total_charges'] = df.total_charges.replace(' ', np.nan).astype(float)
    
    # reassigning dataframe and dropping the null values from 'total_charges' column
    df = df[df.tenure != 0]

    #rename column names for clarity
    df = df.rename(columns ={'gender': 'is_male', 'senior_citizen': 'is_senior', 'tenure': 'tenure_months',
                                   'partner': 'has_partner', 'dependents': 'has_dependents',
                                    'phone_service': 'has_phone_service','multiple_lines': 'has_multiple_lines', 
                                    'online_security': 'has_online_security', 'online_backup': 'has_online_backup' , 
                                    'device_protection': 'has_device_protection', 'tech_support': 'has_tech_support',
                                   'streaming_tv': 'has_streaming_tv', 'streaming_movies': 'has_streaming_movies', 
                                   'paperless_billing': 'has_paperless_billing', 'churn': 'did_churn'})
    
    
    columns = ['is_male',
               'has_partner',
               'has_dependents',
               'has_phone_service',
               'has_multiple_lines',
               'has_online_security',
               'has_online_backup',
               'has_device_protection',
               'has_tech_support',
               'has_streaming_tv',
               'has_streaming_movies',
               'has_paperless_billing',
               'did_churn',
               'contract_type',
               'internet_service_type',
               'payment_type'
              ]
    # get dummies for columns that have two values (yes,no) or gender, and dropping first
    dummy_df = pd.get_dummies(df[columns], drop_first = True)

    
    # combine df and dummy_df that I created
    df = pd.concat([df, dummy_df], axis =1)

    # dropping columns that are now duplicates, from the dummies created, or not needed
    df = df.drop(columns = columns)
    df = df.drop(columns = ['payment_type_id', 'internet_service_type_id', 'contract_type_id'])

    
    
    return df     





def data_split(df, random_state=123):
    '''
    This function splits a dataframe into train, validate, and test 
    in order to create and validate models. It takes in a dataframe. The  
    target variable (for stratification purposes) is set within the function, 
    and contains an integer for setting a seed for replication. 
    Test is 20% of the original dataset. The remaining 80% of the dataset is 
    divided between valiidate and train, with validate being .30*.80= 24% of 
    the original dataset, and train being .70*.80= 56% of the original dataset. 
    The function returns, train, validate and test dataframes. 
    '''
    
     
    train, test = train_test_split(df, test_size = .2, random_state=123, stratify=df.did_churn_Yes)
    
   
    train, validate = train_test_split(train, test_size=.3, random_state=123, stratify=train.did_churn_Yes)


    print(f'train -> {train.shape}')
    print(f'validate -> {validate.shape}')
    print(f'test -> {test.shape}')
    
    # results in 3 dataframes
    return train, validate, test



    
