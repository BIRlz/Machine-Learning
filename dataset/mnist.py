#原始的mnist数据集的构成是28*28*3，但是在实际试验中，这个规格可能并不适合我们的要求，因此在这儿使用一个脚本做一些相应的转换

import numpy as np
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

#直接读取的mnist是一个一位数组，或者是单个向量，reshape可以变成（length，28,28,1）的规格
def reshape_mnist(mnist):
    return mnist.reshape(mnist.shape[0],28,28,1).astype('float32')
    
#加padding，将28*28*1的mnist改变为32*32*1
def pad_mnist(mnist):
    padding = ((0,0),(2,2),(2,2),(0,0))
    mnist = np.pad(mnist,padding,'constant')
    return mnist

#变为3通道
def add_channels(mnist):
    mnist = np.tile(mnist,(1,1,1,3))
    length = mnist.shape[0]
    p = np.random.permutation(length)
    mnist = mnist[p]
    return mnist.reshape(length,32,32,3)
    
    
#load mnist
mnist = input_data.read_data_sets('MNIST_data',one_hot = True)

images_train,labels_train = mnist.train.images,mnist.train.labels
images_test,labels_test = mnist.test.images,mnist.test.labels

images_train = reshape_mnist(images_train)
print(images_train[0].shape)

images_train = pad_mnist(images_train)
print(images_train[0].shape)

images_train = add_channels(images_train)
print(images_train[0].shape)
