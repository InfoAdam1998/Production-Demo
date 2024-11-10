import pandas as pd

def load_data(path = "C:/Users/steve/Desktop/Notebooks/Production-Code-Conversion/rent_apartments.csv"):
    return pd.read_csv(path)
