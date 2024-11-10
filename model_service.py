# 1. pick up model
#    1.1. if config file exists, load the trained model
#    1.2. if config file does not exist -> train model to get it
# 2. make predictions!

from pathlib import Path
from model import build_model
import pickle as pk

class ModelService:
    def __init__(self):
        self.model = None

    def load_model(self, model_name = "rf_v1"):
        model_path = Path(f"models/{model_name}")
        print(model_path)

        if not model_path.exists():
            build_model()

        self.model = pk.load(open(f"models/{model_name}", "rb"))

    def predict(self, input_parameters):
        return self.model.predict([input_parameters])
    
