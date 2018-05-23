#!/usr/bin/env python
# -*- coding:utf-8 -*-

import csv
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
    if type(data) != list():
        raise ValueError
    write_file = open(save_filepath, 'w', newline='')
    writer = csv.writer(write_file)
    row_length = len(data)
    for i in range(row_length):
        writer.writerow(data[i])
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