#import logreg
from sklearn.linear_model import LogisticRegression
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.axes import Axes
import csv

data = []
student = []
nonstudent = []
#(array 0: default (bool), 1: student (bool) 2: balance (number), 3: income (number))
with open( 'Default.csv' , newline='' ) as csvfile :
    myreader = csv.reader( csvfile , delimiter=',' , quotechar='"' )
    for row in myreader :
        print( row )
        break

    for row in myreader :
        data.append((row[0]=="Yes", row[1]=="Yes", float(row[2]), float(row[3])))
        if row[1] == "Yes":
            student.append((row[0]=="Yes", row[1]=="Yes", float(row[2]), float(row[3])))
        else:
            nonstudent.append((row[0]=="Yes", row[1]=="Yes", float(row[2]), float(row[3])))

data_balances = []
data_income = []
data_defaults = []
data_students = []
data_defaults = []
for i in data:
    data_balances.append(i[2])
    data_income.append(i[3])
    data_students.append(i[1])
    data_defaults.append(i[0])

X = np.transpose(np.matrix([data_students, data_balances, data_income]))
y = np.transpose(np.matrix(data_defaults))
#y = np.column_or_1d(y, warn=True)
print(X.shape)
print(y.shape)
logisticRegr = LogisticRegression()
logisticRegr.fit(X, np.ravel(y))
#logisticRegr.predict(x_test[0].reshape(1,-1))
plt.title("students and non-students false negatives")
for i in range(0, len(data)):
    # print(logisticRegr.predict(X[i].reshape(1,-1)))
    # print(y[i])
    # if logisticRegr.predict(X[i].reshape(1,-1)) == [True] and y[i] == [[False]]:
    #     if data[i][1]:
    #         plt.scatter(data[i][2], data[i][3], color='red', marker="x", label="yes default")
    #     else:    
    #         plt.scatter(data[i][2], data[i][3], color='blue', facecolors='none', edgecolors='b', label="no default")

    if logisticRegr.predict(X[i].reshape(1,-1)) == [False] and y[i] == [[True]]:
        if data[i][1]:
            plt.scatter(data[i][2], data[i][3], color='red', marker="x", label="yes default")
        else:    
            plt.scatter(data[i][2], data[i][3], color='blue', facecolors='none', edgecolors='b', label="no default")

fig, ax = plt.subplots()
ax.legend(["student", "non-student"])
# handles, labels1 = ax.get_legend_handles_labels()
# ax.legend(handles=[handles[0],handles[-1]])
ax.grid(True)
ax.set_xlim([0,3000])
ax.set_ylim([0,90000])
plt.xlabel("balance")
plt.ylabel("income")
plt.show()

print(logisticRegr.coef_, logisticRegr.intercept_)

