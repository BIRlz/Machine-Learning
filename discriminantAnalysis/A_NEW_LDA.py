# coding:utf-8
from __future__ import division
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

def class_mean(dataSet,cls):
    feat_vec = []
    for feat in dataSet:
        label = feat[-1]
        if label == cls:
            feat_vec.append(feat[:-1])
    return feat_vec,np.mean(mean_vec,axis=0)

def within_class_SW(cls,class_mean):
    m,n = cls.shape()
    S_W = np.zeros((m,m))
    for j in len(cls):
        for i in range(len(cls[j][0]):
            S_W += (cls[j][i] - class_mean[i])**2
    return S_W

def between_class_SW(dataSet,cls_list):
    m = cls_list.shape(1)
    all_mean = np.mean(dataSet,axis=0)
    cls_mean = []
    S_B = np.zeros((m,m))
    for j in cls_list:
        n = j.shape[0]
        j = j.reshape(4,1)
        all_mean = all_mean.reshape(4,1)
        S_B += n * (j - all_mean).dot(j - all_mean).T)
    return S_B
                       
dataSet = [[1,2,1],[2,3,1],[3,4,2],[4,5,2]]
print(class_mean(dataSet,1))   
print(class_mean(dataSet,2))   
