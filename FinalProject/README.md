The Comedy Network

This program is designed to write it's very one-liner jokes. The code can be run from finalCode.ipynb, granted you has a sub folder called Scripts with a .txt file called oneLiners. This file is provided, but if you would like an updated list, email me at rlloyd8912@gmail.com
To run the code, start with the first module. This loads in the text and prepares some empty lists. The next module arranges the text into sequences based on character. Next, the text is sorted into a list of unique characters. 
The unique characters are then labeled with an index for later use. The sentences are vectorized based on their relative appearances in the text to then feed into the model. The model is then built with a LSTM layer.
The model is then fit on the training data, and predictive text is generated at multiple tempureate distroputions. 
