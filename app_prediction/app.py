#!/usr/bin/env python
# coding: utf-8

import numpy as np
import joblib as jb
import json
import re
import string
from pathlib import Path
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class House(BaseModel):
	suburb: str
	rooms: int
	typeH: str
	postcode: str
	address: str
	buildingArea: float

ROOT_PATH = Path().resolve()

@app.get('/')
async def index():
	return {'text': 'Server is up!'}


def categorical_encoder(cat_name, cat_value):
	
	with open(ROOT_PATH / 'preprocessed_data/{}_encoder.json'.format(cat_name), 'r') as file:
		data = json.load(file)
	values = list(data.values())
	return data[cat_value] if cat_value in data.keys() else int((values[0]+values[-1])/2)

# features = ['Suburb', 'Rooms', 'Type', 'Postcode', 'stname', 'BuildingArea'] 
def inputTransformer(house): 
	
	#st = ' '.join(house.address.split(' ')[1:])
	st = re.sub('\d+', '', house.address).strip(string.punctuation).strip()
	suburb = categorical_encoder('Suburb', house.suburb)
	h_type = categorical_encoder('Type', house.typeH)
	postcode = categorical_encoder('Postcode', house.postcode)
	stname = categorical_encoder('stname', st)
	return [suburb, house.rooms, h_type, postcode, stname, house.buildingArea]

@app.post('/predict')
def get_prediction(house_info: House):

	scaler = jb.load(ROOT_PATH / 'preprocessed_data/scaler.pkl.z')
	model = jb.load(ROOT_PATH / 'preprocessed_data/model.pkl.z')
	
	X = np.array(inputTransformer(house_info)).reshape(1, -1)
	X_poly = scaler.transform(X)
	y_hat = model.predict(X_poly)[0]	
	return {'predicted_price': np.round(np.exp(y_hat), 2)}
	
@app.get('/suburb')
def get_suburbs():
	with open(ROOT_PATH / 'preprocessed_data/Suburb_encoder.json', 'r') as file:
		data = json.load(file)
	return {'suburbs': list(data.keys())}
	
@app.get('/stname')
def get_suburbs():
	with open(ROOT_PATH / 'preprocessed_data/stname_encoder.json', 'r') as file:
		data = json.load(file)
	return {'stname': list(data.keys())}

if __name__ == '__main__':
    uvicorn.run('app:app', host='0.0.0.0', port=5000, reload=True, access_log=False)
