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

boston_housing_dataframe = pd.read_csv()

boston_housing_dataframe = boston_housing_dataframe.reindex(np.random.permutation(boston_housing_dataframe.index))

def preprocess_features(boston_housing_dataframe):
    selected_features = boston_housing_dataframe[
        ["latitude",
         "longitude",
         "housing_median_age",
         "total_rooms",
         "population",
         "households",
         "median_income"
        ]]
    processed_features = selected_features.copy()
    return processed_features


def preprocess_targets(boston_housing_dataframe):
    output_targets = pd.DataFrame()
    output_targets["median_house_value"] = (boston_housing_dataframe["median_house_value"]/1000)
    return output_targets

