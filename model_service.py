# 1. pick up model
#    1.1. if config file exists, load the trained model
#    1.2. if config file does not exist -> train model to get it
# 2. make predictions!
from pathlib import Path
from model import build_model
import pickle as pk
from config import settings
from loguru import logger

class ModelService:
    def __init__(self):
        self.model = None

    def load_model(self):
        
        logger.info(f"checking the existance of model config file at {settings.model_path}/{settings.model_name}")
        model_path = Path(f"{settings.model_path}/{settings.model_name}")
        print(model_path)

        if not model_path.exists():
            logger.warning(f"model at {settings.model_path}/{settings.model_name} was not found -> building {settings.model_name}")
            build_model()
            
        logger.info(f"model {settings.model_name} exist! -> loading model configuration file")
        self.model = pk.load(open(f"{settings.model_path}/{settings.model_name}", "rb"))

    def predict(self, input_parameters):
        
        logger.info(f"making prediction")
        return self.model.predict([input_parameters])
    
