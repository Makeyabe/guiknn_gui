import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from statistics import mode

def knn(k_value,age, weight, height):
    train = pd.read_csv('MOCK_DATA.csv')
    print(train)
    # read data from file
    train = train.drop('id', 1)
    # drop id header
    cols = ['age', 'weight', 'height']
    train.rename(columns = {cols[0]:0, cols[1]:1, cols[2]:2}, inplace=True)
    train['distance'] = 9999
    # # rename columns header and set new column distances
    target = [age, weight, height] #pd.Series([30, 200, 180])
    # # create unidentified target columns to predict knn
    train['distance'] = ((train.loc[:,0]-target[0])**2 + (train.loc[:,1]-target[1])**2 + (train.loc[:,2]-target[2])**2) ** 0.5
    train.loc[::10]
    # # calculate distances by using Euclidean distance
    k = k_value
    train = train.sort_values('distance', ascending=True)
    knn = list(train.head(k).body)
    # create graph
    print(train)
    plotting(train, cols, target, mode(knn))
    return mode(knn)

def plotting(train, cols, target, knn):
    colors = {'slim':'red', 'thin':'blue', 'fat':'green'}
    plt.scatter(
        train[1], 
        train[2], 
        c=train['body'].map(colors))
    plt.scatter(target[1], target[2], c='black', s=100)
    plt.xlabel(cols[1])
    plt.ylabel(cols[2])
    plt.title('Body Scatter Plot : ' + knn)
    plt.show()

# knn(2,25, 60, 180)
