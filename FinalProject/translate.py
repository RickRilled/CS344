import keras
import numpy as np

path = keras.utils.get_file(
    'comedic.txt',
    origin='D:\RealPyCharm\cs344\Final Project\Scripts\comedic.txt')
text = open(path).read().lower()
print('Corpus length:', len(text))
