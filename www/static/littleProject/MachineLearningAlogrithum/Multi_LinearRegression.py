#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('Advertising.csv')
print(data.head())
print(data.tail())
print(data.shape)