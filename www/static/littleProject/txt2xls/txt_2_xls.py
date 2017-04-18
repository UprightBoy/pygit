#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import OrderedDict

import xlwt
import json


def txt2xls(file):
    with open(file, 'r', encoding='UTF-8') as f:
        data = json.load(f, object_pairs_hook=OrderedDict)
        workbook = xlwt.Workbook()
        sheet1 = workbook.add_sheet('student', cell_overwrite_ok=True)
        for index, (key, values) in enumerate(data.items()):
            sheet1.write(index, 0, key)
            for i, value in enumerate(values):
                sheet1.write(index, i + 1, value)
        workbook.save('D:\pygit\www\static\littleProject/txt2xls/student.xls')


def txt_2_xls(file):
    with open(file, 'r', encoding='UTF-8') as f:
        data = json.load(f, object_pairs_hook=OrderedDict)
        workbook = xlwt.Workbook()
        sheet1 = workbook.add_sheet('city', cell_overwrite_ok=True)
        for index, (key, values) in enumerate(data.items()):
            sheet1.write(index, 0, key)
            sheet1.write(index, 1, values)
        workbook.save('D:\pygit\www\static\littleProject/txt2xls/city.xls')


def txtTOxls(file):
    with open(file, 'r', encoding='UTF-8') as f:
        data = json.load(f, object_pairs_hook=list)
        workbook = xlwt.Workbook()
        sheet1 = workbook.add_sheet('numbers', cell_overwrite_ok=True)
        for index, values in enumerate(data):
            for i, value in enumerate(values):
                sheet1.write(index, i, value)
        workbook.save('D:\pygit\www\static\littleProject/txt2xls/numbers.xls')

if __name__ == '__main__':
    txt2xls('D:\pygit\www\static\littleProject/txt2xls/student.txt')
    txt_2_xls('D:\pygit\www\static\littleProject/txt2xls/city.txt')
    txtTOxls('D:\pygit\www\static\littleProject/txt2xls/numbers.txt')
