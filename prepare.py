mport pandas as pd
import numpy as np
import os

from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split

from acquire import get_telco_data




def prep_telco(df):
    '''
    This function takes in a dataframe created from acquiring the telco dataset.
    It drops unnecessary, unhelpful, or duplicated columns, such as 'customer_id', 
    as well as columns that will be encoded, such as 'contract_type', 
    'internet_service_type', and 'payment_type'.  It creates dummy columns that encode 
    'object' type data into numeric values that can be more easily evaluated through 
    the exploration process. It then adds the encoded columns to the dataframe. 
    The function returns the updated dataframe.
    '''
    columns_to_drop = ['payment_type_id', 'internet_service_type_id', 'contract_type_id', 'customer_id']                   
    df = df.drop(columns = columns_to_drop)
    dummy_df = pd.get_dummies(df[['contract_type', 'internet_service_type', 'payment_type']],
                          dummy_na=False,
                         drop_first = [True, True, True])
    df = pd.concat([df, dummy_df], axis=1)
    return df




def summerize_df(df):
    '''
    This function takes in a dataframe and summarizes the data in preparation for cleaning. 
    It uses .shape() to provide the number of rows and columns; .info() which in includes the 
    index as well as the Series names, null values, and datatypes; .describe() which provides 
    the summary statistics. It then provide a new dataframe, replacing empty spaces with NaN values, 
    then gets a count of the NaN values for each Sereis. 
    '''  
    print('-----shape------')
    print('{} rows and {} columns'.format(df.shape[0], df.shape[1]))
    print('---info---')
    print(df.info())
    print(df.describe())
    print('--nulls--')
    df = df.replace(r'^\s*$', np.NaN, regex=True)
    print(df.isna().sum())



    
def train_validate_test_split(df, seed=123):
     '''
    This function splits a dataframe into train, validate, and test 
    in order to create and validate models. It takes in a dataframe 
    and contains an integer for a setting a seed.  The name of the target 
    variable (for stratification purposes), is included inside the function. 
    Test is 20% of the original dataset. The remaining 80% of the dataset is 
    divided between valiidate and train, with validate being .30*.80= 24% of 
    the original dataset, and train being .70*.80= 56% of the original dataset. 
    The function returns, train, validate and test dataframes. 
    '''
    train_validate, test = train_test_split(df, test_size=0.2,
        random_state=19, stratify=df.churn)
    train, validate = train_test_split(train_validate, test_size=0.25,
        random_state=19, stratify=train_validate.churn)

    return train, validate, test
    train_validate, test = train_test_split(df, test_size=0.2, 
                                            random_state=seed, 
                                            stratify=df[target])
    train, validate = train_test_split(train_validate, test_size=0.3, 
                                       random_state=seed,
                                       stratify=train_validate[target])
    return train, validate, test