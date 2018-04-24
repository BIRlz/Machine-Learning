def kMeans(dataMat,k,distE = distEclud , createCent=randCent):
    m = shape(dataMat)[0]    # 获得行数m
    clusterAssment = mat(zeros((m,2))) # 初试化一个矩阵，用来记录簇索引和存储误差                               
    centroids = createCent(dataMat,k) # 随机的得到一个质心矩阵蔟
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        for i in range(m):    #对每个数据点寻找最近的质心
            minDist = inf; minIndex = -1
            for j in range(k): # 遍历质心蔟，寻找最近的质心    
                distJ1 = distE(centroids[j,:],dataMat[i,:]) #计算数据点和质心的欧式距离
                if distJ1 < minDist: 
                    minDist = distJ1
                    minIndex = j
            if clusterAssment[i,0] != minIndex:
                clusterChanged = True
            clusterAssment[i,:] = minIndex, minDist**2
        print centroids
        for ci in range(k):   #更新质心，将每个族中的点的均值作为质心
            index_all = clusterAssment[:,0].A   #取出样本所属簇的索引值
            value = nonzero(index_all==ci)    #取出所有属于第ci个簇的索引值
            sampleInClust = dataMat[value[0]]     #取出属于第i个簇的所有样本点
            centroids[cent,:] = mean(sampleInClust, axis=0) 
    return centroids, clusterAssment
