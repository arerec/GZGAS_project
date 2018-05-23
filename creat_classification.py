#!/usr/bin/env python
# -*- coding:utf-8 -*-

from data_preprocess import GONGSHNAG, MINYONG
from data_preprocess import read_xlsx, write_as_csv


xlsx_path = r"C:\Users\lzp\Desktop\GZgas\用户对应抄表号再对应类型.xlsx"
xlsx_content = read_xlsx(xlsx_path, "Sheet1")
# print(xlsx_content)

result = {}
for key, value in enumerate(xlsx_content):
    if key == 0 or key == 1:
        continue
    if len(value) != 2:
        raise ValueError
    if int(value[0]) in GONGSHNAG:
        result[value[1]] = "工商"
    elif int(value[0]) in MINYONG:
        result[value[1]] = "民用"
    else:
        print("can not map this one")
print(result)