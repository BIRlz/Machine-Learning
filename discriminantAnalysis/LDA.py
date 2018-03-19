import numpy as np 
import csv
from matplotlib import pyplot as plt
import math

#Claculate the x-axis-mean of the class
def calcClassMean(dataSet,label,class):
  meanVec = []
  for cl in range(1,clusters+1):
      meanVec.append(np.mean(dataSet[labels] == class)))
  return meanVec
  
#Clactlate the withinClassSW
def calcWithinClassSW(dataSet,label,class):
  k = len(dataSet[0][0])#get the numbers of features
  m =  dataSet.shape[1]
  S_W = np.zeros((m,m))
  meanVec = calcClassMean(dataSet,labels,class)
  for cl,mv in zip(range(1,clusters+1),meanVec):
    class_sc_mat = np.zeros((m,m))
    for row in dataSet[label == class]:
      row,mv = row.reshape(k,1),mv.reshape(k,1)
      clss_sc_mat += (row-mv).dot((row-mv).T)
    S_W += class_sc_mat
  return S_W
  
#Clactlate the betweenClassSW
  def between_class_SB(data,label,clusters):
    m = data.shape[1]
    all_mean =np.mean(data,axis = 0)
    S_B = np.zeros((m,m))
    mean_vectors = class_mean(data,label,clusters)
    for cl ,mean_vec in enumerate(mean_vectors):
        n = data[label==cl+1,:].shape[0]
        mean_vec = mean_vec.reshape(4,1) # make column vector
        all_mean = all_mean.reshape(4,1)# make column vector
        S_B += n * (mean_vec - all_mean).dot((mean_vec - all_mean).T)
    #print S_B 
    return S_B

def lda():
    data,label=read_iris();
    clusters = 3
    S_W = within_class_SW(data,label,clusters)
    S_B = between_class_SB(data,label,clusters)
    eig_vals, eig_vecs = np.linalg.eig(np.linalg.inv(S_W).dot(S_B))
    #print S_W 
    #print S_B 
    for i in range(len(eig_vals)):
        eigvec_sc = eig_vecs[:,i].reshape(4,1)
        print('\nEigenvector {}: \n{}'.format(i+1, eigvec_sc.real))
        print('Eigenvalue {:}: {:.2e}'.format(i+1, eig_vals[i].real))
    eig_pairs = [(np.abs(eig_vals[i]), eig_vecs[:,i]) for i in range(len(eig_vals))]
    eig_pairs = sorted(eig_pairs, key=lambda k: k[0], reverse=True)
    W = np.hstack((eig_pairs[0][1].reshape(4,1), eig_pairs[1][1].reshape(4,1)))
    print 'Matrix W:\n', W.real
        print data.dot(W)
    return W 
