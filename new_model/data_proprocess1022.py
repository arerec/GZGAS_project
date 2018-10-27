#!/usr/bin/env python
# -*- coding:utf-8 -*-

import xlrd
import csv
import random

def write_as_csv(save_filepath, data):
    if type(data) != list:
        raise ValueError
    write_file = open(save_filepath, 'w', newline='')
    writer = csv.writer(write_file)
    row_length = len(data)
    for i in range(row_length):
        if type(data[i]) is list:
            writer.writerow(data[i])
        else:
            writer.writerow([data[i]])
    write_file.close()

file_path = r"C:\Users\lzp\Desktop\GZgas\1020工商.xlsx"
data = xlrd.open_workbook(file_path)
table = data.sheets()[0]

goshang_data = []
nrows = table.nrows
for i in range(nrows):
    # print(table.row(i))
    row_data = []
    if table.row(i)[0].value is not "" \
                and table.row(i)[1].value is not "" \
                and table.row(i)[2].value is not "" \
                and table.row(i)[3].value is not "" \
                and table.row(i)[4].value is not "" \
                and table.row(i)[5].value is not "" \
            and table.row(i)[6].value is not "" \
            and table.row(i)[7].value is not "" \
            and table.row(i)[8].value is not "" \
            and table.row(i)[9].value is not "" \
            and table.row(i)[10].value is not "" \
            and table.row(i)[11].value is not "":
        row_data.append(table.row(i)[0].value+table.row(i)[1].value)
        row_data.append(table.row(i)[2].value+table.row(i)[3].value)
        row_data.append(table.row(i)[4].value+table.row(i)[5].value)
        row_data.append(table.row(i)[6].value+table.row(i)[7].value)
        row_data.append(table.row(i)[8].value+table.row(i)[9].value)
        row_data.append(table.row(i)[10].value+table.row(i)[11].value)
        row_data.append(1)
        goshang_data.append(row_data)

print(len(goshang_data))


file_path = r"C:\Users\lzp\Desktop\GZgas\1020民用.xlsx"
data = xlrd.open_workbook(file_path)
table = data.sheets()[0]

minyong_data = []
nrows = table.nrows
for i in range(nrows):
    # print(table.row(i))
    row_data = []
    if table.row(i)[0].value is not "" \
            and table.row(i)[2].value is not "" \
            and table.row(i)[4].value is not "" \
            and table.row(i)[6].value is not "" \
            and table.row(i)[8].value is not "" \
            and table.row(i)[10].value is not "":
        row_data.append(table.row(i)[0].value)
        row_data.append(table.row(i)[2].value)
        row_data.append(table.row(i)[4].value)
        row_data.append(table.row(i)[6].value)
        row_data.append(table.row(i)[8].value)
        row_data.append(table.row(i)[10].value)
        row_data.append(0)
        minyong_data.append(row_data)

write_data = goshang_data+minyong_data
random.shuffle(write_data)

write_as_csv(r"C:\Users\lzp\Desktop\GZgas\x_train.csv", write_data)