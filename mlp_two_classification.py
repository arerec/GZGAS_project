#!/usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout
from data_preprocess import read_csv
import matplotlib.pyplot as plt

x = read_csv(r"C:\Users\lzp\Desktop\GZgas\x_train.csv")
print(len(x))
y = read_csv(r"C:\Users\lzp\Desktop\GZgas\y_train.csv")
print(len(y))

x_train = x[:-1000]
y_train = y[:-1000]
x_test = x[-1000:]
y_test = y[-1000:]

model = Sequential()
model.add(Dense(64, input_dim=6, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])
hist = model.fit(x_train, y_train, epochs=300, batch_size=128)
# hist = model.fit(x_train, y_train, epochs=300, batch_size=128, validation_split=0.2)
# print(hist.history)

score = model.evaluate(x_test, y_test, batch_size=128)
print(score)

x=list(range(0,300))
y= hist.history["acc"]
plt.figure()
plt.plot(x,y)
plt.show()

x=list(range(0,300))
y= hist.history["loss"]
plt.figure()
plt.plot(x,y)
plt.show()