#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 17:54:14 2018

@author: byebir
"""
import numpy as np
import matplotlib.pyplot as plt
from math import *
import operator
'''
    input:
        [[property0,property1,property2,...,class],
        [...],
        ...
        [...]]
    output:
        tree
'''

# build dict for every feature
def buildFeatDict(dataSet):
    #return {cls1:a,cls2:b,cls3:c,...}
    currClass = {}
    for featVec in dataSet:
        cls = featVec[-1]
        if cls not in currClass.keys():
            currClass[cls] = 0
        currClass[cls] += 1
    return currClass
# calculate shannoEnt
def calcShannoEnt(dict):
    tot = 0.0
    prob = 0.0
    shannoEnt = 0.0
    for key in dict:
        tot += dict[key]#Get the whole value of all the features
    for key in dict:
        prob = float(dict[key]/tot)#P(x)
        shannoEnt -= log2(prob)*prob#ent = -log2(P(x))* P(x)
    return shannoEnt
#calculate expShannoEnt
def expShannoEnt(dataSet):
    dict = {}
    for featVex in dataSet:
        dict = buildFeatDict(dataSet)
        expShannoEnt = calcShannoEnt(dict)
    return calcShannoEnt(dict)
    
#Only a function to split the dataSet
def splitFeat(dataSet,index,value):
    resDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            tmp = featVec[:axis]
            tmp.extend(featVec[axis+1:])
            resDataSet.append(tmp)
    return resDataSet

#on a single layer
def bestFeat(dataSet):
    numFeature = len(dataSet[0])-1
    expEnt = expShannoEnt(dataSet)
    tmpDataSet = []
    bestEntGain = 0.0
    bestFeat = 0
    for i in range(numFeature):
        featList = [feat[i] for feat in dataSet]# build a list for every feature in dataSet[i]
        vals = set(featList)#get all the value in current list
        #print(featList)
        newEnt = 0.0
        for value in vals:
            subDataSet = splitFeat(dataSet,i,value)#split the current feature to calc the infoGain
            prob = len(subDataSet)/float(len(dataSet))
            newEnt += prob*calcShannoEnt(buildFeatDict(subDataSet))
        infoGain = expEnt - newEnt
        if infoGain > bestEntGain :
            bestEntGain = infoGain
            bestFeat = i
    return bestFeat

#id3 judge how to end the recurrence
def judgeToEnd(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]

#recurrence to build the dicisonTree
def buildDiceisionTree(dataSet,labels):
    classList = [feat[-1] for feat in dataSet]
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    if len(dataSet[0]) == 1:
        return judgeToEnd(classList)
    bestFeat = bestSplitFeat(dataSet)
    bestFeatLabel = labels[bestFeat]
    dicisionTree = {bestFeat:{}}
    del(labels[bestFeat])
    featVaules = [feat[bestFeat] for feat in dataSet]
    uniqueVals = set(featVaules)
    for value in uniqueVals:
        subLabels = labels[:]
        dicisionTree[bestFeat][value] =buildDiceisionTree(splitFeat(dataSet,bestFeat,value),subLabels)
    return dicisionTree


dataLabel = ['age','sliver','student','rate']
'''
dataSet = [['young','high','no','good','no'],
            ['elder','high','no','well','yes'],
            ['old','mid','no','well','yes'],
            ['old','low','yes','well','yes'],
            ['old','low','yes','good','no'],
            ['elder','low','yes','good','yes'],
            ['young','mid','no','well','no'],
            ['young','low','yes','well','yes'],
            ['old','mid','yes','good','yes'],
            ['young','mid','yes','good','yes'],
            ['elder','high','yes','well','yes'],
            ['elder','mid','no','good','yes'],
            ['old','mid','no','good','no'],
            ['old','mid','no','good','yes']]
'''
dataSet = [ [0,2,0,1,1],
            [1,2,0,1,1],
            [2,0,1,1,1],
            [2,0,1,1,0],
            [2,0,1,0,1],
            [1,1,0,0,0],
            [0,0,1,1,1],
            [0,1,0,1,0],
            [2,2,1,0,1],
            [0,1,1,0,1],
            [1,2,1,1,0],
            [1,1,0,0,1],
            [2,1,0,0,0],
            [2,1,0,0,0]]

#print(expShannoEnt(dataSet))
#print(splitFeat(dataSet,1,2))
#print(bestSplitFeat(dataSet))
print(buildDiceisionTree(dataSet,dataLabel))

#Result

'''
    {1: {0: {0: {0: 1, 2: {1: {0: 1, 1: {-1: {0: 0, 1: 1}}}}}}, 
        1: {1: {0: {0: {0: 0, 1: {-1: {0: 0, 1: 1}}, 2: 0}}, 1: 1}}, 2: {0: {0: 1, 1: {0: {0: 1, 1: 0}}, 2: 1}}}}
'''
