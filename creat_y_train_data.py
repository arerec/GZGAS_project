#!/usr/bin/env python
# -*- coding:utf-8 -*-

from data_preprocess import read_xlsx
from data_preprocess import get_type_according_to_usernumber
from data_preprocess import is_discard
from data_preprocess import write_as_csv
from data_preprocess import replace_mean_value
from classification_table import CLASSICIFICATION_TABLE

xlsx_path = r"C:\Users\lzp\Desktop\GZgas\时间线数据.xlsx"
xlsx_content = read_xlsx(xlsx_path, "Sheet1")


#下面是处理时间线数据.xlsx得到干净数据的步骤
x_train = []
y_train = []
user_has_in_list = []
for key, value in enumerate(xlsx_content):
    if key == 0:
        #第一行没用
        continue
    intercept_data = value[2:9]
    # print(is_discard(intercept_data))
    if is_discard(intercept_data):
        continue
    if value[1] in user_has_in_list:
        continue
    y_train.append(get_type_according_to_usernumber(value[1], CLASSICIFICATION_TABLE))
    x_train.append(intercept_data)
    user_has_in_list.append(value[1])

_x_train = [replace_mean_value(x) for x in x_train]
print(len(_x_train))
write_as_csv(r"C:\Users\lzp\Desktop\GZgas\x_train.csv", _x_train)
print(len(y_train))
write_as_csv(r"C:\Users\lzp\Desktop\GZgas\y_train.csv", y_train)