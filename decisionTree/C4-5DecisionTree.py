#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 17:54:14 2018
@author: byebir
"""
#The main difference between ID3 and C4.5 is the splitting standred. 
#In ID3, we regard the infomation-gain as the key to choose which property to split;
#HOWEVER, the infoGain is inclined to the property that has more features.
#In C4.5, we use the infoGainRate to classify the property.

#Only a small difference in code than the ID3.
def bestSplitFeat(dataSet):
    numFeature = len(dataSet[0])-1
    expEnt = expShannoEnt(dataSet)
    tmpDataSet = []
    bestEntGain = 0.0
    bestFeat = -1
    for i in range(numFeature):
        featList = [feat[i] for feat in dataSet]#for every feature in dataSet[i] build a list
        uniqueVals = set(featList)#get all the value in current list
        #print(featList)
        newEnt = 0.0
        splitInfo = 0.0
        for value in uniqueVals:
            subDataSet = splitFeat(dataSet,i,value)#split the current feature to calc the infoGain
            prob = len(subDataSet)/float(len(dataSet))
            newEnt += prob*calcShannoEnt(buildFeatDict(subDataSet))
            splitInfo -= prob*log2(prob)
        infoGainRate = (expEnt - newEnt)/splitInfo
        #print(infoGainRate)
        if infoGainRate > bestEntGain :
            bestEntGain = infoGainRate
            bestFeat = i
    return bestFeat
  
  #To classify
  def classify(deciTree, labels, test):  
    firstStr = deciTree.keys()[0]  
    secondDict = deciTree[firstStr]  
    featIndex = labels.index(firstStr)  
    for key in secondDict.keys():  
        if test[featIndex] == key:  
            if type(secondDict[key]).__name__ == 'dict':  
                classLabel = classify(secondDict[key], labels, test)  
            else: classLabel = secondDict[key]  
    return classLabel  
