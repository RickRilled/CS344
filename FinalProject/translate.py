from keras import layers
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.text import text_to_word_sequence
import keras
import numpy as np
import random
import sys

text_initial = open("Scripts/newComedy.txt", "r").read()

maxlen = 50

step = 3

sentences = []

next_chars = []

tokenizer = Tokenizer(num_words=10000, split=' ')
tokenizer.fit_on_texts(text_initial)
sequences = text_to_word_sequence(text_initial)

for i in range(0, len(sequences) - maxlen, step):
    sentences.append(sequences[i: i + maxlen])
    next_chars.append(sequences[i + maxlen])
print('Number of sequences:', len(sentences))

words = sorted(list(sequences))
words = list(dict.fromkeys(words))
print('Unique shit:', words)

word_indices = dict((char, words.index(char)) for char in words)


print('Vectorization...')
x = np.zeros((len(sentences), maxlen, len(words)), dtype=np.bool)
y = np.zeros((len(sentences), len(words)), dtype=np.bool)
for i, sentence in enumerate(sentences):
    for t, char in enumerate(sentence):
        x[i, t, word_indices[char]] = 1
    y[i, word_indices[next_chars[i]]] = 1

model = keras.models.Sequential()
model.add(layers.LSTM(128, input_shape=(maxlen, len(words))))
model.add(layers.Dense(len(words), activation='softmax'))
model.add(layers.Dense(len(words), activation='softmax'))

optimizer = keras.optimizers.RMSprop(lr=0.1, clipnorm=1.)
model.compile(loss='categorical_crossentropy', optimizer=optimizer)

def sample(preds, temperature=1.0):
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)

for epoch in range(1, 60):
    print('epoch', epoch)
    # Fit the model for 1 epoch on the available training data
    model.fit(x, y,
              batch_size=128,
              epochs=1)

    # Select a text seed at random
    start_index = random.randint(0, len(sequences) - maxlen - 1)
    generated_text = sequences[start_index: start_index + maxlen]
    print('--- Generating with seed: "', generated_text, '"')

    for temperature in [1.0, 1.2]:
        print('------ temperature:', temperature)
        print(generated_text)

        # We generate 400 characters
        for i in range(400):
            sampled = np.zeros((1, maxlen, len(words)))
            for t, char in enumerate(generated_text):
                sampled[0, t, word_indices[char]] = 1.

            preds = model.predict(sampled, verbose=0)[0]
            next_index = sample(preds, temperature)
            next_char = words[next_index]

            generated_text += next_char
            generated_text = generated_text[1:]


            print(next_char)

        print()
