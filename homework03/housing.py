"""
This module will calculate values based on the boston housing market, using
Python/NumPy/Pandas/Keras implementations

Written by Royce Lloyd for CS344 at Calvin College
3/29/2019
"""

from __future__ import print_function

import math

from IPython import display
from matplotlib import cm
from matplotlib import gridspec
from matplotlib import pyplot as plt

import numpy as np
import pandas as pd

from sklearn import metrics
import tensorflow as tf
from tensorflow.python.data import Dataset

tf.logging.set_verbosity(tf.logging.ERROR)
pd.options.display.max_rows = 10
pd.options.display.float_format = '{:.1f}'.format

boston_housing_dataframe = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv")
boston_housing_dataframe = boston_housing_dataframe.reindex(np.random.permutation(boston_housing_dataframe.index))

print(boston_housing_dataframe.shape)
print(boston_housing_dataframe.head())

def preprocess_features(boston_housing_dataframe):
    selected_features = boston_housing_dataframe[
        ["crim",
         "zn",
         "indus",
         "chas",
         "nox",
         "rm",
         "age",
         "dis",
         "rad",
         "tax",
         "ptratio",
         "b",
         "lstat"
        ]]
    processed_features = selected_features.copy()
    return processed_features


def preprocess_targets(boston_housing_dataframe):
    output_targets = pd.DataFrame()
    output_targets["medv"] = (boston_housing_dataframe["medv"]/1000)
    return output_targets


training_ex = preprocess_features(boston_housing_dataframe.head(400))
training_targets = preprocess_targets(boston_housing_dataframe.head(400))

print(training_ex.shape)
print(training_targets.shape)

validation_ex = preprocess_features(boston_housing_dataframe.tail(106))
validation_targets = preprocess_targets(boston_housing_dataframe.tail(106))
