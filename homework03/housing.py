"""
This module will calculate values based on the boston housing market, using
Python/NumPy/Pandas implementations

Written by Royce Lloyd for CS344 at Calvin College
3/30/2019
"""

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split

boston_housing_dataframe = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv")
boston_housing_dataframe = boston_housing_dataframe.reindex(np.random.permutation(boston_housing_dataframe.index))

print(boston_housing_dataframe.shape)
print(boston_housing_dataframe.head())

trainSet, testSet = train_test_split(boston_housing_dataframe, test_size=0.2)
testSet, validateSet = train_test_split(testSet, test_size=0.2)

print(trainSet.shape)
print(testSet.shape)
print(validateSet.shape)


boston_housing_dataframe["crime_in_poverty"] = (
    boston_housing_dataframe["CRIM"] / boston_housing_dataframe["MEDV"])
