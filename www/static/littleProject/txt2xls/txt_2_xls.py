#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import OrderedDict

import xlwt, json


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

if __name__ == '__main__':
    txt2xls('D:\pygit\www\static\littleProject/txt2xls/student.txt')