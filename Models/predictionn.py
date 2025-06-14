import pickle
import pandas as pd
import sklearn

# print(sklearn.__version__)

# model_loaded = None   
with open("Models/model.pkl", 'rb') as f:
    try:
        # print("HElllooo I am tryyyyy")
        model_loaded = pickle.load(f)
        # print("Doneeee the modeeellll is loadedddddd ")        
    except Exception as e:
        print("Failed to load model:", e)
    


def prediction_data(data):
    if model_loaded is not None:
        return model_loaded.predict([data])
    
    raise ValueError("Model Not loaded Properly")

