from sklearn.linear_model import LogisticRegression
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.axes import Axes
import csv

data = []
data_age = []
data_salary = []
data_purchased = []
#(array 0: default (bool), 1: student (bool) 2: balance (number), 3: income (number))
with open( 'SocialNetworkAds.csv' , newline='' ) as csvfile :
    myreader = csv.reader( csvfile , delimiter=',' , quotechar='"' )
    for row in myreader :
        print( row )
        break

    for row in myreader :
        data.append((float(row[0]), float(row[1]), float(row[2])))
        data_age.append(float(row[0]))
        data_salary.append(float(row[1]))
        data_purchased.append(float(row[2]))
        
# for i in range(len(data)):
#     if data[i][2] == 0:
#         plt.scatter(data[i][0], data[i][1], color='red', marker="x", label="yes default")
#     else:
#         plt.scatter(data[i][0], data[i][1], color='blue', facecolors='none', edgecolors='b', label="no default")
def lab03(data, x, y, n):
    indexes = [k for k in range(0,n)]
    maxIndex = 0
    for i in indexes:
        if (pow((data[i][0]-x), 2) + pow((data[i][1]-y)/1000, 2)) > (pow((data[maxIndex][0]-x), 2) + pow((data[maxIndex][1]-y)/1000, 2)):
            maxIndex = i
    for i in range (0, len(data)):
        if i not in indexes:
            if (pow((data[i][0]-x), 2) + pow((data[i][1]-y)/1000, 2)) < (pow((data[maxIndex][0]-x), 2) + pow((data[maxIndex][1]-y)/1000, 2)):
                indexes.remove(maxIndex)
                indexes.append(i)
                maxIndex = indexes[0]
                for j in indexes:
                    if (pow((data[j][0]-x), 2) + pow((data[j][1]-y)/1000, 2)) > (pow((data[maxIndex][0]-x), 2) + pow((data[maxIndex][1]-y)/1000, 2)):
                        maxIndex = j
    averagey = 0
    for i in indexes:
        averagey += data[i][2]
    averagey = averagey/len(indexes)
    return averagey

lab03age = np.arange(min(data_age), max(data_age), 1)
lab03salary = np.arange(min(data_salary), max(data_salary), 2000)
lab03age = lab03age.tolist()
lab03salary = lab03salary.tolist()
lab03purchase = []
for i in lab03age:
    for j in lab03salary:
        print(i, j)
        p = lab03(data, i, j, 3)
        if p > 0.5:
            plt.scatter(i, j, color='blue', facecolors='none', edgecolors='b', label="no default")
        else:
            plt.scatter(i, j, color='red', marker="x", label="yes default")

        #lab03purchase.append(lab03(data, i, j, 5))
plt.show()

