from keras.models import Sequential
# from keras.layers import Dense, LSTM,Dropout
# import tensorflow as tf

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
######################## IMPORT CSV DATA #######################

dataframe = pd.read_csv('ZBH.csv')
dataframe.index =dataframe['Date']
dataframe=dataframe['Close']
print (dataframe)