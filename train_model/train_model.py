#!/usr/bin/env python
# coding: utf-8

import sys
import pandas as pd
import numpy as np
import joblib as jb
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import PolynomialFeatures
from sklearn import neighbors 
from sklearn.metrics import mean_squared_error


def update_buildingArea(ba_features, poly_scaler, model, train_set, test_set, train_set2, test_set2):
    
    idx_na_train = train_set2[train_set2['BuildingArea'].isnull() | (train_set2['BuildingArea'] == 0.0)].index
    idx_na_test = test_set2[test_set2['BuildingArea'].isnull() | (train_set2['BuildingArea'] == 0.0)].index

    train_ba = train_set2.loc[idx_na_train, ba_features]
    test_ba = test_set2.loc[idx_na_test, ba_features]

    X_train_ba = poly_scaler.transform(train_ba.values)
    X_test_ba = poly_scaler.transform(test_ba.values)

    ba_train_pred = model.predict(X_train_ba)
    ba_test_pred = model.predict(X_test_ba)

    train_set.loc[idx_na_train, 'BuildingArea'] = np.exp(ba_train_pred)
    test_set.loc[idx_na_test, 'BuildingArea'] = np.exp(ba_test_pred)
    train_set.loc[idx_na_train, 'BuildingArealog'] = ba_train_pred
    test_set.loc[idx_na_test, 'BuildingArealog'] = ba_test_pred
    
    return train_set, test_set

def design_ba_model(train_set, test_set):

    badf = train_set[train_set['BuildingArea'].between(20, 800) & 
                      train_set['Landsize'].between(1, 10000)].copy()
    badf.drop(columns=['Date', 'Bedroom2', 'Pricelog', 'Price'], inplace=True)
    
    # Features definition
    ba_features = ['stname', 'Rooms', 'Suburb', 'Type', 'Bathroom', 'Car']

    # Dividing the data in train set and validation set
    train_ba, val_ba, y_train_ba, y_val_ba = train_test_split(badf[ba_features], badf['BuildingArealog'], 
                                                              test_size=0.3, random_state=10)
    poly_scaler = Pipeline([
        ('std_scaler', MinMaxScaler()),
        ('polynomial', PolynomialFeatures(degree=4, include_bias=False))
    ])

    X_train_poly_ba = poly_scaler.fit_transform(train_ba)
    X_val_poly_ba = poly_scaler.transform(val_ba)

    train_metrics = []
    val_metrics = []

    model = neighbors.KNeighborsRegressor(4)

    for n_neighbors in range(4, 5):

        model = neighbors.KNeighborsRegressor(n_neighbors)

        ## fit the model
        model.fit(X_train_poly_ba, y_train_ba)

        ## predict training set
        y_train_ba_pred = model.predict(X_train_poly_ba)
        y_val_ba_pred = model.predict(X_val_poly_ba)

        ba_train_RMSE = np.sqrt(mean_squared_error(y_train_ba, y_train_ba_pred))
        ba_val_RMSE = np.sqrt(mean_squared_error(y_val_ba, y_val_ba_pred))

        print("\n----- EVALUATION WITH n_neighbors={} ------".format(n_neighbors))
        print('TRAIN SET \tRMSE: {} \nVALIDATION SET  RMSE: {} \n'.format(ba_train_RMSE, ba_val_RMSE))

        train_metrics.append(ba_train_RMSE)
        val_metrics.append(ba_val_RMSE)
    return ba_features, poly_scaler, model
	
	
def model_design(features,train_set, test_set):
    
    y_train = train_set['Pricelog']
    train, val, y_train, y_val = train_test_split(train_set[features], train_set['Pricelog'], 
                                                  test_size=0.3, random_state=42)
    poly_scaler = Pipeline([
        ('polynomial', PolynomialFeatures(degree=4, include_bias=False)), 
        ('std_scaler', MinMaxScaler())
    ])

    ## DEFINE YOUR FEATURES
    X_train_poly = poly_scaler.fit_transform(train.values)
    X_val_poly = poly_scaler.transform(val.values)

    train_metrics = []
    val_metrics = []

    model = neighbors.KNeighborsRegressor(4)

    for n_neighbors in range(4, 5):
        model = neighbors.KNeighborsRegressor(n_neighbors)

        ## fit the model
        model.fit(X_train_poly, y_train)

        ## predict training set
        y_train_pred = model.predict(X_train_poly)
        y_val_pred = model.predict(X_val_poly)

        train_RMSE = np.sqrt(mean_squared_error(np.exp(y_train), np.exp(y_train_pred)))
        val_RMSE = np.sqrt(mean_squared_error(np.exp(y_val), np.exp(y_val_pred)))


        print("----- EVALUATION WITH {} NEIGHBORS ------".format(n_neighbors))
        print('TRAIN SET \tRMSE: {:.2f} \nVALIDATION SET  RMSE: {:.2f} \n'.format(train_RMSE, val_RMSE))

        train_metrics.append(train_RMSE)
        val_metrics.append(val_RMSE)
    return poly_scaler, model 
	


def train_model(path):
	
	print('\n** Training Model executing **')
	root_dir = Path(path[1]).resolve().parent
	
	# Read the preprocessed_data
	train_set = pd.read_csv(root_dir / 'preprocessed_data/price_features_train.csv')
	test_set = pd.read_csv(root_dir / 'preprocessed_data/price_features_test.csv')
	
	# Infer the missing BuildingArea
	ba_features, ba_poly_scaler, ba_model = design_ba_model(train_set, test_set)
	
	# Update the predicted BuildingArea in the original Dataframes
	train_set, test_set = update_buildingArea(ba_features, ba_poly_scaler, ba_model, train_set, test_set, train_set, test_set)
	
	# Selected features
	features = ['Suburb', 'Rooms', 'Type', 'Postcode', 'stname', 'BuildingArea'] 
	
	poly_scaler, model = model_design(features, train_set, test_set)
	
	jb.dump(poly_scaler, root_dir / 'preprocessed_data/scaler.pkl.z')
	jb.dump(model, root_dir / 'preprocessed_data/model.pkl.z')
	
if __name__ == '__main__':
    train_model(sys.argv)

