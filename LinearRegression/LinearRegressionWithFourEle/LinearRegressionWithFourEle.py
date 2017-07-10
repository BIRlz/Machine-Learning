import numpy as np
import matplotlib.pyplot as plt
import random 

#绘图出来
plt.figure('homework')
plt.rcParams['figure.figsize'] = (10.0, 8.0) #设置画布的尺寸
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['image.cmap'] = 'gray'


#数据的输入
def load_data(filename):
    data = []
    with open(filename,'r') as f:
        for line in f.readlines():
            line = line.split(',')
            current = [int(item) for item in line]
            data.append(current)
    return data

data = load_data('trainData.txt')
data = np.array(data,np.int64)

#对X和Y加载
#训练集
x = data[:,(0,1,2,3)].reshape((-1,4))
y = data[:,4].reshape((-1,1))
#print(x.shape)
#print(y.shape)

#获得y的长度
m = y.shape[0]


#检查是否成功导入数据
print("All the x and Y:"+ '\n')
print('x = ',x,'\n','y = ',y)




#梯度下降求theta,损失函数还是需要计算损失平方和均值

#数据的预处理，标准化
def featureNormalize(X):
    x_norm = X
    #print(X.shape[-1])
    mu = np.zeros((1,X.shape[-1]))
    sigma = np.zeros((1,X.shape[-1]))
    for i in range(X.shape[-1]):
        mu[0,i] = np.mean(X[:,i])#均值
        sigma[0,i] = np.std(X[:,i])#标准差
        #print(mu)
        #print(sigma)
    x_norm = (X - mu) / sigma
    return x_norm,mu,sigma

#计算损失
def computeCost(X,y,theta):
    m = y.shape[0]
    #J = (np.sum((X.dot(theta)-y)**2)) / (2*m)
    C = X.dot(theta) - y
    J2 = (C.T.dot(C))/(2*m)
    return J2

#梯度下降
def gradientDescent(X,y,theta,alpha,num_iters):
    m = y.shape[0]
    #print(m)
    #存储历史误差
    J_hisotry = np.zeros((num_iters,1))
    for iter in range((num_iters)):
        #对J求导
        theta = theta-(alpha/m) * (X.T.dot(X.dot(theta) - y))
        J_hisotry[iter] = computeCost(X,y,theta)
    return J_hisotry,theta

iterations = 10000#训练1k次
alpha = 0.01#学习率
x = data[:,(0,1,2,3)].reshape((-1,4))
y = data[:,4].reshape((-1,1))
m = y.shape[0]
x,mu,sigma = featureNormalize(x)
X = np.hstack([x,np.ones((x.shape[0],1))])
#print(X)
#print(y)
theta = np.zeros((5,1))

j = computeCost(X,y,theta)
J_history,theta = gradientDescent(X,y,theta,alpha,iterations)

print('Theta found by gradient descent',theta)



plt.plot(J_history)
plt.ylabel('loss');
plt.xlabel('iter count')
plt.title('convergence graph')
plt.show()

#预测+验证
def predict(data):
    testx = np.array(data)
    testx = ((testx - mu) / sigma)
    testx = np.hstack([testx,np.ones((testx.shape[0], 1))])
    price = testx.dot(theta)
    print('price is %d ' % (price)+ '\n')

#测试组
predict([75,1615000,14010,150])
predict([80,1605000,14468,155])
predict([86,1590000,15000,165])
predict([98,1595000,15200,175])
predict([87,1590000,15600,175])
predict([77,1600000,16000,190])
predict([63,1610000,16200,200])
