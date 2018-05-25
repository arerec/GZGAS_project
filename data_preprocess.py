#!/usr/bin/env python
# -*- coding:utf-8 -*-

import csv
import numpy as np
from openpyxl import load_workbook

#工商和民用的抄表册号
GONGSHNAG = [181603488, 181603692, 181314025, 181505132, 181425043]
MINYONG = [181603872, 181603873, 181603613, 181603625, 181603626, 181603590, 181603529, 181600804, 181600770,
           181600655, 181389311, 181310020, 181310022, 181310025, 181310023, 181505775, 181505109, 181502391,
           181502332, 181502011, 181425086, 181425033, 181400443, 181400360, 181400358]

def read_xlsx(filepath, sheet_name):
    """
    handle with xlsx file
    """
    output = []
    wb = load_workbook(filepath)
    ws = wb.get_sheet_by_name(sheet_name)
    rows = ws.rows
    for row in rows:
        line = [col.value for col in row]
        output.append(line)
    wb.close()
    return output


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

def get_type_according_to_usernumber(usernumber, classification_table):
    """
    根据用户号返回时民用还是工商类型，民用返回0！！！工商返回的是1！！！
    :param usernumber:
    :param classification_table:
    :return: 0 or 1
    """
    type = classification_table.get(usernumber, "")
    if type == "民用":
        return 0
    elif type == "工商":
        return 1
    else:
        return "this user is not in table"

def is_discard(data_list, null_number = 5):
    """
    根据空数据个数判断该条数据是否丢弃, 要丢弃返回True
    """
    counter = 0
    for i in data_list:
        if i == '':
            counter += 1
    if counter >= null_number:
        return True
    else:
        return False

def replace_mean_value(list_data):
    """
    所有数据转换为int输出
    将列表中的空值换成平均值
    """
    if type(list_data) != list:
        raise ValueError
    list_output = []
    mean_value = get_mean_value(list_data)
    for element in list_data:
        if element == '':
            list_output.append(mean_value)
        else:
            list_output.append(int(element))
    return list_output

def get_mean_value(list):
    """
    求平均值，不计算空值
    """
    int_list_without_null = []
    for i in list:
        if i is not '':
            int_list_without_null.append(int(i))
    mean_value = np.mean(int_list_without_null)
    return mean_value


if __name__ == "__main__":
    a = ['2', '2', '2', '2', '0', '0', '0', '']
    b = get_mean_value(a)
    print(b)