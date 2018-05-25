#!/usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout
from data_preprocess import read_csv

x_train = read_csv(r"C:\Users\lzp\Desktop\GZgas\x_train.csv")
print(x_train)
y_train = read_csv(r"C:\Users\lzp\Desktop\GZgas\y_train.csv")
print(y_train)


model = Sequential()
model.add(Dense(64, input_dim=7, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])
hist = model.fit(x_train, y_train, epochs=20, batch_size=128, validation_split=0.2)
print(hist.history)
