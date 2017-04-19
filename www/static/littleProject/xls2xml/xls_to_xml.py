#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import xlrd, codecs
from lxml import etree
from collections import OrderedDict


def read_xls(file):
    data = xlrd.open_workbook(file)
    table = data.sheets()[0]
    c = OrderedDict()
    for i in range(table.nrows):
        c[table.cell(i, 0).value] = table.row_values(i)[1:]
    print(c)
    return c


def save_xml(data, name, comment):
    output = codecs.open(name + '.xml', 'w', 'UTF-8')
    root = etree.Element('root')
    student_xml = etree.ElementTree(root)
    student = etree.SubElement(root, name)
    student.text = str(data)
    student.append(etree.Comment(comment))
    output.write(etree.tounicode(student_xml.getroot()))
    output.close()


def read_numbers(file):
    data = xlrd.open_workbook(file)
    table = data.sheets()[0]
    c = []
    for i in range(table.nrows):
        c.append(table.row_values(i)[:])
    print(c)
    return c


if __name__ == '__main__':
    s = read_xls('D:\pygit\www\static\littleProject/txt2xls/student.xls')
    save_xml(s, 'student', '学生信息表\n\"id\": [名字，数学，语文，英语]')

    c = read_xls('D:\pygit\www\static\littleProject/txt2xls/city.xls')
    save_xml(c, 'city', '城市信息')

    n = read_numbers('D:\pygit\www\static\littleProject/txt2xls/numbers.xls')
    save_xml(n, 'numbers', "数字信息")
