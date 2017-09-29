#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import operator as op
import matplotlib
import matplotlib.pyplot as plt
import os


def creatDataSet():
    group = np.array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels

group, labels = creatDataSet()


def classify0(inx, dataset, labels, k):
    size = dataset.shape[0]
    diffMat = np.tile(inx, (size, 1)) - dataset
    sqdiffMat = diffMat ** 2
    sqDistances = sqdiffMat.sum(axis=1)
    distances = sqDistances ** 0.5
    sortedDistIndices = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlable = labels[sortedDistIndices[i]]
        classCount[voteIlable] = classCount.get(voteIlable, 0) + 1
    sortedClassCount = sorted(classCount.items(), key=op.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


def file2matrix(filename):
    with open(filename) as f:
        arrayLines = f.readlines()
        numberOfLines = len(arrayLines)
        returnMat = np.zeros((numberOfLines, 3))  # 创建零矩阵
        classLabelVector = []
        index = 0
        for line in arrayLines:
            line = line.strip()
            listFromLine = line.split('\t')
            returnMat[index, :] = listFromLine[0: 3]
            classLabelVector.append(int(listFromLine[-1]))
            index += 1
        return returnMat, classLabelVector
returnMat, classLabelVector = file2matrix('C:/Users/gengzhi/Desktop/machinelearninginaction/Ch02/datingTestSet2.txt')

def autoNorm(dataSet):
    minValue = dataSet.min(0)
    maxValue = dataSet.max(0)
    ranges = maxValue - minValue
    # normDataSet = np.zeros(dataSet.shape)
    m = dataSet.shape[0]
    normDataSet = dataSet - np.tile(minValue, (m, 1))
    normDataSet = normDataSet / np.tile(ranges, (m, 1))
    return normDataSet, ranges, minValue


def datingClassTest():
    hoRatio = 0.10
    datingDataMat, datingLabels = file2matrix('C:/Users/gengzhi/Desktop/machinelearninginaction/Ch02/datingTestSet2.txt')
    normMat, ranges, minValue = autoNorm(returnMat)
    m = normMat.shape[0]
    numTestVecs = int(m * hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i, :], normMat[numTestVecs:m, :],
                                     datingLabels[numTestVecs:m], 3)
        print('the classifier came back with: %d, the real answer is: %d' % (classifierResult, datingLabels[i]))
        if classifierResult != datingLabels[i]: errorCount += 1
    print('the total error rate is : %f ' % (errorCount / float(numTestVecs)))

'''
normMat, ranges, minValue = autoNorm(returnMat)
print(classify0([0.5, 0.8], group, labels, 3))
print(returnMat)
print(classLabelVector[0:20])
print(normMat)
datingClassTest()

fig = plt.figure()
ax = fig.add_subplot(111)
bx = ax.scatter(returnMat[:, 0], returnMat[:, 1], 15.0 * np.array(classLabelVector), 15.0 * np.array(classLabelVector))
plt.show(bx)
'''


def img2vector(filename):
    returnVector = np.zeros((1, 1024))
    with open(filename) as f:
        for i in range(32):
            lineStr = f.readline()
            for j in range(32):
                returnVector[0, 32*i+j] = int(lineStr[j])
    return returnVector


def handWritingClassTest():
    hwLabels = []
    trainingFileList = os.listdir('C:/Users/gengzhi/Desktop/machinelearninginaction/Ch02/trainingDigits')
    m = len(trainingFileList)
    trainingMat = np.zeros((m, 1024))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)
        trainingMat[i, :] = img2vector('C:/Users/gengzhi/Desktop/machinelearninginaction/Ch02/trainingDigits/%s' % fileNameStr)
    testFileList = os.listdir('C:/Users/gengzhi/Desktop/machinelearninginaction/Ch02/testDigits')
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest = img2vector('C:/Users/gengzhi/Desktop/machinelearninginaction/Ch02/testDigits/%s' % fileNameStr)
        classifierResult = classify0(vectorUnderTest, trainingMat, hwLabels, 3)
        print('the classifier came back with: %d ,the real answer is: %d' % (classifierResult, classNumStr))
        if classifierResult != classNumStr:
            errorCount += 1
    print('\n the total number of errors is %d' % errorCount)
    print('\n the total error rate is : %f' % (errorCount / float(mTest)))

handWritingClassTest()

