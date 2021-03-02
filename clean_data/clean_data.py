#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from pathlib import Path
import logging as log
import sys

log.basicConfig(format='%(asctime)s %(message)s')


def read_raw_data(path):
	
	ROOT_PATH = Path(path[1]).resolve().parent
	train_set = pd.read_csv(ROOT_PATH / 'preprocessed_data/train_set.csv',index_col=0) 
	test_set = pd.read_csv(ROOT_PATH / 'preprocessed_data/test_set.csv',index_col=0)
	
	log.info('Data set read successfully')	
	return train_set, test_set


# In[4]:


def remove_na(df):
	
	df['Car'] = df['Car'].fillna(df['Car'].median())
	df['CouncilArea'] = df['CouncilArea'].fillna(df['CouncilArea'].mode()[0])
	
	log.info('Data set read successfully')	
	return df


# In[5]:


def save_clean_data(path, newTrain, newTest):
	
	ROOT_PATH = Path(path[1]).resolve().parent
	newTrain.to_csv(ROOT_PATH / 'preprocessed_data/cleanedTrain.csv', index=False)
	newTest.to_csv(ROOT_PATH / 'preprocessed_data/cleanedTest.csv', index=False)
	

# In[6]:


def clean_data(path):
    
    # Read original data:
    train_set, test_set = read_raw_data(path)
    
    # Fill missing values:
    train_set = remove_na(train_set)
    test_set = remove_na(test_set)
    
    # Save clean data:
    save_clean_data(path, train_set, test_set)


if __name__ == '__main__':
	clean_data(sys.argv)