# coding:utf-8

import os
from flask import Flask
from flask import request, jsonify
import numpy as np
from keras.models import load_model

app = Flask(__name__)

if not os.path.exists("model.h5"):
    print('can not find model!')
else:
    model = load_model('model.h5')
    print('load model sussess!')
print('test model...')
print(model.predict(np.zeros((1, 6, 1))))
print('test done.')

@app.route("/predict",methods=['POST'])
def predict():
    data1 = request.form.get('data1', '')
    data2 = request.form.get('data2', '')
    data3 = request.form.get('data3', '')
    data4 = request.form.get('data4', '')
    data5 = request.form.get('data5', '')
    data6 = request.form.get('data6', '')
    try:
        data1 = float(data1)
        data2 = float(data2)
        data3 = float(data3)
        data4 = float(data4)
        data5 = float(data5)
        data6 = float(data6)
    except Exception as e:
        print(e)
        return jsonify({'result': 'input data error!', 'code': '400'})
    sequence = [data1, data2, data3, data4, data5, data6]
    sequence = np.array(sequence)
    sequence = np.reshape(sequence,(1,6,1))
    pred = model.predict(sequence,  batch_size=1)
    return jsonify({'result': float(pred[0][0]), 'code': '200'})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5678, debug =True)