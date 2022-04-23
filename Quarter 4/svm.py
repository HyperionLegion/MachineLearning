import math
#Bayes
#prob of output=0 given input x1=x1 and x2=x2
#prob o output=1 given inputx1=x1 and x2=x2
#take the prob that is bigger, instead of just 1 number with a threshold, 2 numbers

#Prob of A given B = Prob of A and B / Prob of B (naive bayes rule)
#prob of A and B = Prob of B * Prob of (A given B) = Prob of A * Prob of ( B given A)

#Prob of A given B = Prob of A * Prob of B given A / (Prob of A * Prob of B given A + Prob of not A * Prob of B given not A)
#denom = prob of B and A + prob of B and not A (total probability)
#not A = output = 1
#A output = 0

#Prob of B given A, prob of B given not A, prob of x1, x2 given output = 0, prob of x1, x2 given output = 1
#function = 1/(standard dev * sqrt(2pi)) * exp(-(x-mean)^2/(2*standard dev^2))
#P of x1, x2 = P of x1 * P of x2, means independent events

#prob of output =0 given x1, x2) = Prob(output=0) * Prob(x1, x2 | output =0) / (Prob output=0)*P(x1, x2 | output = 0) + P(output=1)*P(x1, x2 | output = 1)
#Prob of output=1 given x1, x2 = same thing but outpu=1 in numerator ^^^
#Prob of output =0 = pi_0 = n_0/n
#prob of output = 1 = pi_1 = n_1/n
#n = n0 +n1 = 400?
#P(x1, x2 | output = 1) = P(x1 | output=1) * P(x2 | output=1) ASSUMPTION, independent from naive
#P of x1 | output = 1 = f_1(x_1)
#P of x_2 | output = 1 = f_2(x_2)
#p0 * f_0(x_1) * f_0(x_2) / pi_0*f_0(x_1)*f_0(x_2) + pi_1*f_1(x_1)*f_2(x_2)
import csv
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d
import statistics
from scipy.stats import norm
from matplotlib.axes import Axes
from sklearn import svm

x = []
y = []
z = []
with open( 'data.csv' , newline='' ) as csvfile :
    #
    myreader = csv.reader( csvfile , delimiter=',' , quotechar='"' )
    #
    # header
    #
    for row in myreader :
    #
        print( row )
    #
        break
    #
    #
    # data
    #
    for row in myreader :
    #
        x1 = row[0]
    #
        y1 = row[1]
        z1 = row[2]
        purchase = row[2]
        x.append(float(x1))
        y.append(float(y1))
        z.append(float(z1))
    #
        #print( age , salary )
    #
    #
    #
def distancePointLine(a, b, c, x, y):
    return abs((a * x + b * y + c) / math.sqrt(a * a + b * b))

X = [[x[i], y[i]] for i in range(len(x))]
Y = [z[i] for i in range(len(z))]
clf = svm.SVC(kernel='linear')
clf.fit(X, Y)
fig, ax = plt.subplots()

for i in range(len(x)):
    if z[i] == 0:
        ax.scatter(x[i], y[i], color='blue', facecolors='none', edgecolors='b', label="no default")
    else:
        ax.scatter(x[i], y[i], color='red', marker="x", label="yes default")
print(clf.coef_)
print(clf.intercept_)
b0 = clf.intercept_[0]
b1 = clf.coef_[0][0]
b2 = clf.coef_[0][1]
ax.axline((0, -b0/b2), slope=-b1/b2, color='C0', label='by slope')

dist0pair = (0, 0)
dist1pair = (0, 0)
if z[0] == 0:
    dist0pair = (x[0], y[0])
    i = 1
    while z[i] != 1:
        i+= 1
    dist1pair = (x[i], y[i])
else:
    dist1pair = (x[0], y[0])
    i = 1
    while z[i] != 0:
        i+= 1
    dist0pair = (x[i], y[i])

for i in range(len(x)):
    if z[i] == 0:
        if distancePointLine(b1, b2, b0, x[i], y[i]) < distancePointLine(b1, b2, b0, dist0pair[0], dist0pair[1]):
            dist0pair = (x[i], y[i])
    else:
        if distancePointLine(b1, b2, b0, x[i], y[i]) < distancePointLine(b1, b2, b0, dist1pair[0], dist1pair[1]):
            dist1pair = (x[i], y[i])
ax.scatter(dist0pair[0], dist0pair[1], color='blue', marker="x", label="yes default")
ax.scatter(dist1pair[0], dist1pair[1], color='red', facecolors='none', edgecolors='r', label="no default")

    


ax.set_xlim(-3, 5)
ax.set_ylim(-2, 4) 
plt.ylabel('y')
plt.xlabel('x');
plt.show()

fig, ax = plt.subplots()
for i in np.arange(-3, 5, 0.25):
    for j in np.arange(-2, 4, 0.25):
        if clf.predict([[i, j]]) == [0.]:
            ax.scatter(i, j, color='blue', facecolors='none', edgecolors='b', label="no default")
        else:
            ax.scatter(i, j, color='red', marker="x", label="yes default")
ax.axline((0, -b0/b2), slope=-b1/b2, color='C0', label='by slope')

plt.ylabel('y')
plt.xlabel('x');
plt.show()
