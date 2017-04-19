#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import xlrd
import re

with xlrd.open_workbook('D:\pygit\www\static\littleProject/xls_Analysis/bill.xls') as f:
    table = f.sheets()[0]
    c = []
    re_s = re.compile("(^\d+)(秒)")
    re_m_s = re.compile('(\d+)(分)(\d+)(秒)')
    count = 0
    for i in range(9, table.nrows):
        c.append(table.row_values(i)[4])
        if re_s.match(c[i - 9]):
            count += int(re_s.match(c[i - 9]).group(1))
        if re_m_s.match(c[i - 9]):
            count += int(re_m_s.match(c[i - 9]).group(1)) * 60 + int(re_m_s.match(c[i - 9]).group(3))
    if count >= 3600:
        h = count // 3600
        h_m = count % 3600
        if h_m >= 60:
            m = h_m // 60
            s = h_m % 60
        else:
            m = 0
            s = h_m
    else:
        h = 0
        m = count // 60
        s = count % 60

    print(c)
    print(count)
    print('总通话时长:', h, '小时', m, '分', s, '秒')
