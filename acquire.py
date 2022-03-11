import pandas as pd
import numpy as np
import env 
import os
from pydataset import data
import os


def get_telco_data(use_cache=True):
    '''
    This function acquires the telco_churn database in SQL. The function requires the
    use of a personalized .env file that contains the user, password, and host credentials.
    It joins 4 tables together; the customers table, contract_types table, 
    internet_service_types table, and payment_types table. 
    It returns a dataframe and caches the dataframe 
    (saving it to a .csv file, titled: 'telco_churn.csv'), 
    for faster processing after initial acquisition. The resulting dataframe 
    contains all the contract, payment, and internet service options. 
    '''
    
    filename = 'telco_churn.csv'
    
    if os.path.exists(filename):
        print('Reading from csv file...')
        return pd.read_csv(filename)
    
    
    url = f'mysql+pymysql://{env.user}:{env.password}@{env.host}/telco_churn'
    query = '''
    SELECT * 
        FROM customers
        JOIN contract_types 
        USING (contract_type_id)
        JOIN internet_service_types
        USING (internet_service_type_id)
        JOIN payment_types AS pt
        USING (payment_type_id)    
    '''

    print('Getting a fresh copy from SQL database...')
    df = pd.read_sql(query, url)
    print('Saving to csv...')
    df.to_csv(filename, index=False)
    return df










# Acquire & Prepare Modules (.py)

##contains functions to acquire, prepare and split your data. You can have other .py files if you desire to abstract other code away from your final report.

#Your work must be reproducible by someone with their own env.py file.

#Each of your functions are complimented with docstrings. If they are functions you borrowed from instructors, put those docstrings in your own words.

#Functions to acquire and prepare your data should be imported and used in your final report.