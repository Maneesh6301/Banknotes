# -*- coding: utf-8 -*-
"""
Created on Sun Sep 21 00:33:17 2025

@author: manee
"""
import uvicorn
from typing import Union
from Banknotes import Banknote
from fastapi import FastAPI
import numpy as np
import pandas as pd
import pickle
app=FastAPI()
pickle_in=open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post('/predict')
def predict_species(data:Banknote):
    data=data.dict()
    print(data)
    print("Hello")
    variance=data["variance"]
    print(variance)
    skewness=data["skewness"]
    curtosis=data["curtosis"]
    entropy=data["entropy"]
    #print(classifier.predict([[variance,skewness,curtosis,entropy]]))
    #print("Hello")
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    if(prediction[0]>0.5):
        prediction="fake note"
    else:
        prediction="its a Bank note"
    return {
    'prediction':prediction
    }
if __name__=="__main__":
    uvicorn.run(app,host='127.0.0.1',port=8000)
#uvicorn app:app --reload
    