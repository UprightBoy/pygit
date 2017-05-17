#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import xlrd
from sklearn import datasets, linear_model
'''
data_xls = pd.read_excel('C:/Users\gengzhi\Desktop\房价统计excel/input_data.xlsx', 'Sheet1', index_col=None)
data_xls.to_csv('data_csv.csv', encoding='utf-8')


def get_data(file_name):
    data = pd.read_csv(file_name)
    X_parameter = []
    Y_parameter = []
    for single_square_feet, single_price_value in zip(data['square_feet'], data['price']):
        X_parameter.append([float(single_square_feet)])
        Y_parameter.append(float(single_price_value))
    return X_parameter, Y_parameter

print(get_data('D:\pygit\www\static\littleProject\MachineLearningAlogrithum/data_csv.csv'))

'''


def get_data(file_name):
    with xlrd.open_workbook(file_name) as f:
        table = f.sheets()[0]
        x_parameter = []
        y_parameter = []
        for i in range(1, 8):
            x_parameter.append([table.row_values(i)[0]])
            y_parameter.append(table.row_values(i)[1])
    return x_parameter, y_parameter

print(get_data('C:/Users\gengzhi\Desktop\房价统计excel/input_data.xlsx'))


def linear_model_main(x_parameter, y_parameter, predicted_value):
    regr = linear_model.LinearRegression()
    regr.fit(x_parameter, y_parameter)
    predict_outcome = regr.predict(predicted_value)
    predictions = {}
    predictions['intercept'] = regr.intercept_
    predictions['coefficient'] = regr.coef_
    predictions['predicted_value'] = predict_outcome
    return predictions

x, y = get_data('C:/Users\gengzhi\Desktop\房价统计excel/input_data.xlsx')
predict_value = 700
result = linear_model_main(x, y, predict_value)
print("Intercept value:", result['intercept'])   # 线性函数的截距值
print("coefficient:", result['coefficient'])
print("Predicted value:", result['predicted_value'])


def show_linear_line(x_parameter, y_parameter):
    regr = linear_model.LinearRegression()
    regr.fit(x_parameter, y_parameter)
    plt.scatter(x_parameter, y_parameter, edgecolors='blue')
    plt.plot(x_parameter, regr.predict(x_parameter), color='red', linewidth=4)
    plt.xticks(())
    plt.yticks(())
    plt.show()

show_linear_line(x, y)

