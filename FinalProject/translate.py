import keras
import numpy as np

path = keras.utils.get_file(
    'comedic.txt',
    origin='s3://scriptscs344calvincollege/comedic.txt')
text = open(path).read().lower()
print('Corpus length:', len(text))



