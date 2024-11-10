from collection import load_data
import pandas as pd
import re

def prepare_data():
    # Prepare dataset we need:

    #1. load dataset
    data = load_data()

    #2. encoding data columns
    data_encoded = encode_cat_cols(data)

    #3. parse the data column
    df = parse_garden_col(data_encoded)

    return df

def encode_cat_cols(data):
    return pd.get_dummies(data, columns=['balcony',
                                        'parking', 
                                        'furnished', 
                                        'garage', 
                                        'storage'], 
                                        drop_first=True)

def parse_garden_col(data):
    
    data['garden'] = data['garden'].apply(lambda x: 0 if x == 'Not present' else int(re.findall(r'\d+', x)[0]))

    return data
