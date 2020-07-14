
import pandas as py
import numpy as np
from collections import defaultdict

# function to fillna in the property type column 

def fill_property(df, col_1, col_2):
    """
    Function to fillna in the property type column
    Inputs: 
    df : a pandas dataframe
    col_1 : column with missing values
    col_2 : column to check condition before missing values are filled 
    
    Output:
    df: a pandas dataframe    
    """
    df1 = df[col_1].isnull() 
    df2 = df[df1] 
    for var in df2.index:
        df3 = df[col_1][df[col_2] == df[col_2][var]]
        df[col_1].fillna(df3.value_counts().index[0], inplace=True)
    return df



# Function to fillna in the bathrooms column

def fill_bathrooms(df, col_1, col_2):
    """
    Inputs: 
    df : a pandas dataframe
    col_1 : column with missing values (bathrooms)
    col_2 : column to check condition before missing values are filled 
    
    Output:
    df: a pandas dataframe    
    """
    df1 = df[col_1].isnull()
    df2 = df[df1]
    for var in df2.index:
        if int(df[col_2][var]) <=2:
            df[col_1].fillna(1, inplace=True)
        elif int(df[col_2][var]) <=3:
            df[col_1].fillna(1.5, inplace=True)
        else:
            df[col_1].fillna(2, inplace=True)
    return df


# funtion to fill na's in the bedroom and beds columns

def fill_bedrooms_beds(df, col_1, col_2):
    """
    Inputs: 
    df : a pandas dataframe
    col_1 : column with missing values (bedrooms)
    col_2 : column to check condition before missing values are filled 
    
    Output:
    df: a pandas dataframe    
    """
    df1 = df[col_1].isnull()
    df2 = df[df1]
    for var in df2.index:
        df[col_1].fillna(df[col_2][var], inplace=True)
    return df


# fill the NaN on the zipcode column, using zipcode from the neighbourhood

def fill_zip(df, col_1, col_2):
    """
    Function to fill the NaN on the zipcode using neighbourhood
    Inputs: Arg
    df.. Pandas Dataframe 
    col_1. Column with the missing values
    col_2. Column to check the condition. Neighbourhood
    Return:
    df. Pandas dataframe
    """
    df_null = df[df[col_1].isnull()]
    for var in df_null.index:
        zipcode_by_neighbourhood = df.loc[df
                            [col_2] == df_null[col_2][var], col_1]
        df[col_1][var] = zipcode_by_neighbourhood.values[0]
        
    return df


