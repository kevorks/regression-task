from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd
import os


# API folder
api_folder_path = os.path.join(os.getcwd())

# Define the FastAPI app
app = FastAPI(title='Regression Task',
              description='API for Wine Quality Prediction',
              version='0.0.1',
              openapi_tags=[
                  {
                      'name': 'Home',
                      'description': 'API functionality'
                  },
                  {
                      'name': 'Prediction',
                      'description': 'Wine Quality prediction'
                  }
              ]
              )

# Load the model
with open(api_folder_path + '/best_model.pkl', 'rb') as pickle_in:
    pipe = pickle.load(pickle_in)


# Define the request payload model using Pydantic
class PredictionPayload(BaseModel):
    fixed_acidity: float
    volatile_acidity: float
    citric_acid: float
    residual_sugar: float
    chlorides: float
    free_sulfur_dioxide: float
    total_sulfur_dioxide: float
    density: float
    pH: float
    sulphates: float
    alcohol: float


# Expose the prediction functionality
@app.get('/', tags=['Home'])
def index():
    return {'message': 'API is working properly!'}


# Define the prediction endpoint with authentication
@app.post('/predict', tags=['Prediction'])
def predict(payload: PredictionPayload):

    # Convert the payload to a DataFrame
    df = pd.DataFrame([payload.dict()])

    # Make predictions using the pipeline model
    predictions = pipe.predict(df)

    # Return the predictions as a response
    return {'Predicted Wine Quality is': predictions.tolist()}
