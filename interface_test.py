# coding:utf-8

import requests

url = "http://127.0.0.1:5678/predict"
data = {"data1":3,
        "data2": 10,
        "data3": 19,
        "data4": 10,
        "data5": 0,
        "data6": 10,}
response = requests.post(url=url, data=data)
print(response.text)