from collection import load_data
import pandas as pd
import re

from loguru import logger

def prepare_data():
    
    logger.info("Starting up proprocessing pipeline")
    # Prepare dataset we need:

    #1. load dataset
    data = load_data()

    #2. encoding data columns
    data_encoded = encode_cat_cols(data)

    #3. parse the data column
    df = parse_garden_col(data_encoded)

    return df

def encode_cat_cols(data):
    
    cols = ['balcony', 'parking', 'furnished', 'garage', 'storage']
    logger.info(f"Encoding categorical columns: {cols}")
    return pd.get_dummies(data, columns = cols, drop_first=True)

def parse_garden_col(data):
    logger.info(f"Parsing garden column")
    data['garden'] = data['garden'].apply(lambda x: 0 if x == 'Not present' else int(re.findall(r'\d+', x)[0]))

    return data
