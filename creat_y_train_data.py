#!/usr/bin/env python
# -*- coding:utf-8 -*-

from data_preprocess import read_xlsx

xlsx_path = r"C:\Users\lzp\Desktop\GZgas\时间线数据.xlsx"
xlsx_content = read_xlsx(xlsx_path, "Sheet1")
print(xlsx_content)