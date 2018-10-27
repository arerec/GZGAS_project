#!/usr/bin/env python
# -*- coding:utf-8 -*-

from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.layers import Embedding
from keras.layers import LSTM
from data_preprocess import read_csv
import numpy as np
from keras.optimizers import Adam


x = read_csv(r"C:\Users\lzp\Desktop\GZgas\x_train.csv")
print(len(x))
y = read_csv(r"C:\Users\lzp\Desktop\GZgas\y_train.csv")
print(len(y))

x_train = x[:-1000]
x_train = np.reshape(x_train,(len(x_train),6,1))
y_train = y[:-1000]
x_test = x[-1000:]
x_test = np.reshape(x_test,(len(x_test),6,1))
y_test = y[-1000:]

n_step = 6
n_input = 1

model = Sequential()
# model.add(Embedding(max_features, output_dim=256))
model.add(LSTM(128, batch_input_shape=(None, n_step, n_input)))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))

adam = Adam(lr=0.0001)
model.compile(loss='binary_crossentropy',
              optimizer=adam,
              metrics=['accuracy'])

hist = model.fit(x_train, y_train, batch_size=64, epochs=50)
score = model.evaluate(x_test, y_test, batch_size=16)
print(score)

# print(hist.history)
# model.save('model.h5')