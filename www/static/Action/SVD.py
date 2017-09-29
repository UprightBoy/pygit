#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from numpy import *
from numpy import linalg as la

U, sigma, VT = linalg.svd([[1, 1], [7, 7]])   # sigma为奇异值矩阵，以行向量array的形式返回
print(U)
print(type(sigma))
print(sigma)
print(VT)


def loadExData():
    return[[0, 0, 0, 2, 2],
           [0, 0, 0, 3, 3],
           [0, 0, 0, 1, 1],
           [1, 1, 1, 0, 0],
           [2, 2, 2, 0, 0],
           [5, 5, 5, 0, 0],
           [1, 1, 1, 0, 0]]

Data = loadExData()
U, sigma, VT = linalg.svd(Data)   # sigma为奇异值矩阵，以行向量array的形式返回
print(sigma)
sig3 = mat([[sigma[0], 0, 0], [0, sigma[1], 0], [0, 0, sigma[2]]])
# 前三个奇异值的数值远大于其他值，可以选取它们作为近似奇异值来构建原矩阵而不损失较多信息
print(sig3)
print(U[:, : 3] * sig3 * VT[: 3, :])


def eulidSim(inA, inB):
    return 1.0 / (1.0 + la.norm(inA, inB))


def pearsSim(inA, inB):
    if len(inA) < 3:
        return 1.0
    return 0.5 + 0.5 * corrcoef(inA, inB, rowvar=0)[0][1]


def cosSim(inA, inB):
    num = float(inA.T * inB)
    denom = la.norm(inA) * la.norm(inB)
    return 0.5 + 0.5 * (num / denom)

myDat = mat(loadExData())
print(eulidSim(myDat[:, 0], myDat[:, 4]))
