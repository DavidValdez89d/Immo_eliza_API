import pickle
import numpy as np

with open("model/immo_scaler.pkl","rb") as scalefile:
    scaler = pickle.load(scalefile)
    
with open("model/immo_poly_features.pkl","rb") as polyfeaturesfile:
    poly_features = pickle.load(polyfeaturesfile)

with open("model/immo_model.pkl","rb") as modelfile:
    poly_model = pickle.load(modelfile)

def predict(preprocess_item):
    """
    Function that takes immo_eliza preprocessed data as an input and return a price as output.
    :input
    :output
    """
    array_input = np.array([preprocess_item])
    X_scaled_imput = scaler.transform(array_input)
    price_prediction = poly_model.predict(poly_features.fit_transform(X_scaled_imput))
    return float(price_prediction)
