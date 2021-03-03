#!/usr/bin/env python
# coding: utf-8

import sys
import pandas as pd
import numpy as np
import json
from pathlib import Path


def log_transformation(df, origin, target):
    df[target] = df[origin].map(lambda x: np.log(x) if x > 0 else 0)
    return df


# Transformation on the continuos variables
def transform_continuos(train_set, test_set, continuous_variables):
    
    # Tranformation on the target value
    train_set = log_transformation(train_set, origin='Price', target='Pricelog')
    
    for cont in continuous_variables:
        train_set = log_transformation(train_set, origin=cont, target=cont + 'log')
        test_set = log_transformation(test_set, origin=cont, target=cont + 'log')
    return train_set, test_set


def transform_temporal_variables(train_set, test_set):

    # Temporal variables:
    train_set.loc[:, 'Date'] = pd.to_datetime(train_set['Date']).dt.strftime('%m-%Y')
    test_set.loc[:, 'Date'] = pd.to_datetime(test_set['Date']).dt.strftime('%m-%Y')

    # Filling in 'YearBuilt' with the mode
    train_set.loc[:, 'YearBuilt'] = train_set['YearBuilt'].fillna(train_set['YearBuilt'].mode()[0])
    test_set.loc[:, 'YearBuilt'] = test_set['YearBuilt'].fillna(test_set['YearBuilt'].mode()[0])

    # Create a new variable as the Age of the building
    train_set.loc[:, 'Age'] = train_set.apply(lambda x: 
                                              pd.to_numeric(x['Date'].split('-')[1]) - x['YearBuilt'], axis=1)
    test_set.loc[:, 'Age'] = test_set.apply(lambda x: 
                                            pd.to_numeric(x['Date'].split('-')[1]) - x['YearBuilt'], axis=1)
    return train_set, test_set


def transform_categorical(train_set, test_set, categorical_variables):

    train_set.loc[:, 'stname'] = train_set['Address'].map(lambda x:' '.join(x.split(' ')[1:]))
    test_set.loc[:, 'stname'] = test_set['Address'].map(lambda x:' '.join(x.split(' ')[1:]))

    train_set.drop(columns='Address', inplace=True)
    test_set.drop(columns='Address', inplace=True)

    categorical_variables.remove('Address')
    categorical_variables.append('stname')

    # Encoder that will be used before prediction       
    cat_encoder = {}

    # Encode the categorical variables to 'Price'
    fulldf = pd.concat([train_set, test_set], ignore_index=True)
    for cat in categorical_variables:
        temp = fulldf[[cat, 'Price']].groupby(cat).count() / fulldf.shape[0]
        temp_df = temp[temp > 0.01].index
        fulldf[cat]=np.where(fulldf[cat].isin(temp_df),fulldf[cat],'irrelevant')

    for cat in categorical_variables:
        labels_ordered = fulldf.groupby([cat])['Price'].mean().sort_values().index
        labels_ordered = {k:i for i, k in enumerate(labels_ordered,1)}

        cat_encoder[cat] = labels_ordered    
        fulldf[cat] = fulldf[cat].map(labels_ordered)

    for cat in categorical_variables:
        train_set.loc[:, cat] = fulldf.loc[:train_set.shape[0], cat]
        test_set.loc[:, cat] = fulldf.loc[train_set.shape[0]:, cat].values

    # Encode the categorical variables to 'BuildingArea'
    fulldf2 = pd.concat([train_set, test_set], ignore_index=True)
    for cat in categorical_variables:
        temp = fulldf2[[cat, 'BuildingArea']].groupby(cat).count() / fulldf2.shape[0]
        temp_df = temp[temp > 0.01].index
        fulldf2[cat]=np.where(fulldf2[cat].isin(temp_df),fulldf2[cat],'irrelevant')

    for cat in categorical_variables:
        labels_ordered = fulldf2.groupby([cat])['BuildingArea'].mean().sort_values().index
        labels_ordered = {k:i for i, k in enumerate(labels_ordered,1)}
        fulldf2[cat] = fulldf2[cat].map(labels_ordered)

    train_set2 = train_set.copy()
    test_set2 = test_set.copy()

    for cat in categorical_variables:
        train_set2.loc[:, cat] = fulldf2.loc[:train_set.shape[0], cat]
        test_set2.loc[:, cat] = fulldf2.loc[train_set.shape[0]:, cat].values
    return train_set, test_set, train_set2, test_set2, cat_encoder


def read_data(path):
    
    ROOT_PATH = Path(path[1]).resolve().parent
    train_set = pd.read_csv(ROOT_PATH / 'preprocessed_data/cleanedTrain.csv')
    test_set = pd.read_csv(ROOT_PATH / 'preprocessed_data/cleanedTest.csv')    
    return train_set, test_set



def save_data(path, train_set, test_set, train_set2, test_set2, cat_encoder):

    ROOT_PATH = Path(path[1]).resolve().parent
    
    for cat in ['Suburb', 'Type', 'Postcode', 'stname']:
        with open(ROOT_PATH / 'preprocessed_data/{}_encoder.json'.format(cat), 'w') as encoder:
            encoder.write('{}'.format(json.dumps(cat_encoder[cat])))

    train_set.to_csv(ROOT_PATH / 'preprocessed_data/price_features_train.csv', index=False)
    test_set.to_csv(ROOT_PATH / 'preprocessed_data/price_features_test.csv', index=False)

    train_set2.to_csv(ROOT_PATH / 'preprocessed_data/ba_features_train.csv', index=False)
    test_set2.to_csv(ROOT_PATH / 'preprocessed_data/ba_features_test.csv', index=False)


def transform_data(path):
    
    train_set, test_set = read_data(path)
    
    continuous_variables = ['Propertycount', 'Landsize', 'BuildingArea']

    categorical_variables = ['SellerG', 'Method', 'Suburb', 'Address', 
                             'Postcode', 'CouncilArea', 'Regionname', 'Type']
    
    # Tranformation on continuos variables
    train_set, test_set = transform_continuos(train_set, test_set, continuous_variables)
    
    # Transformation on temporal variables:
    train_set, test_set = transform_temporal_variables(train_set, test_set)
    
    # Transformation on categorical variables:
    train_set, test_set, train_set2, test_set2, cat_encoder = transform_categorical(train_set, test_set, categorical_variables)
    
    save_data(path, train_set, test_set, train_set2, test_set2, cat_encoder)

if __name__ == '__main__':
	transform_data(sys.argv)