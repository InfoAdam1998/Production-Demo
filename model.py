from preperation import prepare_data
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
import pickle as pk

from config import settings
from loguru import logger

def build_model():

    logger.info("starting up model building pipeline")
    #1. load preprocessed dataset
    df = prepare_data()

    #2. identify X and y
    X, y = get_X_y(df)

    #3. split dataset
    X_train, X_test, y_train, y_test = split_train_test(X, y)

    #4. train the model
    rf = train_model(X_train, y_train)

    #5. evaluate the model
    evaluate_model(rf, X_test, y_test)

    #6. save the model in a config file
    save_model(rf)

# Define functions for model building
def get_X_y(data, col_X=['area', 'constraction_year', 'bedrooms', 'garden', 'balcony_yes', 'parking_yes', 'furnished_yes', 'garage_yes', 'storage_yes'], col_y="rent"):
    
    logger.info(f"defining X and Y variables. \nX vars: {col_X}\ny var: {col_y}")
    return data[col_X], data[col_y]

def split_train_test(X, y) :
    
    logger.info("splitting data into train and test sets")
    X_train, X_test, y_train, y_test = train_test_split(X,
                                                         y,
                                                         test_size = 0.2)
    return X_train, X_test, y_train, y_test

def train_model(X_train, y_train):

    logger.info("training a model with hyperparameters")
    grid_space = {'n_estimators': [100, 200, 300], 
                  'max_depth': [3, 6, 9, 12]}
    
    logger.debug(f"grid space {grid_space}")
    grid = GridSearchCV(RandomForestRegressor(), 
                        param_grid=grid_space, 
                        cv=5, scoring = 'r2')
    
    model_grid = grid.fit(X_train, y_train)

    return model_grid.best_estimator_

def evaluate_model(model, X_test, y_test):
    
    logger.info(f"evaluatng model performance. SCORE: {model.score(X_test, y_test)}")
    return model.score(X_test, y_test)
    
def save_model(model):
    
    logger.info(f"saving a model to a directory {settings.model_path}/{settings.model_name}")
    pk.dump(model, open(f"{settings.model_path}/{settings.model_name}", "wb"))