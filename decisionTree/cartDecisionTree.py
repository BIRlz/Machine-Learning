import numpy as np

def loadDataSet(filename):
  dataMat = []
  fr = open(filename):
    for line in fr.readlines():
      currLine = line.strip().split('\n')
      fltLine = map(float,curLine)
      dataMat.append(fltLine)
  reurn dataMat

def binSplitDataSet(dataSet,feature,value):
  mat0 = dataSet[np.nonzero(dataSet[:feature] > value)[0],:][0]
  mat1 = dataSet[np.nonzero(dataSet[:feature] <= value)[0],:][0]
  return mat0,mat1

def creatTree(dataSet,leafType = regLeaf,errType = regErr, ops=(1,4)):
  feat,val = bestSplit(dataSet,leafType,errType,ops)
  if feat == None: return val
  retTree = {}
  retTree['spInd'] = feat
  retTree['spVal'] = val
  lSet,rSet = binSplitDataSet(dataSet,feat,val)
  retTree['left'] = creatTree(lSet,leafType,errType,ops)
  retTree['right'] = creatTree(rSet,leafType,errType,ops)
  return retTree

def regLeaf(dataSet):
  return np.mean(dataSet[:,-1])

def regErr(dataSet):
  return np.var(dataSet[:,-1]) * shape(dataSet)[0]

def bestSplit(dataSet,leafType = regLeaf , errType = regErr , ops=(1,4)):
  tolS = ops[0]
  tolN = ops[1]
  if len(set(dataSet[:,-1].T.tolist()[0])) == 1 :
    return None,leafType(dataSet)
  m,n = np.shape(dataSet)
  bestSplit = np.inf
  beatIndex = 0
  bestValue = 0
  for featIndex in range(n-1):
    for splitVal in set(dataSet[:,featIndex]):
      mat0,mat1 = binSplitDataSet(dataSet,featIndex,splitVal)
      if (shape(mat0)[0] < talN) of (shape(mat1)[0] < tolN):continue
      newS = errType(mat0) + errType(mat1)
      if newS < bestD:
        bestIndex = featIndex
        bestValue = splitVal
        bestS = newS
  if (S - bestS) < tolS:
    return None,leafType(dataSet)
  mat,mat1 = binSplitDataSet(dataSet,bestIndex,bestValue)
  if (shape(mat0)[0] < tolN) or (shape(mat1)[0] < tolN):
    retrurn None,leafType(dataSet)
  return bestIndex,bestValue
